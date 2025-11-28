import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input_prompt, image])
    return response.text

# Page Configuration
st.set_page_config(page_title="NutriSnap: AI Calorie Counter", page_icon="🍎", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 12px;
        height: 55px;
        font-size: 18px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px 0 rgba(102, 126, 234, 0.4);
        cursor: pointer;
    }
    .stButton>button p {
        color: white !important;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%) !important;
        color: white !important;
        box-shadow: 0 6px 25px 0 rgba(102, 126, 234, 0.6);
        transform: translateY(-2px);
    }
    .stButton>button:focus {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 4px 20px 0 rgba(102, 126, 234, 0.6);
    }
    .stButton>button:active {
        transform: translateY(0px);
        box-shadow: 0 4px 15px 0 rgba(102, 126, 234, 0.5);
        color: white !important;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #aaaaaa;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }
    .stFileUploader {
        padding: 0px;
        border: none;
    }
    .stFileUploader > div > div > div > div {
        background-color: #1e212b;
        border: 1px dashed #4b5563;
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>🍎 NutriSnap: AI Calorie Counter</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Snap a photo, track your calories, and eat smarter.</p>", unsafe_allow_html=True)

# Main Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📸 Upload & Analyze")
    uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    
    analyze_button = st.button("🔍 Analyze Calories")

    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.markdown('<div class="uploaded-image-container">', unsafe_allow_html=True)
        st.image(image, caption="Your Meal", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 🥗 Nutritional Insights")
    
    if analyze_button and uploaded_file is not None:
        input_prompt = """
        You are an expert nutritionist where you need to see the food items from the image
        and calculate the total calories, also provide the details of every food item with calories intake
        is below format

        1. Item 1 - no of calories
        2. Item 2 - no of calories
        ----
        ----
        Total Calories: X
        """
        
        with st.spinner("🤖 AI is analyzing your food..."):
            try:
                response = get_gemini_response(input_prompt, image)
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown(response)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    elif analyze_button and uploaded_file is None:
        st.warning("Please upload an image first to get started.")
    else:
        st.info("Upload an image and click 'Analyze Calories' to see the nutritional breakdown here.")

# NutriSnap: AI Calorie Counter 🍎

**NutriSnap** is a smart, AI-powered calorie counter application that uses Google's Gemini Pro Vision API to analyze food images and provide instant nutritional insights.

![NutriSnap Demo](https://via.placeholder.com/800x400?text=NutriSnap+Demo+Image)

## 🏷️ Tags & Keywords
`calorie-counter` `food-recognition` `gemini-api` `streamlit` `python` `ai-nutrition` `health-tech` `computer-vision` `machine-learning` `diet-tracker`

## Features

-   **📸 Instant Analysis**: Simply upload a photo of your meal.
-   **🤖 AI-Powered**: Leverages Gemini 2.5 Flash for accurate food identification.
-   **📊 Detailed Breakdown**: Get a list of ingredients and their calorie counts.
-   **🔢 Total Calories**: Automatically calculates the total caloric value.
-   **🎨 Modern UI**: A sleek, dark-themed interface built with Streamlit.

## Prerequisites

-   Python 3.10+
-   A Google Cloud Project with the Gemini API enabled.
-   A Google API Key.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/NutriSnap.git
    cd NutriSnap
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables**:
    -   Create a `.env` file in the root directory.
    -   Add your Google API Key:
        ```env
        GOOGLE_API_KEY=your_actual_api_key_here
        ```

## Usage

1.  Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2.  The app will open in your default web browser.

3.  Upload an image of food (JPG, JPEG, PNG).

4.  Click the **Analyze Calories** button.

## Technologies Used

-   [Streamlit](https://streamlit.io/) - Frontend framework.
-   [Google Gemini API](https://ai.google.dev/) - AI/LLM for vision and text.
-   [Python-dotenv](https://pypi.org/project/python-dotenv/) - Environment management.
-   [Pillow (PIL)](https://python-pillow.org/) - Image processing.


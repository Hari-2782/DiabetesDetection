# Diabetes Prediction Enterprise Web App

This project is an enterprise-level web application for predicting diabetes using machine learning. It features a modern, responsive UI and a robust backend built with Django and scikit-learn.

## Features

- Predicts diabetes based on user input (age, gender, BMI, etc.)
- Professional, enterprise-style Bootstrap UI
- Model evaluation with confusion matrix, ROC curve, and feature importance
- Easily extensible and ready for deployment

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd Fdm_proj-main
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Open your browser and go to:**
    ```
    http://127.0.0.1:8000/
    ```

## Project Structure

- `diabetes_project/` - Django project settings and configuration
- `diabetes_predictor/` - Main app with views, templates, and ML logic
- `final_model.pkl` - Trained machine learning model
- `templates/` - HTML templates for the web UI

## Model

The model is trained using scikit-learn and saved as `final_model.pkl`. It uses features such as age, gender, BMI, hypertension, heart disease, smoking history, HbA1c level, and blood glucose level.

## License

This project is licensed under the MIT License.

---

**For any questions or contributions, please open an issue or submit a pull request.**
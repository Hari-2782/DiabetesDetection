from django.shortcuts import render
import joblib

# Load the model (make sure to use a raw string to avoid unicode escape issues)
model = joblib.load(r'c:\Users\asus\Downloads\Compressed\Fdm_proj-main\Fdm_proj-main\final_model.pkl')

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        # Get data from the form
        gender = int(request.POST['gender'])
        age = float(request.POST['age'])
        hypertension = int(request.POST['hypertension'])
        heart_disease = int(request.POST['heart_disease'])
        smoking_history = int(request.POST['smoking_history'])
        bmi = float(request.POST['bmi'])
        HbA1c_level = float(request.POST['HbA1c_level'])
        blood_glucose_level = float(request.POST['blood_glucose_level'])

        # Prepare the data in the correct format for prediction
        features = [[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]]
        
        # Make a prediction
        prediction = model.predict(features)

        # Interpret the result
        result = 'Diabetes' if prediction[0] == 1 else 'No Diabetes'
        
        return render(request, 'result.html', {'result': result})

    # If not a POST request, redirect to the index page or show an error
    return render(request, 'index.html', {'error': 'Invalid request method.'})

import streamlit as st
import joblib
import numpy as np

# Load the trained model
classifier = joblib.load('model.joblib')

# Function to get user input for prediction
def get_user_input():
    gender = st.radio("Enter gender:", ('Male', 'Female'))
    married = st.radio("Is the applicant married?", ('Yes', 'No'))
    dependents = st.number_input("Enter number of dependents:", min_value=0, step=1)
    education = st.radio("Enter education:", ('Graduate', 'Not Graduate'))
    self_employed = st.radio("Is the applicant self-employed?", ('Yes', 'No'))
    applicant_income = st.number_input("Enter applicant's income:")
    coapplicant_income = st.number_input("Enter co-applicant's income:")
    loan_amount = st.number_input("Enter loan amount:")
    loan_term = st.number_input("Enter loan term (in years):")
    credit_history = st.radio("Enter credit history:", (0, 1))
    property_area = st.selectbox("Enter property area:", ('Rural', 'Urban', 'Semiurban'))

    submit_button = st.button("Submit")

    if submit_button:
        # Encoding categorical input
        gender = 1 if gender == 'Male' else 0
        married = 1 if married == 'Yes' else 0
        education = 1 if education == 'Graduate' else 0
        self_employed = 1 if self_employed == 'Yes' else 0
        property_area = {'Rural': 0, 'Urban': 1, 'Semiurban': 2}[property_area]

        return [gender, married, dependents, education, self_employed, applicant_income,
                coapplicant_income, loan_amount, loan_term, credit_history, property_area]

# Get user input
user_input = get_user_input()

if user_input:
    # Select only the features present in the dataset
    user_input_selected = user_input[:5]

    # Reshape user input for scaling
    user_input_reshaped = np.array(user_input_selected).reshape(1, -1)

    # Make prediction
    prediction = classifier.predict(user_input_reshaped)
    if prediction[0] == 1:
        st.write("Loan Approved!")
    else:
        st.write("Loan Not Approved!")

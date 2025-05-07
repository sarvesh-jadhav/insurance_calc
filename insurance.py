import streamlit as st # type: ignore
st.set_page_config(page_title= "Health Insurance Premium Calculator", layout= "centered")
st.title("Health Insurance Premium calculator")
st.markdown("Estimate your health insurance premium based on personal details")

def calculate_health_insurance_premium(age, gender, smoker, bmi, dependents, base_premium=5000):
    premium= base_premium
    if age>45:
        premium*=1.5
    elif age>30:
        premium*=1.2

    if gender.lower()== 'male':
        premium*=1.2

    if smoker:
        premium*=1.5

    if bmi>30:
        premium*=1.3
    elif bmi<18.5:
        premium*=1.1

    premium+=1000*dependents
    return round(premium,2)

st.sidebar.header("Enter your Details")
age= st.sidebar.slider("Age", max_value=80, min_value=18, value=30)
gender= st.sidebar.selectbox("Gender", ["Male", "Female"])
smoker= st.sidebar.selectbox("Do You Smoke", ["No", "yes"])=="yes"
bmi= st.sidebar.number_input("Body Mass Index(BMI)",max_value=50, min_value=10, value=24 )
dependents= st.sidebar.slider("Number of Dependents", min_value=0, max_value=5, value=0)

premium= calculate_health_insurance_premium(age, gender, smoker, bmi, dependents)

st.subheader("Estimated Premium")
st.success(f"${premium:,} per year")

st.markdown("-----")
st.caption("This is simplified calculator and not an official insurance quote")
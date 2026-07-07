import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

st.title("🧩 Autism Screening Predictor")
st.write("This tool is for educational purposes only and is not a medical diagnosis.")

st.subheader("AQ-10 Screening Questions")
st.write("Answer 1 if the statement applies to you, 0 if it does not.")

A1 = st.selectbox("I often notice small sounds when others do not", [0, 1])
A2 = st.selectbox("I usually concentrate more on the whole picture rather than small details", [0, 1])
A3 = st.selectbox("I find it easy to do more than one thing at once", [0, 1])
A4 = st.selectbox("If there is an interruption I can switch back to what I was doing quickly", [0, 1])
A5 = st.selectbox("I find it easy to read between the lines when someone is talking to me", [0, 1])
A6 = st.selectbox("I know how to tell if someone listening to me is getting bored", [0, 1])
A7 = st.selectbox("When reading a story I find it difficult to work out characters intentions", [0, 1])
A8 = st.selectbox("I like to collect information about categories of things", [0, 1])
A9 = st.selectbox("I find it easy to work out what someone is thinking just by looking at their face", [0, 1])
A10 = st.selectbox("I find it difficult to work out peoples intentions", [0, 1])

st.subheader("Personal Information")

age = st.number_input("Age", min_value=1, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female"])
ethnicity = st.selectbox("Ethnicity", ["White-European", "Asian", "Middle Eastern", "Black", "South Asian", "Latino", "Hispanic", "Pasifika", "Turkish", "Others", "Unknown"])
jundice = st.selectbox("Were you born with jaundice?", ["No", "Yes"])
austim = st.selectbox("Does any family member have autism?", ["No", "Yes"])
used_app_before = st.selectbox("Have you used an autism screening app before?", ["No", "Yes"])
relation = st.selectbox("Who is filling this form?", ["Self", "Parent", "Relative", "Health care professional", "Others", "Unknown"])


if st.button("Predict"):
    # empty dataframe with all training columns
    input_df = pd.DataFrame([np.zeros(len(columns))], columns=columns)

    # Filling the AQ scores
    input_df['A1_Score'] = A1
    input_df['A2_Score'] = A2
    input_df['A3_Score'] = A3
    input_df['A4_Score'] = A4
    input_df['A5_Score'] = A5
    input_df['A6_Score'] = A6
    input_df['A7_Score'] = A7
    input_df['A8_Score'] = A8
    input_df['A9_Score'] = A9
    input_df['A10_Score'] = A10

    # Filling personal info
    input_df['age'] = age
    input_df['gender'] = 1 if gender == "Female" else 0
    input_df['jundice'] = 1 if jundice == "Yes" else 0
    input_df['austim'] = 1 if austim == "Yes" else 0
    input_df['used_app_before'] = 1 if used_app_before == "Yes" else 0

    # Filling one hot encoded columns
    # eg: if ethnicity = "Asian" → ethnicity_Asian
    ethnicity_col = f'ethnicity_{ethnicity}'  
    relation_col = f'relation_{relation}'

    # eg: Placing 1 in ethnicity_Asian column
    if ethnicity_col in input_df.columns:
        input_df[ethnicity_col] = 1

    if relation_col in input_df.columns:
        input_df[relation_col] = 1


    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ This screening suggests a likelihood of ASD. Please consult a healthcare professional.")
    else:
        st.success("✅ This screening does not suggest ASD traits. Please consult a healthcare professional if you have concerns.")
        


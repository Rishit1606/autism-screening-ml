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


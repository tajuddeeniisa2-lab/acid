import pandas as pd
import joblib
import streamlit as st
from PIL import Image

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f5f7fa;
}

/* Title */
h1 {
    color: #0066cc;
    text-align: center;
    font-family: Arial, sans-serif;
}

/* Buttons */
.stButton > button {
    background-color: #0066cc;
    color: blue;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #004c99;
}

/* Text input boxes */
.stTextInput > div > div > input {
    border-radius: 10px;
    border: 2px solid #0066cc;
}

/* Select box */
.stSelectbox {
    border-radius: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #eaf2ff;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border: 2px solid #0066cc;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #ffdddd, #ddddff);
}

h1 {
    color: #4b0082;
    text-align: center;
}

.stButton > button {
    background: linear-gradient(to right, #ff4b4b, #4b6cff);
    color: white;
    border-radius: 15px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
col1,col12=st.columns([1,4])
with col1:
    st.image("logo.png.png",width=500)
with col12:
    st.title("ACID AND BASE INDICATOR")

st.set_page_config(page_title="acid and base indicator",page_icon="$",layout="centered")
st.title("$ chemistry chemical indicator ")
st.write("enter your indicator and your subtance to predict you the colour.")

model = joblib.load("indicator_model.pkl")
tf = joblib.load("indicator_vectorizer.pkl")
indicator = st.text_input("enter your indicator:")
subtance_ph = st.text_input("enter your ph subtance:")
if st.button("submit"):
    if indicator.strip() == "":
        st.error("please enter your indicator")
            

    sample = [indicator + " " + subtance_ph]
    encoded_sample = tf.transform(sample)
    prediction = model.predict(encoded_sample)
    st.write("prediction:",prediction)
    st.success(f"your chemical colour is: {prediction[0]}")
     
       



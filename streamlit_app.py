import streamlit as st
import sklearn
import pickle
import numpy as np
model = pickle.load(open("model.pkl", "rb"))

st.title("Predicting Sales dataset")
st.markdown(
    "We are Predicting the sales based on the TV ads"
)

tv = st.slider('What is price for given TV advertisement budget listing ?', 0, 300, 150)
tv = st.number_input('Enter TV advertisement budget:', min_value=0, max_value=300, value=150)

user_input = [[tv]] #, newspaper, radio]]
#user_input = user_input.astype(float)
if st.button('Predict?'):
    st.write("The model predicts the sales based on the tv ads:", model.predict(user_input).round(2))
    st.markdown(f"<span style='color:green'>The model predicts the sales based on the tv ads: {prediction[0]}</span>", unsafe_allow_html=True)

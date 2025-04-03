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
# Predict sales based on the input
user_input = np.array([[tv]]) 
prediction = model.predict(user_input)[0]

# Display the prediction using a bar chart
st.bar_chart(data=prediction, width=200, height=200, use_container_width=True)

user_input = [[tv]] #, newspaper, radio]]
#user_input = user_input.astype(float)
if st.button('Predict?'):
    st.write("The model predicts the sales based on the tv ads:", model.predict(user_input).round(2))

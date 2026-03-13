import streamlit as st 
import numpy as np
import joblib 

model = joblib.load("model.pkl")

st.title("Monetization Modeler")

views = st.number_input("Enter the Value of Views")
likes = st.number_input("Enter the number of likes")
comments = st.number_input("enter the numbers of comments")
subscribers = st.number_input("Enter the numebr of Subscribers")

engagement_rate = (likes + comments) / views if views !=0 else 0

features = np.array([[views, likes, comments, subscribers, engagement_rate]])

if st.button("predict"):
    input_data = np.array([[views,likes,comments,subscribers,engagement_rate]])
    prediction = model.predict(input_data)
    prediction = model.predict(features)

    st.write("Raw prediction:", prediction[0])

    prediction = max(prediction[0], 0)

    st.success(f"Estimated Revenue: ${prediction:.2f}")
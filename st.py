import streamlit as st
import joblib
model = joblib.load('news-classification-model.pkl')

# Define sentiment labels
news_labels = {0: 'tech', 1: 'business', 2: 'sport', 3: 'entertainment', 4: 'politics'}


# Create Streamlit app
st.title("News Classification")

# Input text area
user_input = st.text_area('Enter news here')

# Prediction button
if st.button("Classify"):
    predicted_label = model.predict([user_input])[0]

    predicted_news_label = news_labels[predicted_label]

    # Display classification
    st.info(f"Predicted News Category: {predicted_news_label}")


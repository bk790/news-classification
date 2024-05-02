import streamlit as st
import joblib

model=joblib.load('news-classification-model.pkl')
news_labels={0:'tech', 1:'business', 2:'sport', 3:'entertainment', 4:'politics'}
st.title("news Classification")
user_input=st.text_area("Enter news here:")
if st.button("predict"):
    predicted_label=model.predict([user_input])[0]
    predicted_news_label=news_labels([str(predicted_label)])
    print(predicted_news_label)

import streamlit as st

st.header("Contact me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address:")
    user_message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message = user_message + user_email
        print("I was Pressed")



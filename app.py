
import streamlit as st
st.title("HR Email Sender")
st.write("Starter UI. Upload contacts and resume, then integrate email_sender.send_bulk().")
contacts=st.file_uploader("Contacts xlsx")
resume=st.file_uploader("Resume PDF")
st.checkbox("Test mode")
st.button("Send")

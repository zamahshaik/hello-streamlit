import streamlit as st

st.set_page_config(page_title = "MEI Chatbot", page_icon = ":robot:", layout = "wide")

# -- Header Section --

st.subheader("Hi, I am a chatbot :wave:")
st.title("I help find PDFs")
st.write("More functionality coming up here!")
with st.form(key = "user_input"):
    srchpdf = st.text_input("Enter the PDF you want to search: ")
    st.form_submit_button("Search")

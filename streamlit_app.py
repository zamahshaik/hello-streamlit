import streamlit as st

st.set_page_config(page_title = "MEI Chatbot", page_icon = ":robot:", layout = "wide")

# -- Header Section --

st.subheader("Hi, I am a chatbot :wave:")
st.title("I help find PDFs")
st.write("More functionality coming up here!")
pdfname = input("Enter the Purchase Order to search for: ")
print(pdfname)

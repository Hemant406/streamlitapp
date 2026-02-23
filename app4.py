import streamlit as st 

st.title("Simple chatbot........")

que = st.text_input("Ask me anything")

if st.button("Ask"):
    st.write("You asked : ",que)
    st.write("Chatbot is buisy , find answer on your own")
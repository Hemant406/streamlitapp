import streamlit as st 

st.title("Welcome to basic streamlit app")

age = st.slider("Select your age",1,100)
city = st.selectbox("Select your city",["Nashik","Mumbai","Pune","Bangalore"])
name = st.text_input("Enter your name")

if st.button("Show details"):
    st.write("Name",name)
    st.write("Age ",age)
    st.write("City",city)
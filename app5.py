import streamlit as st 


st.markdown("""
<style>
            .stButton > button
            {
                background-color:blue;
                color:white;
                border:1px solid black;
                border-radius:5%;
            }
</style>





""",unsafe_allow_html=True)

st.title("Welcome to basic streamlit app")

firstname = st.text_input("Enter your first name")
lastname = st.text_input("Enter your last name")
age = st.slider("Select your age",1,100)
# city = st.selectbox("Select your city",["Nashik","Mumbai","Pune","Bangalore"])

if st.button("Show details"):
    st.write("First Name : ",firstname)
    st.write("Last Name : ",lastname)
    st.write("Age : ",age)
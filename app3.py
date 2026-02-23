import streamlit as st 

st.title("Simple calculator")

num1 = st.number_input("Enter your first number",format="%d",min_value=0)
num2 = st.number_input("Enter your second number",format="%d",min_value=0)

option = st.selectbox("Choose operation",["Addition","Subtraction","Multiplication","Division"])

if st.button("Calculate"):
    if option == "Addition":
        st.write(num1 + num2)
    elif option == "Subtraction":
        st.write(num1 - num2)
    elif option == "Multiplication":
        st.write(num1 * num2)
    elif option == "Division":
        if num2 != 0:
            st.write(num1 / num2)
        else:
            st.write("Cannot divide")


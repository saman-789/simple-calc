import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
number1 = st.number_input("Enter the first number", value=0.0, format="%f")
number2 = st.number_input("Enter the second number", value=0.0, format="%f")

# Dropdown menu for selecting the operation
operation = st.selectbox("Select an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = number1 + number2
        st.write(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = number1 - number2
        st.write(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = number1 * number2
        st.write(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if number2 != 0:
            result = number1 / number2
            st.write(f"The result of division is: {result}")
        else:
            st.write("Division by zero is not allowed.")

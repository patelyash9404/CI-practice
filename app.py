import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"


st.title("Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

operation = st.selectbox(
    "Select an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result of {operation} is: {result}")

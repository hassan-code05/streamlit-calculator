import streamlit as st

# Page title
st.title("Simple Calculator")

# Short description
st.write("Enter two numbers, choose an operation, and click Calculate.")

# Number inputs
number1 = st.number_input("Enter the first number")
number2 = st.number_input("Enter the second number")

# Operation dropdown
operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
if st.button("Calculate"):

    if operation == "Addition":
        result = number1 + number2

    elif operation == "Subtraction":
        result = number1 - number2

    elif operation == "Multiplication":
        result = number1 * number2

    elif operation == "Division":
        if number2 == 0:
            st.error("Cannot divide by zero.")
        else:
            result = number1 / number2

    # Display result
    if operation != "Division" or number2 != 0:
        st.success(f"Result: {result}")

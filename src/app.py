import streamlit as st

st.title("Calculadora")

st.write("Esto es una calculadora muy sencilla que suma dos números.")

number = st.number_input(
    "Insert a number", value=None, placeholder="Escribe un numero..."
)

number2 = st.number_input(
    "Insert a second number", value=None, placeholder="Escribe un numero..."
)

result = number + number2
if result:
     st.write("El resultado de la suma es: ", result)
else:
     st.write("Introduce un número para sumar")

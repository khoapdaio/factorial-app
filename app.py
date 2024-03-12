import streamlit as st
from fatorial import fatorial


def main():
	st.title("Fatorial Calculator")
	number = st.number_input("Enter a number ", min_value=0, max_value=900)
	if st.button("Calculate"):
		result = fatorial(number)
		st.write(f"The factorial of {number} is {result}")


if __name__ == "__main__":
	main()

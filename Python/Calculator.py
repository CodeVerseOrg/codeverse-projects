# Simple calculation example
def simple_calculate():
	a = 5
	b = 3
	result = a + b
	print(f"{a} + {b} = {result}")

# Advanced Calculator in Python
import math

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		return "Error: Division by zero"
	return x / y

def power(x, y):
	return x ** y

def sqrt(x):
	if x < 0:
		return "Error: Negative square root"
	return math.sqrt(x)

def factorial(x):
	if x < 0 or not float(x).is_integer():
		return "Error: Factorial only defined for non-negative integers"
	return math.factorial(int(x))

def calculator():
	print("\n--- Advanced Calculator ---")
	print("Select operation:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	print("5. Power (x^y)")
	print("6. Square Root")
	print("7. Factorial")
	print("0. Exit")

	while True:
		choice = input("\nEnter choice (0-7): ")
		if choice == '0':
			print("Exiting Calculator. Goodbye!")
			break
		elif choice in ['1', '2', '3', '4', '5']:
			try:
				num1 = float(input("Enter first number: "))
				num2 = float(input("Enter second number: "))
			except ValueError:
				print("Invalid input. Please enter numbers.")
				continue
			if choice == '1':
				print(f"Result: {add(num1, num2)}")
			elif choice == '2':
				print(f"Result: {subtract(num1, num2)}")
			elif choice == '3':
				print(f"Result: {multiply(num1, num2)}")
			elif choice == '4':
				print(f"Result: {divide(num1, num2)}")
			elif choice == '5':
				print(f"Result: {power(num1, num2)}")
		elif choice == '6':
			try:
				num = float(input("Enter number: "))
			except ValueError:
				print("Invalid input. Please enter a number.")
				continue
			result = sqrt(num)
			print(f"Result: {result}")
		elif choice == '7':
			try:
				num = float(input("Enter number (non-negative integer): "))
			except ValueError:
				print("Invalid input. Please enter a number.")
				continue
			result = factorial(num)
			print(f"Result: {result}")
		else:
			print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
	calculator()

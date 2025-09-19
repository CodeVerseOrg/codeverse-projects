# Advanced Password Generator in Python
import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
	chars = ''
	if use_upper:
		chars += string.ascii_uppercase
	if use_lower:
		chars += string.ascii_lowercase
	if use_digits:
		chars += string.digits
	if use_symbols:
		chars += string.punctuation
	if not chars:
		return "Error: No character types selected."
	password = ''.join(random.choice(chars) for _ in range(length))
	return password

def main():
	print("\n--- Advanced Password Generator ---")
	try:
		length = int(input("Enter password length (default 12): ") or 12)
	except ValueError:
		print("Invalid input. Using default length 12.")
		length = 12
	use_upper = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
	use_lower = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
	use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
	use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
	password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
	print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
	main()

def check_password_strength(password):
	if len(password) < 6:
		return "Weak"
	elif 6 <= len(password) <= 10:
		return "Medium"
	else:
		letter = any(ch.isalpha() for ch in password)
		digit = any(ch.isdigit() for ch in password)
		if letter and digit:
			return "Strong"
		else:
			return "Medium"

password = input("Enter a password to check strength: ")
print(f"Your password strength is {(check_password_strength(password))}")

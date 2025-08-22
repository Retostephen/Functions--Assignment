'''
Write a function check_even_odds(n) that takes an integer n and returns:
"Even" if the number is even,
"Odd" if the  number is odd.
'''

def check_even_odd(n):
	if n % 2 == 0:
		return "Even"
	else:
		return "Odd"
n = int(input("Enter any Number: "))
print(check_even_odd(n))

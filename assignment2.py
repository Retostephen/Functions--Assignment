'''
Write a function count_vowels(text, vowels ="aeiou") that counts how many vowels appear in a given text
'''

def count_vowels(text, vowels = "aeiou"):
	count = 0
	for ch in text.lower():
		if ch in vowels:
			count += 1
	return count

text = input("Enter text to count number of vowels present: ")
print(count_vowels(text))

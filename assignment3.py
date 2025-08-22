def count_even(numbers):
	count = 0
	for num in numbers:
		if num % 2 == 0:
			count += 1
	return count

numb = input("Enter numbers with spaces in between: ")
numb = list(map(int, numb.split()))
print(count_even(numb))

numbers = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 8]
unique_numbers = set(numbers)
print(unique_numbers)

numbers_1 = [1, 5, 2, 9, 1, 6, 9]
numbers_2 = [3, 7, 2, 4, 6, 3, 8]
set1 = set(numbers_1)
set2 = set(numbers_2)
intersection = set1 & set2
count_unique_numbers = len(intersection)
print(f"Number of unique numbers in common: {count_unique_numbers}")

text = "The first line contains the number of rows, followed by the rows themselves."

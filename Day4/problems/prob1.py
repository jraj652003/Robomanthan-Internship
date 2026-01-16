

"""
    Given an array containing integers,
    return the average of the non-negative integers.
"""


numbers = [3, 7, 0, -4, 2, -5, 12, -33, 5, 9]
print("List:", numbers)

positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)

average_positive_numbers = sum(positive_numbers) / len(positive_numbers)
print(f"Average of non-negative integers: {average_positive_numbers:.2f}")

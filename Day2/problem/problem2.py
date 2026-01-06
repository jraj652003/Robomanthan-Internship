

"""
    data = [5, 3, 9, 1, 5, 10, 5, 2]
    Count how many times 5 appears.
    Find index of 10.
    Sort the list in descending order.
    Remove the last element.
    Print the list and its length.
"""


data = [5, 3, 9, 1, 5, 10, 5, 2]

print("Count of 5:", data.count(5))

print("Index of 10:", data.index(10))

# data.sort()
# data.reverse()
# OR
data.sort(reverse=True)
print("After sorting (descending):", data)

last_element = data.pop()
print("Last element:", last_element)
print("After removed last element:", data)

print("Length of the list:", len(data))
print("List:", data)


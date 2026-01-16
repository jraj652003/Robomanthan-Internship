

"""
    Given two list,
    find the repeating elements.
"""


a = [9, 3, 6, 2, 7, 4]
b = [1, 2, 3, 4, 5, 6]

c = []
for i in a:
    for j in b:
        if i == j and i not in c:
            c.append(i)

print(c)


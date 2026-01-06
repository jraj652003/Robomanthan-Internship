# 📘 Day 2 – Python List

📅 **Date:** 06/01/2026  

---

## Topic: List in Python

A List is a data structure that can hold an **ordered collection** of items.

- Can contain duplicate items
- **Mutable**: items can be modified, replaced or removed
- **Ordered**: maintains the order in which items are added
- **Index-based**: items are accessed using their positive (starting from 0)
- Can store mixed data types (integers, strings booleans, even other lists)

---

## Creating a List

List can be created using square brackets [].

```python
a = [1, 2, 3, 4, 5]                 # List of integers
b = ["Apple", "Banana", "Cherry"]   # List of strings
c = [1, "Hello", 3.14, True]        # Mixed data types

print(a)
print(b)
print(c)
```

Output:

```
[1, 2, 3, 4, 5]
['Apple', 'Banana', 'Cherry']
[1, 'Hello', 3.14, True]
```

---

## Accessing List Elements

Elements can be accessed using **indexing**. Indexes start from **0**, so a[0] gives the first element. Negative indexes allow access from the end (**-1** gives the last element).

```python
a = [10, 20, 30, 40, 50]

print(a[0])
print(a[1])
print(a[-1])
print(a[-2])
```

Output:

```
10
20
50
40
```

---

## Slicing

Slicing is a way to access specific elements in a list.<br>

Example: Get the items from a list starting at position 1 and ending at position 4 (exclusive).

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 1 to 4 (excluded)
print(a[1:4])
```

Output:

```
[2, 3, 4]
```

### Slicing Syntax

```
list_name[start:end:step]
```

Parameters:
- **start (optional):** Index to begin the slice (inclusive). Defaults to 0 if omitted.
- **end (optional):** Index to end the slice (exclusive). Defaults to the length of list if omitted.
- **step (optional):** Step size specifying the interval between elements. Defaults to 1 if omitted

Example:

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements starting from index 2 to the end of the list
print(a[2:])

# Get elements starting from index 0 to index 3 (excluding 3th index)
print(a[:3])

# Get elements from index 1 to index 4 (excluding index 4)
print(a[1:4])

# Get every second element from the list starting from the beginning
print(a[::2])

# Get every third element from the list starting from index 1 to 8 (exclusive)
print(a[1:8:3])
```

Output:

```
[3, 4, 5, 6, 7, 8, 9]
[1, 2, 3]
[2, 3, 4]
[1, 3, 5, 7, 9]
[2, 5, 8]
```

---

## Basic List Functions

- **append():** Adds an element at the end of the list.
- **insert():** Adds an element at a specific position.
- **remove():** Removes the first occurrence of an element.
- **pop():** Removes the element at a specific index or the last element if no index is specified.
- **index():** Returns the position of the first occurrence of a specified element in a list.
- **sort():** Arranges the elements of a list in ascending or descending order, modifying the list in place.

Example:

```python
a = [10, 20, 30, 40, 50]

a.append(10)
print("After append(10):", a)

a.insert(0, 50)
print("After insert(0, 50):", a)

a.remove(30)
print("After remove(30):", a)

popped_element = a.pop()
print("Popped element:", popped_element)
print("After pop():", a)

print("Index of 40:", a.index(40))

a.sort()
print("After sort():", a)

```

Output:

```
After append(10): [10, 20, 30, 40, 50, 10]
After insert(0, 50): [50, 10, 20, 30, 40, 50, 10]
After remove(30): [50, 10, 20, 40, 50, 10]
Popped element: 10
After pop(): [50, 10, 20, 40, 50]
Index of 40: 3
After sort(): [10, 20, 40, 50, 50]
```

---

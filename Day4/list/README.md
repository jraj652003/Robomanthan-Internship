# List Datatype

List is a data structure that can hold an ordered collection of items.

- **Mutable:** items can be modified, replaced, or removed
- **Ordered:** maintains the order in which items are added
- **Index-based:** items are accessed using their position (starting from 0)

## Creating a list

List can be created in several ways, such as using **square brackets**, the **list()** constructor or by **repeating elements**.

```python
# Using square brackets
a = [1, 2, 3, 4, 5]
print(a)

# Using list() constructor
b = list((6, 7, 8, 9, 10))
c = list("HELLO")
print(b)
print(c)

# Creating list with repeated elements
d = [2] * 5
e = [0] * 7
print(d)
print(e)
```

**Output:**

```
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
['H', 'E', 'L', 'L', 'O']
[2, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0]
```

## Accessing list elements

Elements in a list are accessed using indexing.

```python
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[-1])
print(a[1:4])
```

**Output:**

```
10
50
[20, 30, 40]
```

## Adding elements into list

We can add elements to a list using the following methods:

- **append()**: Adds an elements at the end of the list.
- **extend()**: Adds multiple elements to the end of the list.
- **insert()**: Adds an element at a specific position.
- **clear()**: removes all items.

```python
a = []

a.append(10)
print("After append(10):", a)

a.insert(0, 5)
print("After insert(0, 5):", a)

a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

a.clear()
print("After clear():", a)
```

**Output:**

```
After append(10): [10]
After insert(0, 5): [5, 10]
After extend([15, 20, 25]): [5, 10, 15, 20, 25]
After clear(): []
```

## Updating elements in list

We can update elements by accessing them via their index.

```python
a = [10, 20, 30, 40, 50]
a[1] = 25
print(a)
```

**Output:**

```
[10, 25, 30, 40, 50]
```

## Removing elements from list

We can remove elements from a list using:

- **remove():** Removes the first occurrence of an element.
- **pop():** Removes the element at a specific index or the last element if no index is specified.
- **del statement:** Deletes an element at a specified index.

```python
a = [10, 20, 30, 40, 50]

a.remove(30)
print("After remove(30):", a)

popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

del a[0]
print("After del a[0]:", a)
```

**Output:**

```
After remove(30): [10, 20, 40, 50]
Popped element: 20
After pop(1): [10, 40, 50]
After del a[0]: [40, 50]
```

## List Comprehension

List comprehension is a way to create lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as list or range.

```python
squares = [x**2 for x in range(1, 6)]
print(squares)
```

**Output:**

```
[1, 4, 9, 16, 25]
```

**Explanation:**
- **for x in range(1, 6):** loop through each number from 1 to 5 (excluding 6).
- **x\*\*2:** squares each number x.
- **[]:** collects all the squared numbers into a new list.

# Tuple Datatype

Tuple is an **immutable ordered** collection of elements. Ones created they cannot be changed.

## Creating a tuple

A tuple is created by placing all the items inside **parentheses ()**, separated by commas.

```python
tup = ()
print(tup)

# Using String
tup = ("Red", "Green", "Blue")
print(tup)

# Using List
li = [1, 2, 3, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple("Red")
print(tup)
```

**Output:**

```
()
('Red', 'Green', 'Blue')
(1, 2, 3, 4, 5, 6)
('R', 'e', 'd')
```

## Basic operations of tuple

- Accessing a element
- Concatenation of tuples
- Slicing of tuple
- Deleting a tuple

### Accessing a element

We can access the elements of a tuple by using **indexing** and **slicing**.

```python
# Accessing tuple with indexing
tup = tuple("Green")
print(tup[1])

# Accessing a range of elements using slicing
print(tup[1:4])
print(tup[:3])

# Tuple unpacking
tup = ("Red", "Green", "Blue")

# This line unpack values of tup
r, g, b = tup
print(r)
print(g)
print(b)
```

**Output:**

```
r
('r', 'e', 'e')
('G', 'r', 'e')
Red
Green
Blue
```

### Concatenation of tuples

Tuples can be concatenated using the **+** operator.

```python
tup1 = (0, 1, 2, 3)
tup2 = ("Red", "Green", "Blue")

tup3 = tup1 + tup2
print(tup3)
```

**Output:**

```
(0, 1, 2, 3, 'Red', 'Green', 'Blue')
```

### Slicing of tuple

Slicing a tuple means creating new tuple from a subset of elements of the original tuple.

```python
tup = tuple("HELLO WORLD")

# Removing first element
print(tup[1:])

# Reversing the tuple
print(tup[::-1])

# Printing elements of range
print(tup[2:5])
```

**Output:**

```
('E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D')
('D', 'L', 'R', 'O', 'W', ' ', 'O', 'L', 'L', 'E', 'H')
('L', 'L', 'O')
```

### Deleting a tuple

Since tuples are immutable we cannot delete individual elements of a tuple. We can delete an entire tuple using **del statement**.

```python
tup = (0, 1, 2, 3, 4)
del tup

print(tup)
```

**Output:**

```
ERROR!
Traceback ...
...
NameError: name 'tup' is not defined
```

## Tuple unpacking with asterisk (*)

**"*"** operator can be used in tuple unpacking to grab multiple items into a list.

```python
tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a)
print(b)
print(c)
```

**Output:**

```
1
[2, 3, 4]
5
```

# Dictionary Datatype

Dictionary is a data structure that stores data in **key-value pairs** where each key is **unique** and is used to retrieve its associated value.

## Creating a dictionary

A dictionary is created by writing key-value pairs inside **{}** where each key is connected to a value using colon **(:)**. A dictionary can also be created using **dict()** function.

```python
d1 = {
    1: "Red",
    2: "Green",
    3: "Blue"
}
print(d1)

# using dict() constructor
d2 = dict(
    r = "Red",
    g = "Green",
    b = "Blue"
)
print(d2)
```

**Output:**

```
{1: 'Red', 2: 'Green', 3: 'Blue'}
{'r': 'Red', 'g': 'Green', 'b': 'Blue'}
```

## Accessing dictionary items

A value in a dictionary is accessed by using its key. This can be done either with square brackets **[]** or with the **git()** method. Both return the value linked to the given key.

```python
d = {
    "name": "Uday",
    "age": 22,
    "mt": "Telugu"
}

# Access using key
print("Name:", d["name"])

# Access using git()
print("Mother Tongue:", d.git("mt"))
```

**Output:**

```
Uday
Telugu
```

## Adding and Updating dictionary items

New items are added to a dictionary using the assignment operator **(=)** by giving a new key a value. if an existing key is used with assignment operator its value is updated with the new one.

```python
d = {
    "r": "Red",
    "g": "Green"
}

# Adding a new key-value pair
d["b"] = "Blue"

# Updating an existing value
d["g"] = "Gray"

print(d)
```

**Output:**

```
{'r': 'Red', 'g': 'Gray', 'b': 'Blue'}
```

## Removing dictionary items

Dictionary items can be removed using built-in deletion methods that work on keys:

- **del:** removes an item using its key
- **pop():** removes the item with the given key and returns its value
- **clear():** removes all items from the dictionary
- **popitem():** removes and returns the last inserted key-value pair

```python
d = {
    "name": "Uday",
    "age": 22,
    "mt": "Telugu",
    "gender": "M"
}

# Using del
del d["age"]
print(d)

# Using pop()
val = d.pop("mt")
print(val)

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
d.clear()
print(d)
```

**Output:**

```
{'name': 'Uday', 'mt': 'Telugu', 'gender': 'M'}
Telugu
Key: gender, Value: M
{}
```

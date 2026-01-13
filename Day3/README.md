# 📘 Day 3 – String Slicing

📅 **Date:** 12/01/2026  

---

## Topic: String Slicing in Python

String slicing is a way to get specific parts of a string by using start, end and step values.

## Syntax of String Slicing

```
substring = s[start:end:step]
```

**Parameters:**
- **s:** The original string.
- **start (optional):** Starting index (inclusive). Defaults to **0** if omitted.
- **end (optional):** Stopping index (exclusive). Defaults to end of the string if omitted.
- **step (optional):** Interval between indices. A positive value slices from left to right, while a negative value slices from right to left. if omitted, it defaults to 1 (no skipping of characters).

**Return Type:** The result of a slicing operation is always a string (str type) that contains a subset of the characters from the original string.

## String Slicing Examples

```python
s = "Hello, World!"

# Get the entire string
print(s[:])
print(s[::])

# Characters from index 7 to the end
print(s[7:])

# Characters from the start up to index 5 (exclusive)
print(s[:5])

# Characters from index 1 to index 5 (excluding 5)
print(s[1:5])

s = "abcdefghi"

# Every second character
print(s[::2])

# Every third character from index 1 to 8 (exclusive)
print(s[1:8:3])
```

**Output:**

```
Hello, World!
Hello, World!
World!
Hello
ello
acegi
beh
```

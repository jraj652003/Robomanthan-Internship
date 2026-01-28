

"""
    Given a list of temperatures in Celsius, convert each temperature into
    Fahrenheit and store the converted values in a new list
"""


temps_celsius = [36, 47, 56, 32, 90]
temps_fahrenheit = []

for temp_celsius in temps_celsius:
    temp_fahrenheit = temp_celsius * (9 / 5) + 32
    temps_fahrenheit.append(temp_fahrenheit)

print("Temperatures in Celsius:", temps_celsius)
print("Temperatures in Fahrenheit:", temps_fahrenheit)


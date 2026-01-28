

"""
    Given a string containing Celsius temperatures separated by underscore _,
    convert each temperature into Fahrenheit and store the results in a list
"""


temp = "12_30_60_80"

temps_celsius_str = temp.split("_")
temps_fahrenheit = []

for temp_celsius_str in temps_celsius_str:
    temp_celsius = int(temp_celsius_str)
    temp_fahrenheit = temp_celsius * (9 / 5) + 32
    temps_fahrenheit.append(temp_fahrenheit)

print("Temperatures in Celsius (string):", temps_celsius_str)
print("Temperatures in Fahrenheit:", temps_fahrenheit)


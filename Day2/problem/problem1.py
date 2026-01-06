

"""
    Create a list called 'inventory' with "Map", "Potion", "Shield".
    Append the element "Sward" to this list.
    Add the element "Gold Key" to the top of the list.
    Remove the Potion"
    Print the final list and the length of it.
"""


inventory = ["Map", "Potion", "Shield"]
print("Initial Inventory:", inventory)

inventory.append("Sword")
print("I picked up a sword:", inventory)

inventory.insert(0, "Gold Key")
print("Found the gold key:", inventory)

inventory.remove("Potion")
print("Used up the potion:", inventory)

print("Number of items left in the inventory:", len(inventory))
print("Inventory:", inventory)



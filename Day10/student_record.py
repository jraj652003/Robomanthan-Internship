

"""
    Write a program that:
        Takes input from the user for the number of students in a class
        For each student, record their roll number, name, and phone number
        Store each student's detail as a tuple inside a list
        Displays all student records in a clear and user-friendly format
"""


student_records = []

class_strength = int(input("Enter the number of students in the class: "))

for _ in range(class_strength):
    roll_number = int(input("\nEnter the roll number: "))
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    
    student_record = (roll_number, name, phone_number)
    student_records.append(student_record)

print("\nStudent Records:")
for record in student_records:
    print("\n\tRoll Number:", record[0])
    print("\tName:", record[1])
    print("\tPhone Number:", record[2])


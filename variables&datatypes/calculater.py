# Get input from the user
number_1 = float(input("Enter the value no1: "))
number_2 = float(input("Enter the value no2: "))

# Define functions for arithmetic operations
def add(no1, no2):
    return no1 + no2

def subtract(no1, no2):  # Fixed typo: "substract" → "subtract"
    return no1 - no2

def multiply(no1, no2):
    return no1 * no2

def divide(no1, no2):
    if no2 == 0:
        return "Error: Division by zero is not allowed!"
    return no1 / no2

# Display input values
print("Number 1:", number_1)
print("Number 2:", number_2)

# Get the user's choice
print("Enter your choice:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Choice: ")

# Perform the chosen operation
if choice == "1":
    print("Result:", add(number_1, number_2))
elif choice == "2":
    print("Result:", subtract(number_1, number_2))
elif choice == "3":
    print("Result:", multiply(number_1, number_2))
elif choice == "4":
    print("Result:", divide(number_1, number_2))
else:
    print("Invalid choice")


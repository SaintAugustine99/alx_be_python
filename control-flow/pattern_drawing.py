# Prompts the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initializes the row counter
row = 0

# Uses a while loop to iterate through each row
while row < size:
    # Uses a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
    # Prints a newline character to move to the next row
    print()
    # Increments the row counter
    row += 1

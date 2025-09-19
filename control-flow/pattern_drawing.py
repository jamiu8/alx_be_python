# pattern_drawing.py

# Prompt the user for the size of the square
size = int(input("Enter the size of the pattern: "))

# Ensure the size is positive
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    # Outer loop with while -> controls rows
    while row < size:
        # Inner loop with for -> controls columns
        for col in range(size):
            print("*", end="")  # print star without newline
        print()  # move to the next line after finishing one row
        row += 1

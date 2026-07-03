# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C" -> Formula: (value x 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F" -> Formula: (value - 32) x 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

def convertTemp(value, unit):
    # Add your code here
    # Check the unit and use the right formula.
    if unit == "C":
        return round((value * 9 / 5) + 32, 2)
    if unit == "F":
        return round((value - 32) * 5 / 9, 2)

    # If the unit is not C or F, return -1.
    return -1


# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")      -> Expected: 212.0
#   convertTemp(32, "F")       -> Expected: 0.0
#   convertTemp(37, "C")       -> Expected: 98.6
#   convertTemp("invalid", "X") -> Expected: -1

# Add your code here
# Try out the function with the values given above.
print(convertTemp(100, "C"))
print(convertTemp(32, "F"))
print(convertTemp(37, "C"))
print(convertTemp("invalid", "X"))

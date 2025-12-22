# 1. Basic if Statement
# if is used to execute a block of code only if a condition is True.
x = 10
if x > 5:
    print("x is greater than 5")
# Output:
# x is greater than 5

# 2. if-else
# else is used to execute a block when the if condition is False.

x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# Output:
# x is 5 or less

# 3. if-elif-else
# elif (else if) allows checking multiple conditions in order.

x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")

# Output:
# x is greater than 5 but less than or equal to 10

# Key points:
# Python evaluates conditions top-down.
# Only one block executes.

# 4. Multiple elif Cases
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# Output:
# Grade B

# 5. Nested if-else
# You can nest if-else inside another if or elif.

x = 15
y = 20

if x > 10:
    if y > 15:
        print("x > 10 and y > 15")
    else:
        print("x > 10 but y <= 15")
else:
    print("x <= 10")

# Output:
# x > 10 and y > 15

# 6. Single-line if and else (ternary operator)
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)


# Output:
# Odd

# 7. if without else (optional)
x = 3
if x > 0:
    print("Positive number")
# No else required

# Output:
# Positive number

# 8. Edge Cases & Tricks
# 8.1 Multiple conditions with and / or
x = 8
y = 5

if x > 5 and y > 5:
    print("Both are greater than 5")
elif x > 5 or y > 5:
    print("At least one is greater than 5")
else:
    print("Both are 5 or less")

# Output:
# At least one is greater than 5

# 8.2 Checking membership with in
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")

# Output:
# Banana is in the list

# 8.3 Checking for truthy/falsy values
x = []
if x:
    print("List is not empty")
else:
    print("List is empty")

# Output:
# List is empty

# In Python, empty containers ([], {}, (), '') and 0/None are considered False.

# 9. Common mistakes
# Indentation errors
"""
x = 10
if x > 5:
print("x is greater than 5")  # ❌ Wrong indentation
"""

# Using multiple else
"""
x = 5
if x > 0:
    print("Positive")
else:
    print("Zero")  # ✅ Correct
else:
    print("Negative")  # ❌ Error: cannot have 2 else
"""

aa=200
if aa>5:
    print("y1")
if aa>50:
    print("y2")
if aa>55:
    print("y3")
elif aa>65:
    print("y4")
else:
    print("y5")
# output
# y1
# y2
# y3

"""

"""
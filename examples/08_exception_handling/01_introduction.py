"""
=========================================================
Python Exception Handling - Introduction
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 01_introduction.py

Description
-----------
Exception handling allows Python programs to deal with
unexpected errors without immediately terminating the
entire program.

Topics Covered
--------------
✔ What is an Exception?
✔ Error vs Exception
✔ Common Python Exceptions
✔ Why Exception Handling is Important
✔ Real-world Examples
"""

print("=" * 60)
print("EXCEPTION HANDLING - INTRODUCTION")
print("=" * 60)

# =====================================================
# Example 1 - What is an Exception?
# =====================================================

print("\nExample 1 - Exception")

print("""
An exception is an unexpected event that occurs
while a Python program is running.

Example:

10 / 0

This causes a ZeroDivisionError.
""")

# =====================================================
# Example 2 - ZeroDivisionError
# =====================================================

print("\nExample 2 - ZeroDivisionError")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# =====================================================
# Example 3 - ValueError
# =====================================================

print("\nExample 3 - ValueError")

try:
    number = int("hello")
except ValueError:
    print("Invalid number.")

# =====================================================
# Example 4 - TypeError
# =====================================================

print("\nExample 4 - TypeError")

try:
    result = "10" + 5
except TypeError:
    print("Cannot add string and integer.")

# =====================================================
# Example 5 - IndexError
# =====================================================

print("\nExample 5 - IndexError")

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Index does not exist.")

# =====================================================
# Example 6 - KeyError
# =====================================================

print("\nExample 6 - KeyError")

student = {
    "name": "Dhruvi",
    "age": 21
}

try:
    print(student["marks"])
except KeyError:
    print("Key does not exist.")

# =====================================================
# Example 7 - FileNotFoundError
# =====================================================

print("\nExample 7 - FileNotFoundError")

try:
    with open("missing_file.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File was not found.")

# =====================================================
# Example 8 - Multiple Exceptions
# =====================================================

print("\nExample 8 - Multiple Exceptions")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")

# =====================================================
# Example 9 - Why Exception Handling?
# =====================================================

print("\nExample 9 - Why Exception Handling?")

print("""
Without exception handling:

    User Input
        ↓
    Invalid Data
        ↓
    Program Crashes

With exception handling:

    User Input
        ↓
    Invalid Data
        ↓
    Exception Detected
        ↓
    Error Handled
        ↓
    Program Continues
""")

# =====================================================
# Example 10 - AI Engineering Example
# =====================================================

print("\nExample 10 - AI Engineering")

try:

    model_accuracy = float("98.5")

    if not 0 <= model_accuracy <= 100:
        raise ValueError("Accuracy must be between 0 and 100.")

    print(f"Model Accuracy: {model_accuracy}%")

except ValueError as error:

    print(f"Invalid model accuracy: {error}")

# =====================================================
# Common Python Exceptions
# =====================================================

print("\nCommon Python Exceptions")

print("""
ZeroDivisionError
    Division by zero.

ValueError
    Invalid value.

TypeError
    Invalid data type operation.

IndexError
    Invalid list/sequence index.

KeyError
    Missing dictionary key.

FileNotFoundError
    Requested file does not exist.

AttributeError
    Object does not have requested attribute.

NameError
    Variable or name does not exist.

ImportError
    Import operation fails.
""")

# =====================================================
# Error vs Exception
# =====================================================

print("\nError vs Exception")

print("""
Error
-----
A problem that prevents a program from
running or functioning correctly.

Exception
---------
An abnormal event during program execution
that can often be handled by the program.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Handle expected exceptions.

✔ Use specific exception types.

✔ Keep try blocks small.

✔ Provide useful error messages.

✔ Do not silently ignore errors.

✔ Log important production errors.

✔ Never use exceptions as a replacement
  for normal program logic.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is an exception?

A. An exception is an unexpected event that
occurs during program execution.

Q. Why do we use exception handling?

A. To handle runtime problems gracefully
and prevent unnecessary program crashes.

Q. Name common Python exceptions.

A.
• ValueError
• TypeError
• IndexError
• KeyError
• ZeroDivisionError
• FileNotFoundError

Q. What happens if an exception is not handled?

A. The program terminates and Python displays
an error traceback.

Q. Can every exception be handled?

A. Many runtime exceptions can be handled,
but handling should be appropriate rather
than hiding genuine programming bugs.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Exceptions occur during program execution.

✔ Exception handling prevents expected
runtime problems from crashing applications.

✔ Python provides many built-in exception types.

✔ Specific exceptions should be handled
instead of catching everything blindly.

✔ Exception handling is essential for
production applications, APIs, automation,
data pipelines, and AI/ML systems.
""")

"""
=========================================================
Python Try-Except
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 02_try_except.py

Description
-----------
The try-except statement is used to handle exceptions
that may occur while a Python program is running.

If an exception occurs inside the try block, Python
moves to the appropriate except block instead of
immediately terminating the program.

Topics Covered
--------------
✔ Basic try-except
✔ Handling Specific Exceptions
✔ Multiple except Blocks
✔ Exception as Variable
✔ User Input Validation
✔ Nested try-except
✔ Multiple Operations
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("TRY-EXCEPT")
print("=" * 60)

# =====================================================
# Example 1 - Basic try-except
# =====================================================

print("\nExample 1 - Basic try-except")

try:
    result = 10 / 2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# =====================================================
# Example 2 - Handling ZeroDivisionError
# =====================================================

print("\nExample 2 - ZeroDivisionError")

try:
    number = 0
    result = 100 / number
    print(result)

except ZeroDivisionError:
    print("Error: Number cannot be zero.")

# =====================================================
# Example 3 - Handling ValueError
# =====================================================

print("\nExample 3 - ValueError")

try:
    age = int("twenty")
    print(age)

except ValueError:
    print("Error: Please provide a valid integer.")

# =====================================================
# Example 4 - Multiple except Blocks
# =====================================================

print("\nExample 4 - Multiple except Blocks")

try:

    number = int("hello")

    result = 100 / number

    print(result)

except ValueError:
    print("Invalid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# =====================================================
# Example 5 - TypeError
# =====================================================

print("\nExample 5 - TypeError")

try:

    result = "Python" + 10

    print(result)

except TypeError:
    print("Error: Cannot combine these data types.")

# =====================================================
# Example 6 - IndexError
# =====================================================

print("\nExample 6 - IndexError")

numbers = [10, 20, 30]

try:

    print(numbers[10])

except IndexError:
    print("Error: Index is outside the list.")

# =====================================================
# Example 7 - KeyError
# =====================================================

print("\nExample 7 - KeyError")

student = {
    "name": "Dhruvi",
    "age": 21
}

try:

    print(student["marks"])

except KeyError:
    print("Error: 'marks' key does not exist.")

# =====================================================
# Example 8 - Exception as Variable
# =====================================================

print("\nExample 8 - Exception as Variable")

try:

    result = 10 / 0

except ZeroDivisionError as error:

    print("Exception:", error)

# =====================================================
# Example 9 - User Input Validation
# =====================================================

print("\nExample 9 - User Input Validation")

user_input = "25"

try:

    number = int(user_input)

    print("Valid Number:", number)

except ValueError:

    print("Invalid input. Enter a number.")

# =====================================================
# Example 10 - Multiple Operations
# =====================================================

print("\nExample 10 - Multiple Operations")

try:

    number = int("50")

    result = 100 / number

    print("Result:", result)

except ValueError:

    print("Invalid number.")

except ZeroDivisionError:

    print("Division by zero is not allowed.")

# =====================================================
# Example 11 - Nested try-except
# =====================================================

print("\nExample 11 - Nested try-except")

try:

    print("Outer try block")

    try:

        result = 10 / 0

    except ZeroDivisionError:

        print("Inner exception handled.")

except Exception:

    print("Outer exception handled.")

# =====================================================
# Example 12 - Catching Multiple Exceptions
# =====================================================

print("\nExample 12 - Multiple Exceptions")

try:

    value = int("abc")

except (ValueError, TypeError):

    print("Invalid value or type.")

# =====================================================
# Example 13 - File Handling
# =====================================================

print("\nExample 13 - File Handling")

try:

    with open("data.txt", "r") as file:

        content = file.read()

        print(content)

except FileNotFoundError:

    print("Error: File does not exist.")

# =====================================================
# Example 14 - AI Engineering Example
# =====================================================

print("\nExample 14 - AI Engineering")


def calculate_accuracy(correct, total):

    try:

        accuracy = (correct / total) * 100

        return accuracy

    except ZeroDivisionError:

        print("Error: Total predictions cannot be zero.")

        return 0


print(
    "Accuracy:",
    calculate_accuracy(95, 100),
    "%"
)

print(
    "Accuracy:",
    calculate_accuracy(95, 0),
    "%"
)

# =====================================================
# Example 15 - Model Prediction
# =====================================================

print("\nExample 15 - Model Prediction")


def predict(model_name, input_value):

    try:

        value = float(input_value)

        print(
            f"{model_name} prediction input:",
            value
        )

    except ValueError:

        print("Prediction failed: Invalid input.")


predict("ImageClassifier", "0.85")

predict("ImageClassifier", "unknown")

# =====================================================
# Important Rule
# =====================================================

print("\nImportant Rule")

print("""
try:
    risky_operation()

except SpecificException:
    handle_error()

Python executes the except block only when
the matching exception occurs.
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Using an empty except block.

❌ Catching Exception everywhere.

❌ Hiding programming bugs.

❌ Putting too much code inside try.

❌ Using one generic error message
   for completely different problems.

❌ Ignoring the actual exception information.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Catch specific exceptions.

✔ Keep try blocks small.

✔ Use `as error` when the error
  message is useful.

✔ Give users meaningful messages.

✔ Handle only exceptions you expect.

✔ Let unexpected programming errors
  remain visible during development.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is try-except?

A. It is a Python mechanism used to
handle runtime exceptions.

Q. What happens when an exception occurs
inside try?

A. Python stops executing the remaining
try block and searches for a matching
except block.

Q. Can we have multiple except blocks?

A. Yes.

Q. Can one except handle multiple exceptions?

A. Yes.

Example:

except (ValueError, TypeError):
    pass

Q. What is `as error` used for?

A. It stores the exception object so that
we can inspect or display its message.

Q. Should we always use `except Exception`?

A. No. Specific exceptions are generally
better because they avoid hiding unrelated
programming errors.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ try contains code that may raise an exception.

✔ except handles matching exceptions.

✔ Multiple except blocks can handle
  different exception types.

✔ Specific exception handling is preferred.

✔ try-except is essential for reliable
  applications, APIs, data pipelines,
  automation, and AI/ML systems.
""")

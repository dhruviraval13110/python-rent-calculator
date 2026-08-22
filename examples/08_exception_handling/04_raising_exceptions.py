"""
=========================================================
Python Raising Exceptions
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 04_raising_exceptions.py

Description
-----------
Python allows developers to intentionally raise exceptions
when invalid conditions are detected.

The `raise` statement is used to manually generate an
exception.

Topics Covered
--------------
✔ raise statement
✔ Raising Built-in Exceptions
✔ Custom Error Messages
✔ Input Validation
✔ raise inside Functions
✔ Re-raising Exceptions
✔ AI Engineering Validation
✔ Best Practices
"""

print("=" * 60)
print("RAISING EXCEPTIONS")
print("=" * 60)

# =====================================================
# Example 1 - Basic raise
# =====================================================

print("\nExample 1 - Basic raise")

try:

    raise ValueError("Something went wrong.")

except ValueError as error:

    print("Error:", error)

# =====================================================
# Example 2 - Raise ValueError
# =====================================================

print("\nExample 2 - ValueError")

age = -5

try:

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age:", age)

except ValueError as error:

    print("Error:", error)

# =====================================================
# Example 3 - Input Validation
# =====================================================

print("\nExample 3 - Input Validation")


def set_age(age):

    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150.")

    return age


try:

    print(set_age(21))

except ValueError as error:

    print("Invalid age:", error)

# =====================================================
# Example 4 - Raise TypeError
# =====================================================

print("\nExample 4 - TypeError")


def calculate_square(number):

    if not isinstance(number, (int, float)):
        raise TypeError("Number must be an integer or float.")

    return number ** 2


try:

    print(calculate_square(10))

    print(calculate_square("10"))

except TypeError as error:

    print("Type Error:", error)

# =====================================================
# Example 5 - Raise ZeroDivisionError
# =====================================================

print("\nExample 5 - ZeroDivisionError")


def divide(a, b):

    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    return a / b


try:

    print(divide(20, 4))

    print(divide(20, 0))

except ZeroDivisionError as error:

    print("Division Error:", error)

# =====================================================
# Example 6 - Raise inside try
# =====================================================

print("\nExample 6 - raise inside try")

try:

    balance = 500

    withdrawal = 1000

    if withdrawal > balance:
        raise ValueError("Insufficient balance.")

    balance -= withdrawal

except ValueError as error:

    print("Transaction failed:", error)

# =====================================================
# Example 7 - Raising Exception in a Function
# =====================================================

print("\nExample 7 - Function Validation")


def register_user(username):

    if not username:
        raise ValueError("Username cannot be empty.")

    return f"User '{username}' registered successfully."


try:

    print(register_user("Dhruvi"))

except ValueError as error:

    print("Registration Error:", error)

# =====================================================
# Example 8 - Re-raising an Exception
# =====================================================

print("\nExample 8 - Re-raising")


def process_number(value):

    try:

        return int(value)

    except ValueError:

        print("Logging invalid input.")

        raise


try:

    process_number("Python")

except ValueError as error:

    print("Exception received by caller:", error)

# =====================================================
# Example 9 - Custom Validation
# =====================================================

print("\nExample 9 - Password Validation")


def validate_password(password):

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters."
        )

    return "Password accepted."


try:

    print(validate_password("abc"))

except ValueError as error:

    print("Password Error:", error)

# =====================================================
# Example 10 - AI Engineering Example
# =====================================================

print("\nExample 10 - AI Model Validation")


def validate_model_accuracy(accuracy):

    if not isinstance(accuracy, (int, float)):
        raise TypeError(
            "Accuracy must be a number."
        )

    if accuracy < 0 or accuracy > 100:
        raise ValueError(
            "Accuracy must be between 0 and 100."
        )

    return accuracy


try:

    accuracy = validate_model_accuracy(98.5)

    print(f"Model Accuracy: {accuracy}%")

except (TypeError, ValueError) as error:

    print("Model Validation Error:", error)

# =====================================================
# Example 11 - Dataset Validation
# =====================================================

print("\nExample 11 - Dataset Validation")


def validate_dataset(rows):

    if rows <= 0:
        raise ValueError(
            "Dataset must contain at least one row."
        )

    return "Dataset is valid."


try:

    print(validate_dataset(1000))

    print(validate_dataset(0))

except ValueError as error:

    print("Dataset Error:", error)

# =====================================================
# Example 12 - API-style Validation
# =====================================================

print("\nExample 12 - API Validation")


def predict(age):

    if age is None:
        raise ValueError("Age is required.")

    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return "Prediction generated."


try:

    print(predict(21))

except (TypeError, ValueError) as error:

    print("Prediction Error:", error)

# =====================================================
# raise vs return
# =====================================================

print("\nraise vs return")

print("""
return
------
Returns a normal result from a function.

Example:

return result

--------------------------------

raise
-----
Stops normal execution and reports
an exceptional condition.

Example:

raise ValueError("Invalid value")
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Raising exceptions for normal program flow.

❌ Using vague error messages.

❌ Raising the wrong exception type.

❌ Catching an exception immediately
   without doing anything useful.

❌ Hiding the original exception.

❌ Using `raise Exception()` for every problem.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Raise specific exception types.

✔ Provide meaningful error messages.

✔ Validate input at system boundaries.

✔ Use ValueError for invalid values.

✔ Use TypeError for invalid types.

✔ Re-raise exceptions when higher-level
  code needs to handle them.

✔ Do not use exceptions as normal
  control flow.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is the purpose of raise?

A. It manually triggers an exception.

Q. Which keyword is used to raise
an exception?

A. raise

Q. Why use raise?

A. To stop execution when an invalid
condition is detected and communicate
the problem to the caller.

Q. What is the difference between
raise and return?

A.

return:
Returns a normal result.

raise:
Signals an exceptional condition.

Q. Can we re-raise an exception?

A. Yes.

Inside an except block:

raise

re-raises the current exception.

Q. Which exception should be used for
an invalid value?

A. ValueError.

Q. Which exception should be used for
an incorrect data type?

A. TypeError.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ `raise` manually generates exceptions.

✔ It is useful for validation.

✔ ValueError is commonly used for
  invalid values.

✔ TypeError is used for invalid types.

✔ Exceptions can be re-raised.

✔ Explicit validation is important in
  APIs, AI pipelines, data processing,
  and production applications.
""")

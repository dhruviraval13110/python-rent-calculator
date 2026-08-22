"""
=========================================================
Python Assertions
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 06_assertions.py

Description
-----------
Assertions are used to check whether a condition is true
during program execution.

The `assert` statement is mainly useful for debugging,
development, testing, and checking assumptions in code.

Syntax
------
assert condition

or

assert condition, "error message"

Topics Covered
--------------
✔ What is an Assertion?
✔ Basic assert
✔ AssertionError
✔ Custom Assertion Messages
✔ Assertions in Functions
✔ Data Validation
✔ AI/ML Examples
✔ Assertions vs Exceptions
✔ Best Practices
"""

print("=" * 60)
print("ASSERTIONS")
print("=" * 60)

# =====================================================
# Example 1 - Basic Assertion
# =====================================================

print("\nExample 1 - Basic Assertion")

age = 21

assert age >= 18

print("Age is valid.")

# =====================================================
# Example 2 - Failed Assertion
# =====================================================

print("\nExample 2 - Failed Assertion")

try:

    age = 15

    assert age >= 18

except AssertionError:

    print("Assertion failed: Age must be 18 or older.")

# =====================================================
# Example 3 - Assertion with Message
# =====================================================

print("\nExample 3 - Assertion Message")

try:

    marks = 120

    assert 0 <= marks <= 100, \
        "Marks must be between 0 and 100."

except AssertionError as error:

    print("Assertion Error:", error)

# =====================================================
# Example 4 - Checking a Number
# =====================================================

print("\nExample 4 - Number Validation")

number = 10

assert number > 0, "Number must be positive."

print("Number is positive.")

# =====================================================
# Example 5 - Function Assertion
# =====================================================

print("\nExample 5 - Function")


def calculate_square(number):

    assert isinstance(
        number,
        (int, float)
    ), "Input must be a number."

    return number ** 2


try:

    print(calculate_square(10))

    print(calculate_square("10"))

except AssertionError as error:

    print("Assertion Error:", error)

# =====================================================
# Example 6 - List Validation
# =====================================================

print("\nExample 6 - List Validation")

numbers = [10, 20, 30]

assert len(numbers) > 0, \
    "List cannot be empty."

print("List contains data.")

# =====================================================
# Example 7 - Dictionary Validation
# =====================================================

print("\nExample 7 - Dictionary Validation")

student = {
    "name": "Dhruvi",
    "age": 21
}

try:

    assert "name" in student, \
        "Student name is required."

    assert "age" in student, \
        "Student age is required."

    print("Student data is valid.")

except AssertionError as error:

    print("Validation Error:", error)

# =====================================================
# Example 8 - Range Validation
# =====================================================

print("\nExample 8 - Range Validation")

score = 85

try:

    assert 0 <= score <= 100, \
        "Score must be between 0 and 100."

    print("Score is valid.")

except AssertionError as error:

    print("Score Error:", error)

# =====================================================
# Example 9 - AI Model Accuracy
# =====================================================

print("\nExample 9 - AI Model Accuracy")


def validate_accuracy(accuracy):

    assert 0 <= accuracy <= 100, \
        "Accuracy must be between 0 and 100."

    print(
        f"Model accuracy: {accuracy}%"
    )


try:

    validate_accuracy(95.5)

    validate_accuracy(120)

except AssertionError as error:

    print("Model Validation Error:", error)

# =====================================================
# Example 10 - Dataset Validation
# =====================================================

print("\nExample 10 - Dataset Validation")


def validate_dataset(data):

    assert data is not None, \
        "Dataset cannot be None."

    assert len(data) > 0, \
        "Dataset cannot be empty."

    return "Dataset is valid."


try:

    dataset = [10, 20, 30]

    print(validate_dataset(dataset))

except AssertionError as error:

    print("Dataset Error:", error)

# =====================================================
# Example 11 - Feature Validation
# =====================================================

print("\nExample 11 - Feature Validation")


def predict(features):

    assert len(features) == 4, \
        "Model expects exactly 4 features."

    return "Prediction generated."


try:

    print(
        predict(
            [5.1, 3.5, 1.4, 0.2]
        )
    )

except AssertionError as error:

    print("Feature Error:", error)

# =====================================================
# Example 12 - Model State
# =====================================================

print("\nExample 12 - Model State")


class Model:

    def __init__(self):

        self.is_trained = False

    def predict(self):

        assert self.is_trained, \
            "Model must be trained before prediction."

        return "Prediction successful."


model = Model()

try:

    print(model.predict())

except AssertionError as error:

    print("Model Error:", error)

# =====================================================
# Example 13 - Assertion after Training
# =====================================================

print("\nExample 13 - Trained Model")

model.is_trained = True

try:

    print(model.predict())

except AssertionError as error:

    print("Model Error:", error)

# =====================================================
# Assertions vs Exceptions
# =====================================================

print("\nAssertions vs Exceptions")

print("""
ASSERTION
---------

Used mainly for:

✔ Development

✔ Debugging

✔ Internal assumptions

✔ Testing programmer assumptions


EXCEPTION
---------

Used mainly for:

✔ User input validation

✔ File errors

✔ API errors

✔ Database errors

✔ Runtime failures

✔ Production error handling
""")

# =====================================================
# Important Difference
# =====================================================

print("\nImportant Difference")

print("""
Use:

assert condition

when you are checking an assumption
that should normally always be true.

Use:

raise ValueError(...)

when you need reliable runtime
validation in application code.
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Using assert as the only validation
   for user input.

❌ Using assert for security checks.

❌ Using assert for production-critical
   validation.

❌ Writing assertions without useful
   error messages.

❌ Assuming assertions always execute.
""")

# =====================================================
# Python -O Warning
# =====================================================

print("\nImportant Python Behavior")

print("""
Python can be run in optimized mode:

python -O program.py

In optimized mode, assertions can be
removed.

Therefore, assertions should NOT be used
for security-critical or mandatory
production validation.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use assertions for internal assumptions.

✔ Write meaningful assertion messages.

✔ Use exceptions for external/user input.

✔ Use assertions during development and testing.

✔ Do not rely on assert for security checks.

✔ Use proper validation for production systems.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is an assertion?

A. An assertion is a statement used to check
whether a condition is true.

Q. Which keyword is used for assertions?

A. assert

Q. What happens when an assertion fails?

A. Python raises AssertionError.

Q. Can assertions have custom messages?

A. Yes.

Example:

assert age >= 18, "Age must be 18 or older"

Q. Should assert be used for user input validation?

A. Generally no. Explicit exceptions such as
ValueError are more appropriate.

Q. Can assertions be disabled?

A. Yes. Running Python with optimization
can remove assertions.

Q. What is the difference between assert
and raise?

A. assert is mainly for programmer assumptions
and debugging, while raise is used to explicitly
signal runtime/application errors.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Assertions check assumptions.

✔ Failed assertions raise AssertionError.

✔ Custom messages make assertions easier
  to understand.

✔ Assertions are useful in development,
  debugging, and testing.

✔ Do not use assertions as a replacement
  for production validation.

✔ In AI/ML, assertions can help verify
  dataset shape, feature count, model state,
  and metric ranges.
""")

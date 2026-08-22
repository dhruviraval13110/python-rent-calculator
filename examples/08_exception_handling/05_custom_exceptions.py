"""
=========================================================
Python Custom Exceptions
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 05_custom_exceptions.py

Description
-----------
Python allows developers to create their own exception
classes for application-specific errors.

Custom exceptions make large applications easier to
understand, debug, maintain, and scale.

Topics Covered
--------------
✔ What are Custom Exceptions?
✔ Creating Exception Classes
✔ Raising Custom Exceptions
✔ Handling Custom Exceptions
✔ Custom Exception with Attributes
✔ Multiple Custom Exceptions
✔ Inheritance with Exceptions
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("CUSTOM EXCEPTIONS")
print("=" * 60)


# =====================================================
# Example 1 - Basic Custom Exception
# =====================================================

print("\nExample 1 - Basic Custom Exception")


class MyCustomError(Exception):
    pass


try:
    raise MyCustomError("This is a custom error.")

except MyCustomError as error:
    print("Error:", error)


# =====================================================
# Example 2 - Custom Age Exception
# =====================================================

print("\nExample 2 - Age Validation")


class InvalidAgeError(Exception):
    pass


def validate_age(age):

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    if age > 150:
        raise InvalidAgeError("Age must be below 150.")

    return "Age is valid."


try:

    print(validate_age(21))

except InvalidAgeError as error:

    print("Age Error:", error)


# =====================================================
# Example 3 - Custom Balance Exception
# =====================================================

print("\nExample 3 - Banking Exception")


class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance."
            )

        self.balance -= amount

        return self.balance


account = BankAccount(5000)

try:

    print("Remaining Balance:",
          account.withdraw(7000))

except InsufficientBalanceError as error:

    print("Transaction Error:", error)


# =====================================================
# Example 4 - Custom Exception with Attributes
# =====================================================

print("\nExample 4 - Custom Exception Attributes")


class InvalidMarksError(Exception):

    def __init__(self, marks):

        self.marks = marks

        message = (
            f"Invalid marks: {marks}. "
            "Marks must be between 0 and 100."
        )

        super().__init__(message)


def validate_marks(marks):

    if marks < 0 or marks > 100:
        raise InvalidMarksError(marks)

    return True


try:

    validate_marks(120)

except InvalidMarksError as error:

    print("Error:", error)
    print("Invalid Marks:", error.marks)


# =====================================================
# Example 5 - Multiple Custom Exceptions
# =====================================================

print("\nExample 5 - Multiple Custom Exceptions")


class InvalidUsernameError(Exception):
    pass


class WeakPasswordError(Exception):
    pass


def register_user(username, password):

    if not username:
        raise InvalidUsernameError(
            "Username cannot be empty."
        )

    if len(password) < 8:
        raise WeakPasswordError(
            "Password must contain at least 8 characters."
        )

    return "User registered successfully."


try:

    print(register_user("Dhruvi", "123"))

except InvalidUsernameError as error:

    print("Username Error:", error)

except WeakPasswordError as error:

    print("Password Error:", error)


# =====================================================
# Example 6 - Exception Inheritance
# =====================================================

print("\nExample 6 - Exception Inheritance")


class ApplicationError(Exception):
    """Base application exception."""


class DatabaseError(ApplicationError):
    """Database-related error."""


class AuthenticationError(ApplicationError):
    """Authentication-related error."""


try:

    raise DatabaseError(
        "Database connection failed."
    )

except ApplicationError as error:

    print("Application Error:", error)


# =====================================================
# Example 7 - Custom Exception with Error Code
# =====================================================

print("\nExample 7 - Error Code")


class APIError(Exception):

    def __init__(self, message, code):

        self.message = message
        self.code = code

        super().__init__(message)


try:

    raise APIError(
        "Invalid API request.",
        400
    )

except APIError as error:

    print("Message:", error.message)
    print("Code:", error.code)


# =====================================================
# Example 8 - AI Engineering Example
# =====================================================

print("\nExample 8 - AI Model Exceptions")


class ModelError(Exception):
    """Base AI model error."""


class ModelNotLoadedError(ModelError):
    pass


class InvalidInputError(ModelError):
    pass


class AIModel:

    def __init__(self):
        self.loaded = False

    def predict(self, value):

        if not self.loaded:
            raise ModelNotLoadedError(
                "Model has not been loaded."
            )

        if not isinstance(value, (int, float)):
            raise InvalidInputError(
                "Model input must be numeric."
            )

        return value * 2


model = AIModel()

try:

    print(model.predict(10))

except ModelNotLoadedError as error:

    print("Model Error:", error)

except InvalidInputError as error:

    print("Input Error:", error)


# =====================================================
# Example 9 - AI Model Loading
# =====================================================

print("\nExample 9 - Model Loading")


class ModelLoadError(Exception):
    pass


def load_model(path):

    if not path:
        raise ModelLoadError(
            "Model path cannot be empty."
        )

    print(f"Loading model from: {path}")

    return "Model loaded successfully."


try:

    print(load_model("models/model.pkl"))

except ModelLoadError as error:

    print("Loading Error:", error)


# =====================================================
# Example 10 - Dataset Validation
# =====================================================

print("\nExample 10 - Dataset Validation")


class DatasetError(Exception):
    pass


def validate_dataset(rows, columns):

    if rows <= 0:
        raise DatasetError(
            "Dataset contains no rows."
        )

    if columns <= 0:
        raise DatasetError(
            "Dataset contains no columns."
        )

    return "Dataset is valid."


try:

    print(validate_dataset(1000, 20))

except DatasetError as error:

    print("Dataset Error:", error)


# =====================================================
# Example 11 - API Example
# =====================================================

print("\nExample 11 - API Validation")


class APIRequestError(Exception):
    pass


def process_request(data):

    if data is None:
        raise APIRequestError(
            "Request data is missing."
        )

    if not isinstance(data, dict):
        raise APIRequestError(
            "Request data must be a dictionary."
        )

    return "Request processed successfully."


try:

    print(
        process_request(
            {"name": "Dhruvi"}
        )
    )

except APIRequestError as error:

    print("API Error:", error)


# =====================================================
# Why Custom Exceptions?
# =====================================================

print("\nWhy Use Custom Exceptions?")

print("""
Custom exceptions provide:

✔ Clear error meaning

✔ Better debugging

✔ Better application structure

✔ Easier error handling

✔ Domain-specific error messages

✔ Cleaner large-scale applications
""")


# =====================================================
# Custom Exception Structure
# =====================================================

print("\nCustom Exception Structure")

print("""
class MyError(Exception):
    pass


raise MyError("Something went wrong.")


try:
    risky_operation()

except MyError as error:
    print(error)
""")


# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Creating unnecessary custom exceptions.

❌ Inheriting from unrelated classes.

❌ Using vague exception names.

❌ Hiding the original error.

❌ Creating one exception for every tiny problem.

❌ Using custom exceptions instead of normal
   return values for normal program flow.
""")


# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Inherit custom exceptions from Exception.

✔ Give exceptions descriptive names.

✔ Create a base application exception
  for large projects.

✔ Add useful error messages.

✔ Add attributes when extra error
  information is useful.

✔ Catch custom exceptions at the
  appropriate application layer.

✔ Keep the exception hierarchy simple.
""")


# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is a custom exception?

A. A user-defined exception created for
application-specific error conditions.

Q. How do you create a custom exception?

A.

class MyError(Exception):
    pass

Q. Why inherit from Exception?

A. Exception is the standard base class
for most user-defined exceptions.

Q. Can custom exceptions have attributes?

A. Yes.

Q. Can custom exceptions inherit from
another custom exception?

A. Yes. This allows developers to create
an organized exception hierarchy.

Q. Why are custom exceptions useful?

A. They make application errors more
specific, readable, and easier to handle.
""")


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Custom exceptions represent application-specific errors.

✔ They are created by inheriting from Exception.

✔ They can contain custom messages and attributes.

✔ Exception inheritance can create organized
  error hierarchies.

✔ AI systems can use custom exceptions for
  model, dataset, API, and validation errors.

✔ Good custom exceptions make production
  applications easier to debug and maintain.
""")

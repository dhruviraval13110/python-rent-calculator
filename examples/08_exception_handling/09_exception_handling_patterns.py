"""
=========================================================
Python Exception Handling Patterns
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 09_exception_handling_patterns.py

Description
-----------
This file demonstrates common exception-handling patterns
used in real-world Python applications.

Topics Covered
--------------
✔ try-except
✔ try-except-else
✔ try-except-finally
✔ Multiple Exceptions
✔ Exception Chaining
✔ Re-raising Exceptions
✔ Custom Exceptions
✔ Logging
✔ Validation Pattern
✔ Service-Layer Pattern
✔ AI/ML Error Handling
"""

import logging


print("=" * 60)
print("EXCEPTION HANDLING PATTERNS")
print("=" * 60)


# =====================================================
# Pattern 1 - Simple try-except
# =====================================================

print("\nPattern 1 - Simple try-except")


def convert_number(value):

    try:
        return int(value)

    except ValueError:
        print("Invalid integer.")

        return None


print(convert_number("100"))
print(convert_number("abc"))


# =====================================================
# Pattern 2 - Multiple Exceptions
# =====================================================

print("\nPattern 2 - Multiple Exceptions")


def divide_numbers(a, b):

    try:

        a = float(a)
        b = float(b)

        return a / b

    except ValueError:

        print("Both values must be numbers.")

    except ZeroDivisionError:

        print("Cannot divide by zero.")

    return None


print(divide_numbers(20, 5))
print(divide_numbers("abc", 5))
print(divide_numbers(20, 0))


# =====================================================
# Pattern 3 - Multiple Exceptions in One Block
# =====================================================

print("\nPattern 3 - Multiple Exceptions")


def process_value(value):

    try:

        number = int(value)

        return 100 / number

    except (ValueError, ZeroDivisionError) as error:

        print("Processing Error:", error)

        return None


print(process_value("10"))
print(process_value("abc"))
print(process_value("0"))


# =====================================================
# Pattern 4 - try-except-else
# =====================================================

print("\nPattern 4 - try-except-else")


def calculate_average(total, count):

    try:

        average = total / count

    except ZeroDivisionError:

        print("Count cannot be zero.")

        return None

    else:

        print("Calculation successful.")

        return average


print(
    "Average:",
    calculate_average(100, 5)
)

print(
    "Average:",
    calculate_average(100, 0)
)


# =====================================================
# Pattern 5 - try-except-finally
# =====================================================

print("\nPattern 5 - try-except-finally")


def process_file():

    file = None

    try:

        file = open(
            "data.txt",
            "r"
        )

        return file.read()

    except FileNotFoundError:

        print("File not found.")

        return None

    finally:

        if file is not None:

            file.close()

        print("File processing completed.")


process_file()


# =====================================================
# Pattern 6 - Context Manager
# =====================================================

print("\nPattern 6 - Context Manager")

print("""
Preferred file pattern:

with open("data.txt", "r") as file:
    content = file.read()

The context manager automatically
handles resource cleanup.
""")


# =====================================================
# Pattern 7 - Re-raising
# =====================================================

print("\nPattern 7 - Re-raising")


def parse_data(value):

    try:

        return int(value)

    except ValueError:

        print("Logging invalid data.")

        raise


try:

    parse_data("Python")

except ValueError as error:

    print("Caller handled:", error)


# =====================================================
# Pattern 8 - Exception Chaining
# =====================================================

print("\nPattern 8 - Exception Chaining")


def load_configuration():

    try:

        raise FileNotFoundError(
            "config.json was not found."
        )

    except FileNotFoundError as error:

        raise RuntimeError(
            "Application configuration could not be loaded."
        ) from error


try:

    load_configuration()

except RuntimeError as error:

    print("Configuration Error:", error)


# =====================================================
# Pattern 9 - Custom Exception
# =====================================================

print("\nPattern 9 - Custom Exception")


class ValidationError(Exception):
    pass


def validate_email(email):

    if "@" not in email:

        raise ValidationError(
            "Invalid email address."
        )

    return True


try:

    validate_email("dhruvi")

except ValidationError as error:

    print("Validation Error:", error)


# =====================================================
# Pattern 10 - Custom Exception Hierarchy
# =====================================================

print("\nPattern 10 - Exception Hierarchy")


class ApplicationError(Exception):
    pass


class DatabaseError(ApplicationError):
    pass


class AuthenticationError(ApplicationError):
    pass


try:

    raise DatabaseError(
        "Database connection failed."
    )

except ApplicationError as error:

    print("Application Error:", error)


# =====================================================
# Pattern 11 - Logging Exceptions
# =====================================================

print("\nPattern 11 - Logging")


logger = logging.getLogger(
    "exception_patterns"
)

if not logger.handlers:

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(levelname)s - %(message)s"
    )

    handler.setFormatter(
        formatter
    )

    logger.addHandler(handler)

logger.setLevel(logging.INFO)


def safe_division(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        logger.exception(
            "Division operation failed."
        )

        return None


safe_division(10, 0)


# =====================================================
# Pattern 12 - Validation at Boundary
# =====================================================

print("\nPattern 12 - Input Validation")


def create_user(username, age):

    if not isinstance(
        username,
        str
    ):

        raise TypeError(
            "Username must be a string."
        )

    if not username.strip():

        raise ValueError(
            "Username cannot be empty."
        )

    if not isinstance(
        age,
        int
    ):

        raise TypeError(
            "Age must be an integer."
        )

    if age < 0:

        raise ValueError(
            "Age cannot be negative."
        )

    return {
        "username": username,
        "age": age
    }


try:

    user = create_user(
        "Dhruvi",
        21
    )

    print(user)

except (TypeError, ValueError) as error:

    print("User Error:", error)


# =====================================================
# Pattern 13 - Service Layer
# =====================================================

print("\nPattern 13 - Service Layer")


class UserServiceError(Exception):
    pass


def user_service(user_id):

    try:

        if user_id <= 0:

            raise ValueError(
                "Invalid user ID."
            )

        return {
            "id": user_id,
            "name": "Dhruvi"
        }

    except ValueError as error:

        raise UserServiceError(
            "User service failed."
        ) from error


try:

    print(user_service(-1))

except UserServiceError as error:

    print("Service Error:", error)


# =====================================================
# Pattern 14 - AI Model Validation
# =====================================================

print("\nPattern 14 - AI Model Validation")


class ModelError(Exception):
    pass


class ModelNotLoadedError(ModelError):
    pass


class InvalidInputError(ModelError):
    pass


class AIModel:

    def __init__(self):

        self.loaded = False

    def load(self, path):

        if not path:

            raise ModelError(
                "Model path is required."
            )

        self.loaded = True

        print("Model loaded.")

    def predict(self, value):

        if not self.loaded:

            raise ModelNotLoadedError(
                "Model must be loaded first."
            )

        if not isinstance(
            value,
            (int, float)
        ):

            raise InvalidInputError(
                "Input must be numeric."
            )

        return value * 2


model = AIModel()

try:

    model.load(
        "models/model.pkl"
    )

    prediction = model.predict(10)

    print(
        "Prediction:",
        prediction
    )

except ModelNotLoadedError as error:

    print("Model Error:", error)

except InvalidInputError as error:

    print("Input Error:", error)

except ModelError as error:

    print("General Model Error:", error)


# =====================================================
# Pattern 15 - Dataset Processing
# =====================================================

print("\nPattern 15 - Dataset Processing")


class DatasetError(Exception):
    pass


def process_dataset(data):

    if data is None:

        raise DatasetError(
            "Dataset cannot be None."
        )

    if len(data) == 0:

        raise DatasetError(
            "Dataset cannot be empty."
        )

    try:

        values = [
            float(value)
            for value in data
        ]

    except ValueError as error:

        raise DatasetError(
            "Dataset contains invalid values."
        ) from error

    return values


try:

    dataset = process_dataset(
        [10, 20, 30]
    )

    print(
        "Processed dataset:",
        dataset
    )

except DatasetError as error:

    print("Dataset Error:", error)


# =====================================================
# Pattern 16 - API-like Error Handling
# =====================================================

print("\nPattern 16 - API Error Handling")


class APIError(Exception):

    def __init__(
        self,
        message,
        status_code
    ):

        self.message = message
        self.status_code = status_code

        super().__init__(message)


def api_request(data):

    if data is None:

        raise APIError(
            "Request body is missing.",
            400
        )

    return {
        "status": "success",
        "data": data
    }


try:

    print(
        api_request(
            {"name": "Dhruvi"}
        )
    )

except APIError as error:

    print(
        "API Error:",
        error.message
    )

    print(
        "Status Code:",
        error.status_code
    )


# =====================================================
# Pattern 17 - Catch Broad Exception at Top Level
# =====================================================

print("\nPattern 17 - Top-Level Handler")


def application():

    number = int("Python")

    return number


try:

    application()

except ValueError as error:

    logger.error(
        "Application failed: %s",
        error
    )


# =====================================================
# Exception Handling Flow
# =====================================================

print("\nException Handling Flow")

print("""
                    Start
                      |
                    try
                      |
              Exception occurs?
                 /          \\
               YES           NO
                |             |
             except          else
                |             |
                +-------> finally
                              |
                            End
""")


# =====================================================
# Recommended Pattern
# =====================================================

print("\nRecommended Pattern")

print("""
try:
    risky_operation()

except SpecificError as error:
    handle_expected_error()

else:
    process_success()

finally:
    cleanup_resources()
""")


# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Bare except

❌ Huge try blocks

❌ Silent exception handling

❌ Logging sensitive information

❌ Catching exceptions you cannot handle

❌ Losing original exception context

❌ Using exceptions for normal control flow

❌ Returning from finally

❌ Hiding unexpected programming bugs
""")


# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

best_practices = [
    "Catch specific exceptions",
    "Keep try blocks small",
    "Use meaningful error messages",
    "Use else for successful operations",
    "Use finally for cleanup",
    "Prefer context managers",
    "Use custom exceptions for domain errors",
    "Use logging for production errors",
    "Preserve exception context",
    "Validate external input",
    "Never log secrets",
    "Do not hide unexpected errors"
]

for practice in best_practices:

    print(f"✔ {practice}")


# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What are common exception handling patterns?

A. try-except, try-except-else,
try-except-finally, custom exceptions,
exception chaining, and re-raising.

Q. What is exception chaining?

A. It allows one exception to be raised
while preserving the original exception
as its cause.

Example:

raise RuntimeError("High-level error") from error

Q. Why use custom exceptions?

A. They represent application-specific
error conditions clearly.

Q. What is the purpose of finally?

A. It is used for cleanup operations and
executes whether an exception occurs or not.

Q. Why should exceptions be logged?

A. Logging provides useful information
for debugging and monitoring applications.

Q. Should every exception be caught?

A. No. Only exceptions that the current
code can meaningfully handle should be caught.
""")


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ Exception handling protects applications
  from unexpected runtime failures.

✔ Different patterns are useful in
  different situations.

✔ Specific exceptions are preferred.

✔ Custom exceptions improve large projects.

✔ Exception chaining preserves useful context.

✔ Logging helps diagnose production failures.

✔ These patterns are especially useful in
  AI/ML pipelines, APIs, data processing,
  model serving, and automation.
""")

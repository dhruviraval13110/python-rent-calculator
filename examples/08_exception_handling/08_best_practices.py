"""
=========================================================
Python Exception Handling - Best Practices
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 08_best_practices.py

Description
-----------
Professional exception handling is not just about
preventing crashes. Good error handling should make
applications reliable, readable, debuggable, and safe.

This file demonstrates recommended practices for
exception handling in real-world Python applications.

Topics Covered
--------------
✔ Catch Specific Exceptions
✔ Keep try Blocks Small
✔ Meaningful Error Messages
✔ Use finally for Cleanup
✔ Use with for Resources
✔ Avoid Bare except
✔ Avoid Silent Failures
✔ Re-raise Exceptions
✔ Custom Exceptions
✔ Logging
✔ Validation
✔ AI Engineering Practices
"""

import logging


print("=" * 60)
print("EXCEPTION HANDLING - BEST PRACTICES")
print("=" * 60)


# =====================================================
# Best Practice 1 - Catch Specific Exceptions
# =====================================================

print("\nBest Practice 1 - Catch Specific Exceptions")


def convert_number(value):

    try:

        return int(value)

    except ValueError:

        print("Invalid integer value.")

        return None


print(convert_number("100"))
print(convert_number("Python"))

print("""
GOOD:

except ValueError:
    ...

Avoid catching every possible exception
when you only expect a specific one.
""")


# =====================================================
# Best Practice 2 - Avoid Bare except
# =====================================================

print("\nBest Practice 2 - Avoid Bare except")

print("""
BAD:

try:
    risky_operation()

except:
    pass


BETTER:

try:
    risky_operation()

except ValueError:
    handle_error()
""")


# =====================================================
# Best Practice 3 - Keep try Blocks Small
# =====================================================

print("\nBest Practice 3 - Small try Blocks")


def calculate(value):

    try:

        number = int(value)

    except ValueError:

        print("Invalid input.")

        return None

    return number * 2


print(calculate("10"))
print(calculate("abc"))

print("""
Only the operation that may raise the
expected exception is placed inside try.
""")


# =====================================================
# Best Practice 4 - Meaningful Error Messages
# =====================================================

print("\nBest Practice 4 - Meaningful Messages")


def validate_age(age):

    if age < 0:

        raise ValueError(
            "Age cannot be negative."
        )

    if age > 150:

        raise ValueError(
            "Age must be between 0 and 150."
        )

    return True


try:

    validate_age(-5)

except ValueError as error:

    print("Validation Error:", error)


# =====================================================
# Best Practice 5 - Use finally for Cleanup
# =====================================================

print("\nBest Practice 5 - Cleanup")


file = None

try:

    file = open(
        "example.txt",
        "r"
    )

    content = file.read()

except FileNotFoundError:

    print("File not found.")

finally:

    if file is not None:

        file.close()

    print("Cleanup completed.")


# =====================================================
# Best Practice 6 - Prefer with for Files
# =====================================================

print("\nBest Practice 6 - Context Manager")

print("""
Instead of manually opening and closing
files, prefer:

with open("file.txt") as file:
    data = file.read()

The context manager automatically handles
resource cleanup.
""")


# =====================================================
# Best Practice 7 - Never Silently Ignore Errors
# =====================================================

print("\nBest Practice 7 - Do Not Ignore Errors")


def process_data(value):

    try:

        return int(value)

    except ValueError as error:

        print(
            f"Unable to process value: {error}"
        )

        return None


print(process_data("Python"))

print("""
BAD:

except ValueError:
    pass

Ignoring errors makes debugging difficult.
""")


# =====================================================
# Best Practice 8 - Re-Raise When Necessary
# =====================================================

print("\nBest Practice 8 - Re-Raising")


def read_number(value):

    try:

        return int(value)

    except ValueError:

        print("Logging invalid input.")

        raise


try:

    read_number("hello")

except ValueError as error:

    print(
        "Caller received:",
        error
    )


# =====================================================
# Best Practice 9 - Use Custom Exceptions
# =====================================================

print("\nBest Practice 9 - Custom Exceptions")


class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:

        raise InsufficientBalanceError(
            "Insufficient account balance."
        )

    return balance - amount


try:

    print(
        withdraw(5000, 7000)
    )

except InsufficientBalanceError as error:

    print(
        "Transaction Error:",
        error
    )


# =====================================================
# Best Practice 10 - Logging
# =====================================================

print("\nBest Practice 10 - Logging")


logger = logging.getLogger(
    "application"
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


def divide(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        logger.exception(
            "Division failed."
        )

        return None


divide(10, 0)


# =====================================================
# Best Practice 11 - Do Not Log Sensitive Data
# =====================================================

print("\nBest Practice 11 - Protect Sensitive Data")

print("""
Never log:

❌ Passwords
❌ API Keys
❌ Access Tokens
❌ Credit Card Numbers
❌ Authentication Tokens
❌ Private User Information

Example of BAD logging:

logger.info("API key = %s", api_key)

Never expose secrets through logs.
""")


# =====================================================
# Best Practice 12 - Validate at Boundaries
# =====================================================

print("\nBest Practice 12 - Validate Input")


def predict(age):

    if not isinstance(age, int):

        raise TypeError(
            "Age must be an integer."
        )

    if age < 0:

        raise ValueError(
            "Age cannot be negative."
        )

    return "Prediction generated."


try:

    print(predict(21))

except (TypeError, ValueError) as error:

    print("Input Error:", error)


# =====================================================
# Best Practice 13 - Do Not Use Exceptions
# as Normal Program Flow
# =====================================================

print("\nBest Practice 13 - Normal Program Flow")

print("""
BAD:

try:
    value = dictionary["name"]

except KeyError:
    value = "Unknown"


BETTER:

value = dictionary.get(
    "name",
    "Unknown"
)

Use normal Python operations when they
can express the intended logic clearly.
""")


# =====================================================
# Best Practice 14 - Preserve Error Context
# =====================================================

print("\nBest Practice 14 - Preserve Context")


def load_configuration():

    try:

        raise FileNotFoundError(
            "config.json missing"
        )

    except FileNotFoundError as error:

        raise RuntimeError(
            "Unable to load application configuration."
        ) from error


try:

    load_configuration()

except RuntimeError as error:

    print("Configuration Error:", error)


# =====================================================
# Best Practice 15 - AI Engineering Example
# =====================================================

print("\nBest Practice 15 - AI Engineering")


class ModelError(Exception):
    pass


class ModelNotLoadedError(ModelError):
    pass


class InvalidModelInputError(ModelError):
    pass


class AIModel:

    def __init__(self):

        self.loaded = False

    def load(self, path):

        if not path:

            raise ModelError(
                "Model path cannot be empty."
            )

        self.loaded = True

        print(
            "Model loaded successfully."
        )

    def predict(self, value):

        if not self.loaded:

            raise ModelNotLoadedError(
                "Load the model before prediction."
            )

        if not isinstance(
            value,
            (int, float)
        ):

            raise InvalidModelInputError(
                "Model input must be numeric."
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

    logger.error(
        "Model error: %s",
        error
    )

except InvalidModelInputError as error:

    logger.error(
        "Input error: %s",
        error
    )

except ModelError as error:

    logger.error(
        "General model error: %s",
        error
    )


# =====================================================
# Best Practice Checklist
# =====================================================

print("\nBest Practice Checklist")

checklist = [
    "Catch specific exceptions",
    "Keep try blocks small",
    "Use meaningful messages",
    "Use finally for cleanup",
    "Prefer context managers",
    "Avoid bare except",
    "Do not silently ignore errors",
    "Use custom exceptions when useful",
    "Log important failures",
    "Never log secrets",
    "Validate external input",
    "Preserve exception context",
    "Do not use exceptions for normal flow"
]

for item in checklist:

    print(f"✔ {item}")


# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ except:
❌ except Exception everywhere
❌ pass inside exception handlers
❌ Huge try blocks
❌ Unclear error messages
❌ Logging sensitive information
❌ Hiding programming bugs
❌ Using assert for production validation
❌ Using exceptions for normal control flow
❌ Losing the original exception context
""")


# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. Why should we catch specific exceptions?

A. It prevents unrelated errors from being
accidentally hidden and makes the code clearer.

Q. Why should try blocks be small?

A. Small try blocks make it clear which operation
can raise the expected exception.

Q. Why should we avoid bare except?

A. It catches almost everything and can hide
unexpected programming errors.

Q. When should custom exceptions be used?

A. When an application has domain-specific
error conditions that need meaningful names.

Q. Why use logging?

A. Logging provides persistent and structured
information about application behavior and errors.

Q. Should sensitive information be logged?

A. No.

Q. Why use `raise ... from ...`?

A. It preserves the original exception as the
cause of the higher-level exception.

Q. Should exceptions be used for normal control flow?

A. Generally no. Normal Python operations are
usually clearer when they can handle the situation.
""")


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Professional exception handling means:

✔ Catch what you can actually handle.

✔ Keep error-prone code focused.

✔ Give useful error messages.

✔ Clean up resources.

✔ Log important failures.

✔ Protect sensitive information.

✔ Use custom exceptions for domain errors.

✔ Preserve the original error context.

✔ Validate external input.

✔ Avoid hiding unexpected bugs.

These practices are essential for
production AI/ML systems, APIs,
data pipelines, automation, and
backend applications.
""")

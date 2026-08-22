"""
=========================================================
Python Exception Handling - Final Revision
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 12_final_revision.py

Description
-----------
Complete revision of Python Exception Handling.

Topics Covered
--------------
✔ What is an Exception?
✔ try
✔ except
✔ else
✔ finally
✔ raise
✔ Built-in Exceptions
✔ Multiple Exceptions
✔ Custom Exceptions
✔ Exception Chaining
✔ Re-raising
✔ Logging
✔ Assertions
✔ Best Practices
✔ AI/ML Error Handling
"""

import logging


# =====================================================
# Logging
# =====================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


print("=" * 60)
print("PYTHON EXCEPTION HANDLING - FINAL REVISION")
print("=" * 60)


# =====================================================
# 1. Basic Exception
# =====================================================

print("\n1. Basic Exception")

try:

    result = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero.")


# =====================================================
# 2. try-except-else
# =====================================================

print("\n2. try-except-else")

try:

    number = int("100")

except ValueError:

    print("Invalid number.")

else:

    print(
        "Number:",
        number
    )


# =====================================================
# 3. try-except-finally
# =====================================================

print("\n3. try-except-finally")

try:

    print("Processing operation.")

except Exception:

    print("Error occurred.")

finally:

    print("Operation completed.")


# =====================================================
# 4. Multiple Exceptions
# =====================================================

print("\n4. Multiple Exceptions")


def divide(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        return "Cannot divide by zero."

    except TypeError:

        return "Invalid data type."


print(
    divide(10, 2)
)

print(
    divide(10, 0)
)

print(
    divide("10", 2)
)


# =====================================================
# 5. raise
# =====================================================

print("\n5. raise")


def check_age(age):

    if age < 18:

        raise ValueError(
            "Age must be at least 18."
        )

    return True


try:

    check_age(15)

except ValueError as error:

    print(
        "Validation Error:",
        error
    )


# =====================================================
# 6. Custom Exception
# =====================================================

print("\n6. Custom Exception")


class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:

        raise InsufficientBalanceError(
            "Insufficient balance."
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
# 7. Exception Chaining
# =====================================================

print("\n7. Exception Chaining")


def load_data():

    try:

        raise FileNotFoundError(
            "data.csv not found."
        )

    except FileNotFoundError as error:

        raise RuntimeError(
            "Unable to load dataset."
        ) from error


try:

    load_data()

except RuntimeError as error:

    print(
        "Runtime Error:",
        error
    )


# =====================================================
# 8. Re-raising
# =====================================================

print("\n8. Re-raising")


def convert(value):

    try:

        return int(value)

    except ValueError:

        logger.error(
            "Invalid conversion."
        )

        raise


try:

    convert("Python")

except ValueError:

    print(
        "Conversion handled by caller."
    )


# =====================================================
# 9. Assertions
# =====================================================

print("\n9. Assertions")


def calculate_square(number):

    assert isinstance(
        number,
        (int, float)
    ), "Input must be numeric."

    return number ** 2


print(
    "Square:",
    calculate_square(5)
)


# =====================================================
# 10. Logging Exception
# =====================================================

print("\n10. Logging Exception")


def safe_operation():

    try:

        result = 10 / 0

        return result

    except ZeroDivisionError:

        logger.exception(
            "Operation failed."
        )

        return None


safe_operation()


# =====================================================
# 11. Input Validation
# =====================================================

print("\n11. Input Validation")


def validate_number(value):

    try:

        number = float(value)

        if number < 0:

            raise ValueError(
                "Number cannot be negative."
            )

        return number

    except (ValueError, TypeError) as error:

        print(
            "Input Error:",
            error
        )

        return None


print(
    validate_number("25.5")
)

print(
    validate_number("-10")
)

print(
    validate_number("abc")
)


# =====================================================
# 12. File Handling
# =====================================================

print("\n12. File Handling")


def read_file(filename):

    try:

        with open(
            filename,
            "r"
        ) as file:

            return file.read()

    except FileNotFoundError:

        print(
            "File does not exist."
        )

        return None

    except PermissionError:

        print(
            "Permission denied."
        )

        return None


read_file(
    "unknown.txt"
)


# =====================================================
# 13. Data Processing
# =====================================================

print("\n13. Data Processing")


def clean_data(data):

    cleaned = []

    for value in data:

        try:

            cleaned.append(
                float(value)
            )

        except (
            ValueError,
            TypeError
        ):

            logger.warning(
                "Skipping invalid value: %s",
                value
            )

    return cleaned


data = [
    "10",
    "20.5",
    "abc",
    30,
    None
]

print(
    "Cleaned:",
    clean_data(data)
)


# =====================================================
# 14. AI/ML Model Error Handling
# =====================================================

print("\n14. AI/ML Model Error Handling")


class ModelError(Exception):
    pass


class ModelNotLoadedError(ModelError):
    pass


class InvalidModelInputError(ModelError):
    pass


class SimpleModel:

    def __init__(self):

        self.loaded = False

    def load(self):

        self.loaded = True

        print(
            "Model loaded."
        )

    def predict(self, value):

        if not self.loaded:

            raise ModelNotLoadedError(
                "Model is not loaded."
            )

        if not isinstance(
            value,
            (int, float)
        ):

            raise InvalidModelInputError(
                "Input must be numeric."
            )

        return value * 2


model = SimpleModel()


try:

    model.load()

    prediction = model.predict(
        25
    )

    print(
        "Prediction:",
        prediction
    )

except ModelNotLoadedError as error:

    print(
        "Model Error:",
        error
    )

except InvalidModelInputError as error:

    print(
        "Input Error:",
        error
    )

except ModelError as error:

    print(
        "General Model Error:",
        error
    )


# =====================================================
# 15. Important Built-in Exceptions
# =====================================================

print("\n15. Important Built-in Exceptions")

exceptions = [
    "ValueError",
    "TypeError",
    "ZeroDivisionError",
    "IndexError",
    "KeyError",
    "FileNotFoundError",
    "PermissionError",
    "NameError",
    "AttributeError",
    "ImportError",
    "ModuleNotFoundError",
    "OverflowError",
    "RuntimeError"
]

for exception in exceptions:

    print(
        f"• {exception}"
    )


# =====================================================
# 16. Exception Handling Flow
# =====================================================

print("\n16. Exception Handling Flow")

print("""
try
 |
 |-- No Error --> else
 |
 |-- Error -----> except
 |
 +--------------> finally
"""


# =====================================================
# 17. Quick Rules
# =====================================================

print("\n17. Quick Rules")

print("""
RULE 1
------
Catch specific exceptions.

RULE 2
------
Keep try blocks small.

RULE 3
------
Use finally for cleanup.

RULE 4
------
Use else for successful operations.

RULE 5
------
Use raise to explicitly create errors.

RULE 6
------
Use custom exceptions for application-specific errors.

RULE 7
------
Use logging for production error tracking.

RULE 8
------
Do not log passwords or API keys.

RULE 9
------
Do not silently ignore exceptions.

RULE 10
-------
Do not use assertions as a replacement
for production validation.
""")


# =====================================================
# 18. Common Bad Code
# =====================================================

print("\n18. Common Bad Code")

print("""
BAD:

try:
    operation()

except:
    pass


BAD:

try:
    operation()

except Exception:
    print("Something went wrong.")


BETTER:

try:
    operation()

except SpecificError as error:
    logger.error(
        "Operation failed: %s",
        error
    )
""")


# =====================================================
# 19. Interview Revision
# =====================================================

print("\n19. Interview Revision")

print("""
Q1. What is an exception?

An exception is an event that interrupts
normal program execution because of an error
or unexpected condition.

Q2. Which keywords are used for exception handling?

try
except
else
finally
raise

Q3. What does try do?

It contains code that may produce an exception.

Q4. What does except do?

It handles an exception.

Q5. What does else do?

It executes when no exception occurs.

Q6. What does finally do?

It executes regardless of whether an exception
occurs or not.

Q7. What does raise do?

It manually raises an exception.

Q8. What is a custom exception?

A programmer-defined exception class used for
application-specific errors.

Q9. What is exception chaining?

It preserves the original exception while
raising another higher-level exception.

Q10. Why use logging?

To record application events and errors for
debugging and monitoring.

Q11. What is AssertionError?

It occurs when an assert condition evaluates
to False.

Q12. Should assert replace input validation?

No. Explicit validation and exceptions are
better for production-critical checks.
""")


# =====================================================
# 20. Final Checklist
# =====================================================

print("\n20. FINAL CHECKLIST")

topics = [
    "try",
    "except",
    "else",
    "finally",
    "raise",
    "Built-in exceptions",
    "Multiple exceptions",
    "Custom exceptions",
    "Exception chaining",
    "Re-raising",
    "Logging",
    "Assertions",
    "Input validation",
    "File error handling",
    "AI/ML error handling",
    "Best practices"
]

for topic in topics:

    print(
        f"✔ {topic}"
    )


# =====================================================
# Final Summary
# =====================================================

print("\n" + "=" * 60)
print("MODULE 08 - EXCEPTION HANDLING COMPLETED")
print("=" * 60)

print("""
You should now understand:

✔ How exceptions work

✔ How to handle exceptions

✔ How to raise exceptions

✔ How to create custom exceptions

✔ How to log errors

✔ How to validate input

✔ How to handle files and data

✔ How to use assertions

✔ How to build production-style
  error handling

✔ How exception handling can be
  applied to AI/ML systems
""")

print(
    "\nException Handling Revision Complete."
)

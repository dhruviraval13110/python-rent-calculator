"""
=========================================================
Python else and finally
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 03_else_finally.py

Description
-----------
The else and finally blocks are used together with
try-except to control what happens after an operation.

else:
    Runs only when no exception occurs.

finally:
    Runs whether an exception occurs or not.

Topics Covered
--------------
✔ try-except-else
✔ try-except-finally
✔ try-except-else-finally
✔ File Handling
✔ Database-like Operations
✔ Resource Cleanup
✔ AI Engineering Example
✔ Best Practices
"""

print("=" * 60)
print("ELSE AND FINALLY")
print("=" * 60)

# =====================================================
# Example 1 - Basic else
# =====================================================

print("\nExample 1 - Basic else")

try:

    number = 10 / 2

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Division successful.")
    print("Result:", number)

# =====================================================
# Example 2 - else is skipped on exception
# =====================================================

print("\nExample 2 - else with Exception")

try:

    number = 10 / 0

except ZeroDivisionError:

    print("Division failed.")

else:

    print("This will not execute.")

# =====================================================
# Example 3 - finally
# =====================================================

print("\nExample 3 - Basic finally")

try:

    print("Inside try block.")

except Exception:

    print("Exception occurred.")

finally:

    print("Finally block executed.")

# =====================================================
# Example 4 - finally after exception
# =====================================================

print("\nExample 4 - finally after Exception")

try:

    result = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero.")

finally:

    print("Cleanup operation completed.")

# =====================================================
# Example 5 - try-except-else-finally
# =====================================================

print("\nExample 5 - Complete Structure")

try:

    number = int("100")

    result = 500 / number

except ValueError:

    print("Invalid number.")

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Operation successful.")
    print("Result:", result)

finally:

    print("Operation completed.")

# =====================================================
# Example 6 - File Handling
# =====================================================

print("\nExample 6 - File Handling")

file = None

try:

    file = open("data.txt", "r")

    content = file.read()

except FileNotFoundError:

    print("File was not found.")

else:

    print("File read successfully.")
    print(content)

finally:

    if file is not None:
        file.close()

    print("File resource handled.")

# =====================================================
# Example 7 - User Input
# =====================================================

print("\nExample 7 - User Input")

user_input = "25"

try:

    number = int(user_input)

except ValueError:

    print("Invalid input.")

else:

    print("Valid number:", number)

finally:

    print("Input processing finished.")

# =====================================================
# Example 8 - Multiple Operations
# =====================================================

print("\nExample 8 - Multiple Operations")

try:

    value = 20

    result = value / 5

except ZeroDivisionError:

    print("Division failed.")

else:

    print("Division successful.")
    print("Result:", result)

finally:

    print("Calculation finished.")

# =====================================================
# Example 9 - Function with finally
# =====================================================

print("\nExample 9 - Function")


def process_data(data):

    try:

        number = int(data)

        return number * 2

    except ValueError:

        print("Invalid data.")
        return None

    finally:

        print("process_data() finished.")


print(process_data("50"))

print(process_data("hello"))

# =====================================================
# Example 10 - Return and finally
# =====================================================

print("\nExample 10 - finally with return")


def test_return():

    try:

        return "Returned from try"

    finally:

        print("Finally executes before function returns.")


print(test_return())

# =====================================================
# Example 11 - AI Engineering Example
# =====================================================

print("\nExample 11 - AI Engineering")


def evaluate_model(correct_predictions, total_predictions):

    try:

        accuracy = (
            correct_predictions
            / total_predictions
        ) * 100

    except ZeroDivisionError:

        print("Cannot calculate accuracy.")

        return None

    else:

        print("Model evaluation successful.")

        return accuracy

    finally:

        print("Evaluation process completed.")


print(
    "Accuracy:",
    evaluate_model(95, 100),
    "%"
)

print(
    "Accuracy:",
    evaluate_model(95, 0)
)

# =====================================================
# Example 12 - API-like Operation
# =====================================================

print("\nExample 12 - API-like Operation")


def fetch_prediction(value):

    try:

        number = float(value)

        prediction = number * 2

    except ValueError:

        print("Invalid prediction input.")

    else:

        print("Prediction successful.")

        return prediction

    finally:

        print("Prediction request completed.")


print(fetch_prediction("10.5"))

print(fetch_prediction("AI"))

# =====================================================
# Execution Order
# =====================================================

print("\nExecution Order")

print("""
try
 ↓
Exception?
 ├── YES → except
 │
 └── NO  → else
              ↓
           finally
              ↓
           Continue

finally executes regardless of whether
an exception occurred.
""")

# =====================================================
# Important Difference
# =====================================================

print("\nImportant Difference")

print("""
else
----
Runs only when try completes successfully.

finally
-------
Runs whether an exception occurs or not.

Example:

try:
    operation()

except Exception:
    handle_error()

else:
    success_operation()

finally:
    cleanup()
""")

# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Putting success logic inside finally.

❌ Using finally for error handling.

❌ Forgetting to release resources.

❌ Putting unnecessary code in finally.

❌ Returning from finally and accidentally
   overriding another return value.
""")

# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

print("""
✔ Use else for successful execution logic.

✔ Use finally for cleanup.

✔ Close files and release resources.

✔ Keep try blocks focused.

✔ Prefer `with` for file handling when possible.

✔ Avoid returning from finally.
""")

# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. What is the purpose of else?

A. It executes only when the try block
completes without an exception.

Q. What is the purpose of finally?

A. It executes whether an exception occurs
or not and is commonly used for cleanup.

Q. Can finally execute when an exception occurs?

A. Yes.

Q. Can we use try without except?

A. Yes, if finally is present.

Example:

try:
    operation()
finally:
    cleanup()

Q. What is the difference between else and finally?

A.

else:
Runs only after successful try execution.

finally:
Runs regardless of success or failure.
""")

# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
✔ else runs when no exception occurs.

✔ finally runs regardless of exceptions.

✔ else is useful for success logic.

✔ finally is useful for cleanup.

✔ The complete structure is:

try
except
else
finally

✔ These blocks are important for reliable
file handling, APIs, databases, automation,
and AI/ML applications.
""")

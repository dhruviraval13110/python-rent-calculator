"""
=========================================================
Python Exception Handling - Mini Project
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 11_mini_project.py

Mini Project
------------
AI Model Prediction System

Description
-----------
A small real-world style application that demonstrates
professional exception handling in an AI/ML-like workflow.

The system:

✔ Validates user input
✔ Loads a model
✔ Validates prediction input
✔ Generates predictions
✔ Handles custom exceptions
✔ Logs errors
✔ Handles multiple failure cases
✔ Uses a clean application structure

Concepts Used
-------------
✔ try
✔ except
✔ else
✔ finally
✔ raise
✔ Custom Exceptions
✔ Logging
✔ Input Validation
✔ Exception Chaining
"""

import logging


# =====================================================
# Logging Configuration
# =====================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


print("=" * 60)
print("AI MODEL PREDICTION SYSTEM")
print("=" * 60)


# =====================================================
# Custom Exceptions
# =====================================================


class AIApplicationError(Exception):
    """Base exception for the application."""


class ModelNotLoadedError(AIApplicationError):
    """Raised when prediction is attempted before loading."""


class ModelLoadError(AIApplicationError):
    """Raised when the model cannot be loaded."""


class InvalidInputError(AIApplicationError):
    """Raised when prediction input is invalid."""


class PredictionError(AIApplicationError):
    """Raised when prediction fails."""


# =====================================================
# AI Model Class
# =====================================================


class AIModel:

    def __init__(self):

        self.loaded = False
        self.model_name = None

    # -------------------------------------------------
    # Load Model
    # -------------------------------------------------

    def load(self, model_path):

        try:

            if not model_path:

                raise ModelLoadError(
                    "Model path cannot be empty."
                )

            logger.info(
                "Loading model from: %s",
                model_path
            )

            # Simulated model loading
            self.model_name = "Simple AI Model"
            self.loaded = True

        except ModelLoadError:

            logger.exception(
                "Model loading failed."
            )

            raise

        else:

            logger.info(
                "Model loaded successfully."
            )

    # -------------------------------------------------
    # Validate Input
    # -------------------------------------------------

    def validate_input(self, value):

        if value is None:

            raise InvalidInputError(
                "Input value is required."
            )

        if not isinstance(
            value,
            (int, float)
        ):

            raise InvalidInputError(
                "Input must be a number."
            )

        if value < 0:

            raise InvalidInputError(
                "Input cannot be negative."
            )

        return True

    # -------------------------------------------------
    # Predict
    # -------------------------------------------------

    def predict(self, value):

        if not self.loaded:

            raise ModelNotLoadedError(
                "Model must be loaded before prediction."
            )

        try:

            self.validate_input(value)

            # Simulated prediction
            prediction = value * 2

            return prediction

        except InvalidInputError:

            logger.exception(
                "Invalid prediction input."
            )

            raise

        except Exception as error:

            raise PredictionError(
                "Prediction failed."
            ) from error


# =====================================================
# Helper Function
# =====================================================


def display_prediction(
    model,
    value
):

    try:

        prediction = model.predict(
            value
        )

    except ModelNotLoadedError as error:

        print(
            "Model Error:",
            error
        )

    except InvalidInputError as error:

        print(
            "Input Error:",
            error
        )

    except PredictionError as error:

        print(
            "Prediction Error:",
            error
        )

    else:

        print(
            f"Input: {value}"
        )

        print(
            f"Prediction: {prediction}"
        )

    finally:

        print(
            "Prediction request completed."
        )


# =====================================================
# Create Model
# =====================================================


model = AIModel()


# =====================================================
# Example 1 - Prediction Before Loading
# =====================================================

print("\nExample 1 - Prediction Before Loading")

display_prediction(
    model,
    10
)


# =====================================================
# Example 2 - Load Model
# =====================================================

print("\nExample 2 - Load Model")

try:

    model.load(
        "models/simple_model.pkl"
    )

except ModelLoadError as error:

    print(
        "Model Loading Error:",
        error
    )


# =====================================================
# Example 3 - Valid Prediction
# =====================================================

print("\nExample 3 - Valid Prediction")

display_prediction(
    model,
    25
)


# =====================================================
# Example 4 - Invalid String Input
# =====================================================

print("\nExample 4 - Invalid String Input")

display_prediction(
    model,
    "hello"
)


# =====================================================
# Example 5 - Negative Input
# =====================================================

print("\nExample 5 - Negative Input")

display_prediction(
    model,
    -10
)


# =====================================================
# Example 6 - None Input
# =====================================================

print("\nExample 6 - None Input")

display_prediction(
    model,
    None
)


# =====================================================
# Example 7 - Multiple Predictions
# =====================================================

print("\nExample 7 - Multiple Predictions")

inputs = [
    10,
    20,
    30,
    "invalid",
    50
]

for value in inputs:

    display_prediction(
        model,
        value
    )


# =====================================================
# Example 8 - Batch Prediction
# =====================================================

print("\nExample 8 - Batch Prediction")


def batch_predict(
    model,
    values
):

    predictions = []

    for value in values:

        try:

            prediction = model.predict(
                value
            )

            predictions.append(
                prediction
            )

        except InvalidInputError as error:

            logger.warning(
                "Skipping invalid value '%s': %s",
                value,
                error
            )

            continue

    return predictions


batch_inputs = [
    5,
    10,
    "bad",
    15,
    -2,
    20
]

results = batch_predict(
    model,
    batch_inputs
)

print(
    "Successful predictions:",
    results
)


# =====================================================
# Example 9 - Safe Application Runner
# =====================================================


def run_application():

    application_model = AIModel()

    try:

        application_model.load(
            "models/model.pkl"
        )

        values = [
            5,
            10,
            15
        ]

        predictions = batch_predict(
            application_model,
            values
        )

        return predictions

    except AIApplicationError as error:

        logger.error(
            "Application error: %s",
            error
        )

        return []

    except Exception as error:

        logger.exception(
            "Unexpected application failure."
        )

        return []


print("\nExample 9 - Application Runner")

results = run_application()

print(
    "Application Results:",
    results
)


# =====================================================
# Example 10 - Exception Chaining
# =====================================================

print("\nExample 10 - Exception Chaining")


def model_operation():

    try:

        raise FileNotFoundError(
            "model.pkl not found."
        )

    except FileNotFoundError as error:

        raise ModelLoadError(
            "Unable to load AI model."
        ) from error


try:

    model_operation()

except ModelLoadError as error:

    print(
        "High-level error:",
        error
    )


# =====================================================
# Application Flow
# =====================================================

print("\nApplication Flow")

print("""
User Input
    |
    ↓
Validate Input
    |
    ↓
Load Model
    |
    ↓
Generate Prediction
    |
    ├── Invalid Input
    │       ↓
    │   Handle Error
    │
    ├── Model Error
    │       ↓
    │   Handle Error
    │
    └── Success
            ↓
       Return Prediction
            |
            ↓
        Log Result
""")


# =====================================================
# Exception Handling Strategy
# =====================================================

print("\nException Handling Strategy")

print("""
1. Validate input early.

2. Use specific custom exceptions.

3. Handle expected errors.

4. Log important failures.

5. Preserve original exceptions.

6. Do not expose sensitive information.

7. Keep application logic separate
   from error-handling logic.

8. Allow unexpected programming errors
   to remain visible during development.
""")


# =====================================================
# Common Mistakes
# =====================================================

print("\nCommon Mistakes")

print("""
❌ Using bare except.

❌ Returning fake predictions after errors.

❌ Ignoring invalid input.

❌ Hiding model-loading failures.

❌ Logging sensitive information.

❌ Catching every exception at every level.

❌ Using exceptions for normal program flow.

❌ Creating overly complicated exception hierarchies.
""")


# =====================================================
# Best Practices
# =====================================================

print("\nBest Practices")

best_practices = [
    "Use custom exceptions for domain-specific errors",
    "Validate input before processing",
    "Catch specific exceptions",
    "Use logging for failures",
    "Use finally for cleanup when required",
    "Use else for successful operations",
    "Preserve exception context",
    "Do not silently ignore errors",
    "Keep exception handling readable",
    "Separate application logic from error handling"
]

for practice in best_practices:

    print(
        f"✔ {practice}"
    )


# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. Why use custom exceptions in an AI application?

A. They allow model, input, dataset, and prediction
errors to be represented separately and handled
appropriately.

Q. What happens when prediction is attempted before
the model is loaded?

A. ModelNotLoadedError is raised.

Q. Why validate input before prediction?

A. It prevents invalid data from reaching the
prediction logic and makes errors easier to handle.

Q. Why use logging?

A. Logging helps developers monitor and debug
production systems.

Q. What is exception chaining?

A. It preserves the original exception while
raising a higher-level application exception.

Q. What is the purpose of finally?

A. It provides a place for cleanup operations
that should happen regardless of success or failure.
""")


# =====================================================
# Final Summary
# =====================================================

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print("""
This mini project demonstrates how exception handling
can be applied to a realistic AI/ML workflow.

Implemented:

✔ Custom exceptions
✔ Model loading
✔ Input validation
✔ Prediction handling
✔ Batch prediction
✔ Logging
✔ Exception chaining
✔ try-except
✔ try-except-else
✔ try-except-finally
✔ Production-style error handling

This pattern can be extended to:

• Machine Learning APIs
• FastAPI applications
• Model serving systems
• Data pipelines
• Automation systems
• Backend applications
• AI agents
""")

print("\nAI Model Prediction System completed.")

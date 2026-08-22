"""
=========================================================
Python Exception Handling - Real World Examples
=========================================================

Author      : Dhruvi Raval
Repository  : Python for AI Engineering
Module      : 08 - Exception Handling
File        : 10_real_world_examples.py

Description
-----------
This file demonstrates practical exception handling
patterns used in real-world Python applications.

Topics Covered
--------------
✔ User Input Validation
✔ File Processing
✔ JSON Processing
✔ Configuration Validation
✔ API-like Processing
✔ Database-like Operations
✔ Data Cleaning
✔ AI Model Prediction
✔ ML Dataset Validation
✔ Logging Errors
✔ Custom Exceptions
"""

import json
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
print("REAL-WORLD EXCEPTION HANDLING EXAMPLES")
print("=" * 60)


# =====================================================
# Example 1 - User Input Validation
# =====================================================

print("\nExample 1 - User Input Validation")


def get_age(user_input):

    try:

        age = int(user_input)

        if age < 0 or age > 150:

            raise ValueError(
                "Age must be between 0 and 150."
            )

        return age

    except ValueError as error:

        print("Invalid age:", error)

        return None


print("Age:", get_age("21"))

print("Age:", get_age("abc"))

print("Age:", get_age("-5"))


# =====================================================
# Example 2 - Safe Division
# =====================================================

print("\nExample 2 - Safe Division")


def safe_divide(a, b):

    try:

        return a / b

    except ZeroDivisionError:

        logger.error(
            "Cannot divide by zero."
        )

        return None

    except TypeError:

        logger.error(
            "Both values must be numeric."
        )

        return None


print(safe_divide(20, 5))

print(safe_divide(20, 0))

print(safe_divide("20", 5))


# =====================================================
# Example 3 - File Processing
# =====================================================

print("\nExample 3 - File Processing")


def read_file(filename):

    try:

        with open(
            filename,
            "r"
        ) as file:

            return file.read()

    except FileNotFoundError:

        logger.error(
            "File '%s' was not found.",
            filename
        )

        return None

    except PermissionError:

        logger.error(
            "Permission denied for '%s'.",
            filename
        )

        return None

    except OSError as error:

        logger.error(
            "File operation failed: %s",
            error
        )

        return None


content = read_file(
    "example.txt"
)

print(
    "File content:",
    content
)


# =====================================================
# Example 4 - JSON Processing
# =====================================================

print("\nExample 4 - JSON Processing")


def parse_json(json_data):

    try:

        data = json.loads(json_data)

        return data

    except json.JSONDecodeError as error:

        logger.error(
            "Invalid JSON: %s",
            error
        )

        return None


valid_json = """
{
    "name": "Dhruvi",
    "age": 21
}
"""

invalid_json = """
{
    "name": "Dhruvi",
    "age":
}
"""


print(
    "Valid JSON:",
    parse_json(valid_json)
)

print(
    "Invalid JSON:",
    parse_json(invalid_json)
)


# =====================================================
# Example 5 - Configuration Validation
# =====================================================

print("\nExample 5 - Configuration Validation")


class ConfigurationError(Exception):
    pass


def load_config(config):

    if not isinstance(
        config,
        dict
    ):

        raise ConfigurationError(
            "Configuration must be a dictionary."
        )

    required_keys = [
        "database",
        "api_key"
    ]

    for key in required_keys:

        if key not in config:

            raise ConfigurationError(
                f"Missing configuration: {key}"
            )

    return config


try:

    config = {
        "database": "production_db",
        "api_key": "hidden"
    }

    print(
        load_config(config)
    )

except ConfigurationError as error:

    logger.error(
        "Configuration error: %s",
        error
    )


# =====================================================
# Example 6 - API-like Request
# =====================================================

print("\nExample 6 - API-like Request")


class APIError(Exception):

    def __init__(
        self,
        message,
        status_code
    ):

        self.message = message
        self.status_code = status_code

        super().__init__(message)


def process_api_request(request):

    if request is None:

        raise APIError(
            "Request body is missing.",
            400
        )

    if not isinstance(
        request,
        dict
    ):

        raise APIError(
            "Request must be a dictionary.",
            400
        )

    if "name" not in request:

        raise APIError(
            "Name field is required.",
            400
        )

    return {
        "status": "success",
        "message": "Request processed."
    }


try:

    response = process_api_request(
        {
            "name": "Dhruvi"
        }
    )

    print(response)

except APIError as error:

    print(
        "API Error:",
        error.message
    )

    print(
        "Status:",
        error.status_code
    )


# =====================================================
# Example 7 - Database-like Operation
# =====================================================

print("\nExample 7 - Database-like Operation")


class DatabaseError(Exception):
    pass


def save_user(user):

    try:

        if not user:

            raise ValueError(
                "User data is empty."
            )

        if "name" not in user:

            raise ValueError(
                "Name is required."
            )

        logger.info(
            "User saved successfully."
        )

        return True

    except ValueError as error:

        raise DatabaseError(
            "Unable to save user."
        ) from error


try:

    save_user(
        {
            "name": "Dhruvi"
        }
    )

except DatabaseError as error:

    logger.error(
        "Database Error: %s",
        error
    )


# =====================================================
# Example 8 - Data Cleaning
# =====================================================

print("\nExample 8 - Data Cleaning")


def clean_numbers(data):

    cleaned_data = []

    for value in data:

        try:

            number = float(value)

            cleaned_data.append(
                number
            )

        except ValueError:

            logger.warning(
                "Skipping invalid value: %s",
                value
            )

    return cleaned_data


raw_data = [
    "10",
    "20.5",
    "abc",
    "30",
    "unknown",
    "40"
]


cleaned = clean_numbers(
    raw_data
)

print(
    "Cleaned data:",
    cleaned
)


# =====================================================
# Example 9 - AI Model Validation
# =====================================================

print("\nExample 9 - AI Model Validation")


class ModelError(Exception):
    pass


class ModelNotLoadedError(ModelError):
    pass


class InvalidInputError(ModelError):
    pass


class SimpleModel:

    def __init__(self):

        self.loaded = False

    def load(self, path):

        if not path:

            raise ModelError(
                "Model path is required."
            )

        self.loaded = True

        logger.info(
            "Model loaded successfully."
        )

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


model = SimpleModel()

try:

    model.load(
        "models/model.pkl"
    )

    result = model.predict(
        10
    )

    print(
        "Prediction:",
        result
    )

except ModelNotLoadedError as error:

    logger.error(
        "Model error: %s",
        error
    )

except InvalidInputError as error:

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
# Example 10 - ML Dataset Validation
# =====================================================

print("\nExample 10 - ML Dataset Validation")


class DatasetError(Exception):
    pass


def validate_dataset(
    features,
    labels
):

    if features is None:

        raise DatasetError(
            "Features cannot be None."
        )

    if labels is None:

        raise DatasetError(
            "Labels cannot be None."
        )

    if len(features) == 0:

        raise DatasetError(
            "Features cannot be empty."
        )

    if len(labels) == 0:

        raise DatasetError(
            "Labels cannot be empty."
        )

    if len(features) != len(labels):

        raise DatasetError(
            "Features and labels must "
            "contain the same number of samples."
        )

    return True


try:

    features = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    labels = [
        0,
        1,
        0
    ]

    validate_dataset(
        features,
        labels
    )

    print(
        "Dataset validation successful."
    )

except DatasetError as error:

    logger.error(
        "Dataset Error: %s",
        error
    )


# =====================================================
# Example 11 - Prediction Pipeline
# =====================================================

print("\nExample 11 - Prediction Pipeline")


def prediction_pipeline(
    model,
    input_data
):

    try:

        if model is None:

            raise ModelNotLoadedError(
                "Model is not available."
            )

        if input_data is None:

            raise InvalidInputError(
                "Input data is missing."
            )

        if not isinstance(
            input_data,
            (int, float)
        ):

            raise InvalidInputError(
                "Input must be numeric."
            )

        prediction = model.predict(
            input_data
        )

        return prediction

    except ModelError:

        logger.exception(
            "Prediction pipeline failed."
        )

        return None


try:

    result = prediction_pipeline(
        model,
        25
    )

    print(
        "Pipeline result:",
        result
    )

except Exception as error:

    logger.error(
        "Unexpected pipeline error: %s",
        error
    )


# =====================================================
# Example 12 - Retry-like Pattern
# =====================================================

print("\nExample 12 - Retry-like Pattern")


def unstable_operation(attempt):

    if attempt < 3:

        raise ConnectionError(
            "Temporary connection failure."
        )

    return "Operation successful."


max_attempts = 5

for attempt in range(
    1,
    max_attempts + 1
):

    try:

        result = unstable_operation(
            attempt
        )

        print(result)

        break

    except ConnectionError as error:

        logger.warning(
            "Attempt %d failed: %s",
            attempt,
            error
        )

else:

    logger.error(
        "All attempts failed."
    )


# =====================================================
# Example 13 - Safe Type Conversion
# =====================================================

print("\nExample 13 - Safe Type Conversion")


def safe_float(value):

    try:

        return float(value)

    except (
        ValueError,
        TypeError
    ):

        logger.warning(
            "Unable to convert '%s' to float.",
            value
        )

        return None


values = [
    "10.5",
    "20",
    "hello",
    None
]


for value in values:

    print(
        value,
        "->",
        safe_float(value)
    )


# =====================================================
# Example 14 - Authentication Example
# =====================================================

print("\nExample 14 - Authentication")


class AuthenticationError(Exception):
    pass


def authenticate(
    username,
    password
):

    if not username:

        raise AuthenticationError(
            "Username is required."
        )

    if not password:

        raise AuthenticationError(
            "Password is required."
        )

    if password != "correct-password":

        raise AuthenticationError(
            "Invalid credentials."
        )

    return "Authentication successful."


try:

    print(
        authenticate(
            "dhruvi",
            "wrong-password"
        )
    )

except AuthenticationError as error:

    logger.warning(
        "Authentication failed: %s",
        error
    )


# =====================================================
# Important Production Rules
# =====================================================

print("\nImportant Production Rules")

print("""
✔ Validate external input.

✔ Catch only exceptions you can handle.

✔ Use specific exception types.

✔ Log unexpected failures.

✔ Never expose sensitive information.

✔ Use custom exceptions for business logic.

✔ Preserve the original exception context.

✔ Use retry logic only for temporary failures.

✔ Keep error messages useful.

✔ Do not hide unexpected programming errors.
""")


# =====================================================
# Interview Questions
# =====================================================

print("\nInterview Questions")

print("""
Q. Give a real-world use case of exception handling.

A. File processing, API requests, database operations,
user input validation, dataset processing, and
AI model prediction.

Q. How would you handle invalid data in an ML pipeline?

A. Validate the data, handle expected conversion
or validation errors, log invalid records, and
raise meaningful exceptions for critical failures.

Q. Why are custom exceptions useful?

A. They allow applications to represent domain-specific
errors clearly and handle them at the correct layer.

Q. How should temporary network failures be handled?

A. They can often be handled with controlled retries,
logging, and a maximum retry limit.

Q. Should all invalid records crash a data pipeline?

A. Not necessarily. Non-critical invalid records can
sometimes be logged and skipped, while critical
data-quality failures should stop the pipeline.
""")


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
Real-world exception handling is used in:

✔ User input
✔ File operations
✔ JSON parsing
✔ Configuration
✔ APIs
✔ Databases
✔ Data cleaning
✔ ML datasets
✔ Model loading
✔ Model prediction
✔ Authentication
✔ Network operations

Good exception handling makes applications
more reliable, maintainable, and easier to debug.
""")

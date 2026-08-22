"""
=========================================================
Python for AI Engineering
Module 09 - File Handling
File 01 - Reading Files
=========================================================

Description:
------------
This file introduces file handling in Python.

Topics Covered:
---------------
1. Opening a file
2. Reading the complete file
3. Reading a single line
4. Reading multiple lines
5. Using read()
6. Using readline()
7. Using readlines()
8. Using with open()
9. FileNotFoundError
10. File modes
11. Best practices
12. AI/ML use cases
"""

print("=" * 60)
print("MODULE 09 - FILE HANDLING")
print("01 - READING FILES")
print("=" * 60)


# =====================================================
# 1. What is File Handling?
# =====================================================

print("\n1. What is File Handling?")

print("""
File handling means working with files
using Python.

Python can:

- Create files
- Read files
- Write files
- Append data
- Delete files
- Process large datasets
""")


# =====================================================
# 2. Creating a Sample File
# =====================================================

print("\n2. Creating a Sample File")

with open(
    "sample.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "Python for AI Engineering\n"
    )

    file.write(
        "Learning File Handling\n"
    )

    file.write(
        "Reading files with Python\n"
    )

print("sample.txt created successfully.")


# =====================================================
# 3. Reading the Complete File
# =====================================================

print("\n3. Reading Complete File")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

        print(content)

except FileNotFoundError:

    print(
        "Error: sample.txt was not found."
    )


# =====================================================
# 4. Reading a Specific Number of Characters
# =====================================================

print("\n4. Reading Specific Characters")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read(10)

        print(
            "First 10 characters:"
        )

        print(content)

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 5. Using readline()
# =====================================================

print("\n5. Using readline()")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        first_line = file.readline()

        print(
            "First line:"
        )

        print(first_line)

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 6. Reading Multiple Lines
# =====================================================

print("\n6. Reading Multiple Lines")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        first_line = file.readline()
        second_line = file.readline()

        print(
            "Line 1:",
            first_line.strip()
        )

        print(
            "Line 2:",
            second_line.strip()
        )

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 7. Using readlines()
# =====================================================

print("\n7. Using readlines()")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        lines = file.readlines()

        print(
            "All lines:"
        )

        print(lines)

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 8. Loop Through File
# =====================================================

print("\n8. Loop Through File")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            print(
                line.strip()
            )

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 9. File Modes
# =====================================================

print("\n9. File Modes")

print("""
Common file modes:

r  -> Read
w  -> Write
a  -> Append
x  -> Create new file
rb -> Read binary
wb -> Write binary

Example:

open("data.txt", "r")
""")


# =====================================================
# 10. FileNotFoundError
# =====================================================

print("\n10. Handling FileNotFoundError")


filename = "does_not_exist.txt"

try:

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        data = file.read()

        print(data)

except FileNotFoundError:

    print(
        f"Error: '{filename}' does not exist."
    )


# =====================================================
# 11. Checking File Content
# =====================================================

print("\n11. Processing File Content")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

        words = content.split()

        print(
            "Number of words:",
            len(words)
        )

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 12. Counting Lines
# =====================================================

print("\n12. Counting Lines")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        lines = file.readlines()

        print(
            "Number of lines:",
            len(lines)
        )

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 13. Counting Characters
# =====================================================

print("\n13. Counting Characters")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

        print(
            "Number of characters:",
            len(content)
        )

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 14. Why Use with open()?
# =====================================================

print("\n14. Why Use with open()?")


print("""
Preferred:

with open("sample.txt", "r") as file:
    data = file.read()

The file is automatically closed
after the block finishes.

This is safer and cleaner than
manually calling file.close().
""")


# =====================================================
# 15. File Object
# =====================================================

print("\n15. File Object")


try:

    with open(
        "sample.txt",
        "r",
        encoding="utf-8"
    ) as file:

        print(
            "File name:",
            file.name
        )

        print(
            "File mode:",
            file.mode
        )

        print(
            "Is closed:",
            file.closed
        )

except FileNotFoundError:

    print(
        "File not found."
    )


# =====================================================
# 16. AI/ML Use Case
# =====================================================

print("\n16. AI/ML Use Case")


print("""
File handling is extremely important
in AI and Machine Learning.

Examples:

- Reading CSV datasets
- Reading JSON datasets
- Reading text data
- Loading configuration files
- Reading model metadata
- Processing logs
- Reading training data
- Saving predictions
- Loading prompts
- Processing documents

Example:

with open("training_data.txt", "r") as file:
    data = file.read()

The data can then be cleaned and
processed before sending it to an
AI/ML pipeline.
""")


# =====================================================
# 17. Practical Example - Dataset File
# =====================================================

print("\n17. Practical Dataset Example")


with open(
    "dataset.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("40\n")
    file.write("50\n")


numbers = []

try:

    with open(
        "dataset.txt",
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            try:

                number = float(
                    line.strip()
                )

                numbers.append(
                    number
                )

            except ValueError:

                print(
                    "Invalid value:",
                    line.strip()
                )

except FileNotFoundError:

    print(
        "Dataset file not found."
    )


print(
    "Loaded numbers:",
    numbers
)


# =====================================================
# 18. Calculate Average
# =====================================================

print("\n18. Calculate Average")


if numbers:

    average = sum(numbers) / len(numbers)

    print(
        "Average:",
        average
    )

else:

    print(
        "No data available."
    )


# =====================================================
# 19. Best Practices
# =====================================================

print("\n19. Best Practices")

print("""
✔ Use with open()

✔ Specify encoding when appropriate.

✔ Handle FileNotFoundError.

✔ Keep file operations simple.

✔ Validate data read from files.

✔ Avoid loading huge files completely
  into memory when unnecessary.

✔ Use line-by-line processing for
  large datasets.

✔ Never hard-code sensitive file paths
  or credentials.

✔ Use meaningful file names.
""")


# =====================================================
# 20. Interview Questions
# =====================================================

print("\n20. Interview Questions")

print("""
Q1. What is file handling?

A:
File handling is the process of creating,
reading, writing, and modifying files
using a programming language.

Q2. What is the difference between
read(), readline(), and readlines()?

A:

read()
Reads the complete file or a specified
number of characters.

readline()
Reads one line at a time.

readlines()
Reads all lines and returns them as
a list.

Q3. Why use with open()?

A:
It automatically closes the file and
makes resource management safer.

Q4. What does "r" mean?

A:
It opens a file in read mode.

Q5. What happens if a file does not exist
when using read mode?

A:
Python raises FileNotFoundError.

Q6. Why is file handling important in AI?

A:
AI systems frequently process datasets,
configuration files, logs, documents,
text files, and model-related data.

Q7. Why should large files not always
be loaded using read()?

A:
read() loads the complete content into
memory. For large files, line-by-line
processing can be more memory efficient.
""")


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("MODULE 09 - FILE HANDLING")
print("01 - READING FILES COMPLETED")
print("=" * 60)

print("""
You learned:

✔ File handling basics
✔ open()
✔ read()
✔ readline()
✔ readlines()
✔ with open()
✔ File modes
✔ FileNotFoundError
✔ Reading datasets
✔ File processing
✔ AI/ML file use cases
✔ File handling best practices
""")

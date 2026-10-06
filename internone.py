# ============================================================
# PYTHON & DATA SCIENCE FUNDAMENTALS
# ============================================================

print("===== PYTHON & DATA SCIENCE FUNDAMENTALS =====\n")

# ------------------------------------------------------------
# 1. VARIABLES AND BASIC DATA TYPES
# ------------------------------------------------------------

name = "Sakshi"
age = 20
course = "Artificial Intelligence and Data Science"
marks = 85.5
is_student = True

print("1. VARIABLES")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)
print("Student:", is_student)


# ------------------------------------------------------------
# 2. ARITHMETIC OPERATIONS
# ------------------------------------------------------------

a = 20
b = 10

print("\n2. ARITHMETIC OPERATIONS")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


# ------------------------------------------------------------
# 3. LIST
# ------------------------------------------------------------

subjects = ["Python", "Machine Learning", "Data Science", "AI"]

print("\n3. LIST")
print("Subjects:", subjects)
print("First subject:", subjects[0])

subjects.append("Deep Learning")
print("After adding subject:", subjects)


# ------------------------------------------------------------
# 4. DICTIONARY
# ------------------------------------------------------------

student = {
    "name": "Sakshi",
    "age": 20,
    "course": "AI & Data Science",
    "marks": 85
}

print("\n4. DICTIONARY")
print("Student Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])


# ------------------------------------------------------------
# 5. IF-ELSE CONDITION
# ------------------------------------------------------------

print("\n5. IF-ELSE")

if student["marks"] >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")


# ------------------------------------------------------------
# 6. FOR LOOP
# ------------------------------------------------------------

print("\n6. FOR LOOP")

for subject in subjects:
    print("Subject:", subject)


# ------------------------------------------------------------
# 7. WHILE LOOP
# ------------------------------------------------------------

print("\n7. WHILE LOOP")

i = 1

while i <= 5:
    print("Number:", i)
    i += 1


# ------------------------------------------------------------
# 8. FUNCTION
# ------------------------------------------------------------

print("\n8. FUNCTION")

def calculate_average(marks):
    return sum(marks) / len(marks)

marks_list = [80, 85, 90, 75, 88]

average = calculate_average(marks_list)

print("Marks:", marks_list)
print("Average:", average)


# ------------------------------------------------------------
# 9. FILE HANDLING
# ------------------------------------------------------------

print("\n9. FILE HANDLING")

file_name = "sample.txt"

# Write data into file
with open(file_name, "w") as file:
    file.write("Python Data Science Fundamentals\n")
    file.write("Learning Python for Data Science\n")

# Read data from file
with open(file_name, "r") as file:
    data = file.read()

print("File Content:")
print(data)


# ------------------------------------------------------------
# 10. BASIC DATA SCIENCE USING NUMPY
# ------------------------------------------------------------

import numpy as np

print("\n10. NUMPY")

data = np.array([10, 20, 30, 40, 50])

print("Data:", data)
print("Mean:", np.mean(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Standard Deviation:", np.std(data))


# ------------------------------------------------------------
# 11. DATA ANALYSIS USING PANDAS
# ------------------------------------------------------------

import pandas as pd

print("\n11. PANDAS")

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 95]
})

print("\nDataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# ------------------------------------------------------------
# 12. DATA ANALYSIS
# ------------------------------------------------------------

print("\n12. DATA ANALYSIS")

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Age:", df["Age"].mean())


# ------------------------------------------------------------
# 13. FILTERING DATA
# ------------------------------------------------------------

print("\n13. FILTERING DATA")

high_marks = df[df["Marks"] >= 85]

print("Students with marks >= 85:")
print(high_marks)


# ------------------------------------------------------------
# 14. DATA SCIENCE CONCEPTS
# ------------------------------------------------------------

print("\n14. DATA SCIENCE CONCEPTS")

print("""
Data Science is the process of collecting, cleaning,
analyzing and interpreting data to obtain useful insights.

Major steps in Data Science:
1. Data Collection
2. Data Cleaning
3. Data Exploration
4. Data Analysis
5. Data Visualization
6. Machine Learning
7. Model Evaluation
8. Decision Making
""")


# ------------------------------------------------------------
# FINAL OUTPUT
# ------------------------------------------------------------

print("\n==============================================")
print("Python & Data Science Fundamentals Completed!")
print("==============================================")
# Input Libraries

import matplotlib.pyplot as plt
import pandas as pd

# Import Data

data = [
   {
      "student": "Ana",
      "study_hours": 2,
      "attendance": 96,
      "homework_completed": 10,
      "exam_score": 82
   },
   {
      "student": "Bob",
      "study_hours": 1,
      "attendance": 96,
      "homework_completed": 7,
      "exam_score": 79
   },
   {
      "student": "Cyle",
      "study_hours": 1,
      "attendance": 88,
      "homework_completed": 9,
      "exam_score": 77
   },
   {
      "student": "Duke",
      "study_hours": 4,
      "attendance": 95,
      "homework_completed": 9,
      "exam_score": 98
   },
   {
      "student": "Emel",
      "study_hours": 1,
      "attendance": 70,
      "homework_completed": 4,
      "exam_score": 60
   },
   {
      "student": "Fia",
      "study_hours": 2,
      "attendance": 88,
      "homework_completed": 8,
      "exam_score": 85
   },
   {
      "student": "Gon",
      "study_hours": 1,
      "attendance": 92,
      "homework_completed": 7,
      "exam_score": 80
   },
   {
      "student": "Harley",
      "study_hours": 2,
      "attendance": 90,
      "homework_completed": 6,
      "exam_score": 83
   },
   {
      "student": "Ivy",
      "study_hours": 3,
      "attendance": 85,
      "homework_completed": 8,
      "exam_score": 86,
   },
   {
      "student": "Josh",
      "study_hours": 4,
      "attendance": 96,
      "homework_completed": 10,
      "exam_score": 95
   }

]

#-------------------------
# List 

study_hours = [2, 1, 1, 4, 1, 2, 1, 2, 3, 4]

attendance = [96, 90, 88, 95, 70, 88, 92, 90, 85, 96]

homework_completed = [10, 7, 9, 9, 4, 8, 7, 6, 8, 10]

exam_score = [82, 79, 77, 98, 60, 85, 80, 83, 86, 95]

#------------------------------

# Relationship between the input and the Exam Score

# Study Hours vs Exam Score
plt.figure(figsize=(6, 4))

plt.scatter(study_hours, exam_score)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

#------------------------------
# Attendance vs Exam Score
plt.figure(figsize=(6, 4))

plt.scatter(attendance, exam_score)

plt.title("Attendance vs Exam Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Exam Score")

plt.show()

#-------------------------------

# Homework vs Exam Score

plt.figure(figsize=(6, 4))

plt.scatter(homework_completed, exam_score)

plt.title("Homework Completed vs Exam Score")
plt.xlabel("Homework Completed")
plt.ylabel("Exam Score")

#--------------------------
df = pd.DataFrame(data)
print(df.head())

#---------------------------

features = ["study_hours", "attendance", "homework_completed"]

plt.figure(figsize=(12, 4))

for i, feature in enumerate(features, 1):
    plt.subplot(1, 3, i)
    plt.scatter(df[feature], df["exam_score"])
    plt.title(f"{feature} vs Exam Score")
    plt.xlabel(feature)
    plt.ylabel("Exam Score")

plt.tight_layout()
plt.show()

#---------------------------

print(df[["study_hours", "attendance","homework_completed", "exam_score"]].corr())

#-------------------------------------

import pandas as pd

# Import Data
data = [
   {
      "student": "Ana",
      "study_hours": 2,
      "attendance": 96,
      "homework_completed": 10,
      "exam_score": 82
   },
   {
      "student": "Bob",
      "study_hours": 1,
      "attendance": 96,
      "homework_completed": 7,
      "exam_score": 79
   },
   {
      "student": "Cyle",
      "study_hours": 1,
      "attendance": 88,
      "homework_completed": 9,
      "exam_score": 77
   },
   {
      "student": "Duke",
      "study_hours": 4,
      "attendance": 95,
      "homework_completed": 9,
      "exam_score": 98
   },
   {
      "student": "Emel",
      "study_hours": 1,
      "attendance": 70,
      "homework_completed": 4,
      "exam_score": 60
   },
   {
      "student": "Fia",
      "study_hours": 2,
      "attendance": 88,
      "homework_completed": 8,
      "exam_score": 85
   },
   {
      "student": "Gon",
      "study_hours": 1,
      "attendance": 92,
      "homework_completed": 7,
      "exam_score": 80
   },
   {
      "student": "Harley",
      "study_hours": 2,
      "attendance": 90,
      "homework_completed": 6,
      "exam_score": 83
   },
   {
      "student": "Ivy",
      "study_hours": 3,
      "attendance": 85,
      "homework_completed": 8,
      "exam_score": 86,
   },
   {
      "student": "Josh",
      "study_hours": 4,
      "attendance": 96,
      "homework_completed": 10,
      "exam_score": 95
   }

]
df = pd.DataFrame(data)
from sklearn.linear_model import LinearRegression

X = df[["study_hours", "attendance", "homework_completed"]]

y = df["exam_score"]

model = LinearRegression()

model.fit(X, y)

#---------------------
#Prediction Score we Want

new_student = [[3, 94, 9]]

prediction = model.predict(new_student)

print(prediction)
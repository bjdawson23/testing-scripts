# Online Python - IDE, Editor, Compiler, Interpreter


# dictionary comprehension to create a dictionary of the numbers 1–5 mapped to their cubes
{number: number ** 3 for number in range(1, 6)}

# set - unique set of values, so the below would only return 0-15
nums = list(range(16)) + list(range(7))
set(nums)

# Unites the sets - 1, 2, 3, 4, 5
{1, 3, 5} | {2, 3, 4}
# diff between right and the left sets - 1, 5
{1, 3, 5} -  {2, 3, 4}
# intersection of right and the left sets - 3
{1, 3, 5} &  {2, 3, 4}

# set right side is a superset of the left side will = true
set('h d a f g').issuperset('ha dad')



# check writing - take value less than 1000 and convert to text
# Dictionary mapping numbers to words
num_words = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
    16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
    30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
    80: "Eighty", 90: "Ninety"
}

# Function to convert number into word equivalent
def number_to_words(n):
    if n < 20:
        return num_words[n]
    elif n < 100:
        tens, remainder = divmod(n, 10)
        return num_words[tens * 10] + ("-" + num_words[remainder] if remainder else "")
    elif n < 1000:
        hundreds, remainder = divmod(n, 100)
        return num_words[hundreds] + " Hundred" + (" and " + number_to_words(remainder) if remainder else "")

# User input for check amount
amount = int(input("Enter a check amount (less than 1000): "))
if 0 <= amount < 1000:
    print(f"Check Amount in Words: {number_to_words(amount)} Dollars")
else:
    print("Invalid amount. Please enter a number less than 1000.")



# check value any number 
# Dictionary mapping numbers to words
num_words = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
    16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
    30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
    80: "Eighty", 90: "Ninety"
}

# Number scale words
num_scales = [(1000000, "Million"), (1000, "Thousand"), (100, "Hundred")]

# Function to convert number into words recursively
def number_to_words(n):
    if n < 20:
        return num_words[n]
    elif n < 100:
        tens, remainder = divmod(n, 10)
        return num_words[tens * 10] + ("-" + num_words[remainder] if remainder else "")
    for value, name in num_scales:
        if n >= value:
            leading, remainder = divmod(n, value)
            return number_to_words(leading) + f" {name}" + (" " + number_to_words(remainder) if remainder else "")

# Function to convert a check amount to words (including cents)
def check_amount_to_words(amount):
    dollars = int(amount)  # Extract whole dollar part
    cents = round((amount - dollars) * 100)  # Extract cents
    
    dollar_words = number_to_words(dollars) + " Dollars"
    cent_words = number_to_words(cents) + " Cents" if cents > 0 else ""

    return f"{dollar_words} and {cent_words}" if cents > 0 else dollar_words

# User input for check amount
amount = float(input("Enter a check amount (any value): "))
if amount >= 0:
    print(f"Check Amount in Words: {check_amount_to_words(amount)}")
else:
    print("Invalid amount. Please enter a positive number.")




# check any amount by region
# Dictionary mapping numbers to words
num_words = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
    16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
    30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
    80: "Eighty", 90: "Ninety"
}

# Number scale words
num_scales = [(1000000, "Million"), (1000, "Thousand"), (100, "Hundred")]

# Currency symbols and names
currency_data = {
    "USD": ("Dollars", "Cents"),
    "EUR": ("Euros", "Cents"),
    "GBP": ("Pounds", "Pence"),
    "INR": ("Rupees", "Paise")
}

# Function to convert number into words
def number_to_words(n):
    if n < 20:
        return num_words[n]
    elif n < 100:
        tens, remainder = divmod(n, 10)
        return num_words[tens * 10] + ("-" + num_words[remainder] if remainder else "")
    for value, name in num_scales:
        if n >= value:
            leading, remainder = divmod(n, value)
            return number_to_words(leading) + f" {name}" + (" " + number_to_words(remainder) if remainder else "")

# Function to convert check amount to words with currency
def check_amount_to_words(amount, currency="USD"):
    dollars = int(amount)  
    cents = round((amount - dollars) * 100)  

    currency_name, cent_name = currency_data.get(currency, ("Dollars", "Cents"))
    
    dollar_words = number_to_words(dollars) + f" {currency_name}"
    cent_words = number_to_words(cents) + f" {cent_name}" if cents > 0 else ""

    return f"{dollar_words} and {cent_words}" if cents > 0 else dollar_words

# User input for check amount
amount = float(input("Enter check amount: "))
currency = input("Enter currency (USD, EUR, GBP, INR): ").upper()

if amount >= 0 and currency in currency_data:
    print(f"Check Amount in Words: {check_amount_to_words(amount, currency)}")
else:
    print("Invalid input. Please enter a valid amount and currency.")




# check with name and generate QR code
import qrcode

# Function to generate QR code for payment details
def generate_qr_code(recipient, amount, date):
    check_details = f"Recipient: {recipient}\nAmount: ${amount:.2f}\nDate: {date}"
    qr = qrcode.make(check_details)
    
    # Save the QR code image
    qr.save("check_qr.png")
    print("QR Code generated and saved as 'check_qr.png'.")

# Example usage
recipient = input("Enter recipient name: ")
amount = float(input("Enter check amount: "))
date = input("Enter check date (YYYY-MM-DD): ")

generate_qr_code(recipient, amount, date)









# basic text slicing for list, tuples or strings
text = "Python is fun"
print(text[0:6])   # Output: Python
print(text[7:])    # Output: is fun
print(text[:6])    # Output: Python
print(text[::-1])  # Output: nuf si nohtyP (Reversed)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data[1:8:2])  # Output: [2, 4, 6, 8]
print(data[::-2])   # Output: [9, 7, 5, 3, 1] (Reverse skipping)

# sorting 
from itertools import groupby

data = [("Apple", "Fruit"), ("Banana", "Fruit"), ("Carrot", "Vegetable"), ("Tomato", "Fruit"), ("Spinach", "Vegetable")]


# Sort first before grouping
data.sort(key=lambda x: x[1])

# Group by category
for category, items in groupby(data, key=lambda x: x[1]):
    print(f"{category}: {[item[0] for item in items]}")

import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Department": ["HR", "IT", "HR", "Finance", "IT"],
        "Salary": [50000, 60000, 52000, 58000, 62000]}

df = pd.DataFrame(data)

# Grouping by Department
grouped = df.groupby("Department")["Salary"].mean()

print(grouped)


# sort within each group 
import pandas as pd

# Sample Data
data = {"Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Department": ["HR", "IT", "HR", "Finance", "IT"],
        "Salary": [50000, 60000, 52000, 58000, 62000]}

df = pd.DataFrame(data)

# Sorting within each group by Salary in descending order
df_sorted = df.sort_values(["Department", "Salary"], ascending=[True, False])

print(df_sorted)



# sales breakdown by department
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
data = {"Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Department": ["HR", "IT", "HR", "Finance", "IT"],
        "Salary": [50000, 60000, 52000, 58000, 62000]}

df = pd.DataFrame(data)

# Sorting within each department
df_sorted = df.sort_values(["Department", "Salary"], ascending=[True, False])

# Create an interactive Seaborn bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x="Department", y="Salary", data=df_sorted, hue="Name", palette="coolwarm", edgecolor="black")

plt.xlabel("Department")
plt.ylabel("Salary")
plt.title("Sorted Salary Breakdown by Department")
plt.legend(title="Employee")
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.show()




# Salary progression over time line chart 


import numpy as np

# Simulating salary trends over 5 years
years = np.arange(2020, 2025)
salary_trends = {
    "Alice": [50000, 52000, 54000, 56000, 58000],
    "Bob": [60000, 62000, 64000, 66000, 68000],
    "Charlie": [52000, 54000, 56000, 58000, 60000],
    "David": [58000, 60000, 62000, 64000, 66000],
    "Emma": [62000, 64000, 66000, 68000, 70000],
}

# Convert dictionary to DataFrame
df_trends = pd.DataFrame(salary_trends, index=years)

# Plot interactive line chart
plt.figure(figsize=(8, 5))
for employee in df_trends.columns:
    plt.plot(df_trends.index, df_trends[employee], marker="o", label=employee)

plt.xlabel("Year")
plt.ylabel("Salary")
plt.title("Salary Progression Over 5 Years")
plt.legend(title="Employee")
plt.grid(True)
plt.show()











from pathlib import Path

for i in range(1, 5):
    folder_name = f"folder_{i}"
    Path(folder_name).mkdir(exist_ok=True)
    print(f"Folder '{folder_name}' created.")

#create a beautiful spiral pattern using a loop
import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

for i in range(100):
    t.color(colors[i % len(colors)])
    t.forward(i * 2)
    t.right(59)

turtle.done()




# create Olympic rings
import turtle

rings = [(-120, 0, "blue"), (0, 0, "black"), (120, 0, "red"),
         (-60, -50, "yellow"), (60, -50, "green")]

turtle.bgcolor("white")

for x, y, color in rings:
    t = turtle.Turtle()
    t.color(color)
    t.width(10)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(60)

turtle.done()



# format two dimensional list into tabular look
def display_table(matrix):
    if not matrix:
        print("Empty matrix.")
        return

    num_columns = len(matrix[0])

    # Print column indices as headers
    print("    ", end="")  # Space for row index
    for col in range(num_columns):
        print(f"{col:>4}", end="")  # Right-aligned column numbers
    print("\n" + "-" * (num_columns * 4 + 4))  # Divider

    # Print rows with row indices
    for row_index, row in enumerate(matrix):
        print(f"{row_index:>2} |", end="")  # Row index
        for value in row:
            print(f"{value:>4}", end="")  # Right-aligned values
        print()

# Example usage
data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

display_table(data)


# same as above with nice format
def display_table(matrix):
    if not matrix:
        print("Empty matrix.")
        return

    num_columns = len(matrix[0])

    # Print column indices as headers (centered)
    print("    ", end="")  # Space for row index
    for col in range(num_columns):
        print(f"{col:^6}", end="")  # Adjust column width
    print("\n" + "=" * (num_columns * 6 + 6))  # Divider with '='

    # Print rows with row indices
    for row_index, row in enumerate(matrix):
        print(f"{row_index:^2} |", end="")  # Row index
        for value in row:
            print(f"{value:^6}|", end="")  # Centered and adds grid lines
        print("\n" + "-" * (num_columns * 6 + 6))  # Row separator

# Example usage
data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

display_table(data)





# Sample dictionary usage
sample_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Data Science", "Machine Learning"]
}

# Accessing values
print(sample_dict["name"])  # Output: Alice

# Adding a new key-value pair
sample_dict["job"] = "Software Engineer"

# Iterating over dictionary items
for key, value in sample_dict.items():
    print(f"{key}: {value}")

# Dictionary of student grades
student_grades = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "History": 92, "Art": 95},
    "Bob": {"Math": 78, "Science": 83, "English": 80, "History": 76, "Art": 82},
    "Charlie": {"Math": 92, "Science": 89, "English": 94, "History": 88, "Art": 90},
    "David": {"Math": 76, "Science": 80, "English": 75, "History": 72, "Art": 78},
    "Emma": {"Math": 88, "Science": 86, "English": 91, "History": 85, "Art": 87}
}

# Function to calculate the average grade of a student and ave of the total
def calculate_average(grades):
    return sum(grades.values()) / len(grades)

# Function to calculate the overall average grade of all students
def calculate_overall_average(student_grades):
    total_sum = 0
    total_count = 0
    for grades in student_grades.values():
        total_sum += sum(grades.values())
        total_count += len(grades)
    return total_sum / total_count

# Displaying each student's grades and their average
for student, grades in student_grades.items():
    student_average = calculate_average(grades)
    print(f"{student}: {grades}, Average Grade: {student_average:.2f}")

# Calculating and displaying overall average
overall_average = calculate_overall_average(student_grades)
print(f"\nOverall Average Grade of All Students: {overall_average:.2f}")





# with a graph by subject
import matplotlib.pyplot as plt

# Dictionary of student grades
student_grades = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "History": 92, "Art": 95},
    "Bob": {"Math": 78, "Science": 83, "English": 80, "History": 76, "Art": 82},
    "Charlie": {"Math": 92, "Science": 89, "English": 94, "History": 88, "Art": 90},
    "David": {"Math": 76, "Science": 80, "English": 75, "History": 72, "Art": 78},
    "Emma": {"Math": 88, "Science": 86, "English": 91, "History": 85, "Art": 87}
}

# Function to calculate the average grade per subject
def calculate_subject_averages(student_grades):
    subject_totals = {}
    subject_counts = {}

    for grades in student_grades.values():
        for subject, grade in grades.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + grade
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Calculate subject averages
subject_averages = calculate_subject_averages(student_grades)

# Plotting the data
subjects = list(subject_averages.keys())
averages = list(subject_averages.values())

plt.figure(figsize=(8, 5))
plt.bar(subjects, averages, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.title("Average Grade Per Subject")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the graph
plt.show()




# pie chart with numbers on it
import matplotlib.pyplot as plt

# Dictionary of student grades
student_grades = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "History": 92, "Art": 95},
    "Bob": {"Math": 78, "Science": 83, "English": 80, "History": 76, "Art": 82},
    "Charlie": {"Math": 92, "Science": 89, "English": 94, "History": 88, "Art": 90},
    "David": {"Math": 76, "Science": 80, "English": 75, "History": 72, "Art": 78},
    "Emma": {"Math": 88, "Science": 86, "English": 91, "History": 85, "Art": 87}
}

# Function to calculate the average grade per subject
def calculate_subject_averages(student_grades):
    subject_totals = {}
    subject_counts = {}

    for grades in student_grades.values():
        for subject, grade in grades.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + grade
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Calculate subject averages
subject_averages = calculate_subject_averages(student_grades)

# Plotting the data
subjects = list(subject_averages.keys())
averages = list(subject_averages.values())

plt.figure(figsize=(8, 8))
plt.pie(averages, labels=subjects, autopct="%1.1f%%", startangle=140, colors=['blue', 'green', 'red', 'purple', 'orange'])
plt.title("Average Grade Per Subject")
plt.show()




# pie chart with numbers and percentages on it
import matplotlib.pyplot as plt

# Dictionary of student grades
student_grades = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "History": 92, "Art": 95},
    "Bob": {"Math": 78, "Science": 83, "English": 80, "History": 76, "Art": 82},
    "Charlie": {"Math": 92, "Science": 89, "English": 94, "History": 88, "Art": 90},
    "David": {"Math": 76, "Science": 80, "English": 75, "History": 72, "Art": 78},
    "Emma": {"Math": 88, "Science": 86, "English": 91, "History": 85, "Art": 87}
}

# Function to calculate the average grade per subject
def calculate_subject_averages(student_grades):
    subject_totals = {}
    subject_counts = {}

    for grades in student_grades.values():
        for subject, grade in grades.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + grade
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Calculate subject averages
subject_averages = calculate_subject_averages(student_grades)

# Prepare data for pie chart
subjects = list(subject_averages.keys())
averages = list(subject_averages.values())

# Define color palette
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

plt.figure(figsize=(8, 8))

# Formatting labels to include actual values
def format_labels(pct, all_avg):
    absolute = int(round(pct * sum(all_avg) / 100, 0))
    return f"{absolute} ({pct:.1f}%)"

plt.pie(averages, labels=subjects, autopct=lambda pct: format_labels(pct, averages), startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})

plt.title("Average Grade Per Subject")
plt.show()




# pie chart with nice visuals and legend
import matplotlib.pyplot as plt
import seaborn as sns

# Dictionary of student grades
student_grades = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "History": 92, "Art": 95},
    "Bob": {"Math": 78, "Science": 83, "English": 80, "History": 76, "Art": 82},
    "Charlie": {"Math": 92, "Science": 89, "English": 94, "History": 88, "Art": 90},
    "David": {"Math": 76, "Science": 80, "English": 75, "History": 72, "Art": 78},
    "Emma": {"Math": 88, "Science": 86, "English": 91, "History": 85, "Art": 87}
}

# Function to calculate the average grade per subject
def calculate_subject_averages(student_grades):
    subject_totals = {}
    subject_counts = {}

    for grades in student_grades.values():
        for subject, grade in grades.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + grade
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Calculate subject averages
subject_averages = calculate_subject_averages(student_grades)

# Prepare data for pie chart
subjects = list(subject_averages.keys())
averages = list(subject_averages.values())

# Use seaborn color palette for better aesthetics
colors = sns.color_palette("pastel")

plt.figure(figsize=(8, 8))

# Explode effect to highlight slices
explode_values = [0.05] * len(subjects)  # Slightly separate all slices

# Formatting labels to include actual values
def format_labels(pct, all_avg):
    absolute = int(round(pct * sum(all_avg) / 100, 0))
    return f"{absolute} ({pct:.1f}%)"

wedges, texts, autotexts = plt.pie(
    averages, labels=subjects, autopct=lambda pct: format_labels(pct, averages),
    startangle=140, colors=colors, explode=explode_values, shadow=True, wedgeprops={'edgecolor': 'black'}
)

# Adjust text formatting
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight("bold")

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight("bold")

# Adding a legend
plt.legend(wedges, subjects, title="Subjects", loc="upper right", fontsize=10, title_fontsize=12)

plt.title("Average Grade Per Subject", fontsize=14, fontweight='bold')
plt.show()




# pie chart with fade in and out affect
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.animation as animation

# Dictionary of student grades
student_grades = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "History": 92, "Art": 95},
    "Bob": {"Math": 78, "Science": 83, "English": 80, "History": 76, "Art": 82},
    "Charlie": {"Math": 92, "Science": 89, "English": 94, "History": 88, "Art": 90},
    "David": {"Math": 76, "Science": 80, "English": 75, "History": 72, "Art": 78},
    "Emma": {"Math": 88, "Science": 86, "English": 91, "History": 85, "Art": 87}
}

# Function to calculate the average grade per subject
def calculate_subject_averages(student_grades):
    subject_totals = {}
    subject_counts = {}

    for grades in student_grades.values():
        for subject, grade in grades.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + grade
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Calculate subject averages
subject_averages = calculate_subject_averages(student_grades)

# Prepare data for pie chart
subjects = list(subject_averages.keys())
averages = list(subject_averages.values())

# Use Seaborn color palette
colors = sns.color_palette("coolwarm", len(subjects))

fig, ax = plt.subplots(figsize=(8, 8))

# Function to animate the fade-in effect
def animate(frame):
    ax.clear()
    fade_factor = frame / 50  # Gradual fade-in from 0 to 1
    explode_values = [0.05 * fade_factor for _ in subjects]  
    ax.pie(averages, labels=subjects, autopct="%1.1f%%", startangle=90,
           colors=[(r * fade_factor, g * fade_factor, b * fade_factor) for r, g, b in colors], 
           explode=explode_values, shadow=True, wedgeprops={'edgecolor': 'black'})

# Creating the animation
ani = animation.FuncAnimation(fig, animate, frames=50, interval=100)

plt.title("Animated Pie Chart: Fade-In Effect on Average Grades", fontsize=14, fontweight='bold', color="midnightblue")
plt.show()





# Sample word count program using a dictionary
def word_count(text):
    word_freq = {}  # Dictionary to store word frequencies
    words = text.lower().split()  # Convert text to lowercase and split into words
    
    for word in words:
        word = word.strip(",.!?()[]{}\"'")  # Remove punctuation
        word_freq[word] = word_freq.get(word, 0) + 1  # Count occurrences
    
    return word_freq

# Example usage
text = "Python is great. Python is easy! Learn Python, it's fun!"
word_counts = word_count(text)

# Print word frequencies
for word, count in word_counts.items():
    print(f"{word}: {count}")




# Word count program with file reading and sorting
def word_count_from_file(filename):
    word_freq = {}  # Dictionary to store word frequencies
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.lower().split()  # Convert text to lowercase and split into words
            for word in words:
                word = word.strip(",.!?()[]{}\"'")  # Remove punctuation
                word_freq[word] = word_freq.get(word, 0) + 1  # Count occurrences
    
    # Sort dictionary by frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_word_freq

# Example usage
filename = "sample.txt"  # Replace with your file name
word_counts = word_count_from_file(filename)

# Print sorted word frequencies
for word, count in word_counts.items():
    print(f"{word}: {count}")



# word count excluding common stopwords and plotting it to a graph
import matplotlib.pyplot as plt

# Define common stopwords
stopwords = {"the", "and", "is", "in", "on", "at", "to", "for", "with", "of", "a", "an", "that", "this"}

# Word count program with file reading, sorting, and visualization
def word_count_from_file(filename):
    word_freq = {}  # Dictionary to store word frequencies
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.lower().split()  # Convert text to lowercase and split into words
            for word in words:
                word = word.strip(",.!?()[]{}\"'")  # Remove punctuation
                if word not in stopwords:  # Exclude stopwords
                    word_freq[word] = word_freq.get(word, 0) + 1  # Count occurrences
    
    # Sort dictionary by frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_word_freq

# Function to visualize word frequency
def plot_word_frequencies(word_freq):
    words = list(word_freq.keys())[:10]  # Get top 10 most frequent words
    counts = list(word_freq.values())[:10]

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color="skyblue")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top 10 Most Frequent Words (Excluding Stopwords)")
    plt.xticks(rotation=45)
    plt.show()

# Example usage
filename = "sample.txt"  # Replace with your file name
word_counts = word_count_from_file(filename)

# Display word count results
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Visualize word frequencies
plot_word_frequencies(word_counts)



# word count with interactive menu to word search, graph, filter by frequencey, top words
import matplotlib.pyplot as plt

# Define common stopwords
stopwords = {"the", "and", "is", "in", "on", "at", "to", "for", "with", "of", "a", "an", "that", "this"}

# Word count program with interactive search and filtering
def word_count_from_file(filename):
    word_freq = {}  # Dictionary to store word frequencies
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.lower().split()  # Convert text to lowercase and split into words
            for word in words:
                word = word.strip(",.!?()[]{}\"'")  # Remove punctuation
                if word not in stopwords:  # Exclude stopwords
                    word_freq[word] = word_freq.get(word, 0) + 1  # Count occurrences
    
    # Sort dictionary by frequency in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_word_freq

# Function to search for a word interactively
def search_word(word_freq):
    word = input("\nEnter a word to check frequency: ").lower().strip()
    print(f"\n'{word}' appears {word_freq.get(word, 0)} times.")

# Function to filter words based on frequency threshold
def filter_words(word_freq):
    min_count = int(input("\nEnter minimum frequency to display words: "))
    filtered = {word: count for word, count in word_freq.items() if count >= min_count}
    print("\nFiltered word counts:")
    for word, count in filtered.items():
        print(f"{word}: {count}")

# Function to visualize word frequency
def plot_word_frequencies(word_freq):
    words = list(word_freq.keys())[:10]  # Get top 10 most frequent words
    counts = list(word_freq.values())[:10]

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color="skyblue")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top 10 Most Frequent Words (Excluding Stopwords)")
    plt.xticks(rotation=45)
    plt.show()

# Example usage
filename = "sample.txt"  # Replace with your file name
word_counts = word_count_from_file(filename)

# Main interactive menu
while True:
    print("\nInteractive Word Count Menu:")
    print("1. View top words")
    print("2. Search for a word")
    print("3. Filter by frequency")
    print("4. Show word frequency graph")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    elif choice == "2":
        search_word(word_counts)
    elif choice == "3":
        filter_words(word_counts)
    elif choice == "4":
        plot_word_frequencies(word_counts)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")



# list comprehension to generate 50 randome numbers (1-5) and display in two columns
import random
from collections import Counter

# Generate a list of 50 random integers in the range 1–5
random_numbers = [random.randint(1, 5) for _ in range(50)]

# Summarize with Counter
counts = Counter(random_numbers)

# Display results in two-column format
print("Number | Count")
print("----------------")
for number, count in sorted(counts.items()):
    print(f"{number:<7} | {count}")


# list comprehension to generate 50 randome numbers (1-5) and display tabular and sorted
import random
from collections import Counter

# Generate a list of 50 random integers in the range 1–5
random_numbers = [random.randint(1, 5) for _ in range(50)]

# Summarize with Counter
counts = Counter(random_numbers)

# Sort results by highest occurrence first
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# Display results in a well-formatted table
print(f"{'Number':<10}{'Count':<10}")
print("-" * 20)

for number, count in sorted_counts:
    print(f"{number:<10}{count:<10}")

# list comprehension to generate 50 randome numbers (1-5) and display tabular and sorted with graph
import random
import matplotlib.pyplot as plt
from collections import Counter

# Generate a list of 50 random integers in the range 1–5
random_numbers = [random.randint(1, 5) for _ in range(50)]

# Summarize with Counter
counts = Counter(random_numbers)

# Sort results by highest occurrence first
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# Extract values for plotting
numbers = [num for num, count in sorted_counts]
frequencies = [count for num, count in sorted_counts]

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(numbers, frequencies, color='skyblue', edgecolor='black')
plt.xlabel("Numbers")
plt.ylabel("Frequency")
plt.title("Frequency of Randomly Generated Numbers (1–5)")
plt.xticks(numbers)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()





# line with numbers on it
import matplotlib.pyplot as plt

# Dictionary of student grades
student_grades = {
    "Alice": {"Math": 85, "Science": 90, "English": 88, "History": 92, "Art": 95},
    "Bob": {"Math": 78, "Science": 83, "English": 80, "History": 76, "Art": 82},
    "Charlie": {"Math": 92, "Science": 89, "English": 94, "History": 88, "Art": 90},
    "David": {"Math": 76, "Science": 80, "English": 75, "History": 72, "Art": 78},
    "Emma": {"Math": 88, "Science": 86, "English": 91, "History": 85, "Art": 87}
}

# Function to calculate the average grade per subject
def calculate_subject_averages(student_grades):
    subject_totals = {}
    subject_counts = {}

    for grades in student_grades.values():
        for subject, grade in grades.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + grade
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Calculate subject averages
subject_averages = calculate_subject_averages(student_grades)

# Plotting the data
subjects = list(subject_averages.keys())
averages = list(subject_averages.values())

plt.figure(figsize=(8, 5))
plt.plot(subjects, averages, marker='o', linestyle='-', color='blue', label="Average Grade")
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.title("Average Grade Per Subject")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding data labels
for i, avg in enumerate(averages):
    plt.text(subjects[i], avg, f"{avg:.2f}", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.legend()
plt.show()






# rolling two six-sided dice creates 36 possible outcomes, the number 7 will be the most frequent sum while 2 and 12 will be the least frequent
import random
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def roll_dice_simulation(num_rolls):
    sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls)]
    
    # Count occurrences of each sum (2-12)
    sum_counts = Counter(sums)
    
    # Create a sorted list of sums (2 to 12)
    possible_sums = list(range(2, 13))
    frequencies = [sum_counts.get(sum_value, 0) for sum_value in possible_sums]

    return possible_sums, frequencies

def plot_dice_sums(num_rolls):
    possible_sums, frequencies = roll_dice_simulation(num_rolls)

    # Create DataFrame for Seaborn
    import pandas as pd
    df = pd.DataFrame({"Sum": possible_sums, "Frequency": frequencies})

    # Plot using horizontal bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(y="Sum", x="Frequency", data=df, palette="coolwarm", orient="h")

    plt.xlabel("Frequency")
    plt.ylabel("Sum of Two Dice")
    plt.title(f"Dice Roll Sum Frequencies for {num_rolls} Rolls")
    plt.show()

# Example usage
plot_dice_sums(10000)  # Simulate rolling two dice 10,000 times










# multiples of 5 starting at number 3
multiples3 =  [x for x in range(3, 30, 5)]

# generator expression that cubes the even integers in a list
list(x ** 3 for x in [10, 3, 7, 1, 9, 4, 2] if x % 2 == 0)


# roll dice 5,000,000 times
import random
from collections import Counter

# Number of rolls
num_rolls = 5_000_000

# Simulate rolling a six-sided die
rolls = [random.randint(1, 6) for _ in range(num_rolls)]

# Count occurrences of each outcome
outcome_counts = Counter(rolls)

# Display results
for face, count in sorted(outcome_counts.items()):
    print(f"Face {face}: {count} times")


# find all prime number in 1 through 10,000
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)  # Assume all numbers are prime initially
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for num in range(2, int(limit**0.5) + 1):  # Only go up to the square root of the limit
        if primes[num]:  # If num is still prime, mark multiples as not prime
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    return [num for num in range(limit + 1) if primes[num]]  # Collect all prime numbers

# Find primes from 1 to 10,000
prime_numbers = sieve_of_eratosthenes(10_000)

# Print the result
print(prime_numbers)


# test if word is a palindrome
def is_palindrome(s):
    # Normalize the string by removing spaces and converting to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A Santa at NASA"))  # True



# print all anagrams of an input word...
from itertools import permutations

def generate_anagrams(s):
    # Create all possible permutations of the given string
    anagrams = set(''.join(p) for p in permutations(s))
    
    return sorted(anagrams)  # Sorting for readability

# Example usage
word = "abc"
anagrams = generate_anagrams(word)

# Print the results
print(anagrams)



# Print every possible word for a given phone number
from itertools import product

# Mapping of digits to letters (like on a phone keypad)
digit_to_letters = {
    "2": "ABC", "3": "DEF", "4": "GHI",
    "5": "JKL", "6": "MNO", "7": "PQRS",
    "8": "TUV", "9": "WXYZ"
}

def generate_word_combinations(phone_number):
    if len(phone_number) != 7 or not phone_number.isdigit():
        return "Please enter a valid seven-digit number."

    # Get the possible letters for each digit
    letter_options = [digit_to_letters[d] for d in phone_number if d in digit_to_letters]

    # Generate all possible letter combinations
    possible_words = [''.join(combo) for combo in product(*letter_options)]

    return possible_words

# Example usage
phone_number = "2345678"
word_combinations = generate_word_combinations(phone_number)

# Display a sample of results
print(word_combinations[:20])  # Show only first 20 combinations for readability





# Get user input and separate characters
number = input("Enter a five-digit integer: ")

# Ensure the input is exactly five digits
if len(number) == 5 and number.isdigit():
    # Print each digit separated by three spaces
    print("   ".join(number))
else:
    print("Invalid input! Please enter a five-digit integer.")

for character in 'Branton':
    print(character, end=" ")

for character in reversed('Branton'):
    print(character, end=" ")

for character in 'Branton':
    print(character.upper(), end=" ")

for character in 'Branton':
    print(character.lower(), end=" ")

for index, character in enumerate('Branton'):
    print(f"Index {index}: {character}")

vowels = "AEIOUaeiou"
for character in 'Branton':
    if character in vowels:
        print(character, end=" ")

vowels = "AEIOUaeiou"
for character in 'Branton':
    if character not in vowels:
        print(character, end=" ")

vowels = "AEIOUaeiou"
vowel_count = 0
consonant_count = 0
for character in 'Branton':
    if character in vowels:
        vowel_count += 1
    elif character.isalpha():  # Ensures non-alphabet characters aren’t counted
        consonant_count += 1
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

vowels = "AEIOUaeiou"
uppercase_count = 0
lowercase_count = 0
for character in 'Branton':
    if character.isupper():
        uppercase_count += 1
    elif character.islower():
        lowercase_count += 1
print(f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")

uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0
text = "Branton123!@#"
for character in text:
    if character.isupper():
        uppercase_count += 1
    elif character.islower():
        lowercase_count += 1
    elif character.isdigit():
        digit_count += 1
    else:
        special_count += 1
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")

text = "Branton123!@#"
filtered_text = ""
for character in text:
    if character.isalpha():  # Keeps only letters (A-Z, a-z)
        filtered_text += character
print(f"Filtered text (only letters): {filtered_text}")

text = "Branton123!@#"
modified_text = ""
for character in text:
    if character.isdigit():
        modified_text += "*"
    else:
        modified_text += character
print(f"Modified text (digits replaced): {modified_text}")

text = "Branton123!@#"
filtered_text = "".join(sorted([c for c in text if c.isalpha()]))
print(f"Sorted text (only letters): {filtered_text}")


# Get user input for palindrome
number = input("Enter a five-digit integer: ")

# Ensure the input is exactly five digits
if len(number) == 5 and number.isdigit():
    # Check if the number is the same forward and backward
    if number == number[::-1]:
        print(f"{number} is a palindrome!")
    else:
        print(f"{number} is not a palindrome.")
else:
    print("Invalid input! Please enter a five-digit integer.")



# cube each element of a list, calls it with the list containing numbers 1 through 10, and then displays the modified list
def cube_elements(lst):
    return [x**3 for x in lst]

# Define the list
numbers = list(range(1, 11))

# Call the function
cubed_numbers = cube_elements(numbers)

# Show the result
print(cubed_numbers)

This function uses list comprehension to efficiently cube each element in the given list. After calling it, the output will be:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]






# Get user input for initial population and growth rate
current_population = int(input("Enter the current world population: "))
growth_rate = float(input("Enter the annual growth rate (as a percentage, e.g., 1 for 1%): ")) / 100  # Convert to decimal

# Headers for the table
print(f"\n{'Year':<10} {'Population':<20} {'Increase':<20}")

# Initialize variables
population = current_population
double_year = None
quadruple_year = None

# Loop through 100 years
for year in range(1, 101):
    increase = population * growth_rate  # Calculate yearly increase
    population += increase  # Update population
    
    # Print the data in table format
    print(f"{year:<10} {int(population):<20} {int(increase):<20}")
    
    # Determine when population doubles and quadruples
    if double_year is None and population >= 2 * current_population:
        double_year = year
    if quadruple_year is None and population >= 4 * current_population:
        quadruple_year = year

# Print results for doubling and quadrupling population
print(f"\nThe population will double in year {double_year}.")
print(f"The population will quadruple in year {quadruple_year}.")



# Find mean, median and mode of a set up numbers
import statistics

# Define the dataset
numbers = [9, 11, 22, 34, 17, 22, 34, 22, 34, 40]

# Calculate mean, median, and mode
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
mode_value = statistics.multimode(numbers)  # Handles multiple modes

# Display results
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")


# Square numbers in a list
numbers = [2, 4, 6, 8]
squared_numbers = [num ** 2 for num in numbers]
print(f"Squared numbers: {squared_numbers}")



# Get user input for range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
# Ensure valid range
if start > end:
    print("Invalid range! The starting number should be less than or equal to the ending number.")
else:
    print(f"\nSquares of numbers from {start} to {end}:")
    for num in range(start, end + 1):
        print(f"{num} squared is {num ** 2}")


# Function to Square a number input
def square(num):
    return num ** 2
print(square(9))  # Output: 81



# simulates rolling a six-sided die 500,000 times and counts the frequency of each outcome
import random
# Initialize a dictionary to store frequency counts
dice_rolls = {i: 0 for i in range(1, 7)}
# Roll the dice 500,000 times
for _ in range(500_000):
    roll = random.randint(1, 6)
    dice_rolls[roll] += 1
# Display the results
print(f"{'Roll':<10} {'Frequency':<10}")
for roll, frequency in sorted(dice_rolls.items()):
    print(f"{roll:<10} {frequency:<10}")




# play craps with dice rolls
import random

def roll_dice():
    """Rolls two dice and returns their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def play_craps():
    """Simulates a game of Craps."""
    print("Rolling dice... 🎲🎲")
    first_roll = roll_dice()
    print(f"You rolled: {first_roll}")

    # Instant win conditions
    if first_roll in [7, 11]:
        print("You win! 🎉")
    # Instant lose conditions
    elif first_roll in [2, 3, 12]:
        print("Craps! You lose. 😞")
    else:
        # Establish the point
        point = first_roll
        print(f"Your point is {point}. Rolling until you match it or roll a 7...")
        
        while True:
            roll = roll_dice()
            print(f"You rolled: {roll}")
            if roll == point:
                print("You hit your point! You win! 🎉")
                break
            elif roll == 7:
                print("You rolled a 7. You lose. 😞")
                break

play_craps()


# play and BET on craps
import random

def roll_dice():
    """Rolls two dice and returns their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def play_craps():
    """Simulates a game of Craps with betting."""
    balance = 100  # Starting balance

    while balance > 0:
        print(f"\nYour current balance: ${balance}")
        bet = int(input("Enter your bet (or 0 to exit): "))

        if bet == 0:
            print("Thanks for playing! See you next time.")
            break
        elif bet > balance:
            print("You can't bet more than you have! Try again.")
            continue

        print("\nRolling dice... 🎲🎲")
        first_roll = roll_dice()
        print(f"You rolled: {first_roll}")

        # Instant win conditions
        if first_roll in [7, 11]:
            print("You win! 🎉")
            balance += bet  # Increase balance
        # Instant lose conditions
        elif first_roll in [2, 3, 12]:
            print("Craps! You lose. 😞")
            balance -= bet  # Deduct bet
        else:
            # Establish the point
            point = first_roll
            print(f"Your point is {point}. Rolling until you match it or roll a 7...")
            
            while True:
                roll = roll_dice()
                print(f"You rolled: {roll}")
                if roll == point:
                    print("You hit your point! You win! 🎉")
                    balance += bet  # Increase balance
                    break
                elif roll == 7:
                    print("You rolled a 7. You lose. 😞")
                    balance -= bet  # Deduct bet
                    break

    print("\nGame over! Your final balance is ${balance}.")

play_craps()



# play craps 2 player
import random

def roll_dice():
    """Rolls two dice and returns their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def play_craps():
    """Simulates a multiplayer Craps game with betting."""
    # Initialize player balances
    players = ["Player 1", "Player 2"]
    balances = {player: 100 for player in players}  # Each starts with $100
    
    while all(balance > 0 for balance in balances.values()):
        for player in players:
            print(f"\n{player}'s balance: ${balances[player]}")
            bet = int(input(f"{player}, enter your bet (or 0 to exit): "))

            if bet == 0:
                print(f"{player} has exited the game!")
                return
            
            elif bet > balances[player]:
                print("You can't bet more than you have! Try again.")
                continue

            print(f"\n{player} is rolling dice... 🎲🎲")
            first_roll = roll_dice()
            print(f"{player} rolled: {first_roll}")

            # Instant win conditions
            if first_roll in [7, 11]:
                print(f"{player} wins! 🎉")
                balances[player] += bet  # Increase balance
            # Instant lose conditions
            elif first_roll in [2, 3, 12]:
                print(f"Craps! {player} loses. 😞")
                balances[player] -= bet  # Deduct bet
            else:
                # Establish the point
                point = first_roll
                print(f"{player}'s point is {point}. Rolling until they match it or roll a 7...")
                
                while True:
                    roll = roll_dice()
                    print(f"{player} rolled: {roll}")
                    if roll == point:
                        print(f"{player} hit their point! They win! 🎉")
                        balances[player] += bet  # Increase balance
                        break
                    elif roll == 7:
                        print(f"{player} rolled a 7. They lose. 😞")
                        balances[player] -= bet  # Deduct bet
                        break

        # Check if either player is out of money
        if any(balance <= 0 for balance in balances.values()):
            break

    # Final results
    print("\nGame over! Final balances:")
    for player, balance in balances.items():
        print(f"{player}: ${balance}")

play_craps()








# simulate 20 coin flips
import random
flips = ["H" if random.randrange(2) == 0 else "T" for _ in range(20)]
# Count occurrences
heads_count = flips.count("H")
tails_count = flips.count("T")
# Print results
print(" ".join(flips))
print(f"\nTotal Heads: {heads_count}, Total Tails: {tails_count}")




# simulates rolling a six-sided die 500,000 times and counts the frequency of each outcome and display a histogram with Matplotlib.
import random
import matplotlib.pyplot as plt
# Initialize a dictionary to store frequency counts
dice_rolls = {i: 0 for i in range(1, 7)}

# Roll the dice 500,000 times
for _ in range(500_000):
    roll = random.randint(1, 6)
    dice_rolls[roll] += 1

# Extract data for plotting
faces = list(dice_rolls.keys())
frequencies = list(dice_rolls.values())

# Create a histogram
plt.bar(faces, frequencies, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel("Dice Face")
plt.ylabel("Frequency")
plt.title("Dice Roll Frequency Over 500,000 Rolls")

# Show the plot
plt.show()





# print roll of dice 10x random numbers
import random
for roll in range(10):
    print(random.randrange(1,7), end=' ')



# Define the maximum function
def find_maximum(value1, value2, value3):
    return max(value1, value2, value3)

# Call the function with different data types
print(f"Maximum of integers (7, 15, 3): {find_maximum(7, 15, 3)}")
print(f"Maximum of floating-point numbers (4.5, 9.2, 7.8): {find_maximum(4.5, 9.2, 7.8)}")
print(f"Maximum of strings ('apple', 'orange', 'banana'): {find_maximum('apple', 'orange', 'banana')}")





# Get user input to calc factorial
number = int(input("Enter a nonnegative integer: "))

# Ensure the input is nonnegative
if number < 0:
    print("Invalid input! Please enter a nonnegative integer.")
else:
    # Compute factorial using a loop
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is: {factorial}")







grades = [70, 80, 82, 90, 65, 92, 85, 100, 82]

# Initialize a variable to store the total sum of grades
total = 0

# Iterate through the list and add each grade to the total
for grade in grades:
    total += grade

# Calculate the average
average = total / len(grades)

print(f"The average grade is: {average:.2f}")




grades = [70, 80, 82, 90, 65, 92, 85, 100, 82]

# Remove the lowest grade
grades.remove(min(grades))

# Initialize total sum
total = 0

# Calculate the sum using a loop
for grade in grades:
    total += grade

# Compute the average
average = total / len(grades)

print(f"The average grade (excluding lowest) is: {average:.2f}")



grades = [70, 80, 82, 90, 65, 92, 85, 100, 82]

# Define threshold
threshold = 75

# Create a new list of grades above the threshold
filtered_grades = [grade for grade in grades if grade >= threshold]

# Calculate the sum
total = sum(filtered_grades)

# Compute the average
average = total / len(filtered_grades)

print(f"The average of grades ≥ {threshold} is: {average:.2f}")



grades = [70, 80, 82, 90, 65, 92, 85, 100, 82]

# Get threshold from user input
threshold = int(input("Enter a threshold value: "))

# Filter grades based on the user-provided threshold
filtered_grades = [grade for grade in grades if grade >= threshold]

# Ensure there's at least one grade above the threshold
if filtered_grades:
    average = sum(filtered_grades) / len(filtered_grades)
    print(f"The average of grades ≥ {threshold} is: {average:.2f}")
else:
    print(f"No grades are ≥ {threshold}. Try a lower threshold.")







sales = [200, 1500, 3000, 100, 5000]
for sale in sales:
    if sale > 2500:
        print(f"Found a sale above the threshold: {sale}")
        break  # Exit the loop as soon as we find the first sale above 2500


sales = [200, 1500, 3000, 100, 5000]

for sale in sales:
    if sale > 4000:
        print(f"Found a sale above the threshold: {sale}")
        break

sales = [200, 1500, 3000, 100, 5000]

for sale in sales:
    if sale < 1000:
        continue  # Skip sales that are less than 1000
    print(f"Processing significant sale: {sale}")



pie = 3.14159
radius = 5
circumference = 2*pie*radius
area = pie*(radius**2)
remain = 26 % 2
print (pie)
print (radius)
print (circumference)
print (area)
print (remain)

if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")


if 10 % 2 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")

print("Number\tSquare\tCube")  # Header row
for num in range(6):  # Iterate from 0 to 5
    print(f"\t{num}\t\t\t{num**2}\t\t\t{num**3}")  # Print values with tab spacing


print (ord('a'))


# Get user input
num = input("Enter a five-digit number: ")

# Check if input is exactly five digits
if len(num) == 5 and num.isdigit():
    # Separate digits with three spaces
    print("   ".join(num))
else:
    print("Invalid input. Please enter a five-digit integer.")


sales: list = [12000, 15000, 18000, 13000, 17000]
for sale in sales:
    print(f"Monthly sales: {sale}")




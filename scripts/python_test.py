# Online Python - IDE, Editor, Compiler, Interpreter

from pathlib import Path

for i in range(1, 5):
    folder_name = f"folder_{i}"
    Path(folder_name).mkdir(exist_ok=True)
    print(f"Folder '{folder_name}' created.")


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




grades = [70, 80, 82, 90, 65, 92, 85, 100, 82]

# Initialize a variable to store the total sum of grades
total = 0

# Iterate through the list and add each grade to the total
for grade in grades:
    total += grade

# Calculate the average
average = total / len(grades)

print(f"The average grade is: {average:.2f}")






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




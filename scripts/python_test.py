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




'''
# Taking input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculating the sum
result = num1 + num2

# Printing the sum
print("The sum of", num1, "and", num2, "is:", result)
'''
'''
def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example usage:
num = int(input("Enter a number: "))
even_or_odd(num)
'''
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
num = int(input("Enter a number to calculate its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}.")
    '''
'''
def greet_user():
    name = input("What is your name? ")
    print(f"Hello, {name}! Nice to meet you.")

# Call the function to execute the program
greet_user()
'''

'''
def main():
    # Get input from user
    user_input = input("Enter a string to write to a text file: ")

    # Specify the file path
    file_path = "output.txt"

    # Open the file in write mode ("w")
    file = open(file_path, 'w')

    # Write the input string to the file
    file.write(user_input)

    # Close the file
    file.close()

    print(f'Successfully wrote "{user_input}" to {file_path}')


if __name__ == "__main__":
    main()
    '''
'''
def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Example usage:
filename = 'C:/Users/user/Desktop/sample.txt'  # Replace with your file name
read_and_print_file(filename)
'''
'''

def main():
    # Take input from the user
    user_input = input("Enter a string: ")

    # Calculate the length of the string
    length_of_string = len(user_input)

    # Print the length of the string
    print(f"The length of the string '{user_input}' is {length_of_string}.")


if __name__ == "__main__":
    main()
'''
'''
def concatenate_strings(str1, str2):
    concatenated_string = str1 + str2
    return concatenated_string

# Example usage:
string1 = "Hello, "
string2 = "world!"
result = concatenate_strings(string1, string2)
print("Concatenated string:", result)
'''
'''def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

# Example usage:
main_string = "Hello, how are you today?"
substring1 = "how"
substring2 = "world"

# Check if substring1 is present in main_string
print(f"Substring '{substring1}' is present: {check_substring(main_string, substring1)}")

# Check if substring2 is present in main_string
print(f"Substring '{substring2}' is present: {check_substring(main_string, substring2)}")'''

'''def convert_to_uppercase(input_string):
    return input_string.upper()

# Example usage:
input_string = "Hello, World!"

# Convert input_string to uppercase
uppercase_string = convert_to_uppercase(input_string)

# Print the original and uppercase strings
print(f"Original string: {input_string}")
print(f"Uppercase string: {uppercase_string}")
'''

'''
def generate_fibonacci(n):
    fibonacci_sequence = []

    # First two numbers in Fibonacci sequence
    a, b = 0, 1

    # Handle case where n = 1 separately
    if n >= 1:
        fibonacci_sequence.append(a)

    # Generate Fibonacci sequence up to nth number
    for _ in range(1, n):
        fibonacci_sequence.append(b)
        a, b = b, a + b

    return fibonacci_sequence


# Example usage:
n = 10
fib_sequence = generate_fibonacci(n)

# Print the Fibonacci sequence
print(f"First {n} numbers in Fibonacci sequence:")
print(fib_sequence)
'''

'''
def sum_of_digits(number):
    # Convert number to string to iterate through each digit
    num_str = str(number)

    # Initialize sum variable
    digit_sum = 0

    # Iterate through each digit in the string representation of the number
    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum


# Example usage:
number = 12345

# Calculate the sum of digits
result = sum_of_digits(number)

# Print the result
print(f"The sum of digits of {number} is: {result}")
'''
'''
import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

# Input birth year from user
while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid year.")

# Calculate age based on birth year
age = calculate_age(birth_year)

# Print the calculated age
print(f"You are {age} years old.")
'''
'''
def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

# Read multiple lines of input
input_lines = read_multiple_lines()

# Print all the lines entered
print("\nAll lines entered:")
for line in input_lines:
    print(line)
'''
'''
import csv

def read_csv_file(file_name):
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

# Example usage:
file_name = 'C:/Users/user/Downloads/data.csv'

# Read and print contents of CSV file
print(f"Contents of '{file_name}':")
read_csv_file(file_name)
'''
'''
def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count for the character in the dictionary
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency

# Example usage:
input_string = "hello world"

# Count the frequency of each character in the input string
frequency_dict = count_character_frequency(input_string)

# Print the character frequencies
print("Character frequencies:")
for char, freq in frequency_dict.items():
    print(f"Character '{char}' occurs {freq} times")
'''
'''
def convert_to_title_case(input_string):
    # Split the input string into words
    words = input_string.split()

    # Initialize an empty list to store capitalized words
    title_case_words = []

    # Iterate through each word and capitalize the first letter
    for word in words:
        # Capitalize the first letter and concatenate with the rest of the word
        capitalized_word = word[0].upper() + word[1:].lower()
        title_case_words.append(capitalized_word)

    # Join the capitalized words back into a single string
    title_case_string = ' '.join(title_case_words)

    return title_case_string

# Example usage:
input_string = "hello world! how are you today?"

# Convert input_string to title case
title_case_output = convert_to_title_case(input_string)

# Print the title case output
print(f"Original string: {input_string}")
print(f"Title case output: {title_case_output}")
'''

'''
def are_anagrams(string1, string2):
    # Remove spaces and convert to lowercase for case insensitivity
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if the lengths of the strings are equal
    if len(string1) != len(string2):
        return False

    # Sort characters in both strings and compare
    return sorted(string1) == sorted(string2)


# Example usage:
string1 = "listen"
string2 = "silent"

# Check if string1 and string2 are anagrams
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")

'''
'''
import string


def remove_punctuation(input_string):
    # Create a translation table
    translator = str.maketrans('', '', string.punctuation)

    # Remove punctuation using the translation table
    cleaned_string = input_string.translate(translator)

    return cleaned_string


# Example usage:
input_string = "Hello, world! This is a test string."

# Remove punctuation from input_string
cleaned_string = remove_punctuation(input_string)

# Print the cleaned string
print(f"Original string: {input_string}")
print(f"String without punctuation: {cleaned_string}")
'''
'''
def calculate_sum(numbers):
    total = sum(numbers)
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of numbers in the list
total_sum = calculate_sum(numbers)

# Print the total sum
print(f"The sum of numbers {numbers} is: {total_sum}")
'''
'''
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage:
numbers = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2

# Count occurrences of element_to_count in numbers list
occurrences = count_occurrences(numbers, element_to_count)

# Print the number of occurrences
print(f"The element {element_to_count} appears {occurrences} times in the list.")
'''

'''
def find_min_max(numbers):
    if not numbers:
        return None, None  # Handle empty list case

    minimum = min(numbers)
    maximum = max(numbers)

    return minimum, maximum


# Example usage:
numbers = [5, 2, 8, 1, 6, 9, 3]

# Find minimum and maximum values in numbers list
min_value, max_value = find_min_max(numbers)

# Print the results
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
'''
'''
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
'''
'''

# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2


def main():
    print("Simple Calculator")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")

    # Input from user
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    # Perform operation based on operator
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator!")
        return

    # Print the result
    print(f"{num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    main()
'''
'''
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                # Read all lines from source and write to destination
                for line in source:
                    destination.write(line)
        print(f"Contents from '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except IOError as e:
        print(f"Error occurred: {e}")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")

    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
'''
'''

def check_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)

    if starts_with_prefix:
        print(f"The string '{string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{string}' does not start with the prefix '{prefix}'.")

    if ends_with_suffix:
        print(f"The string '{string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{string}' does not end with the suffix '{suffix}'.")


def main():
    string = input("Enter a string: ")
    prefix = input("Enter a prefix to check: ")
    suffix = input("Enter a suffix to check: ")

    check_prefix_suffix(string, prefix, suffix)


if __name__ == "__main__":
    main()
'''


def string_to_list_of_characters(input_string):
    # Using list() constructor to convert string to list of characters
    characters_list = list(input_string)
    return characters_list


def main():
    input_string = input("Enter a string: ")
    characters_list = string_to_list_of_characters(input_string)

    print(f"The string '{input_string}' converted to a list of characters is:")
    print(characters_list)


if __name__ == "__main__":
    main()
































































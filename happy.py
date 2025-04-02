# Task 1: Sum of integers in a list

# Create an empty list to store integers
numbers = []

# Ask the user how many numbers they want to input
num_count = int(input("How many numbers do you want to add to the list? "))

# Loop to get user input for each number
for i in range(num_count):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Compute the sum of the list
total_sum = sum(numbers)

# Print the list and the sum
print(f"Your list of numbers: {numbers}")
print(f"Sum of all integers: {total_sum}")


# Task 2: Tuple of favorite books

# Create a tuple with five favorite books
favorite_books = ("To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice", "The Hobbit")

# Use a for loop to print each book on a separate line
print("My favorite books:")
for book in favorite_books:
    print(book)
    
# Task 3: Dictionary to store person information

# Create an empty dictionary
person = {}

# Ask the user for input and store it in the dictionary
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("\nPerson Information:")
print(person)


# Task 4: Find common elements in two sets

# Create two empty sets
set1 = set()
set2 = set()

# Ask the user for the first set
print("Enter integers for the first set (one at a time, press Enter after each):")
for i in range(3):  # Let's take 3 numbers for each set
    num = int(input(f"Enter number {i+1} for set 1: "))
    set1.add(num)

# Ask the user for the second set
print("\nEnter integers for the second set (one at a time, press Enter after each):")
for i in range(3):
    num = int(input(f"Enter number {i+1} for set 2: "))
    set2.add(num)

# Find the common elements using intersection
common_elements = set1.intersection(set2)

# Print the sets and the common elements
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")
print(f"Common elements: {common_elements}")

# Task 5: Filter words with odd number of characters

# Create a list of words
words = ["cat", "dog", "hello", "world", "python", "a", "code"]

# Use list comprehension to filter words with odd length
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the original and filtered lists
print(f"Original list: {words}")
print(f"Words with odd number of characters: {odd_length_words}")
# temp = int(input("What is the temperature today?"))
# if temp > 30:
#     print("It's hot outside!")
# elif temp < 10:
#     print("It's cold outside!")
# else:
#     print("The weather is nice today!")

# Example of a for loop
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(f"I love {fruit}!")

# name = input("What is your name?") 
# age = int(input("What is your age?"))

# def introduce(name, age):
#     return f"My name is {name}, and I'm {age} years old."

# print(introduce(name, age))


# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))

# # Define the large_power function
# def large_power(base, exponent):
#     # Calculate base raised to the exponent
#     result = base ** exponent
#     # Check if the result is greater than 5000
#     if result > 5000:
#         return True
#     else:
#         return False
    
# # Call the function and print the result
# print(large_power(base, exponent))
# print(base ** exponent )

# Define the divisible_by_ten function
def divisible_by_ten(num):
    # Check if num is divisible by 10 using the modulo operator
    # If num % 10 == 0, the number is divisible by 10
    return num % 10 == 0

# Test the function with some examples
print(divisible_by_ten(20))  # Should return True (20 is divisible by 10)
print(divisible_by_ten(15))  # Should return False (15 is not divisible by 10)
print(divisible_by_ten(0))   # Should return True (0 is divisible by 10)
print(divisible_by_ten(-30)) # Should return True (-30 is divisible by 10)
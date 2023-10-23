"""

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-5.py
Write a program that prompts one user for their first name, 
then a second user for their first name. Using the format method, 
output a string that follows this template.

Hello, person1. My name is person2.


"""
p1 = input("Please enter the name of person one.")
p2 = input("Please enter the name of person two:")
# Get input for the name of person one and person two - O'Hara

my_string = "Hello, {0}. My name is {1}.".format(p1, p2)
# Use .format to format string - O'Hara

print (my_string)
# Print string - O'Hara
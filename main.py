
"""For the my integration project I will have a combination of code that displays what i learned in this class.
The user will enter their name to begin the program and enter multiple different whole numbers in the program. After
those whole numbers are entered the user has a choice to use any operator from the display menu to calculate those two
numbers.The program also contains a range counter and
code that tells you to input a 4 digit year to determine if its a leap year or not."""


__author__ = "Devon Villalona"
print('Hello there!', sep=' ')
print('Enter your name to to begin!', end='\n')
name = input()
print("Welcome, " + name + '!')  # Sting operator that uses the input name and combines it


def main():
    """This function lets you input two whole numbers and
    lets you use any operator to calculate those two numbers."""

    while True:   # A while loop that makes sure the program won't crash when entering wrong value
        try:

            first_number = int(input("Enter a whole number between 1 and 10: "))
            break
        except ValueError:
            print("Error. This value must be a whole number! Try Again!")
    while True:
        try:

            second_number = int(input("Enter another whole number between 1 and 10: "))
            break
        except ValueError:
            print("Error. This value must be a whole number! Try Again!")

    operator = input("""
     Enter a + to add.
     A - to subtract. A / to divide. 
     A % to use modulus. A // for floor division. 
     A * to multiply. 
     To use exponential calculation use **: """)

    if operator == "+":
        add_numbers(first_number, second_number)  # If-elif statement saying if the user inputs any of signs
        # It will will perform the operation with the function

    elif operator == "-":
        subtract_numbers(first_number, second_number)
    elif operator == "/":
        divide_numbers(first_number, second_number)
    elif operator == "%":
        modulus_numbers(first_number, second_number)
    elif operator == "//":
        floor_division(first_number, second_number)
    elif operator == "*":
        multiply_numbers(first_number, second_number)
    elif operator == "**":
        exponent(first_number, second_number)


# https://realpython.com/python-range/ source that helped me with this code.
print("Now lets make a range counter!")  # This is a range counter that inputs two integers and will have it display,
# the numbers in between.
print(" ")
print("Put in a whole first number!")
while True:  # A while loop that makes sure the program won't crash when entering wrong value
    try:
        number1 = int(input())
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")

print("Put a whole second number!")
while True:  # A while loop that makes sure the program won't crash when entering wrong value
    try:
        number2 = int(input())
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")
if number1 >> number2:
    number1, number2 = number2, number1
else:
    number1, number2 = number1, number2
both_numbers = list(range(number1, number2))

print(" ")
print("The numbers in between are:")
print(number1, number2)

for both_numbers in range(number1, number2):
    print(both_numbers + 1)

# https://www.programiz.com/python-programming/examples/leap-year this is a source that helped me with the leap year.
print("Now lets move on to the second part!")  # input any year to see if it is leap year or common year.
while True:  # A while loop that makes sure the program won't crash when entering wrong value
    try:
        year = int(input("Input any 4 digit year:  "))
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")
if (year % 4 == 0) and (year % 100 != 0):
    print('This is a leap year!', year)
elif year / 400 == 0:
    print('This is a leap year!', year)
else:
    print('This is a common year!', year)
while True:  # A while loop that makes sure the program won't crash when entering wrong value
    try:
        current_run = int(input("How many miles do you run now? "))
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")
while True:  # A while loop that makes sure the program won't crash when entering wrong value
    try:
        running_goal = int(input("What is your running goal? "))
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")
miles = 1

if not current_run == '1':
    print("Go run more!")
while current_run < running_goal:
    current_run += current_run * 0.1
    miles += 1

print("If you increase your distance each day by 10%, you can reach your running goal in " + str(miles), "days!")
while True:  # A while loop that makes sure the program won't crash when entering wrong value.
    try:
        gym_set = int(input("How many times do you squat? "))
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")
while True:  # A while loop that makes sure the program won't crash when entering wrong value.
    try:
        gym_set2 = int(input("How many times do you bench? "))
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")
while True:  # A while loop that makes sure the program won't crash when entering wrong value.
    try:
        gym_set3 = int(input("How many times do you dead lift "))
        break  # This breaks the loop if the input is a whole number.
    except ValueError:
        print("Error. This value must be a whole number! Try Again!")
if gym_set >= 5 and gym_set2 >= 5 or gym_set3 >= 5:
    print("Great job and continue to go!")
else:
    print("Never too late to go more!")


def add_numbers(num1, num2):
    """This function prints num1 and num 2 with a + sign and = sign.
    Also adds both whole numbers. """
    print(num1, "+", num2, "=", num1 + num2)


def subtract_numbers(num1, num2):
    """ This function prints num1 and num 2 with a - sign and = sign.
    Also subtracts both whole numbers. """

    print(num1, "-", num2, "=", num1 - num2)


def divide_numbers(num1, num2):
    """ This function prints num1 and num 2 with a / sign and = sign.
    Also divides both whole numbers. """

    print(num1, "/", num2, "=", num1 / num2)


def modulus_numbers(num1, num2):
    """ This function prints num1 and num 2 with a % sign and = sign.
    Uses the modulus on both whole numbers. """
    print(num1, "%", num2, "=", num1 % num2)


def floor_division(num1, num2):
    """This function prints num1 and num 2 with a // sign and = sign.
    Also uses floor division on both whole numbers. """
    print(num1, "//", num2, "=", num1 // num2)


def multiply_numbers(num1, num2):
    """This function prints num1 and num 2 with a * sign and = sign.
    Also multiply both whole numbers. """
    print(num1, "*", num2, "=", num1 * num2)


def exponent(num1, num2):
    """This function prints num1 and num 2 with a ** sign and = sign.
    Also uses the exponentiation of both whole numbers."""
    print(num1, "**", num2, "=", num1 ** num2)


main()

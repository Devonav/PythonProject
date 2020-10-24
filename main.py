# Devon Villalona
# For the my integration project I will have a combination code that displays what i learned in this class.
# The user will enter their name to begin the program and enter two integers after.
# After the user inputs the two integers,
# then the user has a choice to use the following numeric operators to get the final result.

print('Hello there!', sep=' ')
print('Enter your name to to begin!',  end='\n')
name = input()
print("Welcome, "+name+'!')  # Sting operator that uses the input name and combines it


def add_numbers(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)    # This prints num1 and num 2 with a + sign and = sign.
# Also adds both integers


def subtract_numbers(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)    # This prints num1 and num 2 with a - sign and = sign.
# Also subtracts both integers.


def divide_numbers(num1, num2):
    print(num1, "/", num2, "=", num1 / num2)    # This prints num1 and num 2 with a / sign and = sign.
# Also divides both integers.


def modulus_numbers(num1, num2):
    print(num1, "%", num2, "=", num1 % num2)    # This prints num1 and num 2 with a % sign and = sign.
# Uses the modulus on both integers.


def floor_division(num1, num2):
    print(num1, "//", num2, "=", num1 // num2)  # This prints num1 and num 2 with a // sign and = sign.
# Also uses floor division on both integers


def multiply_numbers(num1, num2):
    print(num1, "*", num2, "=", num1 * num2)    # This prints num1 and num 2 with a * sign and = sign.
# Also multiply both integers


def exponent(num1, num2):
    print(num1, "**", num2, "=", num1 ** num2)  # This prints num1 and num 2 with a ** sign and = sign.
# Also uses the Exponentiation of both integer


def main():
    first_number = int(input("Enter a number between 1 and 10: "))
    second_number = int(input("Enter another number between 1 and 10: "))
    operator = input("""Enter a + to add.
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


main()
# https://realpython.com/python-range/ source that helped me with this code.
print("Now lets make a range counter!")  # This is a range counter that inputs two integers and will have it display,
# the numbers in between.
print(" ")
print("Put in your first number!")
number1 = int(input())

print("Put in your second number!")
number2 = int(input())
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
year = int(input("Input any year:  "))
if (year % 4 == 0) and (year % 100 != 0):
    print('This is a leap year!', year)
elif year / 400 == 0:
    print('This is a leap year!', year)
else:
    print('This is a common year!', year)
current_run = int(input("How many miles do you run now? "))
running_goal = int(input("What is your running goal? "))
miles = 1

if not current_run == '1':
    print("Go run more!")
while current_run < running_goal:  
    current_run += current_run * 0.1
    miles += 1

print("If you increase your distance each day by 10%, you can reach your running goal in " + str(miles), "days!")
gym_set = int(input("How many times do you squat? "))
gym_set2 = int(input("How many times do you bench? "))
gym_set3 = int(input("How many times do you dead lift "))
if gym_set >= 5 and gym_set2 >= 5 or gym_set3 >= 5:
    print("Great job and continue to go!")
else:
    print("Never too late to go more!")

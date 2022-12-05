from math import *

def my_meal(food, drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal("Lasagna", "Redbull")

#Question 2 (part 3)
number = int(input("Enter a number to cube: "))
def cube(number):
    sum = number ** 3
    return sum

def by_three(number):
        if number % 3 == 0:
            print(cube(number))
        else:
            print("False") 

by_three(number)
       


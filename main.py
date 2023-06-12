# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    numbers = [0,1, 2, 3, 4, 5]
    drawn_numbers = set(random.sample(numbers, k=4))
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    drawn_numbers.add(number1)
    drawn_numbers.add(number2)





if __name__=="__main__":
    print_hi()
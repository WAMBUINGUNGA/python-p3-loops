#!/usr/bin/env python3
def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")


def square_integers(int_list):
    squared = []
    for i in int_list:
        squared.append(i ** 2)
    return squared


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Call the functions to see the output
happy_new_year()

example_list = [1, 2, 3, 4, 5]
squared_list = square_integers(example_list)
print(squared_list)  # Output: [1, 4, 9, 16, 25]

fizzbuzz()

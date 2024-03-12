#!/usr/env python3

# for loop
pennies = [ 2018, 2001, 2012 ]

for penny in pennies:
    print(f'The year is {penny}')

# while loop
num = 0

while num <= 9:  # if true, continue, but if false, stop
    print(f'the number is {num}')
    num += 1  # num = num + 1
print(f"while loop done. 'num' is now {num}")

num_2 = 0

while True:
    print(f'my 2nd number is {num_2}')
    if num_2 == num:
        break
    num_2 += 1
print(f'"num" is {num} and "num_2" is {num_2}')

while True:
    user_input = input(": ")
    if user_input == "exit":
        break
    print("Oh, you're still here, huh?")
print("Thank you, come again!")
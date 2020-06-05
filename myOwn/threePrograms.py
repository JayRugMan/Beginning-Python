#!/usr/bin/python3
# from youtube video:
# https://youtu.be/qmWCT_OgrKQ


def customerList():
    def getCust():
        fName, lName = input("Enter Customer Name (first last): ").split()
        return {'fName': fName, 'lName': lName}

    def getCustQuerry():
        customers = []
        while True:
            yesNo = input("Enter Customer (yes/no): ").lower()
            if yesNo == 'yes' or yesNo == 'y':
                while True:
                    try:
                        customers.append(getCust())
                        break
                    except ValueError:
                        print("Please enter first and last name")
                        continue
            elif yesNo == 'no' or yesNo == 'n':
                break
            else:
                continue
        return customers

    customers = getCustQuerry()
    for dict in customers:
        print('Customer name is {fName} {lName}'.format(**dict))


def factorial():
    def factorialInner(num):
        if num <= 1:
            return 1
        else:
            result = num * factorialInner(num - 1)
            return result
    while True:
        num = input('Pick an Integer: ')
        try:
            print('{}! = {}'.format(num, factorialInner(int(num))))
            break
        except ValueError:
            print('Try entering just an integer')
            continue


def fibinachi():
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = fib(n-1) + fib(n-2)
            return result

    def fibYield(n):
        for num in range(1, n):
            yield fib(num)

    while True:
        num = input('Pick an Integer: ')
        try:
            print(list(fibYield(int(num))))
            break
        except ValueError:
            print('Try entering just an integer')
            continue


def printOptions():
    print('''
\t\t OPTIONS
1 Customer list
2 Factorials
3 Fibinachi sequence
''')


def mainSelect():
    while True:
        try:
            selection = int(input('Which program? '))
            if 0 < selection < 4:
                return selection
                break
            else:
                print('Enter 1, 2, or 3')
                continue
        except ValueError:
            print('Enter 1, 2, or 3')
            continue


def main():
    printOptions()
    selection = mainSelect()
    if selection == 1:
        customerList()
    elif selection == 2:
        factorial()
    elif selection == 3:
        fibinachi()
    else:
        print('Something went sidways....')


main()

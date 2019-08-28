#!/usr/bin/python3

# fibs = [0, 1]
# num = int(input('How many Fibonacci numbers do you want? '))
# for i in range(num-2):
#     fibs.append(fibs[-2] + fibs[-1])
# [print(nm) for nm in fibs]


def fibSeq(num):
    fibs = [0, 1]
    for i in range(num-2):
        fibs.append(fibs[-2] + fibs[-1])

    return fibs


num = int(input('How many Fibonacci numbers do you want? '))
print(', '.join(map(str, fibSeq(num))))

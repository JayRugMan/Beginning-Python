#!/usr/bin/python3
print("Paste ascii art below: ")

lines = []
setbit = 0
while True:
    line = input()
    if line:
        lines.append(line)
        setbit = 1
    elif setbit == 1:
        break

for line in lines:
    print(line)

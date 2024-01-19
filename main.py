digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

with open("codes.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

print(lines)

def sum_of_line(s):
    i = 0
    first, last = '', ''

    #find first
    for c in s:
        if c in digits:
            first = c
            break

    #find last
    for i in range(len(s) - 1, -1, -1):
        if s[i] in digits:
            last = s[i]
            break


    return int(first + last)

print(sum_of_line(lines[2]))

total = 0

for s in lines:
    total += sum_of_line(s)

print(total)



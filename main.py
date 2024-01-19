digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
digit_map = {'fiveight':'58', 'nineight':'98', 'threeight':'18', 'oneight':'18','zerone':'01','twone':'21','sevenine':'79','eighthree':'83','eightwo':'82', 'eight':'8', 'two':'2', 'zero': '0', 'one':'1', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7',  'nine':'9'}

with open("codes.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

print(lines)

def sum_of_line(s):
    i = 0
    first, last = '', ''

    #find and replace spelled out digits:
    for key in digit_map:
        s = s.replace(key, digit_map[key])



    #find first digit
    for c in s:
        if c in digits:
            first = c
            break

    #find last digit
    for i in range(len(s) - 1, -1, -1):
        if s[i] in digits:
            last = s[i]
            break


    return int(first + last)

print(sum_of_line('zoneight234'))

total = 0

for s in lines:
    total += sum_of_line(s)

print(total)


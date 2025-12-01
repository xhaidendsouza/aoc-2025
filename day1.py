test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

input = test_input

input = input.strip().split("\n")
num = 50
count = 0
for line in input:
    if line[0] == 'R':
        num += int(line[1:])
        count += abs(num//100)
        num %= 100
    else:
        num -= int(line[1:])
        count += abs(num//100) + (1 if (num%100 == 0) else 0) - (1 if (num == -int(line[1:])) else 0)
        num %= 100
print(count)
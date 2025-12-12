import math
test_input = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

input = test_input
input = [line.split(":") for line in input.strip().split("\n")]

def partA():
    count = 0
    for line in input:
        if math.prod([int(num) for num in line[0].split('x')]) > sum([int(num)*i for num, i in zip(line[1].split(), [7, 6, 5, 7, 7, 7])]):
            count += 1
    print(count)

def partB():
    pass

partA()
partB()
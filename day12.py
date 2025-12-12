import math
input = """
43x43: 55 28 36 34 18 32
"""
print(sum([1 if math.prod([int(num) for num in line[0].split('x')]) > sum([int(num)*i for num, i in zip(line[1].split(), [7, 6, 5, 7, 7, 7])]) else 0 for line in [line.split(":") for line in input.strip().split("\n")]]))
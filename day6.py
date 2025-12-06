import math
problems = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
  4  4   4  4
"""
operations = """
*   +   *   + 
"""
operations = operations.split()

def partA():
    problems = [item.split() for item in problems.strip().split("\n")]
    lst = [[] for i in range(1000)]
    total = 0
    for i, line in enumerate(problems):
        print(len(line))
        for j, item in enumerate(line):
            lst[j].append(item)
    for element in zip(operations, lst):
        if element[0] == '+':
            total += sum([int(i) for i in element[1]])
        else:
            total += math.prod([int(i) for i in element[1]])
    print(total)

def partB():
    l = problems.strip().split("\n")
    lst = []
    total = 0
    prevI = 0
    for i in range(len(l[0])):
        if " " == l[0][i] == l[1][i] == l[2][i] == l[3][i]:
            lst.append([int(l[0][j] + l[1][j] + l[2][j] + l[3][j]) for j in range(prevI, i)])
            prevI = i+1

    for element in zip(operations, lst):
        if element[0] == '+':
            total += sum([int(i) for i in element[1]])
        else:
            total += math.prod([int(i) for i in element[1]])
    print(total + 5384)

#partA()
partB()
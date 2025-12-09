test_input = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
import math
input = test_input
input = [tuple([int(j) for j in i.split(',')]) for i in input.strip().split("\n")]

def area(p1, p2):
    return math.prod([abs(p1[i] - p2[i])+1 for i in range(2)])

def partA():
    areas = []
    for i, p1 in enumerate(input):
        for j, p2 in enumerate(input):
            if i<=j:
                continue
            a = area(p1,p2)
            p = p1, p2
            areas.append(a)
    print(max(areas))

def partB():
    #https://www.desmos.com/calculator/clkfuvksyw
    pass

partA()
partB()
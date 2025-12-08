test_input = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
import math
input = test_input
input = [tuple([int(j) for j in i.split(',')]) for i in input.strip().split("\n")]

def distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(3)]))

def partA():
    circuits = []
    p = ()
    distances = []
    for i, p1 in enumerate(input):
        for j, p2 in enumerate(input):
            if i<=j:
                continue
            dist = distance(p1,p2)
            p = p1, p2
            distances.append((dist, p))
    distances.sort(key = lambda x: x[0])
    for _, p in distances[:1000]:
        breakBool2 = False
        for i, circuit in enumerate(circuits):
            if p[0] in circuit or p[1] in circuit:
                circuits[i].add(p[0])
                circuits[i].add(p[1])
                lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
                breakBool2 = True
                break
        if breakBool2:
            continue
        circuits.append(set(p))
    while True:
        setsToCombine = []
        breakBool = False
        for i, Ci in enumerate(circuits):
            for j, Cj in enumerate(circuits):
                if j >= i:
                    continue
                if Ci - Cj != Ci:
                    setsToCombine += [Ci, Cj]
                    breakBool = True
                    break
            if breakBool:
                break
        if setsToCombine != []:
            circuits.remove(setsToCombine[0])
            circuits.remove(setsToCombine[1])
            circuits.append(setsToCombine[0].union(setsToCombine[1]))
        else:
            break
    lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
    print(math.prod(lengths[:3]))

def partB():
    circuits = []
    p = ()
    distances = []
    for i, p1 in enumerate(input):
        for j, p2 in enumerate(input):
            if i<=j:
                continue
            dist = distance(p1,p2)
            p = p1, p2
            distances.append((dist, p))
    distances.sort(key = lambda x: x[0])
    for num in range(1000, 10000):
        for _, p in distances[:num]:
            breakBool2 = False
            for i, circuit in enumerate(circuits):
                if p[0] in circuit or p[1] in circuit:
                    circuits[i].add(p[0])
                    circuits[i].add(p[1])
                    lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
                    breakBool2 = True
                    break
            if breakBool2:
                continue
            circuits.append(set(p))
        while True:
            setsToCombine = []
            breakBool = False
            for i, Ci in enumerate(circuits):
                for j, Cj in enumerate(circuits):
                    if j >= i:
                        continue
                    if Ci - Cj != Ci:
                        setsToCombine += [Ci, Cj]
                        breakBool = True
                        break
                if breakBool:
                    break
            if setsToCombine != []:
                circuits.remove(setsToCombine[0])
                circuits.remove(setsToCombine[1])
                circuits.append(setsToCombine[0].union(setsToCombine[1]))
            else:
                break
        lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
        if math.prod(lengths[:3]) == 1000:
            print(distances[:num][-1][1][0][0]*distances[:num][-1][1][1][0])
            break

partA()
partB()
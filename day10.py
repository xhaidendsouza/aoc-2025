test_input = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
#input = test_input
input = input.strip().split("\n")

def partA():
    allLights = [tuple([i for i, chr in enumerate(line[line.find('[')+1:line.find(']')]) if (chr=="#")]) for line in input]
    allButtons = [[tuple([int(num) for num in point.strip('()').split(",")]) for point in line[line.find(']')+1:line.find('{')].strip('').split()] for line in input]
    def combine(b1, b2):
        b3 = list(b2)
        for b in b1:
            if b in b2:
                b3.remove(b)
            else:
                b3.append(b)
        return tuple(sorted(b3))
    def combinePresses(btns1, btns2):
        btns1 = list(btns1)
        btns2 = list(btns2)
        btns3 = set()
        for i in range (len(btns1)-1):
            for j in range(i, len(btns2)):
                btns3.add(combine(btns1[i],btns2[j]))
        return btns3
    total = 0
    for i, (lights, buttons) in enumerate(zip(allLights, allButtons)):
        l = lights
        b = buttons
        tb = True
        for j in range(1, 9):
            if l in b:
                total += j
                tb = False
                break
            b = combinePresses(buttons, b)
        if tb: print(f"Machine {i} left")
    print(total)

def partB():
    allJoltages = [tuple([int(num) for num in line[line.find('{')+1:line.find('}')].split(",")]) for line in input]
    allButtons = []
    for i, line in enumerate(input):
        machine = []
        for point in line[line.find(']')+1:line.find('{')].strip('').split():
            button = [0]*len(allJoltages[i])
            for num in range(len(allJoltages[i])):
                if str(num) in point.strip('()').split(","):
                    button[num] = 1
                else:
                    button[num] = 0
            machine.append(tuple(button))
        allButtons.append(machine)

    def combine(b1, b2):
        b3 = list(b2)
        for i in range(len(b1)):
            b3[i] = b1[i] + b2[i]
        return tuple(b3)
    def combinePresses(btns1, btns2, joltages):
        btns3 = set()
        for i in range (len(btns1)-1):
            for j in range(i, len(btns2)):
                b = combine(btns1[i],btns2[j])
                if all([val <= jolt for jolt, val in zip(list(joltages), list(b))]):
                    btns3.add(b)
        return list(btns3)
    
    total = 0
    for i, (joltages, buttons) in enumerate(zip(allJoltages, allButtons)):
        print(i)
        j = joltages
        b = buttons
        tb = True
        for k in range(1, 15):
            #print(j, b)
            if j in b:
                total += k
                tb = False
                break
            #print("hi", buttons, b, j, "bye")
            b = combinePresses(buttons, b, j)
        if tb: print(f"Machine {i} left")
    print(total)

partA()
partB()
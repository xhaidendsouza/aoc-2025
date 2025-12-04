test_input="""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
input = test_input
input = input.strip().split("\n")
input = [list(line) for line in input]

def partA():
    count = 0
    for h in range(len(input)):
        line = input[h]
        for i in range(len(line)):
            char = line[i]
            if char == "@":
                cnt = 0
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if((h+j)>=0 and (h+j)<len(input) and (i+k) >= 0 and (i+k) < len(line)):
                            cnt += int(input[h+j][i+k] == "@")
                        else:
                            pass
                if cnt<5:
                    count+=1
    print(count)
                        


def partB():
    count = 0
    while True:
        removableList = []
        for h in range(len(input)):
            line = input[h]
            for i in range(len(line)):
                char = line[i]
                if char == "@":
                    cnt = 0
                    for j in range(-1, 2):
                        for k in range(-1, 2):
                            if((h+j)>=0 and (h+j)<len(input) and (i+k) >= 0 and (i+k) < len(line)):
                                cnt += int(input[h+j][i+k] == "@")

                            else:
                                pass
                    if cnt<5:
                        removableList.append([h, i])
        if len(removableList) == 0:
            break
        for item in removableList:
            input[item[0]][item[1]] = "."
            count += 1

    print(count)

partA()
partB()
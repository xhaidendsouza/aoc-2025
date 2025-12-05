test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
input = test_input
input = input.strip().split("\n\n")
ranges = [[int(i) for i in i.split("-")] for i in input[0].strip().split("\n")]
nums = [int(i) for i in input[1].strip().split("\n")]

def partA():
    count=0
    for num in nums:
        for range in ranges:
            if num >= range[0] and num <= range[1]:
                count+=1
                break
    print(count)
                    

def partB():
    while True:
        newRanges = []
        rangesToRemove = []
        for i,rng in enumerate(ranges):
            if len(newRanges) != 0:
                break
            for j,rng2 in enumerate(ranges):
                if rng2[0] <= rng[1]+1 and rng2[0] >= rng[0] and rng2[1] >= rng[1] and i != j:
                    newRanges.append([rng[0],rng2[1]])
                    rangesToRemove.append(rng)
                    rangesToRemove.append(rng2)
                if len(newRanges) != 0:
                    break
                if rng[0] <= rng2[1]+1 and rng[0] >= rng2[0] and rng[1] >= rng2[1] and i != j:
                    newRanges.append([rng2[0],rng[1]])
                    rangesToRemove.append(rng)
                    rangesToRemove.append(rng2)
                if len(newRanges) != 0:
                    break
                if rng[0] >= rng2[0] and rng[1] <= rng2[1] and i != j:
                    newRanges.append(rng2)
                    rangesToRemove.append(rng)
                    rangesToRemove.append(rng2)
                if len(newRanges) != 0:
                    break
                if rng2[0] >= rng[0] and rng2[1] <= rng[1] and i != j:
                    newRanges.append(rng)
                    rangesToRemove.append(rng2)
                    rangesToRemove.append(rng)
                if len(newRanges) != 0:
                    break
        if rangesToRemove == []:
            break
        for element in rangesToRemove:
            try:
                ranges.remove(element) 
            except:
                print("Fail to remove: ", element)
        for element in newRanges:
            try:
                ranges.append(element)
            except:
                print("Fail to append: ", element)
    print(sum([rng[1] - rng[0] for rng in ranges]) + len(ranges))


partA()
partB()
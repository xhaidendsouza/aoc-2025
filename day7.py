test_input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

input = test_input
input = input.strip().split("\n")
def partA():
    beams = set([input[0].find('S')])
    count = 0
    for line in input:
        newBeams = set()
        for beam in beams:
            if line[beam] == "^":
                count+=1
                newBeams.add(beam-1)
                newBeams.add(beam+1)
            else:
                newBeams.add(beam)
        beams = newBeams
    print(count)

def partB():
    beams = {input[0].find('S'): 1}
    for i, line in enumerate(input):
        newBeams = {}
        for beam,cnt in beams.items():
            if line[beam] == "^":
                if beam-1 in newBeams:
                    newBeams[beam-1] += cnt 
                else:
                    newBeams[beam-1] = cnt
                if beam+1 in newBeams:
                    newBeams[beam+1] += cnt 
                else:
                    newBeams[beam+1] = cnt
            else:
                if beam in newBeams:
                    newBeams[beam] += cnt
                else:
                    newBeams[beam] = cnt
        beams = newBeams
    print(sum(beams.values()))
partB()
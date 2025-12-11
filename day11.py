test_input = """
svr: aaa bbb
aaa: you hhh fft
fft: ccc
you: bbb ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
input = test_input
input = input.strip().split('\n')
devices = {}
for line in input:
    devices[line.strip().split(':')[0]] = line.strip().split(':')[1].strip().split()

def partA():
    def findPaths(d):
        if 'out' in devices[d]: return 1
        else: return sum([findPaths(device) for device in devices[d]])
    print(findPaths('you'))

def partB():
    definedPaths = {}
    def findPaths(d, endpoint):
        try:
            return definedPaths[d+endpoint]
        except:
            if endpoint in devices[d]: return 1
            elif 'out' in devices[d]: return 0
            else:
                a = sum([findPaths(device, endpoint) for device in devices[d]])
                definedPaths[d+endpoint] = a
                return a
    #dac2fft = findPaths('dac', 'fft') is always 0, so svr2dac, dac2out is uneeded
    print(findPaths('svr', 'fft')*findPaths('fft', 'dac')*findPaths('dac', 'out'))
partA()
partB()
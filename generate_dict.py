SOWPODS = {2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
TWL = {2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}

sowpods = 'sowpods.txt'
twl = 'twl18.txt'


with open(sowpods, 'r') as f:
    line = f.readline()
    while line:
        line = line[0:-1]
        if 1 < len(line) < 10:
            SOWPODS[len(line)].add(line)
        line = f.readline()


with open(twl, 'r') as f:
    line = f.readline()
    while line:
        line = line[0:-1]
        if 1 < len(line) < 10:
            TWL[len(line)].add(line)
        line = f.readline()

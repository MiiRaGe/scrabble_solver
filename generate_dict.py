ALL_WORDS = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

dictionnary = 'sowpods.txt'
dictionnary2 = 'twl18.txt'
with open(dictionnary2, 'r') as f:
    line = f.readline()
    while line:
        line = line[0:-1]
        if len(line) > 1 and len(line) < 10:
            ALL_WORDS[len(line)].append(line)
        line = f.readline()

SEVEN_SET = {x for x in ALL_WORDS[7]}
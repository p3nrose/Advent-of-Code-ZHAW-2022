

# lowercase characters a to z have priority 1 to 26
# uppercase characters A to Z have priority 27 to 52

prioritySum = 0

f = open('input/3.in')
lines = f.readlines()

for line in lines:
    line = line.strip()
    tempSum = 0
    firstHalf = line[:int(len(line) / 2)]
    secondHalf = line[-(int(len(line) / 2)):]

    #print(firstHalf)
    #print(secondHalf)
    foundChar = ''
    for char in firstHalf:
        if secondHalf.find(char) != -1:
            foundChar = char
        else:
            print('nothing found')

    #print(foundChar)
    if len(foundChar) > 0:
        if foundChar.islower():
            prioritySum += ord(foundChar) - 96
        else:
            prioritySum += ord(foundChar) - 64 + 26

print(prioritySum)

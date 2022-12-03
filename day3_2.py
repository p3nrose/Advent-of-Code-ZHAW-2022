# lowercase characters a to z have priority 1 to 26
# uppercase characters A to Z have priority 27 to 52

prioritySum = 0

f = open('input/3.in')
lines = f.readlines()

# group of 3 lines find the character in common
for i in range(0, len(lines), 3):
    print('i: ' + str(i))
    firstElf = lines[i].strip()
    secondElf = lines[i+1].strip()
    thirdElf = lines[i+2].strip()
    foundChar = ''
    for char in firstElf:
        if secondElf.find(char) != -1 and thirdElf.find(char) != -1:
            foundChar = char

    if len(foundChar) > 0:
        if foundChar.islower():
            prioritySum += ord(foundChar) - 96
        else:
            prioritySum += ord(foundChar) - 64 + 26

print(prioritySum)


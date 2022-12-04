# In how many assignment pairs does one range fully contain the other?

# example input:
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8

sum_fully_contained = 0

f = open('input/4.in')
lines = f.readlines()

for line in lines:
    line = line.strip()
    line = line.split(',')
    firstElfStart = int(line[0].split('-')[0])
    firstElfEnd = int(line[0].split('-')[1])
    secondElfStart = int(line[1].split('-')[0])
    secondElfEnd = int(line[1].split('-')[1])
    firstElf = list(range(firstElfStart, firstElfEnd + 1))
    secondElf = list(range(secondElfStart, secondElfEnd + 1))

    #first task isFullyContained = bool(set(firstElf).issubset(secondElf) or set(secondElf).issubset(firstElf))
    isFullyContained = bool(set(firstElf) & set(secondElf))

    if isFullyContained:
        sum_fully_contained += 1

print(sum_fully_contained)



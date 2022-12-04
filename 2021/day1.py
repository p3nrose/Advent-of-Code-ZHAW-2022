

f = open('input/day1.txt', 'r')

lines = f.readlines()

sum_increase = 0

for line in lines:
    lines[lines.index(line)] = line.strip()

#sliding window of 3 lines
sumArray = []
for i in range(0, len(lines)-2):
    sum = 0
    arr = lines[i:i+3]
    for j in arr:
        sum += int(j)
    sumArray.append(sum)

for k in range(0, len(sumArray)):
    if sumArray[k] != sumArray[0]:
        if sumArray[k] > sumArray[k-1]:
            sum_increase += 1

print(sum_increase)

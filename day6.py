f = open('input/day6.txt')

line = f.readline()

# check if character is in buffer of 4
for i in range(0, len(line)):
    buffer = line[i:i + 14]
    #print(buffer)
    if len(buffer) >= 14:
        #check if a character is only once in buffer of 14
        noDups = set(buffer)
        if len(buffer) == len(noDups):
            print(i+14)
            break


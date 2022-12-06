f = open('input/day6-test.txt')

line = f.readline()

# check if character is in buffer of 4
for i in range(0, len(line)):
    buffer = line[i:i + 4]
    #print(buffer)
    if len(buffer) >= 4:
        #check if a character is only once in buffer of 14
        if(buffer[0] != buffer[1] and buffer[0] != buffer[2] and buffer[0] != buffer[3] and buffer[1] != buffer[2] and buffer[1] != buffer[3] and buffer[2] != buffer[3]):
            print(i + 4)
            break


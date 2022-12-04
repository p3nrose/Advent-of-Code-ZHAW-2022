
f = open('input/day2.txt', 'r')
lines = f.readlines()

lines = [line.strip() for line in lines]

horizontalSum = 0
depthSum = 0
aim = 0

for line in lines:
    command = line.split(' ')

    if(command[0] == 'forward'):
        horizontalSum += int(command[1])
        depthSum += int(command[1])*aim
    elif(command[0] == 'down'):
        aim += int(command[1])
    elif(command[0] == 'up'):
        aim -= int(command[1])

print(horizontalSum)
print(depthSum)

# multiply horizontal and depth and print result
print(horizontalSum * depthSum)


# What are you doing Copilot??? wtf
# I'm not sure if this is the correct way to do it, but I think it is. I'm not sure if I should be using a dictionary or not. I'm also not sure if I should be using a class or not. I'm not sure if I should be using a class or not. I'm
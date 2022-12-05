# f = open('input/day5-eggnog-test.txt')
# copilot is funny :D , i think he likes eggnog

# Test input containers:
containersTest = [['Z', 'N'],
                  ['M', 'C', 'D'],
                  ['P']]

containers = [['W', 'M', 'L', 'F'],
             ['B', 'Z', 'V', 'M', 'F'],
             ['H', 'V', 'R', 'S', 'L', 'Q'],
             ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
             ['L', 'S', 'W'],
             ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
             ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
             ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
             ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']]

f = open('input/day5-steps.txt')
steps = f.readlines()

for step in steps:
    step = step.strip()
    step = step.split(' ')

    amount = int(step[1])
    fromContainer = int(step[3]) - 1
    toContainer = int(step[5]) - 1

    cargoCrane = containers[fromContainer][amount*-1:].copy()
    for i in range(amount):
        containers[fromContainer].pop()
    containers[toContainer].extend(cargoCrane)

    # Task 1
    # for i in range(amount):
    #     cargoCrane = containers[fromContainer].pop()
    #     containers[toContainer].extend(cargoCrane)

for container in containers:
    print(container[-1])

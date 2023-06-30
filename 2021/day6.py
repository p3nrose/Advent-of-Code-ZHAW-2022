# Read the initial population of lanternfish from the input
with open('input/day6.txt') as f:
  population = [int(x) for x in f.read().split(',')]

# Simulate the growth of the lanternfish population for 17 days
for day in range(17):
  # Decrease the timer for each lanternfish by 1
  for i in range(len(population)):
    population[i] -= 1
  # Check for lanternfish that have reached 0 and create new ones
  for i in range(len(population)):
    if population[i] == 0:
      population[i] = 6
      population.append(8)

# Print the size of the population after 17 days
print(len(population))
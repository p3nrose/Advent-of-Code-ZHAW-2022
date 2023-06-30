# Read the diagnostic report from input
report = []
while True:
  try:
    line = input()
    if line:
      report.append(line)
    else:
      break
  except EOFError:
    break

# Compute the gamma rate
gamma = ""
for i in range(len(report[0])):
  # Count the number of 0s and 1s in the ith position of all numbers
  zeros = ones = 0
  for number in report:
    if number[i] == '0':
      zeros += 1
    else:
      ones += 1

  # The gamma rate is the most common bit in the ith position of all numbers
  if zeros > ones:
    gamma += '0'
  else:
    gamma += '1'

# Compute the epsilon rate
epsilon = ""
for i in range(len(report[0])):
  # Count the number of 0s and 1s in the ith position of all numbers
  zeros = ones = 0
  for number in report:
    if number[i] == '0':
      zeros += 1
    else:
      ones += 1

  # The epsilon rate is the least common bit in the ith position of all numbers
  if zeros < ones:
    epsilon += '0'
  else:
    epsilon += '1'

# Print the power consumption, which is the product of the gamma and epsilon rates
print(int(gamma, 2) * int(epsilon, 2))

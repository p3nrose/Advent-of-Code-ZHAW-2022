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


# Function to compute the rating of a particular type (oxygen generator or CO2 scrubber)
def compute_rating(type):
    # Start with the full list of binary numbers
    numbers = report

    # Iterate over the bits of the numbers
    for i in range(len(numbers[0])):
        # Count the number of 0s and 1s in the ith position of all numbers
        zeros = ones = 0
        for number in numbers:
            if number[i] == '0':
                zeros += 1
            else:
                ones += 1

        # Determine the criteria for keeping a number, depending on the type of rating
        if type == "oxygen":
            if zeros >= ones:
                criteria = '0'
            else:
                criteria = '1'
        elif type == "CO2":
            if zeros <= ones:
                criteria = '0'
            else:
                criteria = '1'

        # Keep only numbers that match the criteria
        numbers = [number for number in numbers if number[i] == criteria]

    # Return the remaining number (which is the rating value)
    return numbers[0]


# Compute the oxygen generator and CO2 scrubber ratings
oxygen_rating = compute_rating("oxygen")

CO2_rating = compute_rating("CO2")

# Print the life support rating, which is the product of the oxygen generator and CO2 scrubber ratings
print(int(oxygen_rating, 2) * int(CO2_rating, 2))

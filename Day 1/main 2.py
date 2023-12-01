# This was during development, this approach doesn't work because of certain edge cases.

numbers = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
dataset = open("Day 1\\Data.txt", "r").readlines()

sum = 0
for line in dataset:
    cleanLine = line

    # Find alphabetical numbers and replace them by numeric digits
    i=0
    while(i < len(cleanLine)):
        for word, num in numbers.items():
            test = cleanLine[i:i+len(word)]
            if(cleanLine[i:i+len(word)] == word):
                cleanLine = cleanLine.replace(test, num)
        i+=1
    

    first = -1
    second = -1

    # Find and assign the digits to appropriate variables
    for char in cleanLine:
        if (char.isdigit()):
            if(first == -1): first = char
            else: second = char

    if(second == -1):
        second = first

    # Assemble the number and add it to the sum
    sum += (int(f"{first}{second}"))

# The answer (but wrong)
print(sum)
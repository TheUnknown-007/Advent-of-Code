numbers = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
dataset = open("Day 1\\Data.txt", "r").readlines()

sum = 0
for line in dataset:
    first = -1
    second = -1


    # Find the first digit, going left to right, comparing each character and substring
    i=0
    while(i < len(line)):
        if(line[i].isdigit()): 
            first = line[i]
            break

        # Susbtring of n character is matched to the alphabetical number with n characters
        breaker = False
        for word, num in numbers.items():
            test = line[i:i+len(word)]
            if(test == word):
                first = numbers[test]
                breaker = True
                break

        if breaker: break
        i+=1


    # Same thing, Find the last digit, going right to left
    i = len(line) - 1
    while(i >= 0):
        if(line[i].isdigit()): 
            second = line[i]
            break

        # Susbtring of n character is matched to the alphabetical number with n characters
        breaker = False
        for word, num in numbers.items():
            test = line[i-len(word):i]
            if(test == word):
                second = numbers[test]
                breaker = True
                break

        if breaker: break
        i-=1

    
    # Assemble the number from digits and add it to the sum
    sum += (int(f"{first}{second}"))

# The answer
print(sum)
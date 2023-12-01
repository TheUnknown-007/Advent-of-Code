# For testing purposes, generates dataset according to specified instructions
# Then compares the actual answer by the answer from the algorithm

import random
numbers = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
numbersList = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
charList = "abcdefghijklmnopqrstuvwxyz"


# ----- Generate Data

dataset = {}
n = 0

while n < 1000:

    string = ""
    length = random.randrange(5,12)
    i = 0
    num1 = -1
    num2 = -1
    while i < length:
        choice = random.randrange(0,3)

        if(choice == 0): 
            x = str(random.randrange(1,9))
            string += x
            num2 = x
            if(num1 == -1): num1 = x

        if(choice == 1): 
            x = random.choice(numbersList)
            string += x
            num2 = numbers[x]
            if(num1 == -1): num1 = numbers[x]
        
        if(choice == 2): string += random.choice(charList)
        
        i+=1
    
    dataset[string] = [num1, num2]
    n+=1



# ----- Test Algorithm

for k in dataset:
    cleanLine = k

    i=0
    while(i < len(cleanLine)):
        for word, num in numbers.items():
            test = cleanLine[i:i+len(word)]
            if(cleanLine[i:i+len(word)] == word):
                cleanLine = cleanLine.replace(test, num)
        i+=1

    first = -1
    second = -1

    for char in cleanLine:
        if (char.isdigit()):
            if(first == -1): first = char
            else: second = char

    if(second == -1):
        second = first
    
    v = dataset[k]
    if(v != [first, second ]):
        print("Error detected")

Map = open("Day 3\\Data2.txt", "r").read()
cleanMap = Map.replace("\n", "")
charPerLine = 140
specialChars = "`~!@#$%^&*()_+=-,/';[]\\|}{\":}?<>"
numbers = []

print(len(Map))

import regex
import random

allowedChar = "1234567890."
pattern = f"[^{regex.escape(allowedChar)}]"

newLine = "\n"

# Find number indexes
for n,line in enumerate(Map.split("\n")):
    num = ""
    index = -1
    for k, char in enumerate(line):
        # if num == "852":
        #     print("w")
        if char.isdigit():
            num += char
            if index == -1: 
                index = n*(charPerLine+1) + k
        else:
            if num != "":
                numbers.append((num, index))
            num = ""
            index = -1
       
    if num != "": numbers.append((num, index))

sum = 0

file = open("Day 3\\Positives.txt", "w")
file2 = open("Day 3\\Negatives.txt", "w")

# Go through each number, evaluate condition, and add it to sum
for (key,value) in numbers:
    surrounding = ""
    surrounding2 = ""

    if ((value - charPerLine - 2) >= 0) and (value - charPerLine + len(key)) >= 0:
        surrounding += Map[value - charPerLine - 2: value - charPerLine + len(key)]
        surrounding2 = surrounding.replace("\n", ".") + "\n"
    else:
        surrounding2 = len(key)*'.' + "..\n"

    if((value - 1) >= 0):        
        surrounding += Map[value - 1]
        surrounding2 += Map[value - 1].replace("\n", ".")
    else:
        surrounding2 += '.'

    surrounding2 += key

    if((value + len(key)) <= len(Map)): 
        surrounding += Map[value + len(key)]
        surrounding2 += Map[value + len(key)].replace("\n", ".") + "\n"
    else:
        surrounding2 = ".\n"

    if ((value + (charPerLine)) <= len(Map)) and (value + (charPerLine) + 2 + len(key)) <= len(Map): 
        surrounding += Map[value + (charPerLine): value + (charPerLine) + 2 + len(key)]
        surrounding2 += Map[value + (charPerLine): value + (charPerLine) + 2 + len(key)].replace("\n", ".")
    else:
        surrounding2 += len(key)*'.' + "..\n"
    


    

    #print( Map[0:13 ].replace(newLine, ""))
        
    #print(f'{key}\t: {value} => {surrounding.replace(newLine, "")}')
    #print(surrounding2+"\n")

    # match = regex.search(pattern, surrounding)

    if(any([c in surrounding for c in specialChars])):
    # if(bool(match)):
        sum += int(key)
    #     file.write(regex.sub("\d+", "", surrounding2.replace("\n", "").replace(".", "")) + "\n")
    # else: 
    #     file2.write(surrounding2.replace(".", "").replace("\n", "") + "\n")

    # test = random.randint(0,2)
    # if(test == 1):
    #     if(any([c in surrounding for c in specialChars])):
    #         file2.write(surrounding2.replace(".", "").replace("\n", "") + "\n")
    #     else:
    #         file.write(regex.sub("\d+", "", surrounding2.replace("\n", "").replace(".", "")) + "\n")

print(sum)

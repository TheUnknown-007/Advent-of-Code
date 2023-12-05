import regex

# There shouldn't be any other characters, right?
specialChars = "`~!@#$%^&*()_+=-,/';[]\\|}{\":}?<>"

# Alternate approach using regex search, for matching any characters other than ones specified here
allowedChar = "1234567890."
pattern = f"[^{regex.escape(allowedChar)}]"

Map = open("Day 3\\Exhaustive3.txt", "r").read()
charPerLine = 5

numbers = []
gearSum = 0
sum = 0

# Step 1: Find each number with its index (character offset)
for n,line in enumerate(Map.split("\n")):
    num = ""
    index = -1
    for k, char in enumerate(line):
        
        if char.isdigit(): # Add to the sequence if its a number
            num += char
            if index == -1:
                index = n*(charPerLine+1) + k

        else:
            if num != "": # The number sequence has finished, save the number and its offset
                numbers.append((num, index, len(num)))
            
            # Reset the state
            num = ""
            index = -1

    # Literally second last fix. Could have never guessed this would be an issue
    # Fortunately, I checked the edge case where the number was on the edge. No pun intended lol
    # Any numbers on the far right end, was skipped because the per line loop would finish before saving the number
    if num != "": numbers.append((num, index, len(num)))

#print(Map[90:100])

#for n,line in enumerate(Map.split("\n")):
for k, char in enumerate(Map):
    if char == "*":
        num1 = ""
        num2 = ""
        for (num,start,length) in numbers:


            # Top Left
            if (k - charPerLine - 2) >= start and (k - charPerLine - 2) <= start+(length-1):
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num: 
                    num2 = num
            
            # Top Mid
            if (k - charPerLine - 1) >= start and (k - charPerLine - 1) <= start+(length-1):
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num: 
                    num2 = num
                
            # Top Right
            if (k - charPerLine)     >= start and (k - charPerLine)     <= start+(length-1):
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num: 
                    num2 = num

            # Bottom Left
            if (k + charPerLine) >= start and (k + charPerLine) <= start+(length-1):
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num: 
                    num2 = num

            # Bottom Mid
            if (k + charPerLine + 1)     >= start and (k + charPerLine + 1)     <= start+(length-1):
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num: 
                    num2 = num

            # Bottom Right
            if (k + charPerLine + 2)     >= start and (k + charPerLine + 2)     <= start+(length-1):
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num: 
                    num2 = num
            
            # Back
            if k == start+length:
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num:
                    num2 = num

            # Front
            if k + 1 == start:
                if num1 == "": 
                    num1 = num
                elif num2 == "" and num1 != num:
                    num2 = num
            
            # Multiple number and add to sum
            if(num1 != "" and num2 != ""):
                gearSum += int(num1) * int(num2)
                print("========\n" + Map[k - 7 : k - 4] + "\n" + Map[k - 1] + "*" + Map[k + 1] + "\n" + Map[k + 5 : k + 8] + "\n\n")
                break

                
print(gearSum)

        
        

    

# Go through each number, evaluate condition, and add it to sum
for (num,start,length) in numbers:
    surrounding = ""

    # Took me a bit of experimenting to dial in the values, because they're bit counter intuitive

    # Line above the number
    if ((start - charPerLine - 2) >= 0) and (start - charPerLine + length) >= 0:
        surrounding += Map[start - charPerLine - 2: start - charPerLine + length]

    # Character before the number
    if((start - 1) >= 0):        
        surrounding += Map[start - 1]

    # Character after the number
    if((start + length) <= len(Map)): 
        surrounding += Map[start + length]

    # Line below the number
    if ((start + (charPerLine)) <= len(Map)) and (start + (charPerLine) + 2 + length) <= len(Map): 
        surrounding += Map[start + (charPerLine): start + (charPerLine) + 2 + length]
    

    # Alternate approach where regex finds characters that are not digits or dots. It yields incorrect results.
    # match = regex.search(pattern, surrounding)
    # if bool(match):
    #     sum += int(key)

    # Last fix I made, and switched back to the approach below
    # Check if any character from special character is in the surrounding string
    if(any([c in surrounding for c in specialChars])):
        sum += int(num)

# Final Answer  
print(sum)
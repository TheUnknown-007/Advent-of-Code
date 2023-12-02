sum = 0
power = 0

maxR = 12
maxG = 13
maxB = 14

with open("Day 2\\Data.txt", "r") as file:
    
    k = 1
    for line in file.readlines():
        tokens = line.replace(":", " :").replace(",", " ,").replace(";", " ;").replace("\n", "").split(" ")
        #tokens = line.replace(":", " :").replace(",", " ,").replace(";", " ;").split(" ")

        currentR = 0
        currentG = 0
        currentB = 0

        i = 0
        while i < len(tokens):
            if(i == 0):
                i+=3; continue
            
            test = tokens[i]
            test2 = tokens[i+1]
            if(tokens[i].isdigit()):
                match tokens[i+1]:
                    case 'red':   
                        if(int(tokens[i]) > currentR): currentR = int(tokens[i])
                    case 'green': 
                        if(int(tokens[i]) > currentG): currentG = int(tokens[i])
                    case 'blue':  
                        if(int(tokens[i]) > currentB): currentB = int(tokens[i])
                i+=3; continue

            i+=1

        if(currentR <= maxR and currentG <= maxG and currentB <= maxB): 
            sum += k

        power += currentR * currentG * currentB
        k+=1

print("Part 1: " + str(sum))
print("Part 2: " + str(power))
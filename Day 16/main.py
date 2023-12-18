# Single threaded, sequential approach towards splitters.
# Recursive and Multithreading approaches were unviable.

Map = open("Day 16\\Data.txt", "r").readlines()
Map = [x.replace("\n", "") for x in Map]
EnergyMap = Map[:] # Shallow copy so it doesnt impact the original Map
rowCount = 110
columnCount = 110

initial_direction = 1        # 1: right   -1: left   -2: up   2: down
initial_position = [0, 0]    # X Y coordinates

CallsList = [] # The calls to the methods are saved and then invoked sequentially

# Replace a specific character by index in a string.
def Change_Character(string, index, character):
    if 0 <= index < len(string):
        return string[:index] + character + string[index + 1:]
    else: raise(Exception("Index out of range."))

# The main method which traces the path of beam of light
def Calculate_Light(position, direction):
    global CallsList
    global EnergyCount

    while (True):
        
        # Stop if we've reached the end of the map
        if((position[0] >= rowCount or position[0] < 0) or (position[1] >= columnCount or position[1] < 0)):
            break

        match (Map[position[0]][position[1]]):

            # Reflector. Reflect depending on the incoming direction
            case "\\":
                if(direction > 0):  direction =  2 if direction ==  1 else  1
                else:               direction = -2 if direction == -1 else -1

            # Reflector. Reflect depending on the incoming direction
            case "/":
                if(direction > 0):  direction = -2 if direction ==  1 else -1
                else:               direction =  2 if direction == -1 else  1

            # Vertical Splitter
            case "|":
                # Split only if hit on flat side
                if direction != 2 and direction != -2:
                    # Stop if splitter is already encountered. Avoid loops
                    if EnergyMap[position[0]][position[1]] == "#":
                        break
                    # If the splitter isn't on the edge, save the parameters for the method call
                    if(position[0] > 0 and position[0] < rowCount):
                        CallsList.append([[position[0]-1, position[1]], -2])
                    # Change the direction. The current call only follows forward directions (Down and Right)
                    direction = 2

            # Horizontal Splitter
            case "-":
                # Split only if hit on flat side
                if direction != 1 and direction != -1:
                    # Stop if splitter is already encountered. Avoid loops
                    if EnergyMap[position[0]][position[1]] == "#":
                        break
                    # If the splitter isn't on the edge, save the parameters for the method call
                    if(position[1] > 0 and position[1] < columnCount):
                        CallsList.append([[position[0], position[1]-1], -1])
                    # Change the direction. The current call only follows forward directions (Down and Right)
                    direction = 1

            # Encountered the end. Stop
            case "\n":
                break

        EnergyMap[position[0]] = Change_Character(EnergyMap[position[0]], position[1], "#")

        # # Realtime showcase of light travelling the map. Used debugging purposes
        # os.system("cls")
        # print(*EnergyMap, sep="\n")
        # time.sleep(0.01)
        
        if(direction > 0): position[1 if direction == 1  else 0] += 1
        else:              position[1 if direction == -1 else 0] -= 1

BestConfiguration = [[], 0] # Position and 


################################################################################################################
################################################################################################################
########################## Find the best Configuration #########################################################
################################################################################################################
################################################################################################################

print("Checking top and bottom edges")

# Go through top and bottom edges and find best configuration
initial_direction = 2
k = 0
while k <= 110:
    n = 0
    while n < columnCount:
        initial_position = [k, n]
        EnergyMap = Map[:]
        CallsList = []

        # Initial Call to the method
        Calculate_Light(initial_position, initial_direction)

        # Go through all calls, invoke, and then remove from list.
        while len(CallsList) != 0:
            # The calls dynamically increase as splitters are encountered. Eventually all splitters will be explored.
            Calculate_Light(CallsList[0][0], CallsList[0][1])
            CallsList.pop(0)

        energizedTileCount = 0
        for row in EnergyMap:
            for char in row:
                if char == "#": energizedTileCount += 1
        if energizedTileCount > BestConfiguration[1]: BestConfiguration = [[k,n], energizedTileCount]
        print(f"\nFinished [{k},{n}] edge")
        print(BestConfiguration)

        n+=1
    k += 110
    initial_direction = -2

print("Checking left and right edges")

# Go through left and right edges and find best configuration
initial_direction = 1
k = 0
while k <= 110:
    n = 0
    while n < columnCount:
        initial_position = [n, k]
        EnergyMap = Map[:]
        CallsList = []

        # Initial Call to the method
        Calculate_Light(initial_position, initial_direction)

        # Go through all calls, invoke, and then remove from list.
        while len(CallsList) != 0:
            # The calls dynamically increase as splitters are encountered. Eventually all splitters will be explored.
            Calculate_Light(CallsList[0][0], CallsList[0][1])
            CallsList.pop(0)
        
        energizedTileCount = 0
        for row in EnergyMap:
            for char in row:
                if char == "#": energizedTileCount += 1
        if energizedTileCount > BestConfiguration[1]: BestConfiguration = [[k,n], energizedTileCount]
        print(f"\nFinished [{n},{k}] edge")
        print(BestConfiguration)

        n+=1
    k += 110
    initial_direction = -1


print(BestConfiguration)
# Recursive approach towards splitters.
# Requires high recursion depth. Limit is reached even when set to high

import sys
sys.setrecursionlimit(1000000) # May need to be increased

Map = open("Day 16\\Data.txt", "r").readlines()
Map = [x.replace("\n", "") for x in Map]
EnergyMap = Map[:] # Shallow copy so it doesnt impact the original Map
columnCount = 110
rowCount = 110

initial_direction = 1        # 1: right   -1: left   -2: up   2: down
initial_position = [0, 0]    # X Y coordinates


# Replace a specific character by index in a string.
def Change_Character(string, index, character):
    if 0 <= index < len(string):
        return string[:index] + character + string[index + 1:]
    else: raise(Exception("Index out of range."))

# The main method which traces the path of beam of light
def Calculate_Light(position, direction):

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
                        Calculate_Light([position[0]-1, position[1]], -2)
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
                        Calculate_Light([position[0], position[1]-1], -1)
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
        

Calculate_Light(initial_position, initial_direction)

print(*EnergyMap, sep="\n")
energizedTileCount = 0
for row in EnergyMap:
    for char in row:
        if char == "#": energizedTileCount += 1
print(energizedTileCount)
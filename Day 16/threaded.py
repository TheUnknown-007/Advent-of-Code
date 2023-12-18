# Multi Threaded approach towards splitters. Individual threads trace individual paths
# The edits to energy map aren't synced properly. Doesn't yield correct results.

import threading

Map = open("Day 16\\Test.txt", "r").readlines()
Map = [x.replace("\n", "") for x in Map]
EnergyMap = Map[:]
columnCount = 10
rowCount = 10

initial_direction = 1        # 1: right   -1: left   -2: up   2: down
initial_position = [0, 0]
beamCount = 1

lock = threading.Lock()
ThreadList = []
EnergyMapPerThread = []

def Change_Character(string, index, character):
    if 0 <= index < len(string):
        return string[:index] + character + string[index + 1:]
    else: raise(Exception("Index out of range."))

def Calculate_Light(position, direction):
    global Map
    global EnergyMapPerThread
    global ThreadList

    localEnergyMap = Map[:]

    while (True):
        if((position[0] >= columnCount or position[0] < 0) or (position[1] >= rowCount or position[1] < 0)):
            with lock: EnergyMapPerThread.append(localEnergyMap)
            break

        newRow = Change_Character(localEnergyMap[position[0]], position[1], "#")
        localEnergyMap[position[0]] = newRow

        match (Map[position[0]][position[1]]):
                    
            case "\\":
                if(direction > 0):  direction =  2 if direction ==  1 else  1
                else:               direction = -2 if direction == -1 else -1

            case "/":
                if(direction > 0):  direction = -2 if direction ==  1 else -1
                else:               direction =  2 if direction == -1 else  1

            case "|":
                if(position[0] > 0 and position[0] < rowCount):
                    thread = threading.Thread(target=Calculate_Light, args = ([position[0]-1, position[1]], -2))
                    print("Thread")
                    thread.start()
                    thread.join()
                    ThreadList.append(thread)
                direction = 2

            case "-":
                if(position[1] > 0 and position[1] < columnCount):
                    thread = threading.Thread(target=Calculate_Light, args = ([position[0], position[1]-1], -1))
                    print("Thread")
                    thread.start()
                    thread.join()
                    ThreadList.append(thread)
                direction = 1

            case "\n":
                with lock: EnergyMapPerThread.append(localEnergyMap)
                break


        if(direction > 0): position[1 if direction == 1  else 0] += 1
        else:              position[1 if direction == -1 else 0] -= 1
        

Calculate_Light(initial_position, initial_direction)
# start = time.time()
# for thread in ThreadList:
#     thread.join()

# print(*EnergyMap, sep="\n")
# print(time.time() - start)

for y,row in enumerate(EnergyMap):
    newRow = ""
    for x,char in enumerate(row):
        found = False
        if char == "#":
            newRow += "#"
            continue
        else:
            for threadMap in EnergyMapPerThread:
                if(threadMap[y][x] == "#"):
                    newRow += "#"
                    found = True
                    break

        if not found: newRow += '.'
    EnergyMap[y] = newRow

print(*EnergyMap, sep="\n")
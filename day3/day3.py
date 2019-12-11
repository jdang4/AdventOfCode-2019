import sys

masterMap = {}
originX = 0
originY = 0

# helper function to help me determine if there is an intersection with my map
def containsKey(key, val) :
    global masterMap
    if key in masterMap :
        if val in masterMap[key] :
            return True 
        else :
            return False 
    else :
        return False

# finding the distance of the intersection from starting point
def getDistanceFromOrigin(originX, originY, currX, currY) :
    return abs(originX - currX) + abs(originY - currY)


# returns the number of steps it took wire 1 to get to
def getSteps(posX, posY) :
    global masterMap

    return masterMap[posX][posY]

# inputs is a single wire
def move(wire, line, minDistance, minSteps) :
    global masterMap, originX, originY

    currX = originX 
    currY = originY
    counter = 0
    
    for mov in wire :
        direction = mov[:1]
        steps = int(mov[1:])
        dirX = 0
        dirY = 0

        if direction == 'R' :
            dirX = 1
            dirY = 0
        elif direction == 'L' :
            dirX = -1
            dirY = 0
        elif direction == 'U' :
            dirX = 0
            dirY = 1
        elif direction == 'D' :
            dirX = 0
            dirY = -1

        else :
            raise Exception('\nERROR!\n')

        for _ in range(steps) :
            currX += dirX 
            currY += dirY 
            counter += 1
            if line == 2 and containsKey(currX, currY) is True :
  
                dist = getDistanceFromOrigin(originX, originY, currX, currY)
                minDistance = min(minDistance, dist)
                calSteps = counter + getSteps(currX, currY)
                minSteps = min(minSteps, calSteps)

            if line == 1:
                # using nested map
                if currX in masterMap :
                    masterMap[currX][currY] = counter

                else :
                    masterMap[currX] = {}
                    masterMap[currX][currY] = counter 

    return minDistance, minSteps
                    

def Parts_One_and_Two(inputs) :
    global masterMap
    wire1 = inputs[0].split(',')
    wire2 = inputs[1].split(',')
    minDistance = sys.maxsize
    minSteps = sys.maxsize

    minDistance, minSteps = move(wire1, 1, minDistance, minSteps)
    minDistance, minSteps = move(wire2, 2, minDistance, minSteps)

    print('\nMinimum Distance From Origin: ', minDistance)
    print('Minimum Number of Steps to Intersection: ', minSteps, '\n')

if __name__ == '__main__' :
    with open('input.txt') as file :
        inputs = file.read().splitlines()

    Parts_One_and_Two(inputs)
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

# inputs is a single wire
def move(wire, line, minDistance) :
    global masterMap, originX, originY

    currX = originX 
    currY = originY

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

            if line == 2 and containsKey(currX, currY) is True :
  
                dist = getDistanceFromOrigin(originX, originY, currX, currY)

                if dist < minDistance :
                    minDistance = dist

            if line == 1:
                # using nested map
                if currX in masterMap :
                    masterMap[currX][currY] = currX

                else :
                    masterMap[currX] = {}
                    masterMap[currX][currY] = currX

    return minDistance

def partOne(inputs) :
    global masterMap
    wire1 = inputs[0].split(',')
    wire2 = inputs[1].split(',')
    minDistance = sys.maxsize

    minDistance = move(wire1, 1, minDistance)
    minDistance = move(wire2, 2, minDistance)

    print('\nMinimum Distance From Origin: ', minDistance, '\n')

if __name__ == '__main__' :
    with open('input.txt') as file :
        inputs = file.read().splitlines()

    partOne(inputs)
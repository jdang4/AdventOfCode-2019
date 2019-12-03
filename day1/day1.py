#!/usr/bin/python3.6

def findFuel(val) :
    fuel = 0

    while True :
        val = int(val / 3) - 2
        if val > 0 :
            fuel += val
        else :
            break

    return fuel 

file = open("input.txt", "r")

totalSum = 0
totalFuelSum = 0

for line in file :
    val = int(line)
    result = int(val / 3) - 2
    fuelRes = findFuel(val)
    totalSum += result 
    totalFuelSum += fuelRes 

print(totalSum)
print(totalFuelSum)



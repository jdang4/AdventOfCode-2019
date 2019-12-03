file = open('input.txt', 'r+')

text = file.read()

myList = text.split(',')

myList = [int(i) for i in myList] 

myList[1] = 12
myList[2] = 2

start = 0
end = 4
while myList[start] != 99 and end < len(myList):
    tmp = myList[start: end]
    
    if tmp[0] == 1 :
        result = myList[tmp[1]] + myList[tmp[2]]
        myList[tmp[3]] = result
        start += 4
        end += 4

    elif tmp[0] == 2 :
        result = myList[tmp[1]] * myList[tmp[2]]
        myList[tmp[3]] = result
        start += 4
        end += 4

print(myList[0])
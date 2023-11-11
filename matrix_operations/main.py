#Initial data input
file = open('input.txt', "r")
input = file.readlines()
file.close()

#data formatting
A = []
B = []
ops = []
for x in range(len(input)):
    input[x] = input[x].replace("\n","")
x = 0
while x < len(input):
    if input[x] == "":
        input.remove(input[x])
    else:
        x+=1
x = 0
while x < len(input): #main array creation very vert ugly, im sorry. 
    if "operations" in input[x]: #Removing the operations so they don't cause problems as they include both A and B
        y = x+1
        while y < len(input):
            tempCont = input[y].replace("A","").replace("B","")
            for z in tempCont:
                ops.append(z)
            input.remove(input[y])
    if "A" in input[x]: #Sorting out A matrix, this could be made into a function, but the tester threw errors on the first task, so I will refrain.
        y = x+1
        while "B" not in input[y]:
            tempCont = input[y].split(" ")
            tempArr = []
            for u in tempCont:
                tempArr.append(int(u))
            A.append(tempArr)
            y+=1
    if "B" in input[x]: #Sorting out B matrix
        y = 0
        y = x+1
        while "operations" not in input[y]:
            tempCont = input[y].split(" ")
            tempArr = []
            for u in tempCont:
                tempArr.append(int(u))
            B.append(tempArr)
            y+=1
    x+=1
x = 0
while x < len(ops): #makink the ops array as small as possible
    if ops[x] == " ":
        ops.remove(ops[x])
    else:
        x+=1


#logic for matrix addition and multiplication
addedMatrix = [[A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
multipliedMatrix = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

#printing logic
for x in ops:
    if x == "+":
        print("A + B")
        for y in addedMatrix:
            print(*y)
        print("")
    if x == "*":
        print("A * B")
        for y in multipliedMatrix:
            print(*y)
        print("")

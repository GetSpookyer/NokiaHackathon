f = open("input.txt", "r")
read = f.readlines()
f.close()
#1st we need to break the main array into the three mazes so we are more free.
mazeA = []
mazeB = []
mazeC = []
for x in range(len(read)):
    if read[x] == "A\n":
        y = x+1
        while read[y] != "\n" and y < len(read):
            mazeA.append(list(read[y].replace(" ","")))
            y += 1
    if read[x] == "B\n":
        y = x+1
        while read[y] != "\n" and y < len(read):
            mazeB.append(list(read[y].replace(" ","")))
            y += 1
    if read[x] == "C\n":
        y = x+1
        while y < len(read) and read[y] != "\n":
            mazeC.append(list(read[y].replace(" ","")))
            y += 1
#we are going to use a very simple algorithm. If it can, it will go down and go trough the directions counter clockwise.
#to handle back and forward loops, if we need to go back, we will replace the '.' with an '&' which for the code works the exact same, it's for us to understand what it does.
def solveMaze(m): #this is the maze array. it is single letter as it is used very often and I'm lazy...
    l = [] #location is given as Y and X as this is the order in arrays. quite annoying to be frank... its's single letter, as it will be used a lot and I'm very lazy...
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == 'S':
                l = [y,x]
    foundGoal = False
    path = [" "] 
    didStep = False
    while foundGoal == False:
        didStep = False
        
        #This is the goal finding logic. If it sees the goal, it steps there instantly, does the last append to the path and breaks the cycle.
        if m[l[0]+1][l[1]] == "G":
            l = [l[0]+1,l[1]]
            path.append("D")
            foundGoal = True
            break
        elif m[l[0]][l[1]+1] == "G":
            l = [l[0],l[1]+1]
            path.append("R")
            foundGoal = True
            break
        elif m[l[0]-1][l[1]] == "G":
            l = [l[0]-1,l[1]]
            path.append("U")
            foundGoal = True
            break
        elif m[l[0]][l[1]-1] == "G":
            l = [l[0],l[1]-1]
            path.append("L")
            foundGoal = True
            break
        
        
        #This is the steping logic. This will let it aimlessly go in the maze.
        if m[l[0]+1][l[1]] == "." and path[-1] != "U":
            l = [l[0]+1,l[1]]
            path.append("D")
            didStep = True
        elif m[l[0]][l[1]+1] == "." and path[-1] != "L":
            l = [l[0],l[1]+1]
            path.append("R")
            didStep = True
        elif m[l[0]-1][l[1]] == "." and path[-1] != "D":
            l = [l[0]-1,l[1]]
            path.append("U")
            didStep = True
        elif m[l[0]][l[1]-1] == "." and path[-1] != "R":
            l = [l[0],l[1]-1]
            path.append("L")
            didStep = True
            
            
            
        if didStep == False:    #this part will only come up if it got stuck as it could not move only backwars which was blocked so it does not enter a loop.
                                #whit this, it will be unable to move into the place it got stuck in as it will not see it as a free splace.
            if m[l[0]+1][l[1]] == ".":
                l = [l[0]+1,l[1]]
                m[l[0]-1][l[1]] = "&"
                path.append("D")
            if m[l[0]][l[1]+1] == ".":
                l = [l[0],l[1]+1]
                m[l[0]][l[1]-1] = "&"
                path.append("R")
            if m[l[0]-1][l[1]] == ".":
                l = [l[0]-1,l[1]]
                m[l[0]+1][l[1]] = "&"
                path.append("U")
            if m[l[0]][l[1]-1] == ".":
                l = [l[0],l[1]-1]
                m[l[0]][l[1]+1] = "&"
                path.append("L")
        
        if len(path) > 50:
            return "error, too many steps, likely in a loop as code is bad."
    
    path = " ".join(path)
    path = path.strip(" ")
    return path

#printing the way we found
pathA = solveMaze(mazeA)
print("A")
print(pathA)
pathB = solveMaze(mazeB)
print(" ")
print("B")
print(pathB)
pathC = solveMaze(mazeC)
print(" ")
print("C")
print(pathC)

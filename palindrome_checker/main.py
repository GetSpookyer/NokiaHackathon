
#Initial data input
file = open('input.txt', "r")
stringArray = file.readlines()
file.close()

#making the data more usabale for me.
whatToDisappear = [" ",".",",","?","!","(",")",'"',"'","\n"]
for x in range(len(stringArray)):
    for y in range(len(whatToDisappear)):
        stringArray[x] = stringArray[x].replace(whatToDisappear[y],"")
    stringArray[x] = list(stringArray[x].lower())

    

#creating the output array and checking for palindromes
printoutData = []
for x in range(len(stringArray)):
    length = len(stringArray[x])
    if length%2 == 0:
        steps = int((length/2))
    else:
        steps = int((length/2)+0.5)
    charsInString = []
    isPalindrome = True
    for y in range(steps):
        if stringArray[x][y] == stringArray[x][-(y+1)]:
            if stringArray[x][y] not in charsInString:
                charsInString.append(stringArray[x][y])
        else:
            isPalindrome = False
            break
    if isPalindrome == True:
        printable = ("YES, "+str(len(charsInString)))
    else:
        printable = ("NO, -1")
    printoutData.append(printable)
        

#printing the output array
for x in printoutData:
    print(x)

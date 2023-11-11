#checking for palindromes  
def palCheck(stringArray):
    length = len(stringArray)
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
        return("Yes, "+str(len(charsInString)))
    else:
        return("No, -1")

#Initial data input
file = open('input.txt', "r")
stringsFromFile = file.readlines()
file.close()

#making the data more usabale for me.
whatToDisappear = [" ",".",",","?","!","(",")",'"',"'","\n"]
for x in range(len(stringsFromFile)):
    for y in range(len(whatToDisappear)):
        stringsFromFile[x] = stringsFromFile[x].replace(whatToDisappear[y],"")
    stringsFromFile[x] = list(stringsFromFile[x].lower())

#creating the output array
printoutData = []
for x in range(len(stringsFromFile)):
    printoutData.append(palCheck(stringsFromFile))
        

#printing the output array
for x in printoutData:
    print(x)

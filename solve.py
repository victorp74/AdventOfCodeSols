
def changeLetter(first, second):
    #print(second)
    if(second == 'X'):
        if(first =='A'):
            return 'Z'
        elif(first =='B'):
            return 'X'
        elif(first =='C'):
            return 'Y'
    if(second == 'Y'):
        if(first =='A'):
            return 'X'
        elif(first =='B'):
            return 'Y'
        elif(first =='C'):
            return 'Z'
    if(second == 'Z'):
        if(first =='A'):
            return 'Y'
        elif(first =='B'):
            return 'Z'
        elif(first =='C'):
            return 'X'
    
    

with open("input.txt","r") as outfile:
    data = outfile.readlines()

#print(data)
arrayStatements = []
for i in data:
    arrayStatements.append(i)

##calculate score for part 1
sumScore =0
for i in arrayStatements:
    if(i[2]=='X'):
        sumScore+=1
    if(i[2]=='Y'):
        sumScore+=2
    if(i[2]=='Z'):
        sumScore+=3
    if ((i[0] == 'A' and i[2]== 'X') or (i[0] == 'B' and i[2]== 'Y') or (i[0] == 'C' and i[2]== 'Z')):
        sumScore+=3
    if((i[0]=='A' and i[2]=='Y') or (i[0]=='B' and i[2]=='Z') or (i[0]=='C' and i[2]=='X')):
        sumScore+=6
print(sumScore)

##calculate score for part 2
sumScore =0
for i in arrayStatements:
    i = i[:2] + str(changeLetter(i[0],i[2])) #just changing the second letter to correct letter for tie/wim/lose so i don't have to rewrite code
    if(i[2]=='X'):
        sumScore+=1
    if(i[2]=='Y'):
        sumScore+=2
    if(i[2]=='Z'):
        sumScore+=3
    if ((i[0] == 'A' and i[2]== 'X') or (i[0] == 'B' and i[2]== 'Y') or (i[0] == 'C' and i[2]== 'Z')):
        sumScore+=3
    if((i[0]=='A' and i[2]=='Y') or (i[0]=='B' and i[2]=='Z') or (i[0]=='C' and i[2]=='X')):
        sumScore+=6
print(sumScore)
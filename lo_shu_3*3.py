
def isMagicSquare(magic):
    sumrow = []
    sumcol = []
    sumdig = []

    for i in range(1,4):
        sum = 0
        for j in range(1,4):
            sum += magic[i-1][j-1]
        sumrow.append(sum)



    for i in range(1,4):
        sum = 0
        for j in range(1,4):
            sum += magic[j-1][i-1]
        sumcol.append(sum)

    i = 0
    j= 0
    sum = 0
    while(i<3):
        sum += magic[i][j]
        i+=1
        j+=1
    sumdig.append(sum)

    i=0
    j=2
    sum = 0
    while(j>=0):
        sum += magic[i][j]
        i+=1
        j-=1
    sumdig.append(sum)
    print(sumrow,sumcol,sumdig)
    if(sumrow[0] == sumrow[1] and sumrow[2] == sumrow[1] and sumrow[0] == sumrow[2] and sumrow[2] == sumcol[0] and sumcol[0] == sumcol[1] and sumcol[1] == sumcol[2] and sumcol[2] == sumdig[0] and sumdig[0] == sumdig[1]):
        return True
    else:
        return False




magic = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
print("Enter values of magic square")
for i in range(1,4):
    for j in range(1,4):
        magic[i-1][j-1] = int(input(f"Enter row {i} column {j} : "))

answer = isMagicSquare(magic)
print(answer)

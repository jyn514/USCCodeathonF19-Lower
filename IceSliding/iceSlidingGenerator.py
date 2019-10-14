import random

random.seed(20)
gridMax = 18
gridDimX = random.randint(8, gridMax)
gridDimY = random.randint(8, gridMax)
energy = random.randint(4, 30)

# print("X: ", x)
# print("Y: ", y)

startX = random.randint(1, gridDimX - 1)
startY = random.randint(1, gridDimY - 1)

curPosX = startX
curPosY = startY


print("startX: ", startX)
print("startY: ", startY)

print("gridDimX: ", gridDimX)
print("gridDimY: ", gridDimY)


board = [[0 for x in range(gridDimX)] for y in range(gridDimY)]
board[curPosY][curPosX] = 2
directionList = []
lastDirection = 0

def printBoard():
  for i in range(gridDimY):
    for j in range(gridDimX):
      print(board[i][j], end = '')
    print()
  print()

def potentiallyPlaceLetter():
  decider = random.randint(0,11)
  if decider > 9 :
    letter = str(chr(random.randint(110,122)))
    board[curPosY][curPosX] = letter
  elif decider == 9:
    letter = str(chr(random.randint(97,109)))
    board[curPosY][curPosX] = letter

    #print(letter)

for j in range(20):
  newDirection = random.randint(1,4)
  tilesToMove = random.randint(4,7)

  board[curPosY][curPosX] = 0

  while newDirection == lastDirection or newDirection % 2 == lastDirection % 2:
    newDirection = random.randint(1,4)
  
  if curPosX == 0:
    if(lastDirection != 1 and lastDirection != 3):
      newDirection = random.randint(1,2)
      if(newDirection == 2):
        newDirection = 3
    else:
      newDirection = 2

  if curPosY == 0:
    if(lastDirection != 2 and lastDirection != 4):
      newDirection = random.randint(2,3)
      if(newDirection == 3):
        newDirection = 4
    else:
      newDirection = 3

  if curPosX == gridDimX -1:
    if(lastDirection != 1 and lastDirection != 3):
      newDirection = random.randint(1,2)
      if(newDirection == 2):
        newDirection = 3
    else:
      newDirection = 4

  if curPosY == gridDimY - 1:
    if(lastDirection != 2 and lastDirection != 4):
      newDirection = random.randint(2,3)
      if(newDirection == 3):
        newDirection = 4
    else:
      newDirection = 1


  if newDirection == 1:
    directionList.append("up")
    for i in range(tilesToMove):
      if curPosY - 1 >= 0 and board[curPosY -1][curPosX] != 1:
        if i == tilesToMove - 1:
          if curPosY - 1 == startY and curPosX == startX:
            tilesToMove = tilesToMove + 1
          else:
            board[curPosY - 1][curPosX] = 1
        else:
          potentiallyPlaceLetter()
          curPosY -= 1
  elif newDirection == 2:
    directionList.append("right")
    for i in range(tilesToMove):
      if curPosX + 1 < gridDimX and board[curPosY][curPosX +1] != 1:
        if i == tilesToMove - 1:
          if curPosY == startY and curPosX + 1== startX:
            tilesToMove = tilesToMove + 1
          else:
            board[curPosY][curPosX + 1] = 1
        else:
          potentiallyPlaceLetter()
          curPosX += 1
  elif newDirection == 3:
    directionList.append("down")
    for i in range(tilesToMove):
      if curPosY + 1 < gridDimY and board[curPosY +1][curPosX] != 1:
        if i == tilesToMove - 1:
          if curPosY + 1 == startY and curPosX == startX:
            tilesToMove = tilesToMove + 1
          else:
            board[curPosY + 1][curPosX] = 1
        else:
          potentiallyPlaceLetter()
          curPosY += 1
  elif newDirection == 4:
    directionList.append("left")
    for i in range(tilesToMove):
      if curPosX - 1 >= 0 and board[curPosY][curPosX -1] != 1:
        if i == tilesToMove - 1:
          if curPosY == startY and curPosX - 1 == startX:
            tilesToMove = tilesToMove + 1
          else:
            board[curPosY][curPosX - 1] = 1
        else:
          potentiallyPlaceLetter()
          curPosX -= 1



  lastDirection = newDirection
  board[curPosY][curPosX] = 2
  print(directionList[-1])
  printBoard()

board[curPosY][curPosX] = 0
board[startY][startX] = 2

#print(gridDimX, end = '')
print(gridDimX,gridDimY,energy)
for i in range(gridDimY):
    for j in range(gridDimX):
      print(board[i][j], end = '')
    print()
for i in range(len(directionList)):
  print(directionList[i])

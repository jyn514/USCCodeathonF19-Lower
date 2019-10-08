import sys
import random
counter = 0

#corners to center
#for z in range(0, numOfGrids):

#print()

# print()

def xPattern(gridDim):
  #X
  for y in range(0, gridDim):
    for x in range(0, gridDim):
      if x == y or y == gridDim - x - 1:
        print(1, end = '')
      else:
        print(0, end = '')
      #counter += 1
    print()

# print()
def border(gridDim):
  #border
  for i in range(0, gridDim):
    for j in range(0, gridDim):
      if(i == 0 or i == gridDim - 1 or j == 0 or j == gridDim - 1):
        print(1, end = '')
      else:
        print(0, end = '')
    print()

# print()

def plus(gridDim):
  #plus
  for i in range(0, gridDim):
    for j in range(0, gridDim):
      if(i == gridDim // 2 or j == gridDim // 2):
        print(1, end = '')
      else:
        print(0, end = '')
    print()

# print()

def checkerboard(gridDim):
  #checkerboard
  for i in range(0, gridDim):
    for j in range(0, gridDim):
      if(j % 2 == 0 and i % 2 == 0):
        print(1, end = '')
      elif (j % 2 != 0 and i % 2 != 0):
        print(1, end = '')
      else:
        print(0, end = '')
    print()

def corner(gridDim):
  for y in range(0, gridDim):
    for x in range(0, gridDim):
      if (counter == x or x == gridDim- 1) and \
      (counter == y or y == gridDim - 1):
        print(1, end = '')
      else:
        print(0, end = '')
    print()

# print()
def fullBoard(gridDim):
  #all
  for i in range(0, gridDim):
    for j in range(0, gridDim):
      print(1, end = '')
    print()

#row = 0
#numOfGrids = 5
gridDim = 11
fileName = ""
for i in range(50):
  if(i < 10):
    fileName="input/input0"
  else:
    fileName="input/input"
  sys.stdout = open(fileName + str(i) + ".txt","w")
  randNum = random.randint(1,6)
  gridDim = random.randint(3,100)
  while gridDim % 2 == 0:
    gridDim = random.randint(3,100)
  print(gridDim)
  if randNum == 1:
    xPattern(gridDim)
  elif randNum == 2:
    border(gridDim)
  elif randNum == 3:
    plus(gridDim)
  elif randNum == 4:
    checkerboard(gridDim)
  elif randNum == 5:
    corner(gridDim)
  elif randNum == 6:
    fullBoard(gridDim)


#xPattern(gridDim)
#border(gridDim)
# plus(gridDim)
#checkerboard(gridDim)
#corner(gridDim)
fullBoard(gridDim)


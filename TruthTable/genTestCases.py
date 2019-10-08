import sys
import random
outFileName = ""
for i in range(2, 50):
  # if(i < 10):
  #   inFileName="input/input0"
  # else:
  #   inFileName="input/input"
  # sys.stdout = open(inFileName + str(i) + ".txt","w")

  # numVars = random.randint(1, 30)
  # rowNum = random.randint(0, (2**numVars) - 1)

  # print(numVars)
  # print(rowNum)


  if(i < 10):
    inFileName="input/input0"
  else:
    inFileName="input/input"
  sys.stdin = open(inFileName + str(i) + ".txt","r")

  if i < 10:
     outFileName = "output/output0"
  else:
    outFileName = "output/output"
  sys.stdout = open(outFileName + str(i) + ".txt","w")
  numVars = sys.stdin.readline()
  numVars = int(numVars)
  rowNum = sys.stdin.readline()
  rowNum = int(rowNum)
  binaryVersion = bin(rowNum)[2:]
  #binaryVersion = '0' * (numVars - length) + binaryVersion
  #print(binaryVersion)
  #print(type(binaryVersion))
  #str(binaryVersion)
  binaryVersion = binaryVersion.replace('0', 'F ')
  binaryVersion = binaryVersion.replace("1", "T ")
  print(binaryVersion)

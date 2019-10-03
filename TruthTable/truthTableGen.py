numVars = 3
numPossibleTruthValues = 2
counter = 0
binaryVersion = 0
currentRowValue = ""
length = 0
numRows = numPossibleTruthValues**numVars
for i in range(65, 65 + numVars):
  print(chr(i), '', end = '')
print()
for i in range(0, numRows):
  binaryVersion = bin(i)[2:]
  #binaryVersion = [binaryVersion:2]
  #print(binaryVersion)
  length = len(binaryVersion)
  binaryVersion = '0' * (numVars - length) + binaryVersion
  #print(binaryVersion)
  #print(type(binaryVersion))
  #str(binaryVersion)
  binaryVersion = binaryVersion.replace('0', 'F ')
  binaryVersion = binaryVersion.replace("1", "T ")
  print(binaryVersion)
  # for i in binaryVersion:
  #   #print(i)

  #   if i == '0':
  #     currentRowValue += '0'
  #   elif i == '1':
  #     currentRowValue += '1'  
  #print()
# def convertBase(numPossibleTruthValues, numVariables):
#   for i in range(0, numPossibleTruthValues**numVariables):
#     if numToConvert - i >= 0:

numVars = input()
rowNum = input()
rowNum = int(rowNum)

binaryVersion = bin(rowNum)[2:]
binaryVersion = binaryVersion.replace('0', 'F ')
binaryVersion = binaryVersion.replace("1", "T ")
print(binaryVersion)
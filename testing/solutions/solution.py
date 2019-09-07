import math
x = input().split(" ")
n = int(x[0])
goal = int(x[1])

scores = []
weights = []

scores = [int(x) for x in input().split(" ")]
weights = [float(x) for x in input().split(" ")]

totalpoints = 0
for i in range(n):
    totalpoints += scores[i] * weights[i]

print(math.ceil((goal - totalpoints)/(1-sum(weights))))

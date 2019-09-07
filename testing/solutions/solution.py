import math
n = int(input())
goal = int(input())

scores = []
weights = []

for _ in range(n):
    scores.append(int(input()))
for _ in range(n):
    weights.append(float(input()))


totalpoints = 0
for i in range(n):
    totalpoints += scores[i] * weights[i]

print(math.floor((goal - totalpoints)/(1-sum(weights))))

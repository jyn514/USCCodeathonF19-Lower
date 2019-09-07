# Guaranteed positive solutions
import random
weights = [1]
while sum(weights) > 0.95:
  n = random.randint(15,15)
  goal = random.randint(80,100)
  finalweight = random.random()
  # We want the sums to have a normal distribution around (1-finalweight)/2
  # Cause why not, it will give us some realistic numbers like 108 and 20
  # Like in real classes ^
  weights = [random.random()*(1-finalweight)/n for _ in range(n)]
  scores = [random.randint(60,100) for _ in range(n)]
print(str(n) + " " + str(goal))
print(" ".join(str(score) for score in scores))
print(" ".join(str(weight) for weight in weights))

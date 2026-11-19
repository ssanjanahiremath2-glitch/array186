
scores = []

n = int(input("Enter number of scores: "))

for i in range(n):
    score = int(input("Enter score: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)

maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)

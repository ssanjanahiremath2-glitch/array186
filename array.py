
scores = []

n = int(input("Enter number of scores: "))

for i in range(n):
    score = int(input("Enter score: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum =", total)
print("Average =", average)


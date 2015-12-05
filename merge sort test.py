import math

allnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6.5]
print allnumbers

halfwayPoint = int(math.floor( len(allnumbers)/2 ))
print halfwayPoint

subset = []
for a in range(len(allnumbers)):
    subset.append([])

for y in range(len(allnumbers)):
    for x in range(halfwayPoint):
        if (len(subset[y]) >= halfwayPoint):
            break
        else:
            subset[y].append(allnumbers[x])
            allnumbers.delete[x]

print subset[0]

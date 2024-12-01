with open("d01.input") as file:
    input = file.read().splitlines()

list_one = []
list_two = []

for line in input:
    list_one.append(int(line.split()[0]))
    list_two.append(int(line.split()[1]))

list_one.sort()
list_two.sort()

# part 1
distances = []
for x in range(len(list_one)):
    distances.append(abs(list_one[x] - list_two[x]))
print(sum(distances))  # a: 1590491

# part 2
similarity_score = 0
for x in range(len(list_one)):
    similarity_score += list_one[x] * list_two.count(list_one[x])
print(similarity_score)  # a: 22588371

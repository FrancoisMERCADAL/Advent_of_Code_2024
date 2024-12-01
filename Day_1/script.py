FILE_NAME = "location_ids.txt"

# PART 1
def sum_distances(file):
    left_part = []
    right_part = []
    sum_ = 0
    for line in file:
        line = line.strip().split("   ")
        left_part.append(int(line[0]))
        right_part.append(int(line[1]))
    left_part.sort()
    right_part.sort()
    for nb_left, nb_right in zip(left_part,right_part):
        sum_ += abs(nb_left-nb_right)
    return sum_

def historian_hysteria_part1():
    file = open(FILE_NAME, "r")
    distances = sum_distances(file)
    file.close()
    return distances

# PART 2
def similarity_score(file):
    left_part = []
    right_part = []
    similarity = 0
    for line in file:
            line = line.strip().split("   ")
            left_part.append(int(line[0]))
            right_part.append(int(line[1]))
    for nb in left_part:
        if nb in right_part:
            similarity += nb * right_part.count(nb)
    return similarity

def historian_hysteria_part2():
    file = open(FILE_NAME, "r")
    similarity = similarity_score(file)
    file.close()
    return similarity

### TEST AREA
# Part 1
print(historian_hysteria_part1())
# Output: 1110981

# Part 2
print(historian_hysteria_part2())
# Output: 24869388

FILE_NAME = "input.txt"

# PART 1
def is_result_possible_p1(nb_list, index, previous_nb, results):
    if index == len(nb_list):
        return results
    else:
        key1 = previous_nb * nb_list[index]
        key2 = previous_nb + nb_list[index]

        results = results + [key1] + [key2]

        res1 = is_result_possible_p1(nb_list, index+1, key1, results)
        res2 = is_result_possible_p1(nb_list, index+1, key2, results)

        return res1 + res2

def get_sum_p1(file):
    sum = 0
    for line in file:
        line = line.strip().split(':')
        line[1] = line[1].replace(' ',',')[1:].split(',')
        nb = int(line[0])
        nb_list = [int(x) for x in line[1]]
        if nb in is_result_possible_p1(nb_list, 1, nb_list[0], [nb_list[0]]):
            sum += nb
    return sum

def bridge_repair_part1():
    file = open(FILE_NAME, "r")
    sum = get_sum_p1(file)
    file.close()
    return sum

# PART 2
def is_result_possible_p2(nb_list, index, previous_nb, results):
    if index == len(nb_list):
        return results
    else:
        key1 = previous_nb * nb_list[index]
        key2 = previous_nb + nb_list[index]
        key3 = int(str(previous_nb) + str(nb_list[index]))

        results = results + [key1] + [key2] + [key3]

        res1 = is_result_possible_p2(nb_list, index+1, key1, results)
        res2 = is_result_possible_p2(nb_list, index+1, key2, results)
        res3 = is_result_possible_p2(nb_list, index+1, key3, results)

        return res1 + res2 + res3

def get_sum_p2(file):
    sum = 0
    for line in file:
        line = line.strip().split(':')
        line[1] = line[1].replace(' ',',')[1:].split(',')
        nb = int(line[0])
        nb_list = [int(x) for x in line[1]]
        if nb in is_result_possible_p2(nb_list, 1, nb_list[0], [nb_list[0]]):
            sum += nb
    return sum

def bridge_repair_part2():
    file = open(FILE_NAME, "r")
    sum = get_sum_p1(file)
    file.close()
    return sum

### TEST AREA
# PART 1
# print(bridge_repair_part1())
# Output: 28730327770375

# PART 2
# print(bridge_repair_part2())
# Output: 424977609625985

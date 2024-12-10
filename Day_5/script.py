FILE_NAME = "pages.txt"

# PART 1
def get_ordered_lines(file):
    rules_key = {}
    middle = False
    sum_mid = 0
    for line in file:
        if line == "\n":
            middle = True
        else:
            line = line.strip()
            if middle == False:
                line = line.split("|")
                if line[0] in rules_key.keys():
                    rules_key[line[0]].append(line[1])
                else:
                    rules_key[line[0]] = [line[1]]
            else:
                line = line.split(",")
                passed_nb = []
                is_wrong = False
                for nb in line:
                    if nb in rules_key.keys():
                        if any(value in passed_nb for value in rules_key[nb]):
                            is_wrong = True
                            break
                    passed_nb.append(nb)
                if is_wrong == False:
                    sum_mid += int(passed_nb[int(len(passed_nb)/2)])
    return sum_mid

def print_queue_part1():
    file = open(FILE_NAME, "r")
    sum_mid = get_ordered_lines(file)
    file.close()
    return sum_mid

# PART 2

### TEST AREA
# PART 1
print(print_queue_part1())
# Output: 3608

# PART 2
#print(print_queue_part2())
# Output: 

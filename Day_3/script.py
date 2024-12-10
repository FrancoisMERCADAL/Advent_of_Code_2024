import regex as re

FILE_NAME = "memory.txt"

# PART 1
def get_mul_sum_p1(file):
    mul_sum = 0
    for line in file:
        line = line.strip()
        mul_array = re.findall('mul\([0-9]+,[0-9]+\)', line)
        mul_array = [re.findall('[0-9]+,[0-9]+', x)[0] for x in mul_array]

        for mul in mul_array:
            mul = mul.split(",")
            mul = [int(x) for x in mul]
            mul_sum += mul[0]*mul[1]
    return mul_sum

def mull_it_over_part1():
    file = open(FILE_NAME, "r")
    mul_sum = get_mul_sum_p1(file)
    file.close()
    return mul_sum

# PART 2
def get_mul_sum_p2(file):
    mul_enabled = True
    mul_sum = 0
    for line in file:
        line = line.strip()
        mul_array = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
        for item in mul_array:
            if item == "do()":
                mul_enabled = True
            elif item == "don't()":
                mul_enabled = False
            else:
                if mul_enabled == True:
                    item = re.findall('[0-9]+,[0-9]+', item)[0].split(",")
                    item = [int(x) for x in item]
                    mul_sum += item[0]*item[1]
    return mul_sum

def mull_it_over_part2():
    file = open(FILE_NAME, "r")
    mul_sum = get_mul_sum_p2(file)
    file.close()
    return mul_sum

### TEST AREA
# PART 1
print(mull_it_over_part1())
# Output: 184576302

# PART 2
print(mull_it_over_part2())
# Output: 118173507

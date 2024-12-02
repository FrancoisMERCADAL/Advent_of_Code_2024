FILE_NAME = "reports.txt"

# PART 1
def find_safe_reports(file):
    safe_reports = 0
    for line in file:
        safe_reports += 1
        up = False
        down = False
        line = [int(x) for x in line.strip().split(" ")]
        if line[0] < line[1]:
            up = True
        else:
            down = True
        for i in range(len(line)-1):
            if abs(line[i]-line[i+1]) == 0 or abs(line[i]-line[i+1]) > 3 or (line[i] > line[i+1] and up == True) or (line[i] < line[i+1] and down == True):
                safe_reports -= 1
                break
    return safe_reports

def red_nosed_reports_part1():
    file = open(FILE_NAME, "r")
    safe_reports = find_safe_reports(file)
    file.close()
    return safe_reports

# Part 2
def find_safe_reports_2(file):
    
    safe_reports = 0
    for line in file:
        safe_reports += 1
        up = False
        down = False
        first_error = False
        line = [int(x) for x in line.strip().split(" ")]
        if line[0] < line[1]:
            up = True
        else:
            down = True

        index = 0
        while index < len(line)-1:
            if first_error == True:
                if line[0] < line[1]:
                    up = True
                    down = False
                else:
                    down = True
                    up = False
            if abs(line[index]-line[index+1]) < 1 or abs(line[index]-line[index+1]) > 3 or (line[index] > line[index+1] and up == True) or (line[index] < line[index+1] and down == True):
                if first_error == False:
                    if up == True and line[index+1] < line[index]:
                        line.pop(index+1)
                    else:
                        line.pop(index)
                    index = 0
                    first_error = True
                else:
                    safe_reports -= 1
                    break
            else:
                index += 1
    
    return safe_reports

def red_nosed_reports_part2():
    file = open(FILE_NAME, "r")
    safe_reports = find_safe_reports_2(file)
    file.close()
    return safe_reports

### TEST AREA
# Part 1
print(red_nosed_reports_part1())
# Output: 502

# Part 2
print(red_nosed_reports_part2())
# Output: 544

FILE_NAME = "words_input.txt"

# PART 1
WORD_TO_SEARCH = 'XMAS'
def horizontal_search(lines, line, col):
    nb = 0
    # Forward
    if col <= len(lines[line]) - len(WORD_TO_SEARCH):
        if lines[line][col] + lines[line][col+1] + lines[line][col+2] + lines[line][col+3] == WORD_TO_SEARCH:
            nb += 1
    # Backward
    if col >= len(WORD_TO_SEARCH) - 1:
        if lines[line][col] + lines[line][col-1] + lines[line][col-2] + lines[line][col-3] == WORD_TO_SEARCH:
            nb += 1
    return nb

def vertical_search(lines, line, col):
    nb = 0
    # Up
    if line >= len(WORD_TO_SEARCH) - 1:
        if lines[line][col] + lines[line-1][col] + lines[line-2][col] + lines[line-3][col] == WORD_TO_SEARCH:
            nb += 1
    # Down
    if line <= len(lines) - len(WORD_TO_SEARCH):
        if lines[line][col] + lines[line+1][col] + lines[line+2][col] + lines[line+3][col] == WORD_TO_SEARCH:
            nb += 1
    return nb

def diagonal_search(lines, line, col):
    nb = 0
    # Up, Forward
    if line >= len(WORD_TO_SEARCH) - 1 and col <= len(lines[line]) - len(WORD_TO_SEARCH):
        if lines[line][col] + lines[line-1][col+1] + lines[line-2][col+2] + lines[line-3][col+3] == WORD_TO_SEARCH:
            nb += 1
    # Up, Backward
    if line >= len(WORD_TO_SEARCH) - 1 and col >= len(WORD_TO_SEARCH) - 1:
        if lines[line][col] + lines[line-1][col-1] + lines[line-2][col-2] + lines[line-3][col-3] == WORD_TO_SEARCH:
            nb += 1
    # Down, Forward
    if line <= len(lines) - len(WORD_TO_SEARCH) and col <= len(lines[line]) - len(WORD_TO_SEARCH):
        if lines[line][col] + lines[line+1][col+1] + lines[line+2][col+2] + lines[line+3][col+3] == WORD_TO_SEARCH:
            nb += 1
    # Down, Backward
    if line <= len(lines) - len(WORD_TO_SEARCH) and col >= len(WORD_TO_SEARCH) - 1:
        if lines[line][col] + lines[line+1][col-1] + lines[line+2][col-2] + lines[line+3][col-3] == WORD_TO_SEARCH:
            nb += 1
    return nb

def find_patterns_p1(file):
    nb_words_found = 0
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    for line in range(len(lines)):
        for col in range(len(lines[line])):
            if lines[line][col] == WORD_TO_SEARCH[0]:
                nb_words_found += horizontal_search(lines, line, col)
                nb_words_found += vertical_search(lines, line, col)
                nb_words_found += diagonal_search(lines, line, col)
    return nb_words_found

def ceres_search_part1():
    file = open(FILE_NAME, "r")
    nb_words_found = find_patterns_p1(file)
    file.close()
    return nb_words_found

# PART 2
def find_patterns_p2(file):
    nb_words_found = 0
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    for line in range(len(lines)):
        for col in range(len(lines[line])):
            if lines[line][col] == "A" and col >= 1 and col <= len(lines[line]) - 2 and line >= 1 and line <= len(lines) - 2:
                list_char = [lines[line-1][col-1],lines[line-1][col+1],lines[line+1][col-1],lines[line+1][col+1]]
                if list_char.count("S") == 2 and list_char.count("M") == 2 and (lines[line-1][col-1] == lines[line-1][col+1] or lines[line-1][col-1] == lines[line+1][col-1]):
                    nb_words_found += 1
    return nb_words_found

def ceres_search_part2():
    file = open(FILE_NAME, "r")
    nb_words_found = find_patterns_p2(file)
    file.close()
    return nb_words_found

### TEST AREA
# PART 1
print(ceres_search_part1())
# Output: 2507

# PART 2
print(ceres_search_part2())
# Output: 1969

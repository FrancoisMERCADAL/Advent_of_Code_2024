FILE_NAME = "input.txt"

def open_file(file):
    t_map = []
    trailheads = []
    index = 0
    for line in file:
        line = list(int(x) for x in line.strip())
        if 0 in line:
            new_pos = [i for i, n in enumerate(line) if n == 0]
            for x in new_pos:
                trailheads.append([index,x])
        t_map.append(line)
        index += 1
    return t_map, trailheads

def get_locations(t_map, position):
    list_positions = []

    # NORTH
    if position[0] > 0:
        list_positions.append([position[0]-1, position[1]])
    # EAST
    if position[1] < len(t_map[0]) - 1:
        list_positions.append([position[0], position[1]+1])
    # SOUTH
    if position[0] < len(t_map[0]) - 1:
        list_positions.append([position[0]+1, position[1]])
    # WEST
    if position[1] > 0:
        list_positions.append([position[0], position[1]-1])
    return list_positions

# PART 1
def get_next_hike_locations_p1(t_map, position, next_locations, visited_9):
    to_return = []
    for next_location in next_locations:
        if t_map[position[0]][position[1]] + 1 == t_map[next_location[0]][next_location[1]] and [next_location[0], next_location[1]] not in visited_9:
            to_return.append(next_location)
        if t_map[next_location[0]][next_location[1]] == 9 and t_map[position[0]][position[1]] == 8:
            visited_9.append([next_location[0], next_location[1]])
    return to_return, visited_9

def define_trailhead_score_p1(t_map, position, score, visited_9):
    if t_map[position[0]][position[1]] == 9:
        score += 1
    else:
        next_locations = get_locations(t_map, position)
        next_locations, new_visited_9 = get_next_hike_locations_p1(t_map, position, next_locations, visited_9)

        for next_location in next_locations:
            score = define_trailhead_score_p1(t_map, next_location, score, new_visited_9)
    return score

def get_trailhead_score_sum_p1(file):
    t_map, trailheads = open_file(file)

    trailhead_score_sum = 0
    for trailhead in trailheads:
        trailhead_score_sum += define_trailhead_score_p1(t_map, trailhead, 0, [])

    return trailhead_score_sum

def hoof_it_part1():
    file = open(FILE_NAME, "r")
    trailhead_score_sum = get_trailhead_score_sum_p1(file)
    file.close()
    return trailhead_score_sum

# PART 2
def get_next_hike_locations_p2(t_map, position, next_locations):
    to_return = []
    for next_location in next_locations:
        if t_map[position[0]][position[1]] + 1 == t_map[next_location[0]][next_location[1]]:
            to_return.append(next_location)
    return to_return

def define_trailhead_score_p2(t_map, position, score):
    if t_map[position[0]][position[1]] == 9:
        score += 1
    else:
        next_locations = get_locations(t_map, position)
        next_locations = get_next_hike_locations_p2(t_map, position, next_locations)

        for next_location in next_locations:
            score = define_trailhead_score_p2(t_map, next_location, score)
    return score

def get_trailhead_score_sum_p2(file):
    t_map, trailheads = open_file(file)

    trailhead_score_sum = 0
    for trailhead in trailheads:
        trailhead_score_sum += define_trailhead_score_p2(t_map, trailhead, 0)

    return trailhead_score_sum

def hoof_it_part2():
    file = open(FILE_NAME, "r")
    trailhead_score_sum = get_trailhead_score_sum_p2(file)
    file.close()
    return trailhead_score_sum

### TEST AREA
# PART 1
# print(hoof_it_part1())
# Output: 548

# PART 2
# print(hoof_it_part2())
# Output: 1252

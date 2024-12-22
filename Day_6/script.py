FILE_NAME = "map.txt"

set_direction = {
    (-1,0):(0,1),
    (0,1):(1,0),
    (1,0):(0,-1),
    (0,-1):(-1,0)
}

def test_is_out(lines,position):
    if position[0] == 0 or position[0] == len(lines) - 1 or position[1] == 0 or position[1] == len(lines[0]) - 1:
        return True
    return False

# PART 1
def get_nb_visited_places(file):
    lines = []
    line_nb = 0
    direction = (-1,0)

    for line in file:
        line = line.strip()
        lines.append(list(line))
        if "^" in line:
            for i in range(len(line)):
                if line[i] == "^":
                    start_position = [line_nb,i]
        line_nb += 1
    
    lines[start_position[0]][start_position[1]] = "X"
    visited_places = 1
    is_out = False
    while is_out != True:
        if lines[start_position[0] + direction[0]][start_position[1] + direction[1]] != "#":
            start_position = [start_position[0] + direction[0],start_position[1] + direction[1]]
            if lines[start_position[0]][start_position[1]] in ("."):
                lines[start_position[0]][start_position[1]] = "X"
                visited_places += 1
            is_out = test_is_out(lines,start_position)
        else:
            direction = set_direction[direction]
    return visited_places

def guard_gallivant_part1():
    file = open(FILE_NAME, "r")
    visited_places = get_nb_visited_places(file)
    file.close()
    return visited_places

# PART 2
def test_is_loop(occured_locations_directions, position_direction):
    if occured_locations_directions.count(position_direction) > 1:
        return True
    return False

lines = []
line_nb = 0
direction = (-1,0)

file = open(FILE_NAME, "r")
for line in file:
    line = line.strip()
    lines.append(list(line))
    if "^" in line:
        for i in range(len(line)):
            if line[i] == "^":
                start_position = [line_nb,i]
    line_nb += 1
file.close()

nb_loops = 0
for line in range(len(lines)):
    for col in range(len(lines[line])):
        if lines[line][col] == ".":
            lines[line][col] = "#"
            occured_locations_directions = [(start_position,direction)]
            is_out = False
            is_loop = False
            while is_out != True or is_loop != True:
                if lines[start_position[0] + direction[0]][start_position[1] + direction[1]] != "#":
                    start_position = [start_position[0] + direction[0],start_position[1] + direction[1]]
                    is_out = test_is_out(lines,start_position)
                    print(start_position,direction,is_out,is_loop)

                    occured_locations_directions.append((start_position,direction))
                    is_loop = test_is_loop(occured_locations_directions,(start_position,direction))
                else:
                    direction = set_direction[direction]
                    occured_locations_directions.append((start_position,direction))
            if is_loop == True:
                nb_loops += 1
            lines[line][col] = "."
print(nb_loops)

### TEST AREA
# PART 1
#print(guard_gallivant_part1())
# Output: 4580

# PART 2
#print(guard_gallivant_part2())
# Output: 

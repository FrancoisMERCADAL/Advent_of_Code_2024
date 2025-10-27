FILE_NAME = "input.txt"

def convert_to_memory_view(line):
    to_return = []
    file_id = 0
    for i in range(len(line)):
        if i % 2 == 0:
            str_to_add = int(line[i]) * (str(file_id) + '-')
            str_to_add = str_to_add.split('-')[:-1]
            to_return += str_to_add
            file_id += 1
        else:
            to_return += list(int(line[i]) * ".")
    return to_return

def get_checksum(amphipod_memory):
    checksum = 0
    for i in range(len(amphipod_memory)):
        if amphipod_memory[i] != '.':
            checksum += i * int(amphipod_memory[i])
    return checksum

# PART 1
def amphipod_function(memory_view):
    index_end = len(memory_view) - 1
    index_start = 0
    while index_end >= 0:
        if list(set(memory_view[index_end:])) == ['.'] and '.' not in memory_view[0:index_end]:
            break
        if memory_view[index_start] != '.':
            index_start += 1
        elif memory_view[index_start] == '.':
            if memory_view[index_end] == '.':
                index_end -= 1
            elif memory_view[index_end] != '.':
                memory_view[index_start] = memory_view[index_end]
                memory_view[index_end] = '.'
    return memory_view

def amphipod_checksum(file):
    for line in file:
        line = line.strip()
        memory_view = convert_to_memory_view(line)
        amphipod_memory = amphipod_function(memory_view)
        checksum = get_checksum(amphipod_memory)
    return checksum

def disk_fragmenter_part1():
    file = open(FILE_NAME, "r")
    checksum = amphipod_checksum(file)
    file.close()
    return checksum

# PART 2
def map_disk(memory_view):
    mapping = {
        "files":[],
        "spaces":[]
    }
    i = 0
    while i < len(memory_view):
        if memory_view[i] == '.':
            size = 1
            index = i
            i += 1
            while i <= len(memory_view) - 1 and memory_view[i] == '.':
                size += 1
                i += 1
            mapping['spaces'].append([index, size])
        else:
            size = 1
            index = i
            file_id = memory_view[i]
            i += 1
            while i <= len(memory_view) - 1 and memory_view[i] == file_id:
                size += 1
                i += 1
            mapping['files'].append([index, size])
        #i += 1
    return mapping

def amphipod_function_v2(memory_view):
    disk_map = map_disk(memory_view)
    file_index_end = len(disk_map['files']) - 1
    while file_index_end > 0:
        file_size = disk_map['files'][file_index_end][1]
        for i in range(len(disk_map['spaces'])):
            if disk_map['spaces'][i][1] >= file_size and disk_map['spaces'][i][0] < disk_map['files'][file_index_end][0]:
                for j in range(file_size):
                    memory_view[disk_map['spaces'][i][0] + j] = str(file_index_end)
                    memory_view[disk_map['files'][file_index_end][0] + j] = '.'
                disk_map['spaces'] = map_disk(memory_view)['spaces']
                break
        file_index_end -= 1
    return memory_view

def amphipod_checksum_v2(file):
    for line in file:
        line = line.strip()
        memory_view = convert_to_memory_view(line)
        amphipod_memory = amphipod_function_v2(memory_view)
        checksum = get_checksum(amphipod_memory)
    return checksum

def disk_fragmenter_part2():
    file = open(FILE_NAME, "r")
    checksum = amphipod_checksum_v2(file)
    file.close()
    return checksum

### TEST AREA
# PART 1
# print(disk_fragmenter_part1())
# Output: 6225730762521

# PART 2
# print(disk_fragmenter_part2())
# Output: 6250605700557

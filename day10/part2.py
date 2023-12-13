from typing import List, Set
import copy, time

# other than the start, any pipe has only two valid neighbors. All others can be ignored
connections = {"-": [(0,1), (0,-1)], 
              "|": [(1,0), (-1,0)],
              "F": [(0,1), (1,0)],
              "7": [(0,-1), (1,0)],
              "L": [(0,1), (-1,0)],
              "J": [(0,-1), (-1,0)],
              }

# N, S, E, W
start_conn = [(-1,0), (1,0), (1,0), (-1,0)]
valid_pipes = [set(["|", "7", "F"]), set(["|", "J", "L"]), set(["-", "7", "J"]), set(["-", "L", "F"])]


def main():
    pipes = []
    start_idx = None
    path = []
    with open("input.txt") as f:
        for i, line in enumerate(f.readlines()):
            if "S" in line:
                start_idx = [i, line.index("S")]
            pipes.append(list(line.strip()))

    cur_idx = leave_start(pipes, start_conn, start_idx, valid_pipes)
    prev_index = start_idx
    path.append(cur_idx)
    while cur_idx != start_idx:
        new_idx = get_next_index(pipes, connections, cur_idx, prev_index)
        prev_index = cur_idx
        cur_idx = new_idx
        path.append(cur_idx)

    get_path_only(path, pipes)   
    print(len(path) / 2)

    # for part 2, expand the map by filling in blank rows and columns between every row and column
    # if connections exist across the rows and columns, those elements would be added to the path set
    # do a fill from the outside in
    # delete any added elements and count the number of outsides and the lenght of the path set
    # insides = total - path elements - outsides  
    new_map = get_path_only(path, pipes)
    expand_map(new_map)
    extend_boundaries(new_map, start_idx)
    fill_from_outside(new_map)
    print(count_interior(new_map))
    print_pipes(shrunk_map(new_map))

def count_interior(pipes) -> int:
    count = 0
    for row in pipes[1::2]:
        for element in row[1::2]:
            if element == ".":
                count+= 1
    return count

def fill_from_outside(pipes):
    stack = [(0,0)]
    while stack:
        cur = stack.pop()
        if not in_bounds(cur, pipes):
            continue
        row, col = cur
        if pipes[row][col] != ".":
            continue
        pipes[row][col] = "O"

        # print("".join(pipes[row]))
        # time.sleep(0.005)
        # print('\033c', end='')
        
        stack.extend([(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)])

def in_bounds(coordinate, array):
    row, col = coordinate
    return row >= 0 and row < len(array) and col >= 0 and col < len(array[0])

def expand_map(pipes: List[List[int]]) -> List[List[int]]:
    len_col = len(pipes)
    len_row = len(pipes[0])
    
    for i in range(len_col - 1, 0, -1):
        pipes.insert(i, ["."] * len_row)

    for row in pipes:
        for i in range(len_row - 1, 0, -1):
            row.insert(i, ".")

    # extend pipes in rows
    for row in pipes:
        for i in range(1, len(row), 2):
            if row[i-1] in ["-", "F", "L"] and row[i+1] in ["-", "7", "J"]:
                row[i] = "-"
    
    # extend pipes in columns
    for col in range(0, len(pipes[0]), 2):
        for row in range(1, len(pipes), 2):
            if pipes[row-1][col] in ["S", "|", "F", "7"] and pipes[row+1][col] in ["S", "|", "L", "J"]:
                pipes[row][col] = "|"

def shrunk_map(pipes: List[List[int]]) -> List[List[int]]:
    return [[x for x in row[1::2]] for row in pipes[1::2]]


def extend_boundaries(pipes: list[list[str]], start_idx):
    for line in pipes:
        line.insert(0, ".")
        line.append(".")
    pipes.insert(0, ["."] * (len(pipes[0])))
    pipes.append(["."] * (len(pipes[0])))
    # shift start down and left by 1
    start_idx[0] += 1
    start_idx[1] += 1


def get_next_index(pipes, connections, cur_index: List[int], prev_index: List[int]) -> List[int]:
    row, col = cur_index
    cur_pipe = pipes[row][col]
    direction1 = [a+b for a, b in zip(cur_index, connections[cur_pipe][0])]
    direction2 = [a+b for a, b in zip(cur_index, connections[cur_pipe][1])]
    if direction1 != prev_index:
        return direction1
    return direction2


def leave_start(pipes, start_conn, start_idx, valid_pipes) -> List[int]:
    row, col = start_idx
    # check each of the 4 directions and pick the first direction that has a valid pipe
    for direction, valid in zip(start_conn, valid_pipes):
        r, c = direction
        if pipes[row + r][col + c] in valid:
            return [row+r, col+c]
        

def get_path_only(path, pipes):
    path_only = [["." for _ in row] for row in pipes]
    for row, col in path:
         path_only[row][col] = pipes[row][col]
    return path_only


def print_pipes(pipes):
    for line in pipes:
        line.append("\n")
    res = ["".join(line) for line in pipes]
    with open("output.txt", "w") as f:
        f.writelines(res)
        

if __name__ == "__main__":
    main()
        
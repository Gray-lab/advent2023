from typing import List

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
            pipes.append(list(line))

    cur_idx = leave_start(pipes, start_conn, start_idx, valid_pipes)
    prev_index = start_idx
    path.append(cur_idx)
    while cur_idx != start_idx:
        new_idx = get_next_index(pipes, connections, cur_idx, prev_index)
        prev_index = cur_idx
        cur_idx = new_idx
        path.append(cur_idx)

    print_path(path, pipes)
    
    print(len(path) / 2)
    

def extend_boundaries(pipes: list[list[str]]):
    for line in pipes:
        line.insert(0, ".")
        line.append(".")
    pipes.insert(0, ["."] * (len(pipes[0]) + 2))
    pipes.append(["."] * (len(pipes[0]) + 2))


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
        

def print_path(path, pipes):
    path_only = [["." for _ in row] for row in pipes]
    for row, col in path:
         path_only[row][col] = pipes[row][col]

    for line in path_only:
        line.append("\n")
    path_only = ["".join(line) for line in path_only]

    with open("output.txt", "w") as f:
        f.writelines(path_only)
        

if __name__ == "__main__":
    main()
        
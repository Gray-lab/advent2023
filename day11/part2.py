from typing import List, Tuple


def main():
    arrays, clear_rows, clear_cols = process_input("input.txt")
    multiplier = 999999
    stars = locate_stars(arrays, clear_cols, clear_rows, multiplier)
    distance_sum = 0
    for star in stars:
        distance_sum += sum(get_distances(star, stars))
    print(int(distance_sum/2))


def locate_stars(arrays, clear_cols, clear_rows, multiplier) -> List[Tuple[int]]:
    stars = []
    for x, row in enumerate(arrays):
        for y, ch in enumerate(row):
            if ch == "#":
                stars.append((x + (multiplier * clear_rows[x]), y + (multiplier * clear_cols[y])))
    return stars


def get_distances(source, stars) -> List[int]:
    x, y = source
    return [abs(star[0] - x) + abs(star[1] - y) for star in stars]


def process_input(filename):
    arrays = []
    clear_rows = []
    clear_cols = []
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            if "#" in line:
                arrays.append(list(line.strip()))
                if clear_rows:
                    clear_rows.append(clear_rows[i - 1])
                else:
                    clear_rows.append(0)
            else:
                arrays.append(list(line.strip()))
                if clear_rows:
                    clear_rows.append(clear_rows[i - 1] + 1)
                else:
                    clear_rows.append(1)
    transposed = [*zip(*arrays)]
    arrays = []
    for i, line in enumerate(transposed):
        if "#" in line:
            arrays.append(line)
            if clear_cols:
                clear_cols.append(clear_cols[i - 1])
            else:
                clear_cols.append(0)
        else:
            arrays.append(line)
            if clear_cols:
                clear_cols.append(clear_cols[i - 1] + 1)
            else:
                clear_cols.append(1)

    arrays = [*zip(*arrays)]
    return arrays, clear_rows, clear_cols


def print_array(array):
    for line in array:
        print("".join(line))


if __name__ == "__main__":
    main()
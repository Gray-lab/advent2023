from typing import List, Tuple


def main():
    arrays = process_input("example.txt")
    stars = locate_stars(arrays)
    distance_sum = 0
    for star in stars:
        distance_sum += sum(get_distances(star, stars))
    print(distance_sum/2)


def locate_stars(arrays) -> List[Tuple[int]]:
    stars = []
    for x, row in enumerate(arrays):
        for y, ch in enumerate(row):
            if ch == "#":
                stars.append((x, y))
    return stars


def get_distances(source, stars) -> List[int]:
    x, y = source
    return [abs(star[0] - x) + abs(star[1] - y) for star in stars]


def process_input(filename):
    arrays = []
    with open(filename) as f:
        for line in f.readlines():
            if "#" in line:
                arrays.append(list(line.strip()))
            else:
                arrays.extend([list(line.strip())] * 2)
    transposed = [*zip(*arrays)]
    arrays = []
    for line in transposed:
        if "#" in line:
            arrays.append(line)
        else:
            arrays.extend([line] * 2)

    arrays = [*zip(*arrays)]
    return arrays


def print_array(array):
    for line in array:
        print("".join(line))


if __name__ == "__main__":
    main()
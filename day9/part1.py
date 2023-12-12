import re
from typing import List

def get_diff_array(input_array) -> List[int]:
     return [input_array[i + 1] - input_array[i] for i in range(len(input_array) - 1)]

def calc_next_val(input_arrays) -> int:
    return sum(array[-1] for array in input_arrays)

total = 0
with open("input.txt") as f:
    for line in f.readlines():
        arrays = []
        arrays.append([int(x) for x in re.findall("-?\d+", line)])
        # return false only if all elements are 0
        while any(arrays[-1]):
            arrays.append(get_diff_array(arrays[-1]))
        total += calc_next_val(arrays)
print(total)
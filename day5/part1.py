from dataclasses import dataclass, field
import re

seeds = []
maps = []

@dataclass
class Transform:
    dest_start: int
    source_start: int
    range_len: int
    start: field(init=False) = 0
    end: field(init=False) = 0
    offset: field(init=False) = 0

    def transform(self, input) -> int:
        if self.start <= input <= self.end:
            return input + self.offset
        return input
    
    def __post_init__(self):
        self.start = self.source_start
        self.end = self.source_start + self.range_len - 1
        self.offset = self.dest_start - self.source_start

with open("input.txt") as f:
    seeds = [int(x) for x in re.findall("\d+", f.readline())]    

    print(seeds)

    mapping = []
    for l in f.readlines():
        if not(l.strip()):
            if mapping:
                maps.append(mapping)
            continue

        nums = [int(x) for x in re.findall("\d+", l)]

        if not nums:
            mapping = []
            continue

        mapping.append(Transform(nums[0], nums[1], nums[2]))
    maps.append(mapping)
    
    location = float('inf')
    for seed in seeds:  
        # print("----")
        for mapping in maps:
            # print("new_mapping")
            for transformation in mapping:
                # print(seed, transformation)
                new_value = transformation.transform(seed)
                # print(new_value, seed)
                if new_value != seed:
                    seed = new_value
                    break
        # print(f"location: {seed}")
        location = min(seed, location)
    print(location)

from dataclasses import dataclass, field
import re
import multiprocessing

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


def process_range(start, end, maps, result_queue):
    local_location = float('inf')
    print(f"processing range {start}-{end}")
    for seed in range(start, end):
        for mapping in maps:
            for transformation in mapping:
                new_value = transformation.transform(seed)
                if new_value != seed:
                    seed = new_value
                    break
        local_location = min(seed, local_location)
    print(f"range {start}-{end} result: {local_location}")
    result_queue.put(local_location)


if __name__ == "__main__":
    result_queue = multiprocessing.Queue()
    processes = []

    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = start + seeds[i + 1]
        process = multiprocessing.Process(target=process_range, args=(start, end, maps, result_queue))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Collect results from the queue
    locations = [result_queue.get() for _ in range(len(processes))]
    final_location = min(locations)
    print(final_location)

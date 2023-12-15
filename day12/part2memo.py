import re

global memo
memo = {}

def main():
    global memo
    groups_array = []
    strings = []
    with open("input.txt") as f:
        for line in f.readlines():
            groups_array.append(1*list(map(lambda x: int(x), re.findall("\d+", line))))
            strings.append(1*line.split()[0])

    # with open("output.txt", "w") as f:
    total = 0
    for i in range(len(strings)):
        res = strings[i]
        # the number of possible positions at any index is dependent on how many groups we have left
        memo = {}
        print(strings[i], groups_array[i])
        line_total = find_positions(res, strings[i], tuple(groups_array[i]), 0, 0)
        print(line_total)
        # f.write(f"{strings[i]} {groups_array[i]} -> {line_total}\n")
        total += line_total
        print(memo)
    print(total)

def find_positions(res, string, groups, cur_index, group_index):
    global memo

    total = 0
    if group_index == len(groups):
        # make sure we used all available "#"
        if res.count("#") == sum(groups):
            print(res)
            return 1
        else: 
            return 0

    if cur_index >= len(string):
        return 0
            
    cur_group = groups[group_index]
    while cur_index <= len(string) - cur_group:
        # check if we can place the group
        if "." not in string[cur_index:cur_index + cur_group]:
            if check_bounds(string, cur_group, cur_index):
                if cur_index > 0 and string[cur_index - 1] == "#":
                    # position has been overshot - we can't leave an unused "#"
                    break
                # success, go to next group
                if (cur_index, group_index) in memo:
                    total += memo[(cur_index, group_index)]
                else:
                    new_res = res[:cur_index] + "#" * cur_group + res[cur_index + cur_group:]
                    pos_count = find_positions(new_res, string, groups, cur_index + 1 + cur_group, group_index + 1)
                    memo[(cur_index, group_index)] = pos_count
                    total += pos_count
        # try next position
        cur_index += 1

    
    return total

def check_bounds(string, cur_group, cur_index):
    if cur_index < len(string) - cur_group and string[cur_index + cur_group] == "#":
        return False
    return True

if __name__ == "__main__":
    main()

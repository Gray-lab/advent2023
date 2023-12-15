import re

global count
count = 0

def main():
    groups_array = []
    strings = []
    with open("input.txt") as f:
        for line in f.readlines():
            groups_array.append(list(map(lambda x: int(x), re.findall("\d+", line))))
            strings.append(line.split()[0])

    for i in range(len(strings)):
        res = strings[i]
        find_positions(res, strings[i], groups_array[i], 0, 0)
    print(count)

def find_positions(res, string, groups, cur_index, group_index):
    global count

    if group_index == len(groups):
        # make sure we used all available "#"
        if res.count("#") == sum(groups):
            count += 1
            print(res)
        return
    
    if cur_index >= len(string):
        return
    
    cur_group = groups[group_index]

    while cur_index <= len(string) - cur_group:
        # check if we can place the group
        if "." not in string[cur_index:cur_index + cur_group]:
            if check_bounds(string, cur_group, cur_index):
                if cur_index > 0 and string[cur_index - 1] == "#":
                    # position has been overshot - we can't leave an unused "#"
                    return
                # success, go to next group
                new_res = res[:cur_index] + "#" * cur_group + res[cur_index + cur_group:]
                find_positions(new_res, string, groups, cur_index + 1 + cur_group, group_index + 1)

        # try next position
        cur_index += 1
    return

def check_bounds(string, cur_group, cur_index):
    if cur_index < len(string) - cur_group and string[cur_index + cur_group] == "#":
        return False
    return True

if __name__ == "__main__":
    main()

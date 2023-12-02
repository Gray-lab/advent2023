res = 0
replacements = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def replaceAll(line:str) -> str:
    while True:
        indexes = []
        for word in replacements.keys():
            if word in line:
                indexes.append((line.index(word), word))
        # done!
        if not indexes:
            return line
        indexes.sort(key = lambda x: x[0])

        first_insert = indexes[0][0]
        line = line[:first_insert] + replacements[indexes[0][1]] + line[first_insert + 1:]

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = replaceAll(line)
        digits = [x for x in line if x in "1234567890"]
        num = digits[0] + digits[-1]
        res += int(num)
        
print(res)


import re

with open("input") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [re.match(r"(\d+)-(\d+) (\w): (\w+)", x).groups() for x in content]

sum = 0
for i in content:
    if((i[3][int(i[0]) - 1] == i[2]) != (i[3][int(i[1]) - 1] == i[2])):
        sum+=1

print(sum)

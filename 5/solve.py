with open("input") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

arr = [0] * 959
for entry in content:
    try:
        arr[int(entry[:7].replace('F', '0').replace('B', '1'), 2) * 8 + int(entry[7:].replace('L', '0').replace('R', '1'), 2)] = 1
    except:
        pass

print(arr)
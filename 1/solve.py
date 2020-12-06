with open("input") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content]

for i in content:
    for j in content:
         for k in content:
              if j + i + k == 2020:
                  print(j*i*k)

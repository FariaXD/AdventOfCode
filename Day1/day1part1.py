import re

lines = []
with open('Day1/input.txt', 'r') as file:
    lines = file.read().splitlines()

i = ["1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet"]

j = [''.join(re.findall(r'\d+', w)) for w in lines]
o = [num[0] + num[-1] if len(num) > 1 else num * 2 for num in j]
result = sum(map(int, o))
print(result)


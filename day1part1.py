import re

i = ["1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet"]

j = [''.join(re.findall(r'\d+', w)) for w in i]
o = [num[0] + num[-1] if len(num) > 1 else num * 2 for num in j]
print(o)
result = sum(map(int, o))
print(result)


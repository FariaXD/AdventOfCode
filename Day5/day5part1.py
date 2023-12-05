lines = []
with open('Day5/input.txt', 'r') as file:
    lines = file.read()
seeds, *blocks = lines.split('\n\n')

seeds = list(map(int, seeds.split(":")[1].split()))
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new_seeds = []
    for seed in seeds:
        for dst,src,rg in ranges:
            if seed in range(src, src + rg):
                new_seeds.append(seed - src + dst)
                break
        else:
            new_seeds.append(seed)
    seeds = new_seeds
print(min(seeds))
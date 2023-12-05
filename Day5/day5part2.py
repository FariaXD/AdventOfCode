lines = []
with open('Day5/input.txt', 'r') as file:
    lines = file.read()
inputs, *blocks = lines.split('\n\n')
inputs = list(map(int, inputs.split(":")[1].split()))


def get_seeds_range(inputs):
    seeds = []
    for i in range(0,len(inputs),2): # create seed range list
        seeds.append((inputs[i], inputs[i]+inputs[i+1]))
    return seeds
seeds = get_seeds_range(inputs)

def check_each_block(blocks):
    global seeds
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split()))) # append each block ranges
        seeds = check_each_block_range(ranges) # seeds for next block
    return seeds
    
        
def check_each_block_range(ranges):
    global seeds
    new_seeds = []
    while len(seeds) > 0: # checks all the seeds until there are none left to be checked
        start, end = seeds.pop() # Remove one seed range (start, end)
        for dst,src,rg in ranges: # for each destination, source, range in ranges
            overlap_start = max(start, src) # calculate if seed range overlaps in current block_range -> gets start of overlap
            overlap_end = min(end, src + rg) # gets end of overlap
            if(overlap_start < overlap_end): # if overlap exists then it can be mapped to another range
                new_seeds.append((overlap_start - src + dst, overlap_end - src + dst)) #new overlapped range ready for next block
                if(overlap_start > start): # checks if there are seeds left of the overlap
                    seeds.append((start, overlap_start)) # creates a new range to be checked
                if(end > overlap_end): # checks if there are seeds right of the overlap
                    seeds.append((overlap_end, end)) # creates a new range to be checked
                break
        else:
            new_seeds.append((start, end)) # if the for loop wasnt broken then append seed range for next block
    return new_seeds # seeds to be checked by new block


print(min(check_each_block(blocks))[0]) # prints the minimum location [0] because this block also has a destination range that can be ignored

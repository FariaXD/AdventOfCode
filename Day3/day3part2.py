import math

lines = []
with open('Day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

debug_input = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."
]


check_omni = [(0,1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1),(0,-1)]

def check_if_in_interval_exclusive(number, interval):
    return number >= 0 and number < interval
def isGearSymbol(char):
    return char == "*"

def get__engine_code(input):

    def check_surroundings(input, i, j):

        def get_number_char_indexes(input, i, j):
            def find_number(index_i, index_j, number, indexes):
                if index_j < len(input[index_i]) and input[index_i][index_j].isdigit():
                    number += input[index_i][index_j]
                    indexes.append(index_j)
                    return find_number(index_i, index_j + 1, number, indexes)
                else:
                    return number, indexes
            return find_number(i,j,"",[])
                
        gear = ()
        number, number_indexes = get_number_char_indexes(input, i, j)
        check_omni = [(0,1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1),(0,-1)]
        for index in number_indexes:
            input[i] = input[i][:index] + "." + input[i][index+1:]
            for dir in check_omni:
                if(check_if_in_interval_exclusive(i+dir[0], len(input)) and
                    check_if_in_interval_exclusive(index+dir[1], len(input[i])) and
                      isGearSymbol(input[i+dir[0]][index+dir[1]])):
                    gear = (i+dir[0],index+dir[1])
                    break
        return number, gear
    
    codes = []
    number_with_gear = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if(input[i][j].isdigit()):
                number, gear = check_surroundings(input,i,j)
                if(gear != ()):
                    number_with_gear.append([number, gear])
    for n in range(len(number_with_gear)):
        numbers = []
        for m in range(n+1,len(number_with_gear)):
            if(number_with_gear[n][1] == number_with_gear[m][1]):
                numbers.append(int(number_with_gear[n][0]))
                numbers.append(int(number_with_gear[m][0]))
                codes.append(math.prod(numbers))
    return sum(map(int, codes))

print(get__engine_code(lines))
                

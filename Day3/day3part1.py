lines = []
with open('Day3/input1.txt', 'r') as file:
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

import re

def is_special_char_except_period(char):
    pattern = re.compile(r'[^a-zA-Z0-9\.]')
    return bool(pattern.match(char))

def check_if_in_interval_exclusive(number, interval):
    return number >= 0 and number < interval

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
                
        valid = False
        number, number_indexes = get_number_char_indexes(input, i, j)
        check_omni = [(0,1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1),(0,-1)]
        for index in number_indexes:
            input[i] = input[i][:index] + "." + input[i][index+1:]
            for dir in check_omni:
                if(check_if_in_interval_exclusive(i+dir[0], len(input)) and
                    check_if_in_interval_exclusive(index+dir[1], len(input[i])) and
                      is_special_char_except_period(input[i+dir[0]][index+dir[1]])):
                    valid = True
                    break
        return number, valid
    
    codes = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if(input[i][j].isdigit()):
                number, valid = check_surroundings(input,i,j)
                if(valid):
                    codes.append(number)
    return sum(map(int, codes))

print(get__engine_code(lines))
                

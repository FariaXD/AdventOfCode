import re

lines = []
with open('Day1/input.txt', 'r') as file:
    lines = file.read().splitlines()

input = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]

word_to_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

#creates a new string only with ints or strings that represent ints like 2eight8one
def replace_words_with_numbers(input_string):
    new_string = ""
    for i in range(len(input_string)):
        charSequence = input_string[i]
        if(input_string[i] in word_to_number.values()):
            new_string+=input_string[i]
        elif(i+1 != len(input_string)):
            for j in range(i+1, len(input_string)):
                charSequence+= input_string[j]
                if(charSequence in word_to_number.keys()):
                    new_string+=charSequence
                    break
    for key, value in word_to_number.items():
        if(key in new_string):
            new_string = new_string.replace(key,value)
    return new_string
	
    


i = [replace_words_with_numbers(i) for i in lines]
o = [num[0] + num[-1] if len(num) > 1 else num * 2 for num in i]
result = sum(map(int, o))
print(result)

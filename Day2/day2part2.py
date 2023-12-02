import math
games_list = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green","Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

lines = []
with open('Day2/input2.txt', 'r') as file:
    lines = file.read().splitlines()

power_game = []
def validate_game(game):
    tmp = game.replace("Game ", "")
    id_game, game_vals = tmp.split(":")
    rounds = game_vals.split(";")
    min_dict = {"red": 0, "blue": 0, "green": 0}
    for round in rounds:
        colors = round.split(",")
        for color in colors:
            numb_color = color.strip().split(" ")
            if(int(numb_color[0]) > min_dict[numb_color[1]]):
                min_dict[numb_color[1]] = int(numb_color[0])
    power_game.append(math.prod(min_dict.values()))
   

a = [validate_game(game) for game in lines]
result = sum(map(int, power_game))
print(result)





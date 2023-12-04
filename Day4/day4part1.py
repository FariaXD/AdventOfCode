lines = []
with open('Day4/input.txt', 'r') as file:
    lines = file.read().splitlines()
def check_card(i):
    j = i.split(":")[1].strip()
    game_numbers, lottery_numbers = j.split("|")
    game_numbers = list(map(int, game_numbers.strip().split()))
    lottery_numbers = list(map(int, lottery_numbers.strip().split()))
    correct_numbers = list(set(game_numbers) & set(lottery_numbers))
    return 2 ** (len(correct_numbers) - 1)
print(sum(map(int, [check_card(i) for i in lines])))
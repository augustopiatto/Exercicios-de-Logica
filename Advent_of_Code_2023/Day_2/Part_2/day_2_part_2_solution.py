import re


def fewest_num(list):
    highest_num = 0
    for number in list:
        num = int(number)
        if num > highest_num:
            highest_num = num
    
    return highest_num


def cube_conundrum(inputs):
    sum = 0
    for game in inputs:
        pattern = r'Game\s+(\d+)\s*:'
        match = re.search(pattern, game)
        if match:
            game_id = int(match.group(1))
            blue_pattern = r'\b(\d+)\s+blue\b'
            red_pattern = r'\b(\d+)\s+red\b'
            green_pattern = r'\b(\d+)\s+green\b'
            blue_matches = re.findall(blue_pattern, game)
            red_matches = re.findall(red_pattern, game)
            green_matches = re.findall(green_pattern, game)

            blue_num = fewest_num(blue_matches)
            red_num = fewest_num(red_matches)
            green_num = fewest_num(green_matches)

            sum += (blue_num * red_num * green_num)
        else:
            raise ValueError("Não existe a palavra 'Game' nesta linha")

    return sum

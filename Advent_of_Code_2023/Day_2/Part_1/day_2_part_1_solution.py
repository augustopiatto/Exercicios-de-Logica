import re


max_existing_conundrum = {"blue": 14, "red": 12, "green": 13}


def check_if_possible(color, list):
    for number in list:
        if int(number) > max_existing_conundrum[color]:
            print("Impossível, número maior do que existe")
            return False
    
    return True


def cube_conundrum(inputs):
    id_sum = 0
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

            blue_possible = check_if_possible("blue", blue_matches)
            red_possible = check_if_possible("red", red_matches)
            green_possible = check_if_possible("green", green_matches)

            if blue_possible and red_possible and green_possible:
                id_sum += game_id
        else:
            raise ValueError("Não existe a palavra 'Game' nesta linha")

    return id_sum

"""
Day 02 of Advent of Code
Rock Paper Scissors
"""


def get_inputs_from_strategy_guide(new_strategy):
    with open('input_2.txt', 'r') as input_file:
        total_score = 0
        for line in input_file.readlines():
            line = line.strip()
            elf_chance, my_chance = line.split(" ")
            match_result = me_vs_elf(elf_chance, my_chance, new_strategy=new_strategy)
            score = your_score_in_single_round(match_result, my_chance, elf_chance, new_strategy=new_strategy)
            total_score += score
    return total_score


def decoder_2(my_chance):
    chances = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    # chances.get(my_chance, 'default')
    try:
        return chances[my_chance]
    except KeyError:
        raise ValueError("Invalid Choice")


def decoder(my_chance):
    if my_chance == 'X':
        my_chance = 'A'
    elif my_chance == 'Y':
        my_chance = 'B'
    elif my_chance == 'Z':
        my_chance = 'C'
    else:
        raise ValueError("Invalid Option")
    return my_chance


def new_decoder(my_chance, elf_chance):
    if my_chance == 'X':
        print('I should lose')
        if elf_chance == 'A':
            my_chance = 'C'
        elif elf_chance == 'B':
            my_chance = 'A'
        elif elf_chance == 'C':
            my_chance = 'B'
        else:
            raise ValueError("Invalid option")
    elif my_chance == 'Y':
        print('I should draw')
        my_chance = elf_chance
    elif my_chance == 'Z':
        print('I should win')
        if elf_chance == 'A':
            my_chance = 'B'
        elif elf_chance == 'B':
            my_chance = 'C'
        elif elf_chance == 'C':
            my_chance = 'A'
        else:
            raise ValueError("Invalid option")
    print(f'So elf played {elf_chance} and I played {my_chance}')
    return my_chance


def me_vs_elf(elf_chance, my_chance, new_strategy= False) -> int:
    if not new_strategy:
        if elf_chance == decoder(my_chance):
            return 0
        if (elf_chance == 'A' and my_chance == 'Y') or \
                (elf_chance == 'B' and my_chance == 'Z') or \
                (elf_chance == 'C' and my_chance == 'X'):
            return 1
        return -1
    elif new_strategy:
        if my_chance == 'X':
            return -1
        if my_chance == 'Y':
            return 0
        return 1


def your_score_in_single_round(result, my_chance, elf_chance, new_strategy=False):
    score = 0
    if not new_strategy:
        if my_chance == 'X':
            score += 1
        elif my_chance == 'Y':
            score += 2
        elif my_chance == 'Z':
            score += 3
    if new_strategy:
        if new_decoder(my_chance, elf_chance) == 'A':
            score += 1
        elif new_decoder(my_chance, elf_chance) == 'B':
            score += 2
        elif new_decoder(my_chance, elf_chance) == 'C':
            score += 3
    if result == 1:
        score += 6
    elif result == 0:
        score += 3
    return score


if __name__ == '__main__':
    old_result = get_inputs_from_strategy_guide(new_strategy=False)
    new_result = get_inputs_from_strategy_guide(new_strategy=True)
    print(old_result)
    print(new_result)

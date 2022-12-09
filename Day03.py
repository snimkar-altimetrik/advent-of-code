"""
Day 03 of Advent of Code
Rucksack Reorganization
"""


def split_input_string_half():
    priorities = []
    with open('input_3.txt', 'r') as input_file:
        for line in input_file.readlines():
            line = line.strip()
            string_length = len(line)
            compartment_one = line[:int(string_length/2)]
            compartment_two = line[int(string_length/2):]
            letters = compare_compartments_3(compartment_one, compartment_two)
            rucksack_priorities = [calculate_priority_2(common_letter) for common_letter in letters]
            priorities.append(sum(rucksack_priorities))
    return sum(priorities)


def input_part_two():
    priorities = []
    with open('input_3.txt', 'r') as input_file:
        count = 0
        group = []
        for line in input_file.readlines():
            if count < 3:
                line = line.strip()
                count += 1
                group.append(line)
            else:
                print(group)
                letters = compare_compartments_3(group[0], group[1], group[2])
                rucksack_priorities = [calculate_priority_2(common_letter) for common_letter in letters]
                priorities.append(sum(rucksack_priorities))
                count = 1
                line = line.strip()
                group = [line]
        print(group)
        letters = compare_compartments_3(group[0], group[1], group[2])
        rucksack_priorities = [calculate_priority_2(common_letter) for common_letter in letters]
        priorities.append(sum(rucksack_priorities))
    return sum(priorities)


def compare_compartments(compartment_one, compartment_two):
    print(compartment_one)
    print(compartment_two)
    matches = set()
    for letter_one in compartment_one:
        for letter_two in compartment_two:
            if letter_one == letter_two:
                matches.add(letter_one)
    return list(matches)


def compare_compartments_2(compartment_one, compartment_two):
    matches = set()
    comp_two = set(compartment_two)
    for letter_one in compartment_one:
        if letter_one in comp_two:
            matches.add(letter_one)
    return list(matches)


def compare_compartments_3(compartment_one, compartment_two, compartment_three=None):
    comp_one = set(compartment_one)
    comp_two = set(compartment_two)
    if compartment_three is None:
        matches = comp_one.intersection(comp_two)
        return list(matches)
    elif compartment_three is not None:
        comp_three = set(compartment_three)
        matches = (comp_one.intersection(comp_two)).intersection(comp_three)
        return list(matches)


def calculate_priority(letter):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabets_weight = {val: idx+1 for idx, val in enumerate(alphabets)}
    if letter.isupper():
        priority = alphabets_weight.get(letter.lower()) + 26
        return priority
    elif letter.islower():
        priority = alphabets_weight.get(letter.lower())
        return priority


def calculate_priority_2(letter):
    import string
    alphabets = list(string.ascii_lowercase+string.ascii_uppercase)
    alphabets_weight = {val: idx+1 for idx, val in enumerate(alphabets)}
    return alphabets_weight.get(letter, 0)


if __name__ == '__main__':
    result = split_input_string_half()
    print(result)
    result_two = input_part_two()
    print(result_two)

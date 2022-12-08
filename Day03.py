"""
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


def compare_compartments_3(compartment_one, compartment_two):
    comp_one = set(compartment_one)
    comp_two = set(compartment_two)
    matches = comp_one.intersection(comp_two)
    return list(matches)


def calculate_priority(letter):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
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








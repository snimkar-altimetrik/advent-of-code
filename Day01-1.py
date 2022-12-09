"""
Day 01 of Advent of Code
Elven Calories
"""

def get_sum_of_calories():
    with open('input_1.txt', 'r') as input_file:
        elves_calories = []
        calories = []
        for line in input_file.readlines():
            line = line.strip()
            if line !='':
                calories.append(int(line))
            else:
                elves_calories.append(sum(calories))
                calories = []
    return elves_calories


def get_sum_of_top_three_calories(all_calories):
    top_three = sorted(all_calories)[-3:]
    result = sum(top_three)
    return result


if __name__ == '__main__':

    all_calorie = get_sum_of_calories()
    max_calorie = max(all_calorie)
    print(max_calorie)
    top_three_sum = get_sum_of_top_three_calories(all_calorie)
    print(top_three_sum)





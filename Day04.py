"""
Day 04 of Advent of Code
Camp Cleanup
"""
from typing import List


def reading_input(partial=False):
    with open('input_4.txt', 'r') as input_file:
        count = 0
        for line in input_file.readlines():
            line = line.strip()
            elves_tasks = line.split(',')
            elf_one_tasks = elves_tasks[0].split('-')
            elf_two_tasks = elves_tasks[1].split('-')
            elf_one = list(map(int, elf_one_tasks))
            elf_two = [int(n) for n in elf_two_tasks]
            if partial is False:
                if are_tasks_fully_overlapping(elf_one, elf_two):
                    print(elf_one, elf_two)
                    count += 1
            elif partial is True:
                if are_tasks_partial_overlapping(elf_one, elf_two) or are_tasks_fully_overlapping(elf_one, elf_two):
                    count += 1
    return count


def are_tasks_fully_overlapping(task_one: List[int], task_two: List)-> bool:
    return (task_one[0] <= task_two[0] and task_one[1] >= task_two[1]) or \
           (task_two[0] <= task_one[0] and task_two[1] >= task_one[1])


def are_tasks_partial_overlapping(task_one: List[int], task_two: List)-> bool:
    return ((task_two[0] <= task_one[0] <= task_two[1]) and task_two[1] < task_one[1]) or \
           ((task_two[0] <= task_one[1] <= task_two[1]) and task_one[0] < task_two[0]) or \
           ((task_one[0] <= task_two[0] <= task_one[1]) and task_one[1] < task_two[1]) or \
           ((task_one[0] <= task_two[1] <= task_one[1]) and task_two[0] < task_one[0])

if __name__ == '__main__':
    result = reading_input()
    print(result)
    result_two = reading_input(partial=True)
    print(result_two)

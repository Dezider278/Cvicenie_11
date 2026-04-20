import random

from numpy.ma.core import minimum


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(list_on_nums):
    numbers = list_on_nums.copy()
    for i in range(len(numbers)):
        min_idx = i
        min_val = numbers[i]
        for o in range(i,len(numbers)):
            if numbers[o] < min_val:
                min_idx = o
                min_val = numbers[o]
        numbers[i],numbers[min_idx] = numbers[min_idx],numbers[i]


    return numbers

print(selection_sort([5, 1, 4, 2, 8]))
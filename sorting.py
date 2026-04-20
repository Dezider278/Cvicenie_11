import random
import matplotlib.pyplot as plt
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

def bubble_sort(list_on_nums):
    numbers = list_on_nums.copy()
    plt.ion()
    plt.show()
    for _ in range(len(numbers)):
        for i in range(len(numbers)):
            try:
                if numbers[i] > numbers[i+1]:
                    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                    index_highlight1 = i
                    index_highlight2 = i + 1
                    colors = ["steelblue"] * len(numbers)
                    colors[index_highlight1] = "tomato"
                    colors[index_highlight2] = "tomato"
                    plt.clf()
                    plt.bar(range(len(numbers)), numbers, color=colors)
                    plt.title("Bubble Sort")
                    plt.pause(0.1)
            except:
                continue
    plt.ioff()
    plt.show()
    return numbers

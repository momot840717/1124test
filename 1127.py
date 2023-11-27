import numpy as np
import random

def merge(sort_left, sort_right):
    result = []
    while len(sort_left) and len(sort_right):
        if sort_left[0] < sort_right[0]:
            result.append(sort_left.pop(0))
        else:
            result.append(sort_right.pop(0))
    
    result += sort_left if len(sort_left) else sort_right
    return result

def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers
    
    mid_index = len(numbers) // 2
    left_numbers = numbers[: mid_index]
    right_numbers = numbers[mid_index:]

    # print(left_numbers, right_numbers)
    divide_left = merge_sort(left_numbers)
    divide_right = merge_sort(right_numbers)
    # print('dd', divide_left, divide_right)
    merge_numbers = merge(divide_left, divide_right)
    # print('mn', merge_numbers)

    return merge_numbers

numbers = list(np.random.randint(1, 1000, size=15))
# print(numbers)
sort_numbers = merge_sort(numbers)
# print(sort_numbers)

def insertion_sort(numbers):
    result = []
    insert_index = int()
    for number in numbers:
        for index in range(len(result)):
            if number <= result[index]:
                insert_index = index
                break
            elif number > result[index]:
                insert_index = index + 1
        result = result[:insert_index] + [number] + result[insert_index:]
    return result

# print(numbers)
insertion_sort_numbers = insertion_sort(numbers)
# print(insertion_sort_numbers)


def binary_search(sort_numbers, target):
    start, end = 0, len(sort_numbers)
    mid_index = (start + end) // 2
    
    if target == sort_numbers[mid_index]:
        return f'The index of target {target} is {numbers.index(target)}, and numbers is {numbers}'
    elif target < sort_numbers[mid_index]:
        return binary_search(sort_numbers[: mid_index], target)
    else:
        return binary_search(sort_numbers[mid_index:], target)
    
# print(binary_search(sorted(numbers), random.choice(numbers)))
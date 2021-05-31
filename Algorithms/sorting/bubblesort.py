import sys
sys.path.insert(1, 'C:/Users/noahd/Desktop/Python Projects/Algorithms')
from biglist import BIG_LIST


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort(BIG_LIST))

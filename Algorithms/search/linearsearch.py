import sys
sys.path.insert(1, 'C:/Users/noahd/Desktop/Python Projects/Algorithms')
from biglist import BIG_LIST

def linearsearch(arr, num):
    count = 0
    for i in arr:
        if i == num:
            return 'Element is present at index: ' + str(count)
        count += 1
    return 'No match found'

print(linearsearch(BIG_LIST, 134))

import sys
import math
sys.path.insert(1, 'C:/Users/noahd/Desktop/Python Projects/Algorithms')
from biglist import SORTED_BIG_LIST

# Returns index of x in arr if present, else -1
def binarysearch(arr, left, right, num):

    # Check base case
    if right >= left:

        mid = left + (right - left) // 2

        # If element is present at the middle
        if arr[mid] == num:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > num:
            return binarysearch(arr, left, mid-1, num)

        # Else the element can only be present
        # in right subarray
        else:
            return binarysearch(arr, mid + 1, right, num)

    else:
        # Element is not present in the array
        return 'Element Not Found'
print(binarysearch(SORTED_BIG_LIST, 0, len(SORTED_BIG_LIST)-1, 500))

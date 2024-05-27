#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false

array = [1,2,46,32,98,61,34,47]

def smart_duplicate_search(array):
    dictionary = dict()
    if len(array)<2:
        return False
    else:
        for _a in array:
            if _a in dictionary:
                return True
            else:
                dictionary[_a] = True
    return False

print(smart_duplicate_search(array))
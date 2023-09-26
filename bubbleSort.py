'''
BUBBLE SORT
-----------
The Algorithm - In Bubble Sort, we start from the beginning of the list then goes to the second last element. It compares the element at the current index to the index just after the current one, and checks if they are sorted, if they are, just continue and if they are not, sort them in the correct order. Repeat this until all the elements are sorted.
Time Complexity - Worst & Average - O(n^2); Best - O(n)
Space Complexity - Stable Algorithm, O(1)
'''

def bubbleSort(unsorted_list: list(int)) -> list(int):
    end_index = len(unsorted_list) - 1
    
    


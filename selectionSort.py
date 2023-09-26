'''
SELECTION SORT
--------------
The Algorithm - In selection sort, we go from the first unsorted element and check if somen other element in the unsorted part is smaller than the element, if it's smaller, set that as the minimum, else continue until you reach the end of the list, and then replace the found minimum element with the first unsorted position from which the search started.
Time Complexity - Worst, Average and Best Case: O(n^2)
Space Complexity - Stable Algorithm, O(1)
'''

def selSort(unsorted_array: list[int]) -> list[int]:
    length = len(unsorted_array)
    
    for i in range(length):
        minimum_index = i
        for j in range(i + 1, length):
            if unsorted_array[j] < unsorted_array[minimum_index]:
                minimum_index = j
        unsorted_array[i], unsorted_array[minimum_index] = unsorted_array[minimum_index], unsorted_array[i]
    return unsorted_array


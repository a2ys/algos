'''
INSERTION SORT
--------------
The Algorithm - In insertion sort, we choose the first element as sorted, then go on from there. When we go to any general index i, we check if the element at index i is less than or greater than the element at the left of it, if it's greater, it stays there and a new element is chosen, but if it's smaller, it shifts to the left and the checks with it's new neighbour, and continues the loop until it reaches the starting point of the array of elements when it puts the selected element in the beginning. This is done until the list is completely sorted.
Time Complexity - Worst & Average Case - O(n^2); Best Case - O(n)
Space Complexity - Stable Algorithm, O(1)
'''

def insertionSort(unsorted_array: list[int]) -> list[int]:
    length = len(unsorted_array)
    
    for i in range(length):
        if (i == 0):
            continue
        else:
            unsorted_element = unsorted_array[i]
            for j in range(i - 1, -1, -1):
                if unsorted_array[j] > unsorted_element:
                    unsorted_array[j + 1] = unsorted_array[j]
                else:
                    break
                unsorted_array[j] = unsorted_element
    return unsorted_array


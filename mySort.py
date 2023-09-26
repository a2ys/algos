'''
MYSORT
----------------------------
The Algorithm - In MySort, We create a new list called sorted_list. The first element is assumed to be the smallest and is inserted in the list normally. Then we go from the first element of the unsorted list to the last element of the unsorted list, everytime we go, we check if the element is greater than or less than the already existing last element; if it's greater we insert that at the same place only, but if it's smaller, we check if it is smaller than the previous one, and do so until we reach the first index when we insert the element there only.
Time Complexity - Worst - O(n^2), Average - O(n log(n)), Best - O(n)
Space Complexity - Unstable Algorithm, O(n)
'''

unsorted_list = [44,32,66,98,13]
length = len(unsorted_list)

sorted_list = list()

for i in range(length):
    if len(sorted_list) == 0:
        sorted_list.append(unsorted_list[i])
    elif unsorted_list[i] >= sorted_list[-1]:
        sorted_list.append(unsorted_list[i])
    else:
        for j in range(len(sorted_list) - 1, -1, -1):
            if j == 0:
                sorted_list.insert(0, unsorted_list[i])
                break
            if unsorted_list[i] >= sorted_list[j]:
                sorted_list.insert(j + 1, unsorted_list[i])
                break
            else:
                continue

print(sorted_list)


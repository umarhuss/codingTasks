numbers = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

for number in numbers:
    if number == 9:
        print("Number Found")


'''
implemented a linear search as the provided list is unordered
and the data set is relatively small. if this list was ordered than 
i would of implemented a binary search. 
'''


def insertion_sort(list):
    index_len = range(1,len(list))
    for i in index_len:
        value_sort = list[i]
    
    while list[i-1] > list[i] and i>0:
        list[i-1],list[i] = list[i], list[-1] 
        i -= 1 



numbers.sort()

def binary_search(arr,target,low_index =None, high_index=None):
    if low_index == None:
        low_index = 0
    if high_index == None:
        high_index = len(arr)-1
    
    if high_index < low_index:
        return 'Target not found'
    
    midpoint = (low_index + high_index) //2

    if arr[midpoint] == target:
        return 'Target found at index ' + str(midpoint)
    elif target > arr[midpoint]:
        new_high_index = high_index +1 
        return binary_search(arr,target,low_index, new_high_index)
    else:
        new_low_index = low_index -1 
        return binary_search(arr,target, new_low_index,high_index)
    
arr =[-40, -3, -1, 1, 2, 4, 5, 7, 9, 16, 18, 35, 100]
target = 9  
    
print(binary_search(arr,target))


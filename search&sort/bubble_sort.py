def bubble_sort(my_lst):
    for i in range(len(my_lst)-1,-1,-1):
        for j in range(1,i+1):
            if my_lst[j-1] > my_lst[j]:
                my_lst[j-1],my_lst[j] = my_lst[j], my_lst[j-1]
    return my_lst

print(bubble_sort([4,6,7,3,2,5]))

'''
-1, -1, -1 refers to:
-1 one from length as index start from zero 
-1 the stopping bound no inclusive so zero 
-1 the step so going down one each time

this also means that we will start from 5 and go down to zero

for range in 1 - 5+1 = 6 so in range 1 to 5 inclusive

with j we start the range from 1 - i+1 which is 6 so 1 to 5 included

we look at the index of j which is 1 at first and the index preceeding
which is 0 and compare and switch if needed 

'''


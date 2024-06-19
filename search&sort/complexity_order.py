#Constant time complexity O(1)
def get_value(my_list, key):
    return my_list[key]

print(get_value([1,2,3,4,5], 3))


def add_values(num1,num2):
    return num1+num2


#Linear time coplexity O(n)
def get_values(my_list, keys):
    values = []
    for key in keys:
        values.append(my_list[key])
    return values
'''
The n value in the keys as this is what is growing each time
as the number of items in keys grows so does the amount of iterations 
and therefore the time complexity. linear complexity 
'''

#nLog(n) time complexity
def print_lsit(lst):
    lst.sort()
    for item in lst:
        print(item)

'''
Reason for this time complexity is that the sort and for loop 
have different time comlexities. sort() has n(log(n)) and loop
has O(n) in this case we take the biggest on. 

n(Log(n)) + n 

we can negate the +n as when the input is larger the n wont make 
much of a difference. 
'''

def double_list(lst):
    for _ in range(len(lst)):
        for item in lst:
            print(item)

'''
In this case we have 2 for loops one inside of the other. both have a linear time complexity 
in this case we n * n  == n^2 which is the O notation. with a nested loop
you * the n  
'''

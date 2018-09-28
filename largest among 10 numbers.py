# your code goes here 
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1,2,14,15,17,13,24,88,77,66]))

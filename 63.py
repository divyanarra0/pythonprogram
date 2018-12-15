def minimum_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(minimum_num_in_list([5,4,2,3,1,7,6,10,8,9]))

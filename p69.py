test_list = [1,2,3,4,5] 
print (" ") 
K = 2
  
# using len() + list slicing 
# remove last K elements 
res = test_list[: len(test_list) - K] 
  
# printing result  
print (str(res)) 

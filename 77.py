def print_factors(x):
   print("")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i),
num = 8
print_factors(num)

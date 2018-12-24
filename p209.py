matrix = [2,4],[3,7] #Assume a list is given
total = 0
for column in range(0, len(matrix[0])):
        for row in range(0, len(matrix)):
            total += matrix[row][column]
        print("")
        total = 0   #Reset total to zero before restarting count
print 26

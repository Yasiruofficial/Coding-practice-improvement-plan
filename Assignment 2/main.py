# def maxSubArray(num_array):
#    grouping_array = [0 for i in range(len(num_array))]
#    grouping_array[0] = num_array[0]
#    for i in range(1,len(num_array)):
#       grouping_array[i] = max(grouping_array[i-1]+num_array[i],num_array[i])
#    return max(grouping_array)
# num_array = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(num_array))


def maxSubArray(num_array):
   sum = num_array[0]
   max_sum = num_array[0]
   
   for i in range(1,len(num_array)):
      if sum+num_array[i] < num_array[i]:
         sum = num_array[i]
      else:
         sum = sum+num_array[i]
      
      if sum > max_sum:
         max_sum = sum
   
   return max_sum
num_array = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(num_array))


# def maxSubArray(num_array):
   
#    max_subarray = num_array[0]
   
#    for i in range(len(num_array)):
#       for j in range(i+1,len(num_array)+1):
#          obj  = slice(i,j)
#          if sum(num_array[obj]) > max_subarray:
#             max_subarray = sum(num_array[obj])
#    return max_subarray
            
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) 
 
   
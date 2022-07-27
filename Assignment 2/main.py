def maxSubArray(num_array):
   
   grouping_array = [0 for i in range(len(num_array))]
   grouping_array[0] = num_array[0]
   
   for i in range(1,len(num_array)):
      grouping_array[i] = max(grouping_array[i-1]+num_array[i],num_array[i])
      
   return max(grouping_array)


num_array = [-2,1,-3,4,-1,2,1,-5,-4]

print(maxSubArray(num_array))
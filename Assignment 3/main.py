givenArray = [
   ["1","1","1","1","1"],
   ["1","0","1","1","1"],
   ["1","1","1","1","1"],
   ["1","0","0","1","0"]
   ]


def findTheLargest(row):
   max = 0
   for i in range(len(row)):
      if row[i] > max:
         max = row[i]
      sum = 0
      for j in range(i,len(row)):
         if row[j] == 0 or row[j] < row[i]:
            sum = 0
         else:
            sum = sum + row[j]
            
         if sum > max:
            max = sum
         
   return max



def getSumOfCol(row_number):
   tempArray = []
   for i in range(len(givenArray[0])):
      if row_number == 0:
         tempArray = list(map(int,givenArray[row_number]))         
      elif int(givenArray[row_number][i]) == 0:
            tempArray.append(0)
            continue
      else:
         sum = 0
         sum = sum + int(givenArray[row_number][i])
         for j in range(row_number):
            next_value = int(givenArray[row_number - (j+1)][i])
            if next_value == 0:
               break
            else:
               sum = sum + next_value
         tempArray.append(sum)
      print(" ---- " ,str(i))
   print(tempArray)      
   return tempArray
               

def largestRectangle(array):
   
   max = 0 
   
   for row in range(len(array)):
      if findTheLargest(getSumOfCol(row)) > max:
         max = findTheLargest(getSumOfCol(row))
      
   print(max)
         
         
largestRectangle(givenArray)
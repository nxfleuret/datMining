import numpy as np
from collections import Counter

numberList = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
numberListLength = len(numberList)

#Mean
def mean(listNum, listLen): 
   totalNumber = sum(listNum)
   mean = totalNumber/listLen
   print("%-10s= %f" %("Mean", mean))

#Mode
def mode(listNum, listLen):
   numberCount = Counter(listNum)
   numCount_list = dict(numberCount)

   max_value = max(list(numberCount.values()))
   mode = [num for num, freq in numCount_list.items() if freq == max_value]
   if len(mode) == listLen:
      print("No Mode in this list")
   else:
      print("Mode      = " + ', '.join(map(str, mode))) 

# Index of the median 
def Qindex(listNum, l, r): 
   n = r - l + 1
   n = (n + 1) // 2 - 1
   return n + l

#Maximum and Minimum Value
def maxminVal(listNum, a):
   if a=="min":
      minimum = listNum[0]
      for num in listNum:
         if num < minimum:
            minimum = num
      return minimum
   if a=="max":
      maximum = listNum[0]
      for num in listNum:
         if num > maximum:
            maximum = num
      return maximum

#Five Number Summary  
def fiveNumSummary(listNum, listLen):
   # listNum = listNum.sort()

   #middle index 
   mid_index = Qindex(listNum, 0, listLen) 

   Q1 = listNum[Qindex(listNum, 0, mid_index)]
   median = listNum[(Qindex(listNum, 0, listLen))]
   Q3 = listNum[Qindex(listNum, mid_index + 1, listLen)]
   print("%-10s= %d" %("Min", maxminVal(listNum,"min")))
   print("%-10s= %d" %("Max", maxminVal(listNum,"max")))
   print("%-10s= %d" %("Q1", Q1))
   print("%-10s= %d" %("Median", median))
   print("%-10s= %d" %("Q3", Q3))

#Outlier - IQR
def outIQR(listNum, listLen):
   mid_index = Qindex(listNum, 0, listLen)
   Q1 = listNum[Qindex(listNum, 0, mid_index)]
   Q3 = listNum[Qindex(listNum, mid_index + 1, listLen)]
   IQR = Q3 - Q1
   lowerBound = Q1 - 1.5*IQR
   upperBound = Q3 + 1.5*IQR

   #list without outliers
   newList = []

   #list of outliers
   outliers = []

   for num in listNum:
      if num>lowerBound and num<upperBound:
         newList.append(num)
      else:
         outliers.append(num)
   print("%-10s= %d" %("IQR", IQR))
   print("\nnew list  = " + str(newList))
   print("outliers  = " + str(outliers))

mean(numberList, numberListLength)
mode(numberList, numberListLength)
fiveNumSummary(numberList, numberListLength)
outIQR(numberList, numberListLength)

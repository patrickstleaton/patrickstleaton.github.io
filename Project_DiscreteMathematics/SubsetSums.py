#This program finds elements in a given array whose sum equals the desired number.
from itertools import *

s_array = []
s_length = input("Please enter the size of S:")

#Find subsets.
def subsets(s):
    return chain(*map(lambda x: combinations(s, x), range(0, len(s)+1)))

#Fill the list.
for i in range(0,s_length):
  s = input("Please enter an element of S:") 
  s_array.append(int(s))
  
subset_total = 0

#Get the desired number.
n = input("Please enter the number N:")

#Traverse subsets to find elements whose sum == n.
for subset in subsets(s_array):
      if sum(subset) == n:
        print list(subset)
        subset_total += 1
   
#Print number of subsets with the sum of n.
if subset_total >= 1:
 print "There are", subset_total, "subsets with the sum of", n    
if subset_total == 0:
  print "Subsets with the sum of",n,"do not exist."
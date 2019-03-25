#This program finds summations of an input integer.
from math import *
#Get value of n
n = int(raw_input("Please enter the value of n: "))
#This function computes summation of 2^i
def sum_one(n):
#Base Case  
  if n==0:
    return int(pow(2,n))
#Inductive Case    
  else:
    return int(pow(2,n) + sum_one(n-1)) 
	
	
#This function computes summation of i(i+1)
def sum_two(n):
#Base Case  
  if n==1:
    return n*(n+1)
#Inductive Case    
  else:
    return n*(n+1) + sum_two(n-1)
#Calls and prints both functions for n and outputs both summations.    
print "The value of the 1st summation is", sum_one(n)
print "The value of the 2nd summation is", sum_two(n)

#This program implements proof by counterexample for Goldbach's conjecture.
from math import *
#Python list(array) of primes to append in while loop.
primes_array = []
n = 3
#Function to check if integer is prime. 
def primeornot(n):
    if n % 2 == 0:
        return False
    else:
        for x in range(3, int(n**1+0.5),2):
            if n % x == 0:
                return False
        return True
		
#Infinite While loop to find counterexample in claim.		
while True:
    if primeornot(n):
        primes_array.append(n)
    else:
	#Claim: Every odd number from 3 onwards can be written as the sum of a prime number and twice a square.
        for x in primes_array:  
            if (sqrt(((n-x)/2))) == int(sqrt(((n-x)/2))):
                break
        else:
            print "\nSmallest counterexample found:",n
            break
    n+=2
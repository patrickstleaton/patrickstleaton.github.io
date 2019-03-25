#This program finds intersections, differences, complements, cartesians, equality, and subsets of two lists.
a_array = []
b_array = []
c_array = []
a_length = int(input("Please enter size of A: "))
b_length = int(input("Please enter size of B: "))
a_total = 0
b_total = 0

def intersection(a, b): 
 c_array = [value for value in a if value in b] 
 return c_array

def difference(a, b):
 c_array = [value for value in b if value not in a]
 return c_array

def complement(a):
 c_array = [value for value in range(1,21) if value not in a]
 return c_array
 
def cartesian(a, b):
    def cartesian(a, b):
        for t1 in a:
            for t2 in b:
                yield t1, t2
                yield t2, t1
    if len(list(cartesian(a,b))) == 0:
      return False
    else:
      return list(cartesian(a, b))
 
def equal(a, b):
 c_array = [value for value in a if value in b]
 if len(c_array) != len(a) and len(b) or len(a) == 0 or len(b) == 0:
  return False
 else:
  return c_array 
  
def subset(a, b):
 if all([c in b for c in a]) == True:
  return True
 else:
  return False
  
for i in range(0,a_length):
 a = raw_input("Please enter an element of A: ") 
 for num in a: 
        if num not in a_array: 
         a_array.append(int(a))
         c_array.append(int(a))
         a_total += 1
 
for i in range(0,b_length):
 b = raw_input("Please enter an element of B: ") 
 for num in b: 
        if num not in b_array: 
         b_array.append(int(b))
         b_total += 1
        for num in b_array: 
         if num not in c_array: 
            c_array.append(num)

if a_total and b_total == 0:
 print "The union of A and B is: empty"
else:
 print "The union of A and B is:", c_array


if sum(intersection(a_array,b_array)) == 0:
 print "The intersection of A and B is: Empty"
else:
 print "The intersection of A and B is:", intersection(a_array, b_array)
 
if sum(difference(a_array,b_array)) == 0:
 print "The difference of B minus A is: Empty"
else:
 print "The difference of B minus A is:", difference(a_array, b_array) 
 
if sum(complement(a_array)) == 0:
 print "The complement of A is: empty"
else:
 print "The complement of A is:", complement(a_array)

if cartesian(a_array,b_array) == False:
 print "The Cartesian product of A and B is: empty"
else:  
 print "The Cartesian product of A and B is:", cartesian(a_array, b_array)  
 
if equal(a_array, b_array) == False and a_total + b_total != 0:
 print "A does not equal B"
else:
 print "A equals B"
 
if subset(a_array, b_array) == False:
 print "A is not a subset of B"
elif sum(a_array) and sum((b_array)) == 0:
 print "A is a subset of B"
else:
 print "A is a subset of B"

if sum(c_array) == 220:
  print "A and B form a partition of U"
else:
  print "A and B do not form a partition of U"
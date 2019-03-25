#This project finds functions, bijections, onto, and one-to-one values between a given list and input list.
y1 = []
x = ["a","b","c"]
n = int(input("Please enter the value of n: "))
#appends value to y1
for i in range (0,n+1):
 y1.append(i)
y = len(range(0,n)) +1
f = (y**len(x))

def combinations():
  row_count = 1
  onetoone = 0
  onto = 0
  bijection = 0
  for a in range (0,len(y1)):
   for b in range (0,len(y1)):
    for c in range (0,len(y1)):
	#prints out all functions
     print "f",row_count,"(a)=",a,"\t","f",row_count,"(b)=",b,"\t","f",row_count,"(c)=",c
     row_count+=1
	 #prints onto, one-to-one, and bijection values.
     if a+b+c>=len(y1)-1:
      onto+=1
     elif a !=b or b !=c:
      onetoone += 1
     elif len(y1) == 3:
      bijection += 3
	  #prints all the values of one-to-one, onto, and bijection values.
  print "There are", row_count-1, "functions total"
  print onto -1, "of them are onto"
  print onetoone, "of them are one-to-one"
  print bijection, "of them are bijections"
  
  #runs function
combinations()

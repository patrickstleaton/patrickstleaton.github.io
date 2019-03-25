#This program utilizes boolean and propositional logic to find the output of three input variables.
p = (str.upper(raw_input("Please enter truth-value of p: ")))
q = (str.upper(raw_input("Please enter truth-value of q: ")))
r = (str.upper(raw_input("Please enter truth-value of r: ")))
#Negation (not)
def neg(p):
  if p == 'T':
     return 'F'
  else:
     return 'T'
#Disjunction (or) 
def dis(p,q):
  if p or q == 'T':
     return 'T'
  else:
     return 'F'
#Conjunction (and)  
def con(p,q):
  if p and q == 'T':
    return 'T'
  else:
    return 'F'
#Implication (proposition)
def imp(p,q):
  if p == 'T' and q == 'F':
    return 'F'
  else:
    return 'T'
ans1 = con(imp(neg(p),q),imp(r,p))
ans2 = con(dis(neg(p),r),dis(q,neg(imp(r,p))))
print "\nTruth-value of statement 1 is:",ans1
print "Truth-value of statement 2 is:",ans2
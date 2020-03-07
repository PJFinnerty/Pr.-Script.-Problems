

q = 653
s = 2
isprime = True 

#while s < q:
for s in range(2, q-1):
    if q % s == 0:
        isprime = False
        break
    s = s + 1

if isprime:
    print(q, "is a prime number.")
else:
    print(q, "is not prime.")


#print(p)
#print(p, "divided by", m, "leaves a remainder of 0")

#if (p % m) == 0:
   # print (p, "divided by", m, "leaves a remainder of 0")
#else:
 #   print(p, "divided by", m, "does not leave a remainder of 0")

#NOW to break down how to do repeat statements



#(p % m) != 0:
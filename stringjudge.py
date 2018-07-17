import operator
L=[1,2,0]
if L==sorted(L) :
    print ("UP")
elif L==sorted(L,reverse=True):
    print("DOWN")
else:
    print("WRONG")

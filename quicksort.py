def quicksort(L,low,high):
    i=low
    j=high
    if i>=j :
        return L
    key = L[i]
    while i<j :
        while i<j and L[j]>=key :
            j-=1
        L[i]=L[j]
        while i<j and L[i]<=key :
            i+=1
        L[j]=L[i]
    L[i]=key
    quicksort(L,low,i-1)
    quicksort(L,j+1,high)
    return L
L=[1,6,5,3,8,7,9,0]
quicksort(L,0,len(L)-1)
print  (L)

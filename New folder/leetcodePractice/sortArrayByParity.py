

def sortArray(A):
    b=[]
    for num in A:
        if(num%2==0):
            b.append(num)
    for num in A:
        if(num%2!=0):
            b.append(num)
            
    return b
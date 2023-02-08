#decreasing space pattern nin
#increasing pattern ni+1
#increasing pattern ni+1

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    
    for j in range(i): #our nested loop knows to print one less coloumn so instead of(i+1)take only(i)
        print("*",end=" ")
    
    for j in range(i+1):
        print("*",end=" ")

    print()    
#add matrices using nested loops

X=[[12,9,3],
  [7,3,4],
  [5,6,2]]


Y=[[1,4,5],
  [2,5,7],
  [0,9,8]]


result=[[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(X)):#first find len(x that is 3 rows and 3 cols)o/p=012
    for j in range(len(X[0])): #nested loop so loop elements in x ,o/p is 012,012,012 three times
        result[i][j]=X[i][j]+Y[i][j] #take result[00000]result[i][j] and add x+y =x[i]+[j]+y[i][j]
                    #takes rows and coloumsn from X and Y matrices and do the sum
for r in result:
    print(r)

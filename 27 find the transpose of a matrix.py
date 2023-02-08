#using nested loop
X=[[12,9],
  [7,3],
  [5,6]]

result=[[0,0,0],
       [0,0,0]]

#transponse making rows coloumns coloumns rows
for i in range(len(X)):#2rows,3 cols
    for j in range(len(X[0])):#result lenght 3rows 2 cols now interchange them
        result[j][i]=X[i][j] #result[j][i]=x[i][j]#rows willbe cols and cols rows
for r in result:
    print(r)


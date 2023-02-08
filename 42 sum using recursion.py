def recursive(data_list):#data[1,2and so on]
    total=0 #initially total is 0
    for x in data_list: #data stores in ele,1
        if type(x)==type([]): # same as sum of nos except this line if we have[3,4],[5,6] then it will go to  def rec(data_list)then checks lement type and again goes to elese block
            total=total+recursive(x)
        else:
            total=total+x#0+1=1+2=3
    return total
print(recursive([1,2,[3,4],[5,6]])) #this data goes to first function
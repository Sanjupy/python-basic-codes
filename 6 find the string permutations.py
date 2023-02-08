#run ,unr,rnu,nru this is called permutations

def get_permuation(string,i=0):#run #the last statement comes here first first iter('run',0)
    if i==len(string): #0==3 in first iter 0==3 false 
        print("".join(string))#this condition satisfies if 3==3
    for j in range(i,len(string)):#(0,3) three times loop (3,3) condition gets stopped 
        words=[c for c in string] #string will convert to list we will get run 3 times same so we need to swap(a,b)=(b,a)[r,u,n]
        
        words[i],words[j]=words[j],words[i]#swaping should be done other wise everytime run run run will come uif we swap then run ,urn,nur will come
        #print(words[i])
        #print(words[j])
        #words[0],words[0]=words[0],words[0]
        #words[1],words[1]=words[1],words[1]#increment
        
        get_permuation(words,i+1)#function will be called and goes to first statement
get_permuation('run') #this condition goes to the first statement





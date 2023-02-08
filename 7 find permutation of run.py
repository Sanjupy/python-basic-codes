def get_permutation(string,i=0):#(run,0) 
    if i==len(string):#if 3=3 then print it
        print("".join(string)) #if 3=3 then it prints and gives output 
    for j in range(i,len(string)):#0,3 
        words=[c for c in string]#in list format
        words[i],words[j]=words[j],words[i]
        get_permutation(words,i+1)#goes to the first statement and increments i value
get_permutation("run")

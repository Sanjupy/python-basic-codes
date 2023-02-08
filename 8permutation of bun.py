#permutation of bun

def get_permutation(string,i=0):
    if i==len(string):#3==3(i value 3 after iterations)==3(bun) then print wille xecute
        print("".join(string))
    for j in range(i,len(string)):#for swapping 
        words=[c for c in string] #letters in list form so we use this
        words[i],words[j]=words[j],words[i] #swapping a,b=b,a
        get_permutation(words,i+1)#for first statement i should increment so i+1
get_permutation("bun")
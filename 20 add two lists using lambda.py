#add two lists using map and lambda

l1=[1,2,3]
l2=[2,3,4]
#output=[3,5,7]
print("original list")
print(l1)
print(l2)
result=map(lambda x,y:x+y,l1,l2)#x,y is l1,l2 :x+y =1+2,2+3,3+4
print("result")
print(list(result))




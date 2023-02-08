def sum(numbers):
    total=0
    for x in numbers:
        total=total+x
    return total

list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
list3=list1+list2
print (sum(list3))


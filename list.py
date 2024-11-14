list1=["Sabu",20,45,"banana"]
list2=[34]
list3=[34,23,17,40]
print("the last element is",list1[-1])
print("the first element is",list1[0])
print("the length of the list is",len(list3))
print(list1[0:3])
add=list1.append("apple")
print("updated list is",list1)
de=list1.remove("banana")
print("updated list is",list1)

sorted=list3.sort()
print("the sorted list is",list3)
reverse=list3.reverse()
print("the reversed list is",list3)
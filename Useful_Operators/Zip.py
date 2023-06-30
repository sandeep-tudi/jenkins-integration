# Here we are going to see how zip is going to pack multiple lists
mylist1 = [1,2,3,5,6,7]
mylist2 = ['a','b','c']
mylist3 = [100,200,300,400,500]
for item in zip(mylist1,mylist2,mylist3):
    print(item)
print(list(zip(mylist1,mylist2)))

for a,b,c in zip(mylist1,mylist3,mylist2):
    print(b)

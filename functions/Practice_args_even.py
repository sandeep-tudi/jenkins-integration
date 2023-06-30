# Print all the even number and push it into a list

def myfunc(*args):
    even_list = []
    for num in args:
        if num % 2 ==0:
            even_list.append(num)
        else:
            pass
    return even_list
nl = myfunc(1,2,3,4,5,6,7,8,9,10,11)
print(nl)
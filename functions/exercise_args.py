def myfunc(*args):
    sum = 0
    for num in args:
        sum = sum+num
    return sum
allsum = myfunc(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(allsum)

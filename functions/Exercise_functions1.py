# print the lesser of 2 numbers if the both the number are even and greater f
# both the numbers are odd
def myfunc (a ,b):
    if a % 2 == 0:
        if b % 2 == 0:
            return min(a,b)
    else:
        return max(a,b)

maxi = myfunc(4,8)
print(maxi)

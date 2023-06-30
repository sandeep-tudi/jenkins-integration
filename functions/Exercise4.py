def makes_twenty(a,b):
    if a + b == 20:
        return True
    elif a ==0 or b ==20:
        return True
    else:
        return False
check = makes_twenty(0,20)
print(check)
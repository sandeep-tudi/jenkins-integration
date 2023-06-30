# Summer of 69
def summer_69(arr):
    count = 0
    for num in range(0,len(arr)):

        if arr[num] in range(6,10):
            # print(arr[num])
            pass
        else:
            count = count + arr[num]

    return count
arr = [2, 1, 6, 9, 11]
nl = summer_69(arr)
print(nl)




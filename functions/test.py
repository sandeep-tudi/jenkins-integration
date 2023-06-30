def three_String(name):

    nstr=''
    # print(len(name))
    for a in range(0,len(name)):
        # print(name[a])
        j = 0
        while j <= 2:
            nstr = nstr+name[a]
            j+=1
    return nstr

rs = three_String('Mississippi')
print(rs)
def paper_doll(name):
    nstr = ''
    # print(len(name))
    for a in range(0, len(name)):
        # print(name[a])
        j = 0
        while j <= 2:
            nstr = nstr + name[a]
            j += 1
    return nstr


rs = paper_doll('Mississippi')
print(rs)


newtext = paper_doll('Hello')
print(newtext)

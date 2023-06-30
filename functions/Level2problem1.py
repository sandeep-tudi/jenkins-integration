def has_33(nums):
    itv = 0
    for a in nums:
        if a == 3:
            if a%3 == 0:
             itv+=1
             if itv ==2:
                return True




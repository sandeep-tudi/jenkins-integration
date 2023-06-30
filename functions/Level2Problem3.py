# BlackJack

def blackjack(a,b,c):
    sum = a+b+c
    if sum <= 21:
        return sum
    for x in (a,b,c):
        if(a or b or c) == 11:
            print('found')

           #adjust_sum = sum-10
            #print(adjust_sum)
            #if adjust_sum <= 21:
            #    return adjust_sum
            #else:
            #     return "burst after adjust Sum"
    #else:
       #return "burst from first if"
result = blackjack(9,9,11)
print(result)


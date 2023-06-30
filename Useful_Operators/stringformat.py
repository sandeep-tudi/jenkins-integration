# print the character and index count using the string format function
index_count=0
word = "abcdh"
for letter in word:
    # print(word[index_count])
    index_count+=1
    print('At indexcount {}, the letter is {}'.format(index_count,letter))
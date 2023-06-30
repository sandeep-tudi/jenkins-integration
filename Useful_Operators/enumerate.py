# In python its common to print string and its index_value. So python has come up with a function called
# enumerate. When using enumerate there is no need to declare the index value.

word = 'abcde'
for index,item in enumerate(word):
    print(index)
    print(item)
    print('\n')

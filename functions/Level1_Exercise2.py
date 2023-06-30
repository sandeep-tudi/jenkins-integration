# Print a string with reverse words

def master_yoda(text):
    new_str = ''
    rev_text =''
    new_str = text.split()
    for words in range(len(new_str)-1,-1,-1):
        rev_text = rev_text+(new_str[words]+" ")
    return rev_text

rev_output = master_yoda('I am home')
print(rev_output)
def old_macdonald(name):
    new_word = ''
    for index_count in range(0,len(name)):
        if index_count == 1 or index_count == 4:
            new_word = new_word+(name[index_count].capitalize())
        else:
            new_word = new_word+name[index_count]

    return new_word

ch_Str = old_macdonald('macdonald')
print(ch_Str)
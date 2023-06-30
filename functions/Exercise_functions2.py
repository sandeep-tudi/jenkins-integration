def animal_checkers(text):
    new_list = []
    new_list = (text.split())
    Fw = (new_list[0][0])
    Sw = (new_list[1][0])

    if(Fw.capitalize()==Sw.capitalize()):
        return True
    else:
        return False

   # return new_list
nl = animal_checkers('Samosa andwitch')
print(nl)

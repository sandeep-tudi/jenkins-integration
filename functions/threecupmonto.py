# this program is used to show the communication between functions


from random import shuffle
def shuffel_list(my_list):
    shuffle(my_list)
    return my_list
# result = shuffel_list(my_list)


def player_guess():
    guess =''

    while guess not in ['0','1','2']:
        guess = input("Pick a number:0,1 or 2\t")

    return int(guess)




def check_guess(mixedup_list, guess):
    if my_list[guess] == 'O':
        print("Correct")
    else:
        print("Wrong Guess!")
        print(mixedup_list)

# Initial List
my_list = ['','O','']

#Shuffel List
mixedup_list = shuffel_list(my_list)
#User guess
guess = player_guess()
# Check Guess
check_guess(mixedup_list,guess)










from random import shuffle 

#Shuffle the list

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# Guess 
def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a cup, 0, 1, or 2: ")

    return int(guess)


# Did the player guess right? 
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong Guess")
        print(mylist)


#Initial List 
mylist = [' ','O',' '] # 1st cup is empty, 2nd cup has a ball, 3rd cup is empty
#Shuffle List 
shuffled_list = shuffle_list(mylist)
#User Guess
guess = player_guess()
#Check Guess
check_guess(shuffled_list,guess)

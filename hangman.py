import random

#
all_words=["tetrahedron","polygon","fashion","computer"]

puzzle=''
s_word=''
lives=3
guess=['a','e','i','o','u']
def pick_word():
    global s_word
    s_word=all_words[random.randint(0,len(all_words)-1)];

def gen_puzzle():
    global puzzle
    puzzle=s_word
    for x in s_word:
        if x not in guess:
            puzzle=puzzle.replace(x,'-')

def check_word():
    global guess
    w=raw_input("Next guess(Lives Remaining): "+ str(lives))
    res=False
    chk=str(w).lower()
    for x in s_word:
        if chk==x:
            res=True
            guess.append(chk)
            gen_puzzle()
    return res

def get_word():
    global lives
    if check_word()==True:
        print "Correct!"
    else:
        lives-=1
        print "BOOO!..That was wrong! Lives remaining: ",str(lives)

def hangman():
    global puzzle
    print puzzle
    print "welcome to the hangman game!"
    pick_word()
    gen_puzzle()
    while lives>-1 and puzzle!=s_word:
        print "puzzle word is-:", puzzle
        get_word()
        if puzzle==s_word:
            print "Congrats!!, you won!"
    if lives<0 and puzzle!=s_word:
        print "you loose!"

hangman()

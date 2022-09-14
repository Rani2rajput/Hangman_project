import random
name=((input("enter your respective name::")))
print("............",name,".............")
print("...........WELLCOME TO THE HANGMAN GAME.........")

def hangman():
    
    list=["rani","sheetal","nikki","hen","chaina","america","landon","indore"]
    word=random.choice(list)
    turn=10
    guessmade=''
    valid_entry=("abcdefghijklmnopqrstuvwxyz")
    
    
    while len(word)>0:
        main_word=""
        for letter in word:
            
            
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        
        if main_word==word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        
            print(main_word)
            print("...**Congrachulation you are the Won**...")
            break
            
            
        print("guess the words",main_word)
        guess=input()
        
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid character")
            guess=input()
        if guess not in word:
            turn=turn-1
            
            if turn==9:
                print("9 turns left!!!!")
                print("------------------")
            if turn==8:
                print("8 turns left!!!!!")
                print("----------------")
                print("         O         ")
            if turn==7:
                print("7 turns left!!!!!")
                print("----------------")
                print("         O         ")
                print("         |         ")
            if turn==6:
                print("6 turns left!!!!!")
                print("-----------------")
                print("         O       ")
                print("         |       ")
                print("        /        ")
            if turn==5:
                print("5 turns left!!!!!")
                print("-----------------")
                print("         O       ")
                print("         |       ")
                print("        / \      ")
            if turn==4:
                print("4 turns left!!!!!")
                print("-----------------")
                print("        \O       ")
                print("         |       ")
                print("        / \      ")
            if turn==3:
                print("3 turns left!!!!!")
                print("-----------------")
                print("        \O/      ")
                print("         |       ")
                print("        / \      ")
            if turn==2:
                print("2 turns left!!!!!")
                print("-----------------")
                print("        \O/ |   ")
                print("         |       ")
                print("        / \      ")
            if turn==1:
                print("1 last turns left!!!!!")
                print("-----------------")
                print("        \O/_|   ")
                print("         |       ")
                print("        / \      ")
            if turn==0:
                print("!!!!!you lose!!!!!!!")
                print(".....This man is die.......")
                print("         O    ")
                print("        /|\      ")
                print("        / \      ")
                
                print("........PLEASE TRY AGAIN........")
                break
hangman()

import random

l=["Rock","Paper","Scissor"]

'''
rock vs paper => paper wins
rock vs scissor => rock wins
paper vs scissor => scissor wins
'''

while True:
    Ccount = 0
    Ucount = 0
    uc = int(input('''
    Game Start......
    1 Yes
    2 No,Exit
    '''))
    if uc == 1:
        for a in range(1,6):
            userinput = int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userinput == 1:
                Uchoice = "Rock"
            elif userinput == 2:
                Uchoice = "Scissor"
            elif userinput == 3:
                Uchoice = "Paper"
            else:
                print("INVALID")
            Cchoice = random.choice(l)

            if Cchoice == Uchoice:
                print("COMPUTER VALUE",Cchoice)
                print("USER VALUE",Uchoice)
                print("Game Draw")
                Ucount = Ucount + 0
                Ccount = Ccount + 0
            elif (Uchoice == "Rock" and Cchoice == "Scissor") or (Uchoice == "Paper" and Cchoice == "Rock") or (Uchoice == "Scissor" and Cchoice == "Paper"):
                print("COMPUTER VALUE", Cchoice)
                print("USER VALUE", Uchoice)
                print("YOU WIN")
                Ucount = Ucount + 1
            else:
                print("COMPUTER VALUE", Cchoice)
                print("USER VALUE", Uchoice)
                print("Computer Win")
                Ccount = Ccount + 1

        if Ucount == Ccount:
            print("SERIES GAME DRAW")
            print("USER SCORE",Ucount)
            print("COMPUTER SCORE",Ccount)
        elif Ucount > Ccount:
            print("YOU WIN")
            print("USER SCORE", Ucount)
            print("COMPUTER SCORE", Ccount)
        else:
            print("COMPUTER WIN")
            print("USER SCORE", Ucount)
            print("COMPUTER SCORE", Ccount)
    else:
        break;

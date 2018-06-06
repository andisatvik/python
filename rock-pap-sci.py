while 1>0:
    ng = input("Do you want to start a new game? (Yes/No): ")

    if ng=="Yes":
        p1 = input("Player 1 make your move: (Rock/Paper/Scissors): ")
        p2 = input("Player 2 make your move: (Rock/Paper/Scissors): ")

        if p1 == "Rock":
            if p2 == "Scissors":
                print("Congrats Player 1")
            else:
                print("Congrats Player 2")
                                                     
        elif p1 == "Scissors":
            if p2 == "Paper":
                print("Congrats Player 1")
            else:
                print("Congrats Player 2")
            
        else:
            if p2 == "Scissors":
                print("Congrats Player 2")
            else:
                print("Congrats Player 1")

    else:
        break

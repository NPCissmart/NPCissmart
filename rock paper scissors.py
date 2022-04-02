import random
while True:
    user_move = input("Enter either rock, paper or scissors: ")
    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)
    print("The computer chose: ", computer_move)
    if user_move==computer_move:
        print("Tie!")
    elif user_move=="rock" and computer_move=="paper":
        print("The computer wins!")
    elif user_move=="paper" and computer_move=="rock":
        print("The player wins!")
    elif user_move=="paper" and computer_move=="scissors":
        print("The computer wins!")
    elif user_move=="scissors" and computer_move=="paper":
        print("The player wins!")
    elif user_move=="rock" and computer_move=="scissors":
        print("The player wins!")
    elif user_move=="scirssors" and computer_move=="rock":
        print("The computer wins!")


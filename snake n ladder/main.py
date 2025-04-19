import random
snakes = {36: 6, 48: 26, 63: 18, 80: 24, 95: 86, 97: 78}
ladders = {2: 38, 4: 14, 8: 30, 48: 76, 50: 67, 71: 93, 80: 99}

def dice():

    return random.randint(1,6)

def snake_ladder(position,roll):
    position+=roll
    if position in snakes:
        print(f"oops Snake at {position}. Move back to {snakes[position]}")
        position=snakes[position]
    elif position in ladders:
        print(f"WOW ladder at {position}. Move up to {ladders[position]}")
        position=ladders[position]
    return position

def starting_game(player_name):
    position=0
    print("You needs to get 6 to start game")
    while position==0:
        if player_name==name:
            input("Press Enter key to roll the dice")
        roll=dice()
        print(f"{player_name} Rolled {roll}")
        if roll==6:
            position=1
            print(f"{player_name} started the game")
        else:
            print(f"{player_name} need to get 6 to started the game")
    return position

def game(name):
    player_pos=starting_game(name)
    com_pos=starting_game("computer")
    while player_pos < 100 and com_pos < 100:
        input("\nPress Enter to roll dice")
        roll=dice()
        print(f"You rolled {roll}")
        currunt_pos=snake_ladder(player_pos,roll)
        if currunt_pos<=100:
            player_pos=currunt_pos
        print(f"You are now at {player_pos} square")
        if player_pos== 100:
            print(f"Congargulations {name}")
            print("you win")
            break
        print("\nComputer's turn")
        roll=dice()
        print(f"Computer rolled {roll}")
        currunt_pos=snake_ladder(com_pos,roll)
        if currunt_pos<=100:
            com_pos=currunt_pos
        print(f"Computer is at {com_pos} square")
        if com_pos==100:
            print(f"Computer wins....{name} You loose..")
            break
name=input("Enter name : ")
game(name)



import random

dungeon = list()

def create_dungeon():
    for x in range(1,6):
        for y in range(1,6):
            dungeon.append((x,y))

def initialize_game():
    person = random.choice(dungeon)
    door = random.choice(dungeon)
    monster = random.choice(dungeon)
    if person == door or door == monster or monster == person:
        initialize_game()

    return (person,door,monster)
        
    

def disp_moves(per,mons):
    print("Find the door, the monster is after you.\nYour current poition in the dungeon is: {}. The monster is at {}".format(per,mons))
    moves = {'up':0,'down':0,'right':0,'left':0}
    x_coor,y_coor = per
    moves['up'] = x_coor-1
    moves['down'] = 5-x_coor
    moves['right'] = 5-y_coor
    moves['left'] = y_coor-1

    move_list = list()
    print("Moves available for you in each direction: ")
    for move in moves:
        if moves[move] != 0:
            move_list.append(move)
            print("{"+str(move)+","+str(moves[move])+"}")
    
    return move_person(per,move_list)

def move_person(person,moves):
    x_coor,y_coor = person
    print("Enter your choice followed by the number of steps(Ex: up,3)")
    inp_move = input("> ").split(",")
    if 'Quit' in inp_move:
        return (person,True)
    else:
        if inp_move[0] in moves:
            if inp_move[0] == 'up':
                person = (x_coor-int(inp_move[1]),y_coor)
            elif inp_move[0] == 'down':
                person = (x_coor+int(inp_move[1]),y_coor)
            elif inp_move[0] == 'left':
                person = (x_coor,y_coor-int(inp_move[1]))
            elif inp_move[0] == 'right':
                person = (x_coor,y_coor+int(inp_move[1]))
        else:
            print("You have entered an invalid input. Please try again by entering valid direction and moves.")
            move_person(person,moves)
    return (person,False)

def start_game():
    GameEnd = False
    create_dungeon()
    if input("This is a dungeon game. You have to escape through the door before the monster gets you."
             "\nEnter 'Play' to continue. You can enter 'Quit' at any point during game to exit. \n> ") == 'Play':
        person,door,monster = initialize_game()
        while GameEnd == False:
            person,GameEnd = disp_moves(person,monster)
            monster = random.choice(dungeon)
            if person == door:
                print("Congratlations!!! You escaped the dungeon alive!")
                GameEnd = True
            elif monster == person:
                print("The monster caugth you. Better luck next time.")
                GameEnd = True
            continue
    print("The game has ended. Hope you had fun!")

start_game()
            

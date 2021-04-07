# game site: https://t.ly/DAxk

def turn_right():
    for i in range(3):
        turn_left()

def jump_hurdle():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()

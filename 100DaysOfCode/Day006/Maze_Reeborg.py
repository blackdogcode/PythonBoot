# game site: https://t.ly/tPTN

def turn_right():
    for i in range(3): turn_left()

def left_is_clear():
    turn_around()
    ret = right_is_clear()
    turn_around()
    return ret

while not at_goal():
    if right_is_clear():
        turn_right()
    elif front_is_clear():
        pass
    else:
        while wall_in_front(): turn_left()
    move()

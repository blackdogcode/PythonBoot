# game site: https://t.ly/tPTN

def turn_around():
    for i in range(2): turn_left()

def turn_right():
    for i in range(3): turn_left()

def left_is_clear():
    turn_around()
    ret = right_is_clear()
    turn_around()
    return ret

while not at_goal():
    if front_is_clear():
        if right_is_clear():
            turn_right()
        move()
        continue
    elif right_is_clear():
        turn_right()
    elif left_is_clear():
        turn_left()
    else:
        while wall_in_front():
            turn_left()
    move()

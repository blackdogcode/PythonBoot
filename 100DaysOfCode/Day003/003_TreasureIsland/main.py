import sys

# ASCII ART: https://ascii.co.uk/art
def print_treasure():
    print(f'*******************************************************************************')
    print(f'          |                   |                  |                     |       ')
    print(f' _________|________________.=""_;=.______________|_____________________|_______')
    print(f'|                   |  ,-"_,=""     `"=.|                  |                   ')
    print(f'|___________________|__"=._o`"-._        `"=.______________|___________________')
    print(f'          |                `"=._o`"=._      _`"=._                     |       ')
    print(f' _________|_____________________:=._o "=._."_.-="`"=.__________________|_______')
    print(f'|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |                   ')
    print(f'|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". `__|___________________')
    print(f'          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |       ')
    print(f' _________|___________| ;`-.o`"=._; ." ` ``."/` . "-._ /_______________|_______')
    print(f'|                   | |o;    `"-.o`"=._``  `` " ,__.--o;   |                   ')
    print(f'|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________')
    print(f'____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____')
    print(f'/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_')
    print(f'____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____')
    print(f'/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_')
    print(f'____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____')
    print(f'/______/______/______/______/______/______/______/______/______/______/[TomekK]')
    print(f'*******************************************************************************')


if __name__ == "__main__":
    print_treasure()
    print(f'Welcome to Treasure Island.\nYour mission is to find the treasure.')

    direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
    if direction != 'left':
        sys.exit('Fall into a hole.\nGame Over.')

    movement = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if movement != 'swim':
        sys.exit('Attacked by trout.\nGame Over.')

    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if door == 'yellow':
        print('You Win!')
    elif door == 'red':
        sys.exit('Burned by fire.\nGame Over.')
    elif door == 'blue':
        sys.exit('Eaten by beasts.\nGame Over.')
    else:
        sys.exit('Game Over.')

"""
File: Steeplechase.py
Name: TODO:jerry
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    pre-condition: karel is on the left side of the wall,facing east
    post-condition: karel is on the right side of the wall
    """
    up()
    cross()
    down()
def cross():
    """
    pre-condition: karel is on the left side of the wall,facing east
    post-condition: karel is on the right side of the wall
    """
    turn_right()
    move()
    turn_right()

def up():
    """
    pre-condition: karel is on the left side of the wall,facing east
    post-condition: karel is on the right side of the wall
    """
    turn_left()
    while not right_is_clear():
        move()




def turn_right():
    turn_left()
    turn_left()
    turn_left()

def down():
    """
    pre-condition: karel is on the left side of the wall,facing east
    post-condition: karel is on the right side of the wall
    """
    while front_is_clear():
        move()


    pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

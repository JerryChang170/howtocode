"""
File: BeeperRow.py
Name:jerry
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *

def main():
    """
    karel will move to the end of the first street in any world
    """

    while front_is_clear():
         if on_beeper():
             move()
         else:
             put_beeper()
             move()
    if not on_beeper():
         put_beeper()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

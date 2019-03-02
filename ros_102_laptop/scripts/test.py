#!/usr/bin/env python

from __future__ import print_function
import sys, select, termios, tty
settings = termios.tcgetattr(sys.stdin)
def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    if key == '\x1b':
        key = sys.stdin.read(2)
        if key == '[A':
            return "up"
        elif key == '[B':
            return "down"
        elif key == '[C':
            return "right"
        elif key == '[D':
            return "left"
        else:
            return "not an arrow key!"
    return key

if __name__=="__main__":
    

    try:
      
        while(1):
            key = getKey()

            if (key == '\x03'):
                break
            print(key)
          

    except Exception as e:
        print(e)

    finally:

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

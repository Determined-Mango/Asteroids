# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this will import everything from constants.py and now I will add f statements to print the width and height
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

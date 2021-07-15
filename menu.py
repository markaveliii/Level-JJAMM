#This file contains methods to display menu, timer and lives of the player all in a Menu class. The display
#is refreshed each time the player hits a key. Lives are lost or won through gameplay. 

import curses, curses.panel
from curses import wrapper
import time

class Menu:
    def __init__(self):                             #holds level start time to calculate time for timer
            self.start_time = round(time.time(),2)

    def reset_timer(self):                              #resets timer for new level
            self.start_time = round(time.time(),2)
            pass

    def display_menu(self, begin_x, playObj):                #Displays menu border, time and lives
            stdscr = curses.initscr()
            curses.start_color()
            curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
            curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_BLACK)
            begin_y = 3
            height = 5
            width = 70
            win = curses.newwin(height, width, begin_y, begin_x+2)
            livesNum = 3;
            lives = "Lives: " + str(livesNum)
            title = "Menu:"
            current_time = round(time.time(), 2)
            time_elapsed = "Time Elapsed: " + str(round((current_time - self.start_time), 2))
            stdscr.refresh()
            for i in range(0, 25):        #printing horizontal border
                    stdscr.addch(begin_y,begin_x+i, "*", curses.color_pair(9)) 
                    stdscr.addch(begin_y+9,begin_x+i, "*", curses.color_pair(9)) 
            for i in range(0, 10):        #printing vertical border
                    stdscr.addch(begin_y+i,begin_x, "*", curses.color_pair(9)) 
                    stdscr.addch(begin_y+i,begin_x+24, "*", curses.color_pair(9)) 
            stdscr.addstr(begin_y+2, begin_x+1, title,curses.color_pair(10))   #printing title, lives, time
            stdscr.addstr(begin_y+3, begin_x+1, lives, curses.color_pair(10))
            stdscr.addstr(begin_y+4, begin_x+1, time_elapsed, curses.color_pair(10))
            stdscr.addstr(begin_y+5, begin_x+1, 'keys: %s' %playObj.key, curses.color_pair(10))
            #TODO: Add if else statements to display win condition
            pass

    def get_time():                      #Helper function to return elapsed time for level
            current_time = round(time.time(), 2)
            return round((current_time - self.start_time), 2)

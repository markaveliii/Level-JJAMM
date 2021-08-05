#This file contains methods to display menu, timer and lives of the player all in a Menu class. The display
#is refreshed each time the player hits a key. Lives are lost or won through gameplay. 

import curses, curses.panel
from curses import wrapper
import time

class Menu:
    def __init__(self):                             #holds level start time to calculate time for timer
            self.start_time = round(time.time(),2)
            self.current_deaths = 0

    def reset_timer(self):                              #resets timer for new level
            self.start_time = round(time.time(),2)
            pass

    def display_menu(self, begin_x, playObj, mapObj):                #Displays menu border, time and lives
            #stdscr = curses.initscr()
            pad = curses.newpad(100,100)
            curses.start_color()
            curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
            curses.init_pair(10, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(11, curses.COLOR_RED, curses.COLOR_BLACK)
            #begin_y = 3
            height = 5
            width = 70
            win = curses.newwin(height, width, begin_y, begin_x+2)
            #change to deaths when player deaths is updated
            deathNum = playObj.deaths;
            deaths = "Deaths: " + str(deathNum)
            title = "Menu:"
            current_time = round(time.time(), 2)
            time_elapsed = "Time Elapsed: " + str(round((current_time - self.start_time), 2))
            #stdscr.refresh()
            for i in range(0, 25):        #printing horizontal border
                    pad.addch(0, i, "*", curses.color_pair(9)) 
                    pad.addch(15, i, "*", curses.color_pair(9)) 
            for i in range(0, 15):        #printing vertical border
                    pad.addch(0 , 0, "*", curses.color_pair(9)) 
                    pad.addch(0 , 24, "*", curses.color_pair(9)) 
            pad.addstr(0+2, begin_x+1, title,curses.color_pair(10))   #printing title, lives, time
            pad.addstr(0+3, begin_x+1, deaths, curses.color_pair(10))
            pad.addstr(0+4, begin_x+1, time_elapsed, curses.color_pair(10))
            pad.addstr(0+5, begin_x+1, 'keys: %s' %playObj.key, curses.color_pair(10))
            pad.addstr(0+7, begin_x+1, "Satchel: ", curses.color_pair(10))
            if playObj.sword == True and playObj.bow == True:
                    if playObj.equipped == 'sword':
                            pad.addstr(0+8, begin_x+1, "***Sword***", curses.color_pair(10))
                            pad.addstr(0+9, begin_x+1, "Bow        ", curses.color_pair(10))
                    else:
                            pad.addstr(0+8, begin_x+1, "Sword      ", curses.color_pair(10))
                            pad.addstr(0+9, begin_x+1, "***Bow***  ", curses.color_pair(10))
            if playObj.bow == True and playObj.sword == False:
                    if playObj.equipped == 'bow':
                            pad.addstr(0+9, begin_x+1, "***Bow***  ", curses.color_pair(10))
                    else:
                            pad.addstr(0+9, begin_x+1, "Bow        ", curses.color_pair(10))
            if playObj.sword == True and playObj.bow == False:
                    if playObj.equipped == 'sword':
                            pad.addstr(0+8, begin_x+1, "***Sword***", curses.color_pair(10))
                    else:
                            pad.addstr(0+8, begin_x+1, "Sword      ", curses.color_pair(10))
            if mapObj.winCond == 'T':
                    pad.addstr(0+11, begin_x+1, "Reach the exit!", curses.color_pair(10))
            if mapObj.winCond == 'E':
                    pad.addstr(0+11, begin_x+1, "Kill all enemies!", curses.color_pair(10))
            if mapObj.winCond == 'K':
                    pad.addstr(0+11, begin_x+1, "Grab the key!", curses.color_pair(10))
            if mapObj.winCond == 'S':
                    pad.addstr(0+11, begin_x+1, "Grab the sword!", curses.color_pair(10))
            if mapObj.winCond == 'B':
                    pad.addstr(0+11, begin_x+1, "Grab the bow!", curses.color_pair(10))
            if self.current_deaths < deathNum:
                    self.current_deaths = deathNum 
                    pad.addstr(0+13, begin_x+1, "XXX You died!!! XXX", curses.color_pair(11))
            else:
                    pad.addstr(0+13, begin_x+1, "                   ", curses.color_pair(11))
            pad.refresh(0, 0, 0, begin_x, 25, mapObj.maxX + 40)
            pass

    def get_time():                      #Helper function to return elapsed time for level
            current_time = round(time.time(), 2)
            return round((current_time - self.start_time), 2)

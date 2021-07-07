#!/usr/bin/python3

import curses, curses.panel
from curses import wrapper
import time

class Menu:
    def __init__(self):
            self.start_time = round(time.time(),2)
    
    def reset_timer(self):
            self.start_time = round(time.time(),2)
            pass

    def display_menu(self, stdscr):
            begin_x = 90;
            begin_y = 7;
            height = 5;
            width = 40;
            livesNum = 3;
            lives = "Lives: " + str(livesNum)
            title = "Menu:"
            current_time = round(time.time(),2)
            time_elapsed = "Time Elapsed: " + str(round((current_time - self.start_time),2))
            stdscr.clear()
            stdscr.refresh()
            for i in range(0, 20):
                    stdscr.addch(begin_y-1,begin_x-1+i, "#") 
                    stdscr.addch(begin_y+19,begin_x-1+i, "#") 
            for i in range(0, 20):
                    stdscr.addch(begin_y-1+i,begin_x-1, "#") 
                    stdscr.addch(begin_y-1+i,begin_x+19, "#") 
            stdscr.addstr(begin_y+5, begin_x+5, title);
            stdscr.addstr(begin_y+6, begin_x+5, lives);
            stdscr.addstr(begin_y+7, begin_x+5, time_elapsed);
            stdscr.refresh();
            k = stdscr.getch()
    
            curses.endwin();
            pass



    def testMenu(self):
        game_menu = Menu() 
        #https://stackoverflow.com/questions/28751080/python-curses-typeerror-when-exiting-wrapper
        stdscr = curses.initscr()
        try: 
                Menu.display_menu(game_menu, stdscr)
                Menu.display_menu(game_menu, stdscr)
                Menu.display_menu(game_menu, stdscr)
                Menu.display_menu(game_menu, stdscr)
                Menu.display_menu(game_menu, stdscr)
                
        except:
                curses.endwin()
                raise
        else:
                curses.endwin()
#wrapper(Menu.display_menu(game_menu, stdscr))
#time.sleep(5)
#wrapper(Menu.display_menu(game_menu, stdscr))
#curses.endwin()

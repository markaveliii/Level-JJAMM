import curses, curses.panel
from curses import wrapper


def menu(stdscr):
	begin_x = 90;
	begin_y = 7;
	height = 5;
	width = 40;
	livesNum = 3;
	lives = "Lives: " + str(livesNum)
	title = "Menu:"
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
	stdscr.refresh();
	k = stdscr.getch()

	curses.endwin();
	return 0;

curses.wrapper(menu)

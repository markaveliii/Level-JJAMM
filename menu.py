import curses, curses.panel
from curses import wrapper


def menu(stdscr):
	begin_x = 80;
	begin_y = 7;
	height = 5;
	width = 40;
	livesNum = 3;
	lives = "Lives: " + str(livesNum)

	title = "Menu!!"
	stdscr.clear()
	stdscr.refresh()
	stdscr.addstr(begin_y, begin_x, title);
	stdscr.addstr(begin_y+1, begin_x, lives);
	stdscr.refresh();
	k = stdscr.getch()

	curses.endwin();
	return 0;

curses.wrapper(menu)

import curses
from random import randint

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)

height, width = stdscr.getmaxyx()

game_window = curses.newwin(height, width, 0, 0)
game_window.keypad(True)
game_window.timeout(50)
game_window.clear()
#pad = curses.newpad(height, width)

center_y = height//2
center_x = width//2

snake = [
	[center_y, center_x],
	[center_y, center_x + 1],
	[center_y, center_x + 2],
	[center_y, center_x + 3],
	[center_y, center_x + 4]
]
# Create food
def create_food():
	return [randint(2, height - 2), randint(2, width - 2)]
food = create_food()

# First move to the left
key = curses.KEY_LEFT

while True:
	game_window.clear()
	
	# Draw food
	game_window.addch(food[0], food[1], ord('O'))
	# Draw snake
	[game_window.addch(y, x, ord('#')) for y,x in snake]

	# Move snake
	new_head = snake[0][:]

	# Listen to input
	next_key = game_window.getch()
	key = next_key if (next_key in [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_RIGHT, curses.KEY_LEFT]) else key
	# key = next_key

	if key == curses.KEY_DOWN:
	    new_head[0] = new_head[0] + 1
	elif key == curses.KEY_UP:
	    new_head[0] = new_head[0] - 1
	elif key == curses.KEY_RIGHT:
	    new_head[1] = new_head[1] + 1
	elif key == curses.KEY_LEFT:
	    new_head[1] = new_head[1] - 1

	# Add new_head to snake
	snake.insert(0, new_head)

	# Check if snake got the food
	if snake[0] == food:
		# Create new food
		food = [randint(2, height - 2), randint(2, width - 2)]
	else:
		snake.pop()

	# Game Over
	if snake[0][0] in [0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:
		curses.endwin()
		quit()


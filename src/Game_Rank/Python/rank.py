





def lose():
	streak = 0


def win():
	streak += 1
	


def update(strr):
	if rank > 0:
		if strr == "W":
			win()
		else:
			lose()


def init():
	rank = 25
	stars = 0
	streak = 0

def game(strr):
	init()
	for s in strr:
		update(s)
		if rank < 0: # Legend
			break
	return rank


def main():
	test1 = "WWW"
	game = game(test1)
	print game




main()
	
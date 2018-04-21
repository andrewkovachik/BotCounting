import os
import sys
import random
import textwrap
import itertools

SIZE_GROUP = 2
COUNT_GOAL = 11
game_tree = None
start = 0
bust = 11
moves = [1, 2, 3]
winners = []

class Bot(object):
    '''Bot object for each person'''
    messages=''
    def __init__(self, name):
        self.name = name

def make_games():
    os.chdir('player')
    players = os.listdir('.')
    matches = list(itertools.combinations(players, SIZE_GROUP)) 
    games = list(list(itertools.permutations(matches[i], SIZE_GROUP))
                 for i in range(len(matches)))
    print(games)
    print('hii')
    return games

def main():
    print('hi')

    games = make_games() 

    print('hiii')
    for g in games:
        print(g)

class State(object):
	"Keep track of game state at each tree node."
	def __init__(self, player=0, count=0, alive=None):
		self.player = player
		self.count = count
		self.alive = alive
	def __repr__(self):
		return repr([self.player, self.count, self.alive])

def next_player(players, current):
	"Get the next player whose turn it is."
	return players[(players.index(current)+1) % len(players)]

def take_turn(turn):
	alive = turn.node.alive
	player = turn.node.player
	next = next_player(alive, player)

	for m in moves:
		# the move would cause a bust
		if turn.node.count + m >= bust:
			new_alive = [p for p in alive if p != player]

			if len(new_alive) == 1:
				# leaf node
				#state = State(next, None, None)
				#new_turn = Tree(state)
				#turn.add_child(new_turn)
				
				# remaining player wins
				winners.append(next)
			else:
				# reset counter and continue playing with fewer players
				state = State(next, start, new_alive)
				new_turn = Tree(state)
				turn.add_child(new_turn)
				take_turn(new_turn)
			
		else:
			# continue playing
			state = State(next, turn.node.count + m, alive)
			new_turn = Tree(state)
			turn.add_child(new_turn)
			take_turn(new_turn)
			

def main(num_players):
	global players, game_tree

	players = range(num_players)

	state = State(players[0], start, players)
	game_tree = Tree(state, None)
	
	take_turn(game_tree)
	
	print len(winners), "games:"
	for p in players:
		print p, "won", winners.count(p)
	#print game_tree
if __name__ == '__main__':
    main()

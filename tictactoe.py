import random
import itertools
import math

class coor:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

magicSquare = [
	[4,9,2],
    [3,5,7],
    [8,1,6]
]

center = [coor(1,1)]
corners = [coor(0,0),coor(0,2),coor(2,0),coor(2,2)]
edges = [coor(0,1),coor(1,2),coor(2,1),coor(1,0)]

compCoor = []
playerCoor = []

def compPlay():

	if(len(compCoor)>=2):
		for combos in list(itertools.combinations(compCoor, 2)):
			chance = 15 - (magicSquare[combos[0].x][combos[0].y] + magicSquare[combos[1].x][combos[1].y])
			for i in range(len(magicSquare)):
				if(chance in magicSquare[i]):
					coordinate = coor(i, magicSquare[i].index(chance))
					if(coordinate in center):
						center.remove(coordinate)
						compCoor.append(coordinate)
						return
					elif(coordinate in corners):
						corners.remove(coordinate)
						compCoor.append(coordinate)
						return
					elif(coordinate in edges):
						edges.remove(coordinate)
						compCoor.append(coordinate)
						return
					else: 
						pass

	if(len(playerCoor)>=2):
		for combos in list(itertools.combinations(playerCoor, 2)):
				chance = 15 - (magicSquare[combos[0].x][combos[0].y] + magicSquare[combos[1].x][combos[1].y])
				for i in range(len(magicSquare)):
					if(chance in magicSquare[i]):
						coordinate = coor(i, magicSquare[i].index(chance))
						if(coordinate in center):
							center.remove(coordinate)
							compCoor.append(coordinate)
							return
						elif(coordinate in corners):
							corners.remove(coordinate)
							compCoor.append(coordinate)
							return
						elif(coordinate in edges):
							edges.remove(coordinate)
							compCoor.append(coordinate)
							return
						else: 
							pass

	if(len(center)>0):
		compCoor.append(center[0])
		center.pop(0)
		return
	elif(len(corners)>0):
		coordinate = random.choice(corners)
		compCoor.append(coordinate)
		corners.remove(coordinate)
		return
	elif(len(edges)>0):
		coordinate = random.choice(edges)
		compCoor.append(coordinate)
		edges.remove(coordinate)
		return
	else:
		return

def playerPlay():	
	number = input("Which square would you like to pick? ")
	number -= 1
	x = int(math.ceil(int(number)/3))
	y = (number % 3) 
	coordinate = coor(x,y)

	if(coordinate in center):
		center.remove(coordinate)
		playerCoor.append(coordinate)
		return
	elif(coordinate in corners):
		corners.remove(coordinate)
		playerCoor.append(coordinate)
		return
	elif(coordinate in edges):
		edges.remove(coordinate)
		playerCoor.append(coordinate)
		return
	else: 
		pass

def check():
	if(len(playerCoor)>=3):
		for combos in list(itertools.combinations(playerCoor, 3)):
			sum = 0
			for combo in combos:
				sum+=magicSquare[combo.x][combo.y]
			if(sum == 15):
				print "WON!!!!!!"
				return True

	if(len(compCoor)>=3):
		for combos in list(itertools.combinations(compCoor, 3)):
			sum = 0
			for combo in combos:
				sum+=magicSquare[combo.x][combo.y]
			if(sum == 15):
				print "LOST!!!!!!"
				return True

	if(len(corners) == 0 and len(center) == 0 and len(edges) == 0):
		print "Tie"
		return True

	return False

def render():
	spaces = [" "," "," "," "," "," "," "," "," "]
	for coordinate in compCoor:
		spaces[3*(coordinate.x)+coordinate.y] = "X"

	for coordinate in playerCoor:
		spaces[3*(coordinate.x)+coordinate.y] = "O"
	print("{0} | {1} | {2}".format(spaces[0],spaces[1],spaces[2]))
	print("---------")
	print("{0} | {1} | {2}".format(spaces[3],spaces[4],spaces[5]))
	print("---------")
	print("{0} | {1} | {2}".format(spaces[6],spaces[7],spaces[8]))

def intro():
	print "Welcome to the game of Computer Tic Tac Toe!!!!"
	print "Use this numbering system when inputing your move. \n"

	spaces = ["1","2","3","4","5","6","7","8","9"]
	print("{0} | {1} | {2}".format(spaces[0],spaces[1],spaces[2]))
	print("---------")
	print("{0} | {1} | {2}".format(spaces[3],spaces[4],spaces[5]))
	print("---------")
	print("{0} | {1} | {2}".format(spaces[6],spaces[7],spaces[8]))
	print "\n\n"

def main():
	intro()
	while True:
		print "Computer move"
		compPlay()
		render()
		if(check()):
			break
		playerPlay()
		print "\nPlayer move"
		render()
		if(check()):
			break

main()

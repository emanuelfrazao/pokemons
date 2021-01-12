import sys

path = sys.stdin.read().rstrip()


class Grid:
	"""
	Representation of Ash's moves in a 2D infinite grid.
	"""

	def __init__(self, path):
		
		# Set the initial position to the origin of the grid
		self.initialPosition = [0,0]

		# Set a correspondence between the moves in the path and the updating instructions for the current position
		self.directions = {
			'N': (1,1),
			'S': (1,-1),
			'E': (0,1),
			'O': (0,-1)
		}

		self.path = path
    
	
	def get_number_of_pokemons(self):
		"""
		Count the number of pokemons Ash catches.
		The algorithm represents the positions seen in the grid as a dictionary, such that:
			each key corresponds to a column that has been passed by;
			each value corresponds to the set of rows of passed positions in the respective column (key).
		Python represents the dictionary and set data structures as hash tables with average O(1) insertion time, hence the algorithm takes on average O(len(path)) time.
		
		The algorithm updates the current position as given by each move by incrementing or decrementing either the column ('E' or 'O', respectively) or the row ('N' or 'S', respectively) number.
			
		Returns: the number of distinct positions passed by, given the path (i.e., the number of caught pokemons)
		
		Example:
		
			Input: 'ENE'
						  -1 0 1 2 3
						   _ _ _ _ _
						3 |_|_|_|_|_|
						2 |_|_|_|_|_|
						1 |_|_|X|X|_|
						0 |_|X|X|_|_|
						
			current = (2,1)
			seenPositions = {'0' : {0}, '1' : {0,1}, '2' : {1}}
			
			Output: 4
		"""
		
		current = self.initialPosition

		seenPositions = {current[0]: {current[1]}}

		for move in self.path:

			# Update current position
			coord, unit = self.directions[move]
			current[coord] += unit
			
			
			# Register current position
			if current[0] not in seenPositions:
				seenPositions[current[0]] = {current[1]}
			else:
				seenPositions[current[0]].add(current[1])
		
		
		return sum([len(s) for s in seenPositions.values()])

	
		
def main():
	
	grid = Grid(path)

	number_of_pokemons = grid.get_number_of_pokemons()

	sys.stdout.write(str(number_of_pokemons))
			
			
if __name__ == "__main__":

	main()
# Create a SIMPLY LINKED LIST
# That ONLY CONTAINS NATURAL NUMBERS (integers greater than zero)
# Which is ALWAYS IN ORDER (lowest to highest)

# I am providing an initializer that may be helpful, but you are welcome to change it if the autograder still works.

# With the following public methods:
#  - insert (given some input, if it is a natural, return the list containing that natural in the correct order)
#  - remove (given some input, returns the list with that element removed)
#      * Challenge problem - what if a natural has been added to the list twice?
#        This case is not tested by the autograder
#  - contains (given some input, returns True if it is in the list, False otherwise)
#  - size (no inputs, returns the number of naturals in the list)
#  - head (no inputs, returns the first natural in the list, which should be the minimum)
#  - tail (no inputs, returns the last natural in the list, which should be the maximum)
# Use "None" to denote a list with elements

class SortedNatList:
	def __repr__(self):
		# Provided
		if self.__next != None:
			return "(" + str(self.__data) + ")->" + self.__next.__repr__()
		else:
			return "(" + str(self.__data) + ")"
	def __str__(self):
		# Provided
		return self.__repr__()
		
	def __init__(self,initarg,initnext = None):
		# Provided
		self.__data = initarg
		self.__next = initnext		
		
	def __isAppropriate(self, arg):
		# TODO????: Optional Helper Function: Check if something is a natural (Ints > 0)
		if type(arg) != type("a"):
			return False
		if len(arg) > 1 or not arg.isalpha():
			return False
		else:
			self.__data = arg
			return True
			
	def insert(self,arg):
		# TODO: Return the list with arg in the correct order (if arg is natural)
		if __isAppropriate(self,arg) == True:
			
		
	def remove(self, arg):
		# TODO: Return the list without arg
		if arg == None:
			return (self)
		if head(arg) == self:
			return tail(arg)
		new_tail = remove(self, tail(arg))
		return cons(head(self), new_tail)
		
	def contains(self, arg):
		# TODO: Return True if arg is in the list, False otherwise
		if arg == None:
			return False
		for i in range(len(self)):
			if self[i] == arg:
				return True
			else:
				return False
				
	def size(self):
		# TODO: Return the number of elements in the list
		return len(self)
	
	def head(self):
		# TODO: Return the first element in the list, which should be the minimum
		return self(True)
		
	def tail(self):
		# TODO: Return the last element of the list, which should be the maximum
		return self(False)
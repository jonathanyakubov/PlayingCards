class PlayingCard (object):
	
	rank_dict= {1: 'Ace', 2 : 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
				6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
				11: 'Jack', 12: 'Queen', 13: 'King'}
	suits_dict= {'d': 'Diamonds', 'c': 'Clubs', 'h': 'Hearts', 's': 'Spades'}
	
	rank_numbers_allowed=[1,2,3,4,5,6,7,8,9,10,11,12,13]
	
	suits_allowed=['d', 'c', 'h', 's']
	
	def __init__(self,rank,suit):
		if rank not in self.rank_numbers_allowed:
				raise ValueError("The rank input is not allowed. Please try again.")
		self.rank=rank
		
		if suit not in self.suits_allowed:
			raise ValueError("The value you've input is not a correct suit.")
		
		self.suit=suit
			
	def get_rank(self):
		return self.rank 
		
	def get_suit(self):
		return self.suit
		
	def bj_value(self):
		if self.rank in [1,2,3,4,5,6,7,8,9]:
			return self.rank
		else:
			return 10
			
	def __repr__(self):
		return (self.rank_dict[self.rank] + " " + "of" + " " + self.suits_dict[self.suit])
		

# c=PlayingCard(12, 'c')
# print(c)
# print(c.bj_value())
# print(c.get_rank())
# print(c.get_suit())



def main():
	print("Testing Card Class")
	instances=int(input("How many cards would you like to see? "))
	import random
	suits_allowed=['d', 'c', 'h', 's']
	for i in range(instances):
		suit=random.randint(0,3)
		rank=random.randint(1,13)
		example=PlayingCard(rank,suits_allowed[suit])
		print(example, example.bj_value())
# 		
# main()
	


		

		
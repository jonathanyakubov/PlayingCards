from random import randrange
from playingcard import PlayingCard
from math import sqrt

suit_size = 13  # Number of cards in a suit.
deck_size = 52  # Number of cards in a deck.
num_cards = 260  # Number of cards to create with random rank & suit values


def make_random_cards():
    """Generate num_cards number of random PlayingCard objects.

    This function will generate num_cards RANDOM playing cards
    using your PlayingCard class. That means you will have to choose a random
    suit and rank for a card num_cards times.

    Printing:
        Nothing

    Positional arguments:
        None

    Returns:
        cards_list -- a list of PlayingCard objects.
    """
    cards_list=[]
    test=PlayingCard(2,'c')
    
    for i in range(num_cards):
    	random_card=PlayingCard(randrange(1,14),test.suits_allowed[randrange(0,4)])
    	cards_list.append(random_card)
    

    return list(cards_list)


def freq_count(cards_list):
    """Count every suit-rank combination.

    Returns a dictionary whose keys are the card suit-rank and value is the
    count.

    Printing:
        Nothing

    Positional arguments:
        cards_list -- A list of PlayingCard objects.

    Returns:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'd', 'c', 'h', 's' representing each card suit.  The value for each key
        is a list containing the number of cards at each rank, using the index
        position to represent the rank. For example, {'s': [0, 3, 4, 2, 5]}
        says that the key 's', for 'spades' has three rank 1's (aces), four
        rank 2's (twos), two rank 3's (threes) and 5 rank 4's (fours).  Index
        position 0 is 0 since no cards have a rank 0, so make note.
    """
    # DO NOT REMOVE BELOW
    if type(cards_list) != list or \
            list(filter(lambda x: type(x) != PlayingCard, cards_list)):
        raise TypeError("cards_list is required to be a list of PlayingCard \
                        objects.")
    # DO NOT REMOVE ABOVE

    card_freqs={}
    card_freqs['d']=[0]*14
    card_freqs['c']=[0]*14
    card_freqs['h']=[0]*14
    card_freqs['s']=[0]*14
    for entry in cards_list:
    	if entry.get_suit() == "d":
    		if entry.get_rank()==1:
    			card_freqs['d'][1]+=1
    		elif entry.get_rank()==2:
    			card_freqs['d'][2]+=1
    		elif entry.get_rank()==3:
    			card_freqs['d'][3]+=1
    		elif entry.get_rank()==4:
    			card_freqs['d'][4]+=1
    		elif entry.get_rank()==5:
    			card_freqs['d'][5]+=1
    		elif entry.get_rank()==6:
    			card_freqs['d'][6]+=1
    		elif entry.get_rank()==7: 
    			card_freqs['d'][7]+=1
    		elif entry.get_rank()==8:
    			card_freqs['d'][8]+=1
    		elif entry.get_rank()==9:
    			card_freqs['d'][9]+=1
    		elif entry.get_rank()==10:
    			card_freqs['d'][10]+=1
    		elif entry.get_rank()==11:
    			card_freqs['d'][11]+=1
    		elif entry.get_rank()==12:
    			card_freqs['d'][12]+=1
    		elif entry.get_rank()==13:
    			card_freqs['d'][13]+=1
    	elif entry.get_suit()=="c":	
    		if entry.get_rank()==1:
    			card_freqs['c'][1]+=1
    		elif entry.get_rank()==2:
    			card_freqs['c'][2]+=1
    		elif entry.get_rank()==3:
    			card_freqs['c'][3]+=1
    		elif entry.get_rank()==4:
    			card_freqs['c'][4]+=1
    		elif entry.get_rank()==5:
    			card_freqs['c'][5]+=1
    		elif entry.get_rank()==6:
    			card_freqs['c'][6]+=1
    		elif entry.get_rank()==7: 
    			card_freqs['c'][7]+=1
    		elif entry.get_rank()==8:
    			card_freqs['c'][8]+=1
    		elif entry.get_rank()==9:
    			card_freqs['c'][9]+=1
    		elif entry.get_rank()==10:
    			card_freqs['c'][10]+=1
    		elif entry.get_rank()==11:
    			card_freqs['c'][11]+=1
    		elif entry.get_rank()==12:
    			card_freqs['c'][12]+=1
    		elif entry.get_rank()==13:
    			card_freqs['c'][13]+=1		
    	elif entry.get_suit()=="s":
    		if entry.get_rank()==1:
    			card_freqs['s'][1]+=1
    		elif entry.get_rank()==2:
    			card_freqs['s'][2]+=1
    		elif entry.get_rank()==3:
    			card_freqs['s'][3]+=1
    		elif entry.get_rank()==4:
    			card_freqs['s'][4]+=1
    		elif entry.get_rank()==5:
    			card_freqs['s'][5]+=1
    		elif entry.get_rank()==6:
    			card_freqs['s'][6]+=1
    		elif entry.get_rank()==7: 
    			card_freqs['s'][7]+=1
    		elif entry.get_rank()==8:
    			card_freqs['s'][8]+=1
    		elif entry.get_rank()==9:
    			card_freqs['s'][9]+=1
    		elif entry.get_rank()==10:
    			card_freqs['s'][10]+=1
    		elif entry.get_rank()==11:
    			card_freqs['s'][11]+=1
    		elif entry.get_rank()==12:
    			card_freqs['s'][12]+=1
    		elif entry.get_rank()==13:
    			card_freqs['s'][13]+=1
    	elif entry.get_suit()=="h":
    		if entry.get_rank()==1:
    			card_freqs['h'][1]+=1
    		elif entry.get_rank()==2:
    			card_freqs['h'][2]+=1
    		elif entry.get_rank()==3:
    			card_freqs['h'][3]+=1
    		elif entry.get_rank()==4:
    			card_freqs['h'][4]+=1
    		elif entry.get_rank()==5:
    			card_freqs['h'][5]+=1
    		elif entry.get_rank()==6:
    			card_freqs['h'][6]+=1
    		elif entry.get_rank()==7: 
    			card_freqs['h'][7]+=1
    		elif entry.get_rank()==8:
    			card_freqs['h'][8]+=1
    		elif entry.get_rank()==9:
    			card_freqs['h'][9]+=1
    		elif entry.get_rank()==10:
    			card_freqs['h'][10]+=1
    		elif entry.get_rank()==11:
    			card_freqs['h'][11]+=1
    		elif entry.get_rank()==12:
    			card_freqs['h'][12]+=1
    		elif entry.get_rank()==13:
    			card_freqs['h'][13]+=1
    return card_freqs


def std_dev(counts):
    """Calculate the standard deviation of a list of numbers.

    Positional arguments:
        counts -- A list of ints representing frequency counts.

    Printing:
        Nothing

    Returns:
        _stdev -- The standard deviation as a single float value.
    """
    # DO NOT REMOVE BELOW
    if type(counts) != list or \
            list(filter(lambda x: type(x) != int, counts)):
        raise TypeError("counts is required to be a list of int values.")
    # DO NOT REMOVE ABOVE
    average=(sum(counts)/len(counts))
    _sum=0
    for i in range(len(counts)):
    	_sum+=((counts[i]-average)**2)
    total=(_sum/(len(counts)-1))
    _stdev=sqrt(total)

    return _stdev


def print_stats(card_freqs):
    """Print the final stats of the PlayingCard objects.

    Positional arguments:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'dchs' representing each card suit. The value for each key is a list of
        numbers where each index position is a card rank, and its value is its
        card frequency.

        You will probably want to call th std_dev function in somewhere in
        here.

    Printing:
        Prints the statistic for each suit to the screen, see assignment page
        for an example output.

    Returns:
        None
    """
    # DO NOT REMOVE BELOW
    if type(card_freqs) != dict or \
            list(filter(lambda x: type(card_freqs[x]) != list, card_freqs)):
        raise TypeError("card_freqs is required to be a list of int values.")
    # DO NOT REMOVE ABOVE
	
    values=card_freqs.values()
    print("Standard deviation for the frequency counts of each rank in suit:")   
    stand=[]
    for value in values:
    	stan_dev=std_dev(value)
    	stand.append(stan_dev)
    	
    	
    print("\tDiamonds:", stand[0], "cards\n",
    	   "\tClubs:", stand[1], "cards\n",
    	   "\tHearts:", stand[2], "cards\n",
    	   "\tSpades:", stand[3], "cards")


def main():
    cards = make_random_cards()
    print(cards)
    suit_counts = freq_count(cards)
    print_stats(suit_counts)

main()

# if __name__ == "__main__":
#     main()
import random 

def distribute_card(deck,players):
    """
    Randomly distributes 5 cards to each player.
    
    Args:
        deck(list): List of cards available. 
        Players(list): List of players names.
    Returns:
	    Dict: Each player’s name and their cards they have
    Side Effects: 
	    Removes the cards that been distributed from the deck
    Raises:
	    ValueError: if there not enough cards to give each player 5 cards
"""

# Checks if theres enough cards - Conditonal branching
    if len(deck)< len(players) * 5:
        raise ValueError("Not enough cards for players")
    
    # Creates empty Dict for players hands
    player_hands={}
    
    # Goes through each player - Iteration 
    for player in players:
        # Creates an empty hand for each player
        hand=[]
        
        # Gives each player 5 cards - Iteration
        for i in range(5):
            # Randomly selects a card
             card= random.choice(deck)
        
            # Adds the card to the players hand
             hand.append(card)
             
             #removes card from the deck - Side effect
             deck.remove(card)
        
        # Stores the players cards
        player_hands[player]= hand
    # returns the Dict - Useful result 
    return player_hands
# Test function 
deck= list(range(1,31))    
players = ["Player 1", "Player 2", "Player 3", "Player 4"]

hands = distribute_card(deck, players)

print(hands)
print("Cards remaining:",len(deck))
    
        
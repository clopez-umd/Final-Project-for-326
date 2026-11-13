# Algorithm 1: Card Distribution (Bethel Hailegebriel)
import random 

def distribute_card(deck,players):
    """
    Randomly distributes 5 cards to each player.
    
    Args:
        deck(list): List of cards available. 
        Players(list): List of players names.
    Returns:
	    Dict: Each players name and their cards they have
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






# Algorithm 2: Steal and Shield System (Christian Lopez)
# Relative parameters
def steal_and_shield(attacking_player, target_player): 
    """
    Determines whether a player can successfully steal a card from another 
    player

    Args: 
        attacking_player (player): The player attempting to steal a card 
        target_player(player): The player being targeted and who may lose a card

    Returns: 
        Boolean: True if the steal is successful, False if it is blocked.

    Side Effects: 
        Removes the steal card from attacking players hand
        If the steal is successful, it transfers a card from the target player 
        to attacking player 
        If the target uses a shield card, it removes the shield card and 
        prevents a steal.
    """
    
    # Sequence of steps -- checks if attacking player has a card to steal
    steal_card = None 
    
    # Iteration
    for card in attacking_player.hand:
        
        # Conditional branching
        if card == "Steal":
            steal_card = card
            break
    
    # If steal card does not exist, stop the function
    if steal_card == None:
        return False
    
    # Useful result --> side effect (changing player hand)
    attacking_player.hand.remove(steal_card) 
    
    # Checks if player has shield
    shield_card = None 
    
    # Iteration
    for card in target_player.hand:
        
        # Conditional branching
        if card == "Shield":
            shield_card = card 
            break
        
        # If shield exists, then remove it and block steal
        # Conditional branching
    if shield_card != None: 
        target_player.hand.remove(shield_card)
        return False
        
        # Checks if target player has cards to steal
    if len(target_player.hand) == 0: 
        return False
        
         # Selects the first card in target players hand
    stolen_card = target_player.hand[0]
        
        # Transfers stolen card between players
        # Side effect (changes both players hands)
    target_player.hand.remove(stolen_card)
    attacking_player.hand.append(stolen_card)
    return True

    # Test function. (A successful steal would look like this:)
    # player 1 = mockplayer (["Steal", 3, 5])
    # player 2 = mockplayer ([7, 9, 2])

    # Resultt - steal_and_shield(player1, player2)
    # Print ("successful steal:", result)
        
        
        
        

# Algorithm 3: Swap System (Fischer Yigzaw)
def swap_cards(player1, player2):
    """
    Swaps one random card between the two players.
    
    Args: 
        player1 (dict): The player using the swap card.
        player2 (dict): The player that is being targeted.
    
    Returns: 
        None: Both players' hands are to be updated directly.
    
    Side Effects: 
        Removes the SWAP card from player1's hand. 
        Replaces one random card between both the players. 
    
    Raises: 
        ValueError: If a player swaps with themsevles, and don't have a
        SWAP card, or either has no cards avaiable to replace. 
    
    Iteration:
        Uses a for loop to check each of the cards in player1's hand for SWAP.
    """
    # Checks if both of the players are the same (Conditional branching)
    if player1 is player2:
        raise ValueError("Players cannot swap with themselves")
    # Checks each cards in player's hand (Iteration)
    swap_card = None
    for card in player1["hand"]:
        if card == "SWAP":
            swap_card = card
            break
    
    # Checks if the swap can happen (Conditional branching)
    if swap_card is None:
        raise ValueError("Player 1 does not have a SWAP card")
    if len(player1["hand"]) < 2 or len(player2["hand"]) == 0:
        raise ValueError("Both players need a card to exchange")
    
    # Removes the used SWAP card (Side effect)
    
    player1["hand"].remove(swap_card)
    
    # Randomly selects one card for each player's hand
    
    card1 = random.choice(player1["hand"])
    card2 = random.choice(player2["hand"])
    
    # Exchanges the cards and updates players' hands (Side effect)
    player1["hand"].remove(card1)
    player2["hand"].remove(card2)
    player1["hand"].append(card2)
    player2["hand"].append(card1)
  
  # Test function 
player1 = {"hand": [3, 5, 8, "SWAP"]}
player2 = {"hand": [2, 6, 9]}

print("Before swap", player1["hand"], player2["hand"])

swap_cards(player1, player2)

print("After swap:", player1["hand"], player2["hand"])
   




# Algorithm 4: Turn Management and Game Ending (Sangeeth Mathew)
def manage_turns(players, current_player, completed_rounds, final_scores):
	"""
	Manages player turns, tracks completed rounds, and determines when the game ends. 

	Args:
		players (list): List of players in the game.
		current_player (str): The player whose turn just finished.
		completed_rounds (int): Number of completed rounds.
		final_scores (dict): Total scores of all players.

	Returns:
		tuple: The next player and updated round count.
			   Returns None if the game ends for the next player.

	Side effects:
		Announces the next player, updates round progress, and announces the winner after 6 rounds.
	"""
	# Checks if there are players - Conditional branching
	if len(players) == 0:
		raise ValueError("There must be at least one player")

	# Finds the current player's position in the list
	current_index = players.index(current_player)

	# Moves to the next player
	next_index = current_index + 1

	# Checks if all players have finished their turns 
	# Conditional branching
	if completed_rounds >=6:

		# Finds the highest score
		highest_score = max(final_scores.values())

		# Creates a list of winners
		winners = []

		# Goes through each player - Iteration
		for player in players:

			# Checks if the player has the highest score
			if final_scores{player} == highest_score:
			    winners.append(player)
		# Announces the winner or a tie - Side effect
		if len(winners) == 1:
			print("Game Over!")
			print("Winner:", winners[0])
			print("Final Score:", highest_score)
		else:
			print("Game Over! It's a tie!")
			print("Winners:", winners)
			print("Final Score:", highest_score)

		# Returns None because the game has ended
		return None, completed_rounds

	# Determines who plays next
	next_player = players[next_index]

	# Announces the next player's turn - Side effect
	print("Next Turn:", next_player)
	print("Completed Rounds:", completed_rounds)

	# Returns updated turn information - Useful result
	return next_player, completed_rounds

# Test function
players = ["Player 1", "Player 2", "Player 3", "Player 4"]

final_scores = {
	"Player 1": 20,
	"Player 2": 30,
	"Player 3": 12,
	"Player 4": 25,
}

# Test 1: Normal turn
current_player = "Player 1"
completed_rounds = 3

current_player, completed_rounds = manage_turns(
	players, current_player, completed_rounds, final_scores
)

# Test 1: Final turn of the game
current_player = "Player 3"
completed_rounds = 5

current_player, completed_rounds = manage_turns(
	players, current_player, completed_rounds, final_scores
)
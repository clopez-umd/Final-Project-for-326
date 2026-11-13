# Algorithm 1: Card Distribution


# Algorithm 2: Steal and Shield System (Christian Lopez)

# Relative parameters
def steal_and_shield(attacking_player, target_player): 
    """
    Determines whether a player can successfully steal a card from another player

    Args: 
        attacking_player (player): The player attempting to steal a card 
        target_player(player): The player being targeted and who may lose a card

    Returns: 
        Boolean: True if the steal is successful, False if it is blocked.

    Side Effects: 
        Removes the steal card from attacking players hand
    If the steal is successful, it transfers a card from the target player to attacking player 
    If the target uses a shield card, it removes the shield card and prevents a steal.
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
        
# Algorithm 3: Swap System


# Algorithm 4: Save and Scoring System


# Algorithm 5: Turn Management and Game Ending


"""
For this assignment, each member of your group will write one (1) function (not a class, not a method)
that implements a significant algorithm that will be needed in your final project. The function should:

--> handle one and only one "concern"

    if you're not familiar with the idea of separation of concerns, see this article, especially the 
    introduction and the section titled "SoC for programming functions"

--> have parameters that make sense for the problem you are solving
--> contain all the building blocks of an algorithm:
        sequence of steps
        conditional branching (for example, if statements)
        iteration

--> produce one or more useful results (return value, side effect, or exception)

--> not be similar to any of the other functions written by your group members

--> actually work if given appropriate arguments

--> you may need to make a small amount of fake data to pass to your function; if the concern your 

you may need to write one or more "mock" functions for your real function to call; a mock function 
takes the arguments a real function would take, but rather than do actual computation, it just returns 
an appropriate predetermined value. Please let us know if you need help writing mock functions to 
support your actual function.
"""
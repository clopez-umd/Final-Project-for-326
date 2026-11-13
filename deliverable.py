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


# Algorithm 4: Turn Management and Game Ending
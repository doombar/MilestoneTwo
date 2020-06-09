from random import randint

class CardDeck():

	cards = ('Ace of Hearts', 'Ace of Diamonds', 'Ace of Spades', 'Ace of Clubs', \
			 'Two of Hearts', 'Two of Diamonds', 'Two of Spades', 'Two of Clubs', \
			 'Three of Hearts', 'Three of Diamonds', 'Three of Spades', 'Three of Clubs', \
			 'Four of Hearts', 'Four of Diamonds', 'Four of Spades', 'Four of Clubs', \
			 'Five of Hearts', 'Five of Diamonds', 'Five of Spades', 'Five of Clubs', \
			 'Six of Hearts', 'Six of Diamonds', 'Six of Spades', 'Six of Clubs', \
			 'Seven of Hearts', 'Seven of Diamonds', 'Seven of Spades', 'Seven of Clubs', \
			 'Eight of Hearts', 'Eight of Diamonds', 'Eight of Spades', 'Eight of Clubs', \
			 'Nine of Hearts', 'Nine of Diamonds', 'Nine of Spades', 'Nine of Clubs', \
			 'Ten of Hearts', 'Ten of Diamonds', 'Ten of Spades', 'Ten of Clubs', \
			 'Jack of Hearts', 'Jack of Diamonds', 'Jack of Spades', 'Jack of Clubs', \
			 'Queen of Hearts', 'Queen of Diamonds', 'Queen of Spades', 'Queen of Clubs', \
			 'King of Hearts', 'King of Diamonds', 'King of Spades', 'King of Clubs')

	card_values = (11,11,11,11, \
					2,2,2,2, \
					3,3,3,3, \
					4,4,4,4, \
					5,5,5,5, \
					6,6,6,6, \
					7,7,7,7, \
					8,8,8,8, \
					9,9,9,9, \
					10,10,10,10, \
					10,10,10,10, \
					10,10,10,10, \
					10,10,10,10)

	def __init__(self):
		self.cards_in_pack = list(range(52))
		self.number_of_cards_remaining = 52
		return

	def deal_card(self):
		# Select a random card from the cards left in the pack
		self.number_of_cards_remaining -= 1
		self.delt_card_index = self.cards_in_pack.pop(randint(0,self.number_of_cards_remaining))

		# Return the Card Name and it's value, as a tuple
		return (CardDeck.cards[self.delt_card_index], CardDeck.card_values[self.delt_card_index])











class Player():

	def __init__(self, player_name, account_value):
		self.hand_value = 0
		self.number_of_high_aces = 0
		self.bet_value = 0
		self.player_name = player_name
		self.cards_in_hand = []
		self.account_value = account_value
		return


	def place_stake(self, bet_value):
		'''
		Method used to enter the amount to be staked on current game
		'''
		if bet_value <= self.account_value:
			self.bet_value = bet_value
			self.account_value -= self.bet_value
			return True
		else:
			self.bet_value = 0
			return False


	def collect_winnings(self):
		self.account_value += 2 * self.bet_value

	def return_stake(self):
		self.account_value += self.bet_value


	def add_card_to_hand (self, new_card):
		 self.new_card_type, self.new_card_value = new_card

		 # Add to cards in hand
		 self.cards_in_hand.append(self.new_card_type) 


		 # If the new card value is 11, the card is an Ace. Hence, increment 
		 # the number_of_high_aces value by 1
		 if self.new_card_value == 11:
		 	self.number_of_high_aces += 1


		 # Add the new card value to the current hand value
		 self.hand_value += self.new_card_value


		 # If the hand_value is greater than 21 then check for any high aces.
		 # If any high aces exist, reduce the hand value by 10 and decrement the 
		 # number_of_high_aces value by 1
		 while self.hand_value > 21 and self.number_of_high_aces > 0:
		 	self.hand_value -= 10
		 	self.number_of_high_aces -= 1

		 if self.hand_value <= 21:
		 	return True
		 else:
		 	return False


	def clear_hands(self):
		self.hand_value = 0
		self.number_of_high_aces = 0
		self.cards_in_hand = []




def display_cards(dealer, player):
	print("\n\nThe Dealers cards are:")
	for hand_index in range(len(dealer.cards_in_hand)):
		if hand_index > 0:
			print(",   ", end = "")
		print(f"{dealer.cards_in_hand[hand_index]}", end="")

	print("\n\nYour cards are:")
	for hand_index in range(len(player.cards_in_hand)):
		if hand_index > 0:
			print(",   ", end = "")
		print(f"{player.cards_in_hand[hand_index]}", end="")

	print("\n\n")



def get_initial_inputs():
	play_game = input("Would you like to play the game (Y or N): ")

	# Any string starting with 'y' or 'Y' will be taken as confirmation to play game
	# Any other input will be taken as confirmation not to play game
	if play_game[0].upper() == 'Y' or play_game.upper() == 'YES':
		# The player wishes to play the game so continue to obtain other inputs

		# Any input will be accepted as the players name
		player_name = input("Please Enter Your Name: ")

		# Obtain the initial fund value (used for placing bets)
		while True:
			try:
				player_funds = float(input("Please Enter Your Total Funds Value: "))
			except:
				print('Invalid entry. Please enter a numeric value')
				continue
			else:
				break

		return (True, player_name, player_funds)
	else:
		return (False, "", 0)




def get_player_stake(player):

	while True:
		try:
			player_stake = float(input(f"\n{player.player_name}, please enter your stake for this game: "))
		except:
			print("!!!! INVALID INPUT !!!!\n")
			print("Please enter a numeric value")
		else:
			if player.place_stake(player_stake):
				# If stake accepted then break out of loop
				break
			else:
				print(f"You have insufficient funds to place a bet of {player_stake}.")
				print(f"Your current fund value is {player.account_value}.")
				print(f"Please try again with stake less than or equal to your Fund value.")
				print("\n")	






if __name__ == '__main__':
	# Display Initial Instructions
	print('\n'*100)
	print('Welcome to the Blackjack Table')
	print('------------------------------')
	print("\nYou will be delt 3 cards, face up. The Dealer will be delt 2 cards, one face up, one face down.")
	print("The idea of the game is that the value of your hand should be as close to 21 as possible, without going over 21.")
	print("Having looked at your initial 3 cards, you can choose to add to them, by drawing another card from the deck,")
	print("or you can stick with what you have. If you go over 21 you have lost and you loose your stake. If you stick on a")
	print("hand with a value of less than 21, the Dealer will then turn over his face down card. If the value of the Dealer's")
	print("hand is less than yours, the Dealer will start to add cards to his hand by drawing from the deck. If the Dealer's")
	print("hand attains a value greater than yours but still not greater than 21, you loose. However, if the Dealer's hand")
	print("exceeds 21, you win and you win back your stake plus a further amount equal to your stake.")
	print("Jacks, Queens and Kings all have a value of 10. Aces will initially have a value of 11 but if a hand exceeds 21,")
	print("Aces will automatically take a value of 1.\n\n")


	play_game, player_name, player_funds = get_initial_inputs()


	if play_game:
		# Create the player and dealer objects from the Player class
		player = Player(player_name, player_funds)
		dealer = Player('Dealer', -1)


	while play_game:

		# Create the card_deck object from the CardDeck class
		card_deck = CardDeck() 

		# Clear Hands from any previous games
		player.clear_hands()
		dealer.clear_hands()


		get_player_stake(player)


		# Deal 2 cards to the player and the 1 visible card to the Dealer
		player_continue = player.add_card_to_hand(card_deck.deal_card())
		player_continue = player.add_card_to_hand(card_deck.deal_card())

		dealer_continue = dealer.add_card_to_hand(card_deck.deal_card())

		
		# Indicate the visible cards to the player
		display_cards(dealer, player)

		

		while player_continue:
			# Ask Player if they would like to be delt another card
			deal_new_card = input(f'{player.player_name} would you like another card (Y or N): ')

			if deal_new_card[0].upper() == 'Y':
				player_continue = player.add_card_to_hand(card_deck.deal_card())
				display_cards(dealer, player)
			else:
				# The player's go is over. If the player is not bust hand over to the dealer
				player_continue = False
				while dealer_continue:
					# Give the Dealer another card and check if the Dealer is bust
					dealer_continue = dealer.add_card_to_hand(card_deck.deal_card())
					display_cards(dealer, player)

					if dealer.hand_value >= player.hand_value:
						dealer_continue = False






		if player.hand_value <= 21 and (player.hand_value > dealer.hand_value or dealer.hand_value > 21):
			print(f"{player.player_name}, you Won")
			player.collect_winnings()
		elif player.hand_value == dealer.hand_value:
			print("The Game is a draw")
			player.return_stake()
		else:
			print(f"{player.player_name}, you Lost")



		print(f"You have {player.account_value} remaining in your account.\n")

		play_again = input("Would you like to play again (Y or N): ")

		if play_again[0].upper() == 'Y':
			play_game = True
		else:
			play_game = False
		




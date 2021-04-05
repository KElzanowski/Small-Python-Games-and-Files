"""A game coded from scratch, where you compare famous Instagram account's follower counts to score points."""

from art import logo, vs
from game_data import data
import random
from replit import clear

def check_answer(guess, a_followers, b_followers):
	"""Takes user guess and account follower amounts and compares them."""
	if b_followers > a_followers:
		"""Returns True if guess is b and False if guess is a."""
		return guess == "b"
	else:
		"""Returns the opposite of above."""
		return guess == "a"

game_play = True
score = 0
account_b = random.choice(data)

def game():
	global game_play
	while game_play:
		global score
		print(logo)
		if score >= 1:
			print(f"You're right! Your score is {score}.")

		"""Makes it so account_b is accessible within the function and while loop. Makes account_a previous account_b after completing a round, and if the accounts are the same, selects a different one."""
		global account_b
		account_a = account_b
		account_b = random.choice(data)
		if account_a == account_b:
			account_b = random.choice(data)

		print("Compare A: " + (account_a['name']) + ", " + (account_a['description']) + ", " + "from " + (account_a['country']) + ".")
		print(vs)
		print("Compare B: " + (account_b['name']) + ", " + (account_b['description']) + ", " + "from " + (account_b['country']) + ".")

		game_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

		a_follower_count = (account_a['follower_count'])
		b_follower_count = (account_b['follower_count'])

		"""New variable for checking whether the function returns True or False."""
		is_correct = check_answer(game_guess, a_follower_count, b_follower_count)

		if is_correct:
			score += 1
			clear()
			game()
		else:
			clear()
			print(logo)
			print(f"Sorry that's wrong. Your score was {score}.")
			game_play = False

game()


from art import logo, vs
from random import choice
from game_data import data

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"

def is_correct(answer, a, b):
    """Returns True or False if answer is correct or not"""
    if a > b:
        return answer == 'a'
    else:
        return answer == 'b'

print(logo)
score = 0
game_over = False
account_b = choice(data)

while not game_over:
    account_a = account_b
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)} ")
    print(vs)
    print(f"Compare B: {format_data(account_b)} ")
    guess = input("Who has more followers? : ").lower()

    print("\n"*20)
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    if is_correct(guess, a_followers, b_followers):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_over = True

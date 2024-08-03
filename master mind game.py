def get_number_input(prompt):
    while True:
        try:
            number = input(prompt)
            if number.isdigit() and len(number) == 4:
                return number
            else:
                print("Invalid input. Please enter a 4-digit number.")
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")

def get_guess_input(prompt):
    while True:
        try:
            guess = input(prompt)
            if guess.isdigit() and len(guess) == 4:
                return guess
            else:
                print("Invalid input. Please enter a 4-digit number.")
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")

def give_hint(secret, guess):
    correct_digits = 0
    correct_positions = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            correct_positions += 1
        elif guess[i] in secret:
            correct_digits += 1
    return correct_positions, correct_digits

def play_round(player_number, secret):
    tries = 0
    while True:
        guess = get_guess_input(f"Player {player_number}, enter your guess: ")
        tries += 1
        if guess == secret:
            print(f"Correct! Player {player_number} guessed the number in {tries} tries.")
            return tries
        correct_positions, correct_digits = give_hint(secret, guess)
        print(f"Hint: {correct_positions} digit(s) in correct position, {correct_digits} correct digit(s) but in wrong position.")

def play_game():
    print("Player 1, set your 4-digit number (Player 2, no peeking!):")
    player1_secret = get_number_input("Player 1: ")
    print("\n" * 50)  # Clear the screen to hide the secret number
    player2_tries = play_round(2, player1_secret)
    
    print("Player 2, set your 4-digit number (Player 1, no peeking!):")
    player2_secret = get_number_input("Player 2: ")
    print("\n" * 50)  # Clear the screen to hide the secret number
    player1_tries = play_round(1, player2_secret)
    
    if player1_tries < player2_tries:
        print(f"Player 1 wins with {player1_tries} tries compared to Player 2's {player2_tries} tries!")
    elif player1_tries > player2_tries:
        print(f"Player 2 wins with {player2_tries} tries compared to Player 1's {player1_tries} tries!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()

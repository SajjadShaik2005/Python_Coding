import random

def play_game():
    options = ("rock", "paper", "scissors")
    running = True

    print("Welcome to Rock Paper Scissors!")
    print("Rules: Best of 3 (First to 2 wins!)")

    while running:
        player_score = 0
        computer_score = 0
        round_count = 1

        while player_score < 2 and computer_score < 2:
            print(f"\n--- Round {round_count} ---")
            print(f"Score - You: {player_score}, Computer: {computer_score}")
            
            player_choice = None
            while player_choice not in options:
                player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
            
            computer_choice = random.choice(options)

            print(f"You chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("You win this round!")
                player_score += 1
            else:
                print("You lose this round!")
                computer_score += 1
            
            round_count += 1

        print("\n" + "="*20)
        if player_score == 2:
            print("CONGRATULATIONS! You won the match!")
        else:
            print("GAME OVER! Computer won the match!")
        print(f"Final Score - You: {player_score}, Computer: {computer_score}")
        print("="*20)

        play_again = input("\nPlay another match? (yes/no): ").lower()
        if play_again == "no":
            running = False

    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()

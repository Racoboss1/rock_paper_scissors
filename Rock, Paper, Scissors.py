import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!", 100
    else:
        return "Computer wins!", 0

def main():
    print("Welcome to Rock, Paper, Scissors!")
    total_prize = 0
    decision = ''
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        result, prize = determine_winner(user_choice, computer_choice)
        total_prize += prize
        print(result)
        print(f"Total Prize: ${total_prize}")
        decision = input("Do you want to keep playing? (yes/no): ").lower()
        while decision not in ['yes', 'no', 'y', 'n']:
            print("Invalid choice. Please enter yes or no.")
            decision = input("Do you want to keep playing? (yes/no): ").lower()

        if decision == 'no':
            print(f"Congratulations! You won a total of ${total_prize}. Goodbye!")
            break

if __name__ == "__main__":
    main()

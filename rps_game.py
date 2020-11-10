# Import random library
import random

# Set global variables for scores
user_score = 0
cpu_score = 0
ties = 0


def rps_options():
    """
    Function to display rock, paper, scissor options
    :return:
    """
    # Print options
    print("Please enter a number")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    print("4) Quit")


def rps_result(user, cpu):
    """
    Function to handle rock, paper, scissors round
    """
    # Print inputs
    print("===============================")
    print("User: {} VS CPU: {}".format(user, cpu))
    print("===============================")
    # Set variables to use
    global ties
    global user_score
    global cpu_score

    # If user and cpu select same input
    if user == cpu:
        # Increase global ties by 1
        ties += 1
    # Else if user equals Rock and cpu equals Scissors
    elif user == "Rock" and cpu == "Scissors":
        # Increase global user_score by 1
        user_score += 1
    # Else if user equals Rock and cpu equals Paper
    elif user == "Rock" and cpu == "Paper":
        # Increase global cpu_score by 1
        cpu_score += 1

    # Else if user equals Paper and cpu equals Rock
    elif user == "Paper" and cpu == "Rock":
        # Increase global user_score by 1
        user_score += 1
    # Else if user equals Paper and cpu equals Scissors
    elif user == "Paper" and cpu == "Scissors":
        # Increase global cpu_score by 1
        cpu_score += 1

    # Else if user equals Scissors and cpu equals Paper
    elif user == "Scissors" and cpu == "Paper":
        # Increase global user_score by 1
        user_score += 1
    # Else if user equals Scissors and cpu equals Rock
    elif user == "Scissors" and cpu == "Rock":
        # Increase global cpu_score by 1
        cpu_score += 1

    # Print current score
    print("Current Score\nPlayer Wins: {} | CPU Wins: {} | Ties: {}\n".format(user_score, cpu_score, ties))


def end_game():
    """
    Function to end game
    """
    # Print end game message
    print("Thank you for playing!")
    print("Final Results\nPlayer Wins: {}\nCPU Wins: {}\nTies: {}".format(user_score, cpu_score, ties))
    input("Press Enter to exit.")


if __name__ == "__main__":
    # Print welcome message
    print("Let's Play Rock, Paper, Scissors!")
    # Set options for cpu
    cpu_options = ["Rock", "Paper", "Scissors"]
    # Set dictionary for player options
    user_options = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    # Determine if player wants to play
    playing = True
    while playing:
        # Get cpu input
        cpu_input = random.choice(cpu_options)
        # Display rock, paper, scissor options
        rps_options()
        # Get users input
        user_input = input("Enter a number from 1 to 4\n")
        # If user_input equals 4
        if user_input == "4":
            # Break while loop
            break
        # Else if user_input in user_options
        elif user_input in user_options:
            # Get value of user_input from user_options
            user_input = user_options[user_input]
            # Determine results of round
            rps_result(user_input, cpu_input)
        # Else display invalid input message
        else:
            print("Invalid input\n")
    # Display end game message and final results
    end_game()

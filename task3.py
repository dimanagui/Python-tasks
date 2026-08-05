import random
number_of_rounds = 0
total_score = 0
round_won = 0
while True:
    secret_number = random.randint(1, 100)
    number_of_rounds += 1
    print("I'm thinking of a number between 1 and 100: ")
    print("You have 6 attempts to guess it")
    won = False
    for attempt in range(6):
        print("Attempt " + str(attempt + 1) + "/6")
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Congratulations! \nyou guessed the number")
            won = True
            round_won += 1
            remaining_guesses = 6 - (attempt + 1)
            point_earned = remaining_guesses + 1
            total_score += point_earned
            print("Guesses remaining = " + str(remaining_guesses))
            print("Points earned = " + str(point_earned))
            print("Current score = " + str(total_score))
            break
        elif guess < secret_number:
            if (secret_number - guess) <= 10:
                print("Higher")
            else:
                print("Too Low")
        elif guess > secret_number:
            if (guess - secret_number) <= 10:
                print("Lower")
            else:
                print("Too High")
    if won == False:
        print("You are out of attempts")
        print("The number is " + str(secret_number))
    play_again = input("Play another round (y/n)").lower()
    if play_again == "n":
        print("Round Played = " + str(number_of_rounds))
        print("Round Won = " + str(round_won))
        print("Final Score = " + str(total_score))
        break





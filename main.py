# N to guest
import random

num = random.randint(1, 100)
print(num)
#User to get input from him/her
keep_trying = True
attempts_made = []
while(keep_trying):
    try:
        user_input = int(input("Introduce a valid number from 1 to 100: "))
        attempts_made.append(user_input)
        if user_input == num:
            print("Correct, you've guessed the right number")
            n_attempts_made_list_message = ""
            for a in attempts_made:
                attempts_made+=f"a "
            print(f"You've guessed {len(attempts_made)} times before guessing the right one!! See: {attempts_made}")
            keep_trying = False
        elif user_input < num:
            print("Too Low! Guess again")
        elif user_input > num:
            print("Too High! Guess again")

    except ValueError:
        print("Invalid numbers, please introduce it again")

#only accept numbers until we get the right number
#provide hints to user too low too high i.e
#show all it's moves at the end of the game, perhaps


import random


def main():
    header()
    random_number = str(generate_random_num(4))
    turns = 0
    while True:
        players_number = str(input('Enter a 4 digit number:'))
        if players_guess_check(players_number):
            print(f'Number must have 4 digits.')
        bulls = evaluate_bulls(players_number, random_number)
        cows = evaluate_cows(players_number, random_number) - bulls
        show_current_state(bulls, cows)
        turns += 1
        if bulls == 4:
            final_result(turns)
            break


def header():
    print(f"Hi there! I've generated a random 4 digit number for you." )
    print(f"Let's play a bulls and cows game.")


def generate_random_num(lenght):
    random_num = ''
    while len(random_num) != lenght:
        random_digit = str(int(random.random()*10))
        if random_digit not in random_num:
            random_num += random_digit
    return random_num


def players_guess_check(guess):
    if len(guess) != 4:
        return True
    else:
        return False

def evaluate_bulls(str1, str2):
    bulls = 0
    indx = 0
    for dig in str1:
        if dig == str2[indx]:
            bulls += 1
        indx += 1
    return bulls


def evaluate_cows(str1, str2):
    cows = 0
    for dig in str1:
        if dig in str2:
            cows += 1
    return cows


def show_current_state(bulls, cows):
    print('{} bulls, {} cows'.format(bulls, cows))


def final_result(turns):
    print("Correct, you've guessed the right number in {} guesses!".format(turns))
    if turns in range(4):
        print("That's amazing!")
    elif turns in range(4,7):
        print("That's not bad, try again!")
    else:
        print("That's not very good, try again!")


main()
import random

def main():
    level = get_level()

    score = game_played(level)

    print(f"Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        random_x = random.randint(0, 9)
        random_y = random.randint(0, 9)
    elif level == 2:
        random_x = random.randint(10, 99)
        random_y = random.randint(10, 99)
    else:
        random_x = random.randint(100, 999)
        random_y = random.randint(100, 999)

    return random_x, random_y

def play_round(random_x, random_y):
    attempts = 1
    while attempts <= 3:
        try:
            answer = int(input(f"{random_x} + {random_y} = "))
            if answer == (random_x + random_y):
               return True
            else:
                attempts += 1
                print("EEE")
        except:
            attempts += 1
            print("EEE")
    print(f"{random_x} + {random_y} = {random_x + random_y}")
    return False

def game_played(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        random_x, random_y = generate_integer(level)
        if play_round(random_x, random_y):
            score += 1
        count_round += 1
    return score
if __name__ == "__main__":
    main()

import random

# Define the pockets on the roulette wheel
pockets = list(range(0, 37))
pockets.append('00')

# Define the colors of the pockets
colors = {
    0: 'green',
    '00': 'green',
    1: 'red',
    2: 'black',
    3: 'red',
    4: 'black',
    5: 'red',
    6: 'black',
    7: 'red',
    8: 'black',
    9: 'red',
    10: 'black',
    11: 'black',
    12: 'red',
    13: 'black',
    14: 'red',
    15: 'black',
    16: 'red',
    17: 'black',
    18: 'red',
    19: 'red',
    20: 'black',
    21: 'red',
    22: 'black',
    23: 'red',
    24: 'black',
    25: 'red',
    26: 'black',
    27: 'red',
    28: 'black',
    29: 'black',
    30: 'red',
    31: 'black',
    32: 'red',
    33: 'black',
    34: 'red',
    35: 'black',
    36: 'red'
}

def spin_wheel():
    return random.choice(pockets)

def play_roulette():
    print("Welcome to Roulette!")
    while True:
        bet = input("\nPlace your bet on a number (0-36) or '00': ")
        if bet.lower() == 'exit':
            break
        
        if bet not in pockets:
            print("Invalid bet! Please enter a valid number or 'exit' to quit.")
            continue
        
        amount = int(input("Enter your bet amount: "))
        
        spin = spin_wheel()
        print(f"\nThe ball landed on {spin} ({colors[spin]}).")
        
        if bet == spin:
            winnings = amount * 35
            print(f"Congratulations! You won {winnings} chips.")
        else:
            print("Sorry, you lost your bet.")
        
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    play_roulette()

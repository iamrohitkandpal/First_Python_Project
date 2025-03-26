import random
import time
from collections import defaultdict

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

SPINS = 10
TOTAL_BET = 0
TOTAL_WINNINGS = 0
START_TIME = time.time()

ROWS = 3
COLS = 3

symbols_value = {
    "A": 6,  # Rarest symbol, highest payout
    "B": 5,   # Uncommon symbol
    "C": 3,   # Common symbol
    "D": 2,   # Most common symbol
    "W": 1,  # Wildcard symbol
    "S": 0,  # Scatter symbol
}

symbols_count = {
    "A": 5,    # Rarest (2-3 instances)
    "B": 6,    # Uncommon (4-5 instances)
    "C": 7,    # Common (6-7 instances)
    "D": 7,    # Most common (8-9 instances)
}

def display_status():
    print(f"Spins: {SPINS} | Total Bet: {TOTAL_BET} | Total Winnings: {TOTAL_WINNINGS} | Time Played: {time.time() - START_TIME}")

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    scatter_count = 0

    for column in columns:
        for symbol in column:
            if symbol == "S":
                scatter_count += 1

    if scatter_count >= 3:
        winnings += scatter_count * bet * 2
        print(f"Scatter bonus! {scatter_count} scatters found!")

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row])
        print()

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount) # Convert the string to an integer as we get default input as string
            if amount > 0:
                break
            else:
                print("Invalid amount. Please enter a valid amount.")
        else:
            print("Invalid amount. Please enter a valid amount.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines) # Convert the string to an integer as we get default input as string
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter number of lines from the given limit.")
        else:
            print("Enter a valid number of lines.")
    return lines

def get_bet():
    while True:
        amount = input(f"How much would you like to bet per line ({MIN_BET}-{MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount) # Convert the string to an integer as we get default input as string
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Please add bet according to the limit.")
        else:
            print("Please enter a valid bet.")
    return amount

def spin(balance):
    global TOTAL_BET, TOTAL_WINNINGS
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"{total_bet}/{balance} You don't have enough balance to place this bet.")
        else:   
            TOTAL_BET += total_bet
            break

    print(f"You are betting ${bet} on {lines} lines. Total Bet = ${total_bet}. Good luck!")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine_spin(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    if winnings == 0:
        print("You lost! Better luck next time.")
    else:
        print(f"You won ${winnings}!")
    if winnings > 0:
        print(f"Winning lines:", *winning_lines)
        TOTAL_WINNINGS += winnings

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance: ${balance}")
        start = input("Pres enter to play, Q to quit & S for stats: ")
        if start.lower() == "s":
            display_status()
            continue
        if start.lower() == "q":
            break
        balance += spin(balance)

    print(f"Your final balance is ${balance}.")


main()
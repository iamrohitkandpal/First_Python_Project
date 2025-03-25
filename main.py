import random
# import 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    for line in range(lines):
        

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

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"{total_bet}/{balance} You don't have enough balance to place this bet.")
        else:   
            break

    print(f"You are betting ${bet} on {lines} lines. Total Bet = ${total_bet}. Good luck!")

    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine_spin(slots)

main()
winning_symbols = ["@", "#", "$", "^"]


def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol in ticket:
            if ticket.count(winning_symbol) == 20:
                print(f"ticket \"{ticket}\" - 10{winning_symbol} Jackpot!")
                return True
    return False


def is_winning_ticket(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for winning_symbol in winning_symbols:
        if winning_symbol * 6 in left_half and winning_symbol * 6 in right_half:
            left_symbols_count = left_half.count(winning_symbol)
            right_symbols_count = right_half.count(winning_symbol)
            match_result = min(left_symbols_count, right_symbols_count)
            print(f"ticket \"{ticket}\" - {match_result}{winning_symbol}")
            return True
    return False


tickets = [el.strip() for el in input().split(", ")]

for ticket in tickets:
    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue
    if is_jackpot(ticket):
        continue

    if is_winning_ticket(ticket):
        continue

    print(f"ticket \"{ticket}\" - no match")
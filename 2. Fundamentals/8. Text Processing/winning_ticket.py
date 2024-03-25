tickets_list = input().split(", ")


def ticket_validator(ticket):
    ticket = ticket.strip()
    if len(ticket) != 20:
        return "invalid ticket"
    valid_symbols = ["@", "#", "$", "^"]
    left_half = ticket[:10]
    right_half = ticket[10:]
    for current_symbol in valid_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            valid_symbol_repetition = current_symbol * uninterrupted_match_length
            if valid_symbol_repetition in left_half and valid_symbol_repetition in right_half:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{current_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{current_symbol}'
    return f'ticket "{ticket}" - no match'


for lottery_ticket in tickets_list:
    print(ticket_validator(lottery_ticket))

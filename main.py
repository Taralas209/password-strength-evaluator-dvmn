import urwid

def is_very_long(password):
    return symbols_count(password) > 12

def has_digits(password):
    return any(symbol.isdigit() for symbol in password)

def has_letters(password):
    return any(symbol.isalpha() for symbol in password)

def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)

def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)

def has_symbols(password):
    return any((not symbol.isdigit() and not symbol.isalpha()) for symbol in password)

def on_ask_change(edit, password):
    score = 0
    checks = [
        is_very_long(password),
        has_digits(password),
        has_letters(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
    ]

    for check in checks:
        if check:
            score += 2
    reply.set_text('Password Rating: {}'.format(score))

if __name__ == '__main__':
    symbols_count = len
    ask = urwid.Edit('Enter password: ',  mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()

import urwid

def is_very_long(password):
    return len(password) > 12

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

def show_score(score_field, password_field, password):
    checking_funcs = [
        is_very_long,
        has_digits,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    score = 0
    for is_checked in checking_funcs:
        score += 2 if is_checked(password) else 0

    score_field.set_text(f'Password Rating: {score}')

def main():
    password_field = urwid.Edit('Enter password: ', mask='*')
    score_field = urwid.Text('Password Rating: ')
    menu = urwid.Pile([password_field, score_field])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password_field, 'change', show_score, user_args=[score_field])
    urwid.MainLoop(menu).run()

if __name__ == "__main__":
    main()

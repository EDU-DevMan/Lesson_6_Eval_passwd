import urwid


RAITING_STEP = 2


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return (
        any(symbol.islower() for symbol in password)
        and any(symbol.isupper() for symbol in password)
    )


def has_symbols(password):
    return (
        not password.isalnum()
        and len(password) > 0
        and not any(password.isspace() for symbol in password)
    )


def on_ask_change(edit, passwd):
    scope = 0

    checking_functions = [
        is_very_long(passwd),
        has_digit(passwd),
        has_letters(passwd),
        has_upper_letters(passwd),
        has_lower_letters(passwd),
        has_symbols(passwd),
    ]

    for verific in checking_functions:
        if verific:
            scope = scope + RAITING_STEP

    reply.set_text("Рейтинг пароля: %s" % scope)


if __name__ == "__main__":
    passwd = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    button_inst = urwid.Button("Exit")
    menu = urwid.Pile([passwd, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(passwd, 'change', on_ask_change)
    urwid.MainLoop(menu).run()

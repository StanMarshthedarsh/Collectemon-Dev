def helloworld():
    print("Hello world!")

def coinflip(flip):
    import random
    import time
    random.seed(time.time())
    time.sleep(1)
    result = random.randrange(0, 2)
    if result == 0:
        print("Heads")
        flip = "Heads"

    elif result == 1:
        print("Tails")
        flip = "Tails"



def move_cursor_up(times):
    print(f"\033[{times}A", end="")

def move_cursor_down(times):
    print(f"\033[{times}B", end="")

def move_cursor_right(times):
    print(f"\033[{times}C", end="")

def move_cursor_left(times):
    print(f"\033[{times}D", end="")

def sanitize(inputstr):  # Credits to owner dustyfresh, Retrieved from https://gist.github.com/dustyfresh/10d4e260499612c055f91f824ebd8a64
    sanitized = inputstr
    badstrings = [
        ';',
        '$',
        '&&',
        '../',
        '<',
        '>',
        '%3C',
        '%3E',
        '\'',
        '--',
        '1,2',
        '\x00',
        '`',
        '(',
        ')',
        'file://',
        'input://',
        '"',
        " "
    ]
    bad = False
    for badstr in badstrings:
        if badstr in sanitized:
            bad = True
            sanitized = sanitized.replace(badstr, '')
    if bad == True:
        print(f"Due to security issues, your input was changed to {sanitized}.")
        return sanitized
    else:
        return sanitized
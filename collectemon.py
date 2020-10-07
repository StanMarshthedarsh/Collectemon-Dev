import random
import time
from cs50 import SQL
import math
from functions import sanitize  # Credits to owner dustyfresh for this function, Retrieved from https://gist.github.com/dustyfresh/10d4e260499612c055f91f824ebd8a64
import getpass
from collections import OrderedDict
from playsound import playsound
import os
import sys

def resource_path(relative_path):  # Thanks to stackoverflow for this :) From https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile, user max, whoever u are, tysm!
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # pylint: disable=no-member
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

e = math.e
counting = 0
db = SQL("sqlite:////Users/JayGo/Desktop/projectfiles/pokémon.db")  # SQL connection must now to a PATH to the file, unlike cs50 IDE
print()
print("Welcome to Collectemon!")
playsound(resource_path("welcome.mp3"))
delete = list()
time.sleep(1)
while True:
    try:
        print()
        print("Press: ")
        print("0 to create new user")
        print("1 to login")
        print("2 to view the Collectemon help booklet (Recommended for first-timers)")
        print("3 to quit")
        print()
        login0 = int(input("Input your number here: "))
        playsound(resource_path("click.mp3"))
    except ValueError:
        print("",end="")
        continue
    if login0 == 0:
        login01 = input("Please enter a username (Only letters and numbers are allowed): ")
        playsound(resource_path("click.mp3"))
        login02 = input("Please enter a password for this username: ")
        playsound(resource_path("click.mp3"))
        login1 = sanitize(login01)
        login2 = sanitize(login02)
        check0 = db.execute("SELECT * FROM users WHERE username = ?", login1)
        if len(check0) != 0:
            print("Sorry, this username is taken, please try again!")
            playsound(resource_path("error.mp3"))
        elif login01 == "users":
            print("Sorry, this username cannot be used!")
            playsound(resource_path("error.mp3"))
        elif login01 == "Pokemon":
            print("Sorry, this username cannot be used!")
            playsound(resource_path("error.mp3"))
        elif login01 == "Pokemon_shiny":
            print("Sorry, this username cannot be used!")
            playsound(resource_path("error.mp3"))
        else:
            db.execute(f"INSERT INTO users (username, password) VALUES ('{login1}', '{login2}') ")
            db.execute(f"CREATE TABLE ? (ID INTEGER PRIMARY KEY AUTOINCREMENT, 'pokemon' char(100), 'shiny' char(100) DEFAULT 'False')", login1)
            print("User successfully registered.")
            playsound(resource_path("found.mp3"))
            print(f"Welcome, {login1}!")
            print("Here's 1000 coins and 10 gems as a welcome gift!")
            db.execute(f"UPDATE users SET Coins = 1000, Gems = 10, Exp = 0, Level = 1 WHERE username = '{login1}'")
            break
    elif login0 == 1:
        login01 = input("Username: ")
        playsound(resource_path("click.mp3"))
        login02 = getpass.getpass("Password (Characters you type are not shown for added security): ")
        playsound(resource_path("click.mp3"))
        login1 = sanitize(login01)
        login2 = sanitize(login02)
        check0 = db.execute(f"SELECT * FROM users WHERE username = ?", login1)
        check1 = db.execute(f"SELECT * FROM users WHERE username = ? and password = ?", login1, login2)
        if len(check0) == 0:
            print("Sorry, username does not exist.")
        elif len(check1) == 0:
            print("Incorrect password.")
            playsound(resource_path("wrongpassword.mp3"))
        else:
            print(f"Welcome, {login1}!")
            break
    elif login0 == 2:
        while True:
            try:
                print()
                print("Type in: ")
                print("0 to view the entire help booklet")
                print("1 to view I. INTRODUCTION")
                print("2 to view II. USER INTERFACE")
                print("3 to view III. ACCOUNT CREATION AND LOGIN")
                print("4 to view IV. CURRENCY, LEVELLING, AND RARITY")
                print("5 to view V. CATCHING POKEMON")
                print("6 to view VI. POKESHOP")
                print("7 to view VII. STATS PAGE")
                print("8 to view VIII. BANK")
                print("9 to view IX. POKEMON MANAGER")
                print("10 to view X. TRADING")
                print("11 to view XI. LEADERBOARDS")
                print("12 to view XII. ACCOUNT DELETION")
                print("13 to view XIII. FAQ (Frequently Asked Quesitons)")
                print("14 to view XIV. LIMITATIONS")
                print("15 to view XV. CREDITS")
                print("16 to exit")
                print()
                helping = int(input("Input your number here: "))
                playsound(resource_path("click.mp3"))
            except ValueError:
                print("",end="")
                continue
            if helping == 0:
                print()
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                for line in helpbooklet:
                    print(line)
            elif helping == 1:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 56 and counters < 71:
                        print(line)
            elif helping == 2:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 75 and counters < 99:
                        print(line)
            elif helping == 3:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 104 and counters < 113:
                        print(line)
            elif helping == 4:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 118 and counters < 150:
                        print(line)
            elif helping == 5:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 155 and counters < 175:
                        print(line)
            elif helping == 6:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 180 and counters < 189:
                        print(line)
            elif helping == 7:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 194 and counters < 207:
                        print(line)
            elif helping == 8:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 212 and counters < 219:
                        print(line)
            elif helping == 9:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 224 and counters < 229:
                        print(line)
            elif helping == 10:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 234 and counters < 240:
                        print(line)
            elif helping == 11:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 245 and counters < 265:
                        print(line)
            elif helping == 12:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 270 and counters < 286:
                        print(line)
            elif helping == 13:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 291 and counters < 341:
                        print(line)
            elif helping == 14:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 346 and counters < 358:
                        print(line)
            elif helping == 15:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 363 and counters < 373:
                        print(line)
            elif helping == 16:
                break

    elif login0 == 3:
        print()
        playsound(resource_path("goodbye.mp3"))
        playsound(resource_path("shutdown.mp3"))
        sys.exit()
    else:
        print("", end="")

while True:
    print("\n",end="")
    try:
        print("Main Menu")
        print()
        print("Press: ")
        print("0 to catch Pokemon")
        print("1 to go to the Pokeshop")
        print("2 to view your stats")
        print("3 to go to the bank")
        print("4 to access your Pokemon Manager")
        print("5 to trade with another player")
        print("6 to access the Collectemon Leaderboards")
        print("7 to view the Collectemon help booklet")
        print("8 to quit")
        print()
        pref = int(input("Input your number here: "))
        playsound(resource_path("click.mp3"))
    except ValueError:
        print("",end="")
        continue
    if pref == 0:
        while True:
            print()
            random.seed(time.time())
            drawstart = input("Press enter to get your Pokéballs: ")
            playsound(resource_path("click.mp3"))
            draw = random.random()
            flip = random.random()
            
            if (draw >= 0.3 and draw <= 0.8) and flip >= 0.4:
                print("You got a(n)...")
                playsound(resource_path("wheel.mp3"))
                print("Pokeball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(1)
                print("POKEBALL!")
                playsound(resource_path("point.mp3"))
                ball = 0

            elif (draw >= 0.3 and draw <= 0.8) and flip < 0.4:
                print("You got a(n)...")
                playsound(resource_path("wheel.mp3"))
                print("Pokeball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                print("3 POKEBALLS!")
                playsound(resource_path("point.mp3"))
                playsound(resource_path("point.mp3"))
                playsound(resource_path("point.mp3"))
                ball = 1

            elif (draw >= 0.125 and draw < 0.3) or (draw > 0.8 and draw <= 0.875) and flip >= 0.4:
                print("You got a(n)...")
                playsound(resource_path("wheel.mp3"))
                print("Pokeball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                print("Great Ball!")
                playsound(resource_path("greatball.mp3"))
                ball = 2



            elif (draw >= 0.125 and draw < 0.3) or (draw > 0.8 and draw <= 0.875) and flip < 0.4:
                print("You got a(n)...")
                playsound(resource_path("wheel.mp3"))
                print("Pokeball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                print("3 GREAT BALLS!")
                playsound(resource_path("greatball.mp3"))
                playsound(resource_path("greatball.mp3"))
                playsound(resource_path("greatball.mp3"))
                ball = 3

            elif (draw >= 0.02 and draw < 0.125) or (draw > 0.875 and draw <= 0.98) and flip >= 0.4:
                print("You got a(n)...")
                playsound(resource_path("wheel.mp3"))
                print("Pokeball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                print("ULTRA BALL!")
                playsound(resource_path("ultraball.mp3"))
                ball = 4

            elif (draw >= 0.02 and draw < 0.125) or (draw > 0.875 and draw <= 0.98) and flip < 0.4:
                print("You got a(n)...")
                playsound(resource_path("wheel.mp3"))
                print("Pokeball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(1)
                print("3 ULTRA BALLS!")
                playsound(resource_path("ultraball.mp3"))
                playsound(resource_path("ultraball.mp3"))
                playsound(resource_path("ultraball.mp3"))
                ball = 5

            else:
                print("You got a(n)...")
                playsound(resource_path("wheel.mp3"))
                print("Pokeball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.3)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(0.6)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(1)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Pokeballs!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Great Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Great Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Ultra Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("3 Ultra Balls!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                \r", end="")
                print("Master Ball!\r", end = "")
                time.sleep(2)
                playsound(resource_path("wheel.mp3"))
                print("                  \r", end="")
                print("Pokeball!\r", end = "")
                time.sleep(3)
                playsound(resource_path("wheel.mp3"))
                print("MASTER BALL!")
                playsound(resource_path("masterball.mp3"))
                ball = 6


            prerarity = random.random()
            shiny = random.random()
            
            if prerarity >= 0.375 and prerarity <= 0.625:
                rarity = 1  #COMMON
            elif (prerarity >= 0.275 and prerarity < 0.375) or (prerarity > 0.625 and prerarity <= 0.725):
                rarity = 2
            elif(prerarity >= 0.200 and prerarity < 0.275) or (prerarity > 0.725 and prerarity <= 0.800):
                rarity = 3
            elif(prerarity >= 0.135 and prerarity < 0.200) or (prerarity > 0.800 and prerarity <= 0.865):
                rarity = 4
            elif(prerarity >= 0.085 and prerarity < 0.135) or (prerarity > 0.865 and prerarity <= 0.915):
                rarity = 5
            elif(prerarity >= 0.050 and prerarity < 0.085) or (prerarity > 0.915 and prerarity <= 0.950):
                rarity = 6
            elif(prerarity >= 0.025 and prerarity < 0.050) or (prerarity > 0.950 and prerarity <= 0.975):
                rarity = 7
            elif(prerarity >= 0.015 and prerarity < 0.025) or (prerarity > 0.975 and prerarity <= 0.985):
                rarity = 8
            elif(prerarity >= 0.005 and prerarity < 0.015) or (prerarity > 0.985 and prerarity <= 0.995):
                rarity = 9
            else:
                rarity = 10  #LEGENDARY

            if rarity == 10:
                print("LEGENDARY Pokemon incoming!")
                playsound(resource_path("legendary.mp3"))

            shiny2 = False
            wild_poke = db.execute(f"SELECT * FROM Pokemon WHERE rarity = '{rarity}' ORDER BY RANDOM() LIMIT 1")
            wildpoke = wild_poke[0]["name"]

            if shiny >= 0.490 and shiny <= 0.510:
                shiny2 = True
                print(f"A wild Shiny {wildpoke} appeared!")
                playsound(resource_path("shiny.mp3"))
            else:
                print(f"A wild {wildpoke} appeared!")

            if ball == 0 or ball == 2 or ball == 4 or ball == 6:
                tries = 1
            elif ball == 1 or ball == 3 or ball == 5:
                tries = 3

            if ball == 0 or ball == 1:
                catch_chance = 0.65 - (rarity / 20)
            elif ball == 2 or ball == 3:
                catch_chance = 0.80 - (rarity / 20)
            elif ball == 4 or ball == 5:
                catch_chance = 0.95 - (rarity / 20)
            elif ball == 6:
                catch_chance = 1.00

            while True:
                catch = input("Press enter to attempt to catch it: ")
                playsound(resource_path("click.mp3"))
                caught = random.random()
                if caught >= (0.5 - (catch_chance / 2)) and caught <= (0.5 + (catch_chance / 2)):
                    time.sleep(1)
                    if shiny2 == True:
                        print(f"Congratulations! {wildpoke} was caught!")
                        playsound(resource_path("caught.mp3"))  # This sound effect was made by Pokémon's owners, credits go to them
                        while True:
                            keep = input(f"Would you like to keep it? Input y for yes or n for no: ")
                            playsound(resource_path("click.mp3"))
                            if keep == 'y':
                                db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("Shiny {wildpoke}")')
                                db.execute(f'UPDATE {login1} SET shiny = "True" WHERE pokemon = "Shiny {wildpoke}"')
                                coins = db.execute(f"SELECT Coins FROM users WHERE username = '{login1}'")
                                coins2 = int(coins[0]["Coins"])
                                exp = db.execute(f"SELECT Exp FROM users WHERE username = '{login1}'")
                                exp2 = int(exp[0]["Exp"])
                                coinsgetpoke = ((25 * (pow(e, (0.5887 *  (rarity - 1))))) / 2.5) + 1000
                                totalcoins = int(coins2 + round(coinsgetpoke))
                                gems = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
                                gems2 = int(gems[0]["Gems"])
                                totalgems = gems2 + 1
                                print()
                                print(f"You got {round(coinsgetpoke) - 1000} coins for catching {wildpoke} successfully, and an additional 1000 coins and 1 gem because it's shiny!")
                                playsound(resource_path("coins.mp3"))
                                if rarity != 10:
                                    expgain = pow(rarity + 1, 2) + 50
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                else:
                                    expgain = 200
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                print()
                                print(f"You now have {totalcoins} coins!")
                                print(f"You now have {totalgems} gems!")
                                print(f"You now have {totalexp} exp!")
                                print()
                                level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                                level1 = int(level0[0]["Level"])
                                levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                                levelupexp1 = round((50 * (pow(level1, 1.35))))
                                if totalexp >= levelupexp1:
                                    level1 = level1 + 1
                                    print(f"Congratulations, you are now at level {level1}!")
                                    playsound(resource_path("levelup.mp3"))  # This sound effect was made by Pokémon's owners, credits go to them
                                    db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                                    extracoins = level1 * 100
                                    extragems = int((level1 + 10) / 10)
                                    print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                                    totalcoins = totalcoins + extracoins
                                    totalgems = totalgems + extragems
                                    print()
                                else:
                                    exptonextlvl = levelupexp1 - totalexp
                                    print(f"{exptonextlvl} more exp needed to level up.")
                                db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                                db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                                db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                                print()
                                break
                            elif keep == 'n':
                                print("Pokemon released!")
                                break
                            else:
                                print("", end="")
                        break
                    else:
                        print(f"Congratulations! {wildpoke} was caught!")
                        playsound(resource_path("caught.mp3"))
                        while True:
                            keep = input(f"Would you like to keep it? Input y for yes or n for no: ")
                            playsound(resource_path("click.mp3"))
                            if keep == 'y':
                                db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{wildpoke}")')
                                coins = db.execute(f"SELECT Coins FROM users WHERE username = '{login1}'")
                                coins2 = int(coins[0]["Coins"])
                                exp = db.execute(f"SELECT Exp FROM users WHERE username = '{login1}'")
                                exp2 = int(exp[0]["Exp"])
                                gems = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
                                gems2 = int(gems[0]["Gems"])
                                coinsgetpoke = (25 * (pow(e, (0.5887 *  (rarity - 1))))) / 2.5
                                totalcoins = int(coins2 + round(coinsgetpoke))
                                print()
                                print(f"You got {round(coinsgetpoke)} coins for catching {wildpoke} successfully!")
                                playsound(resource_path("coins.mp3"))
                                if rarity != 10:
                                    expgain = pow(rarity + 1, 2)
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                else:
                                    expgain = 150
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                print()
                                print(f"You now have {totalcoins} coins!")
                                print(f"You now have {totalexp} exp!")
                                print()
                                db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                                db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                                level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                                level1 = int(level0[0]["Level"])
                                levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                                levelupexp1 = round((50 * (pow(level1, 1.35))))
                                if totalexp >= levelupexp1:
                                    level1 = level1 + 1
                                    print(f"Congratulations, you are now at level {level1}!")
                                    playsound(resource_path("levelup.mp3"))
                                    db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                                    extracoins = level1 * 100
                                    extragems = int((level1 + 10) / 10)
                                    print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                                    totalcoins = totalcoins + extracoins
                                    totalgems = gems2 + extragems
                                    db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                                    db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                                    print()
                                else:
                                    exptonextlvl = levelupexp1 - totalexp
                                    print(f"{exptonextlvl} more exp needed to level up.")
                                    print()
                                break
                            elif keep == 'n':
                                print("Pokemon released!")
                                break
                            else:
                                print("", end="")
                        break
                else:
                    if tries != -1:
                        time.sleep(1)
                        print("Oops, the Pokemon broke free!")
                        playsound(resource_path("oops.mp3"))
                    
                    print(f"You have {tries - 1} pokeball(s) left")
                    tries = tries - 1
                    if tries != 0:
                        continue
                if tries == 0 and shiny2 == True:
                    time.sleep(2)
                    print("Sorry, out of Pokeballs!")
                    playsound(resource_path("outofballs.mp3"))
                    while True:
                        spendgems = input(f"Would you like to spend {rarity + 2} gem(s) to get a Master Ball and catch Shiny {wildpoke}? Input y for yes or n for no: ")
                        playsound(resource_path("click.mp3"))
                        if spendgems == 'n':
                            print(f"The wild Shiny {wildpoke} fled. Better luck next time!")
                            playsound(resource_path("lose.mp3"))
                            break
                        elif spendgems == 'y':
                            gems = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
                            gems2 = int(gems[0]["Gems"])
                            if gems2 - rarity >= 0:
                                newgems = gems2 - (rarity + 2)
                                updategems = db.execute("UPDATE users SET Gems = ? WHERE username = ?", newgems, login1)
                                db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("Shiny {wildpoke}")')
                                db.execute(f'UPDATE {login1} SET shiny = "True" WHERE pokemon = "Shiny {wildpoke}"')
                                coins = db.execute(f"SELECT Coins FROM users WHERE username = '{login1}'")
                                coins2 = int(coins[0]["Coins"])
                                exp = db.execute(f"SELECT Exp FROM users WHERE username = '{login1}'")
                                exp2 = int(exp[0]["Exp"])
                                coinsgetpoke = ((25 * (pow(e, (0.5887 *  (rarity - 1))))) / 2.5) + 1000
                                totalcoins = int(coins2 + round(coinsgetpoke))
                                print()
                                print(f"You got {round(coinsgetpoke) - 1000} coins for catching Shiny {wildpoke} successfully, and an additional 1000 coins and 1 gem because it's shiny!")
                                playsound(resource_path("caught.mp3"))
                                playsound(resource_path("coins.mp3"))
                                if rarity != 10:
                                    expgain = pow(rarity + 1, 2) + 50
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                else:
                                    expgain = 200
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                print()
                                print(f"You now have {totalcoins} coins!")
                                print(f"You now have {totalexp} exp!")
                                print(f"You now have {newgems + 1} gems!")
                                print()
                                db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                                db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                                db.execute("UPDATE users SET Gems = ? WHERE username = ?", newgems + 1, login1)
                                level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                                level1 = int(level0[0]["Level"])
                                levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                                levelupexp1 = round((50 * (pow(level1, 1.35))))
                                if totalexp >= levelupexp1:
                                    level1 = level1 + 1
                                    print(f"Congratulations, you are now at level {level1}!")
                                    playsound(resource_path("levelup.mp3"))
                                    db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                                    extracoins = level1 * 100
                                    extragems = int((level1 + 10) / 10)
                                    print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                                    totalcoins = totalcoins + extracoins
                                    totalgems = newgems + 1 + extragems
                                    db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                                    db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                                    print()
                                    break
                                else:
                                    exptonextlvl = levelupexp1 - totalexp
                                    print(f"{exptonextlvl} more exp needed to level up.")
                                    print()
                                break
                            else:
                                print("Sorry, you don't have enough gems to do that :(")
                                print(f"The wild Shiny {wildpoke} fled. Better luck next time!")
                                playsound(resource_path("lose.mp3"))
                                break
                            break
                        else:
                            print("",end="")
                            continue
                    break
                elif tries == 0 and shiny2 == False:
                    time.sleep(2)
                    print("Sorry, out of Pokeballs!")
                    playsound(resource_path("outofballs.mp3"))
                    while True:
                        spendgems = input(f"Would you like to spend {rarity} gem(s) to get a Master Ball and catch {wildpoke}? Input y for yes or n for no: ")
                        playsound(resource_path("click.mp3"))
                        if spendgems == 'n':
                            print(f"The wild {wildpoke} fled. Better luck next time!")
                            playsound(resource_path("lose.mp3"))
                            break
                        elif spendgems == 'y':
                            gems = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
                            gems2 = int(gems[0]["Gems"])
                            if gems2 - rarity >= 0:
                                newgems = gems2 - rarity
                                updategems = db.execute("UPDATE users SET Gems = ? WHERE username = ?", newgems, login1)
                                db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{wildpoke}")')
                                coins = db.execute(f"SELECT Coins FROM users WHERE username = '{login1}'")
                                coins2 = int(coins[0]["Coins"])
                                exp = db.execute(f"SELECT Exp FROM users WHERE username = '{login1}'")
                                exp2 = int(exp[0]["Exp"])
                                gems = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
                                gems2 = int(gems[0]["Gems"])
                                coinsgetpoke = (25 * (pow(e, (0.5887 *  (rarity - 1))))) / 2.5
                                totalcoins = int(coins2 + round(coinsgetpoke))
                                print()
                                print(f"You got {round(coinsgetpoke)} coins for catching {wildpoke} successfully!")
                                playsound(resource_path("caught.mp3"))
                                playsound(resource_path("coins.mp3"))
                                if rarity != 10:
                                    expgain = pow(rarity + 1, 2)
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                else:
                                    expgain = 150
                                    print(f"You also got {expgain} exp!")
                                    totalexp = exp2 + expgain
                                print()
                                print(f"You now have {totalcoins} coins!")
                                print(f"You now have {totalexp} exp!")
                                print(f"You now have {newgems} gems!")
                                print()
                                db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                                db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                                level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                                level1 = int(level0[0]["Level"])
                                levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                                levelupexp1 = round((50 * (pow(level1, 1.35))))
                                if totalexp >= levelupexp1:
                                    level1 = level1 + 1
                                    print(f"Congratulations, you are now at level {level1}!")
                                    playsound(resource_path("levelup.mp3"))
                                    db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                                    extracoins = level1 * 100
                                    extragems = int((level1 + 10) / 10)
                                    print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                                    totalcoins = totalcoins + extracoins
                                    totalgems = gems2 + extragems
                                    db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                                    db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                                    print()
                                    break
                                else:
                                    exptonextlvl = levelupexp1 - totalexp
                                    print(f"{exptonextlvl} more exp needed to level up.")
                                    print()
                                break
                            else:
                                print("Sorry, you don't have enough gems to do that :(")
                                print(f"The wild {wildpoke} fled. Better luck next time!")
                                playsound(resource_path("lose.mp3"))
                                break
                        else:
                            print("",end="")
                            continue
                        break
                    break
                break
            preference = input("Wanna catch another pokemon? Input y for yes and n for no: ")
            playsound(resource_path("click.mp3"))
            if preference != 'y':
                break

    elif pref == 1:
        print()
        print("Welcome to the Pokeshop!")
        playsound(resource_path("pokeshop.mp3"))  # Pokémon Center theme song, Pokémon creators owe this, credits to them. 
        coins = db.execute(f"SELECT Coins FROM users WHERE username = '{login1}'")
        coins2 = int(coins[0]["Coins"])
        gems = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
        gems2 = int(gems[0]["Gems"])
        exp = db.execute(f"SELECT Exp FROM users WHERE username = '{login1}'")
        exp2 = int(exp[0]["Exp"])
        offers = list()
        costs = list()
        rarities = list()
        bought1 = False
        bought2 = False
        bought3 = False
        bought4 = False
        bought5 = False
        time.sleep(1)
        print(f"You currently have {coins2} coins, {gems2} gems, and {exp2} exp")
        time.sleep(1)
        print("Rarity is on a scale of 1-10, 1 being the most common and 10 being legendary")
        time.sleep(1)
        print("An asterisk beside the pokemon's name means you do not have it yet.")
        time.sleep(1)
        print("Here are today's offers: ")
        print("\n",end="")
        print("   Name                     | Rarity | Price ")
        for counter in range(4):

            prerarity = random.random()
            shiny = random.random()

            if prerarity >= 0.375 and prerarity <= 0.625:
                rarity = 1  #COMMON
            elif (prerarity >= 0.275 and prerarity < 0.375) or (prerarity > 0.625 and prerarity <= 0.725):
                rarity = 2
            elif(prerarity >= 0.200 and prerarity < 0.275) or (prerarity > 0.725 and prerarity <= 0.800):
                rarity = 3
            elif(prerarity >= 0.135 and prerarity < 0.200) or (prerarity > 0.800 and prerarity <= 0.865):
                rarity = 4
            elif(prerarity >= 0.085 and prerarity < 0.135) or (prerarity > 0.865 and prerarity <= 0.915):
                rarity = 5
            elif(prerarity >= 0.050 and prerarity < 0.085) or (prerarity > 0.915 and prerarity <= 0.950):
                rarity = 6
            elif(prerarity >= 0.025 and prerarity < 0.050) or (prerarity > 0.950 and prerarity <= 0.975):
                rarity = 7
            elif(prerarity >= 0.015 and prerarity < 0.025) or (prerarity > 0.975 and prerarity <= 0.985):
                rarity = 8
            elif(prerarity >= 0.005 and prerarity < 0.015) or (prerarity > 0.985 and prerarity <= 0.995):
                rarity = 9
            else:
                rarity = 10  #LEGENDARY


            wild_poke = db.execute(f"SELECT * FROM Pokemon WHERE rarity = '{rarity}' ORDER BY RANDOM() LIMIT 1")
            wildpoke = wild_poke[0]["name"]
            if shiny >= 0.490 and shiny <= 0.510:
                shiny2 = True
                unique = db.execute(f'SELECT pokemon FROM {login1} WHERE pokemon = "Shiny {wildpoke}"')
                if len(unique) != 0:
                    print(f"{counter + 1}. Shiny {wildpoke}",end="")
                    for x in range(19 - len(wildpoke)):
                        print(" ",end="")
                    print("|    ",end="")
                    print(rarity,end="")
                    print("   | ",end="")
                    coinsbuypoke = round((25 * (pow(e, (0.5887 *  (rarity - 1)))))) + 1000
                    print(coinsbuypoke,end="")
                    print(" Coins")
                    offers.append(f"Shiny {wildpoke}")
                    costs.append(coinsbuypoke)
                    rarities.append(rarity)
                    playsound(resource_path("newpoke.mp3"))
                else:
                    print(f"{counter + 1}. Shiny {wildpoke}*",end="")
                    for x in range(18 - len(wildpoke)):
                        print(" ",end="")
                    print("|    ",end="")
                    print(rarity,end="")
                    print("   | ",end="")
                    coinsbuypoke = round((25 * (pow(e, (0.5887 *  (rarity - 1)))))) + 1000
                    print(coinsbuypoke,end="")
                    print(" Coins")
                    offers.append(f"Shiny {wildpoke}")
                    costs.append(coinsbuypoke)
                    rarities.append(rarity)
                    playsound(resource_path("newpoke.mp3"))
            else:
                unique = db.execute(f'SELECT pokemon FROM {login1} WHERE pokemon = "{wildpoke}"')
                if len(unique) != 0:
                    print(f"{counter + 1}. {wildpoke}",end="")
                    for x in range(25 - len(wildpoke)):
                        print(" ",end="")
                    print("|    ",end="")
                    print(rarity,end="")
                    print("   | ",end="")
                    coinsbuypoke = round((25 * (pow(e, (0.5887 *  (rarity - 1))))))
                    print(coinsbuypoke,end="")
                    print(" Coins")
                    offers.append(wildpoke)
                    costs.append(coinsbuypoke)
                    rarities.append(rarity)
                    playsound(resource_path("newpoke.mp3"))
                else:
                    print(f"{counter + 1}. {wildpoke}*",end="")
                    length = len(wildpoke)
                    for x in range(24 - len(wildpoke)):
                        print(" ",end="")
                    print("|    ",end="")
                    print(rarity,end="")
                    print("   | ",end="")
                    coinsbuypoke = round((25 * (pow(e, (0.5887 *  (rarity - 1))))))
                    print(coinsbuypoke,end="")
                    print(" Coins")
                    offers.append(wildpoke)
                    costs.append(coinsbuypoke)
                    rarities.append(rarity)
                    playsound(resource_path("newpoke.mp3"))

        print("\n",end="")
        prelegend = db.execute(f"SELECT * FROM Pokemon WHERE rarity = 10 ORDER BY RANDOM() LIMIT 1")
        legend = prelegend[0]["name"]
        legendcost = 25
        unique2 = db.execute(f'SELECT pokemon FROM {login1} WHERE pokemon = "{legend}"')
        if len(unique2) != 0:
            print(f"Legendary Offer: ",end="")
            playsound(resource_path("legendaryoffer.mp3"))
            print(legend,end="")
            print("  |  ",end="")
            print("10",end="")
            print("  |  ",end="")
            print("25 Gems")
            playsound(resource_path("newpoke.mp3"))
        else:
            print(f"Legendary Offer: ",end="")
            playsound(resource_path("legendaryoffer.mp3"))
            print(legend,end="")
            print("*",end="")
            print("  |  ",end="")
            print("10",end="")
            print("  |  ",end="")
            print("25 Gems")
            playsound(resource_path("newpoke.mp3"))

        while True:
            try:
                print("\n",end="")
                print("Press: ")
                print("1 to buy the 1st pokemon in the list")
                print("2 to buy the 2nd")
                print("3 to buy the 3rd")
                print("4 to buy the 4th")
                print("5 to buy the special Legendary Offer")
                print("6 to exit the shop")
                print()
                pick = int(input("Input your number here: "))
                playsound(resource_path("click.mp3"))
            except ValueError:
                print("",end="")
                continue
            if pick == 1 and bought1 == False:
                checkmoney = coins2 - costs[0]
                if checkmoney >= 0:
                    confirm = input(f"Are you sure you want to buy {offers[0]} for {costs[0]} coins? Input y to confirm your decision or n otherwise: ")
                    playsound(resource_path("click.mp3"))
                    if confirm == 'y':
                        playsound(resource_path("buy.mp3"))
                        db.execute(f"UPDATE users SET Coins = {checkmoney} WHERE username = '{login1}'")
                        db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{offers[0]}")')
                        string0 = str(offers[0])
                        print(f"Thanks for buying {offers[0]}! You now have {checkmoney} coins left.")
                        print()
                        if "Shiny" in string0:
                            shining = True
                            db.execute(f"UPDATE {login1} SET shiny = 'True' WHERE pokemon = '{offers[0]}'")
                        else:
                            shining = False
                        if rarity != 10 and shining == True:
                            preexpgain = pow(int(rarities[0]) + 1, 2)
                            expgain = round(preexpgain / 2) + 25
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity != 10 and shining == False:
                            preexpgain = pow(int(rarities[0]) + 1, 2)
                            expgain = round(preexpgain / 2)
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity == 10 and shining == True:
                            expgain = 100
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        else:
                            expgain = 75
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        print(f"You now have {totalexp} exp!")
                        db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                        level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                        level1 = int(level0[0]["Level"])
                        levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                        levelupexp1 = round((50 * (pow(level1, 1.35))))
                        if totalexp >= levelupexp1:
                            level1 = level1 + 1
                            print(f"Congratulations, you are now at level {level1}!")
                            playsound(resource_path("levelup.mp3"))
                            db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                            extracoins = level1 * 100
                            extragems = int((level1 + 10) / 10)
                            print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                            totalcoins = checkmoney + extracoins
                            totalgems = gems2 + extragems
                            db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                            db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                        else:
                            exptonextlvl = levelupexp1 - totalexp
                            print(f"{exptonextlvl} more exp needed to level up.")
                            extracoins = 0
                        bought1 = True
                        coins2 = checkmoney + extracoins
                else:
                    print(f"Sorry, but you don't have enough coins to buy {offers[0]} :( Why don't you catch some more pokemon to earn more coins?")
                    playsound(resource_path("lose.mp3"))
            elif pick == 1 and bought1 == True:
                print("Sorry, you already bought this pokemon.")

            elif pick == 2 and bought2 == False:
                checkmoney = coins2 - costs[1]
                if checkmoney >= 0:
                    confirm = input(f"Are you sure you want to buy {offers[1]} for {costs[1]} coins? Input y to confirm your decision or n otherwise: ")
                    playsound(resource_path("click.mp3"))
                    if confirm == 'y':
                        playsound(resource_path("buy.mp3"))
                        db.execute(f"UPDATE users SET Coins = {checkmoney} WHERE username = '{login1}'")
                        db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{offers[1]}")')
                        string1 = str(offers[1])
                        print(f"Thanks for buying {offers[1]}! You now have {checkmoney} coins left.")
                        print()
                        if "Shiny" in string1:
                            shining = True
                            db.execute(f"UPDATE {login1} SET shiny = 'True' WHERE pokemon = '{offers[1]}'")
                        else:
                            shining = False
                        if rarity != 10 and shining == True:
                            preexpgain = pow(int(rarities[1]) + 1, 2)
                            expgain = round(preexpgain / 2) + 25
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity != 10 and shining == False:
                            preexpgain = pow(int(rarities[1]) + 1, 2)
                            expgain = round(preexpgain / 2)
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity == 10 and shining == True:
                            expgain = 100
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        else:
                            expgain = 75
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        print(f"You now have {totalexp} exp!")
                        db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                        level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                        level1 = int(level0[0]["Level"])
                        levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                        levelupexp1 = round((50 * (pow(level1, 1.35))))
                        if totalexp >= levelupexp1:
                            level1 = level1 + 1
                            print(f"Congratulations, you are now at level {level1}!")
                            playsound(resource_path("levelup.mp3"))
                            db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                            extracoins = level1 * 100
                            extragems = int((level1 + 10) / 10)
                            print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                            totalcoins = checkmoney + extracoins
                            totalgems = gems2 + extragems
                            db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                            db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                        else:
                            exptonextlvl = levelupexp1 - totalexp
                            print(f"{exptonextlvl} more exp needed to level up.")
                            extracoins = 0
                        bought2 = True
                        coins2 = checkmoney + extracoins
                else:
                    print(f"Sorry, but you don't have enough coins to buy {offers[1]} :( Why don't you catch some more pokemon to earn more coins?")
                    playsound(resource_path("lose.mp3"))

            elif pick == 2 and bought2 == True:
                print("Sorry, you already bought this pokemon.")

            elif pick == 3 and bought3 == False:
                checkmoney = coins2 - costs[2]
                if checkmoney >= 0:
                    confirm = input(f"Are you sure you want to buy {offers[2]} for {costs[2]} coins? Input y to confirm your decision or n otherwise: ")
                    playsound(resource_path("click.mp3"))
                    if confirm == 'y':
                        playsound(resource_path("buy.mp3"))
                        db.execute(f"UPDATE users SET Coins = {checkmoney} WHERE username = '{login1}'")
                        db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{offers[2]}")')
                        string2 = str(offers[2])
                        print(f"Thanks for buying {offers[2]}! You now have {checkmoney} coins left.")
                        print()
                        if "Shiny" in string2:
                            shining = True
                            db.execute(f"UPDATE {login1} SET shiny = 'True' WHERE pokemon = '{offers[2]}'")
                        else:
                            shining = False
                        if rarity != 10 and shining == True:
                            preexpgain = pow(int(rarities[2]) + 1, 2)
                            expgain = round(preexpgain / 2) + 25
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity != 10 and shining == False:
                            preexpgain = pow(int(rarities[2]) + 1, 2)
                            expgain = round(preexpgain / 2)
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity == 10 and shining == True:
                            expgain = 100
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        else:
                            expgain = 75
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        print(f"You now have {totalexp} exp!")
                        db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                        level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                        level1 = int(level0[0]["Level"])
                        levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                        levelupexp1 = round((50 * (pow(level1, 1.35))))
                        if totalexp >= levelupexp1:
                            level1 = level1 + 1
                            print(f"Congratulations, you are now at level {level1}!")
                            playsound(resource_path("levelup.mp3"))
                            db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                            extracoins = level1 * 100
                            extragems = int((level1 + 10) / 10)
                            print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                            totalcoins = checkmoney + extracoins
                            totalgems = gems2 + extragems
                            db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                            db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                        else:
                            exptonextlvl = levelupexp1 - totalexp
                            print(f"{exptonextlvl} more exp needed to level up.")
                            extracoins = 0
                        bought3 = True
                        coins2 = checkmoney + extracoins
                else:
                    print(f"Sorry, but you don't have enough coins to buy {offers[2]} :( Why don't you catch some more pokemon to earn more coins?")
                    playsound(resource_path("lose.mp3"))

            elif pick == 3 and bought3 == True:
                print("Sorry, you already bought this pokemon.")

            elif pick == 4 and bought4 == False:
                checkmoney = coins2 - costs[3]
                if checkmoney >= 0:
                    confirm = input(f"Are you sure you want to buy {offers[3]} for {costs[3]} coins? Input y to confirm your decision or n otherwise: ")
                    playsound(resource_path("click.mp3"))
                    if confirm == 'y':
                        playsound(resource_path("buy.mp3"))
                        db.execute(f"UPDATE users SET Coins = {checkmoney} WHERE username = '{login1}'")
                        db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{offers[3]}")')
                        string3 = str(offers[3])
                        print(f"Thanks for buying {offers[3]}! You now have {checkmoney} coins left.")
                        print()
                        if "Shiny" in string3:
                            shining = True
                            db.execute(f"UPDATE {login1} SET shiny = 'True' WHERE pokemon = '{offers[3]}'")
                        else:
                            shining = False
                        if rarity != 10 and shining == True:
                            preexpgain = pow(int(rarities[3]) + 1, 2)
                            expgain = round(preexpgain / 2) + 25
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity != 10 and shining == False:
                            preexpgain = pow(int(rarities[3]) + 1, 2)
                            expgain = round(preexpgain / 2)
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        elif rarity == 10 and shining == True:
                            expgain = 100
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        else:
                            expgain = 75
                            print(f"You also got {expgain} exp!")
                            totalexp = exp2 + expgain
                            exp2 = totalexp
                        print(f"You now have {totalexp} exp!")
                        db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                        level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                        level1 = int(level0[0]["Level"])
                        levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                        levelupexp1 = round((50 * (pow(level1, 1.35))))
                        if totalexp >= levelupexp1:
                            level1 = level1 + 1
                            print(f"Congratulations, you are now at level {level1}!")
                            playsound(resource_path("levelup.mp3"))
                            db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                            extracoins = level1 * 100
                            extragems = int((level1 + 10) / 10)
                            print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                            totalcoins = checkmoney + extracoins
                            totalgems = gems2 + extragems
                            db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                            db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                        else:
                            exptonextlvl = levelupexp1 - totalexp
                            print(f"{exptonextlvl} more exp needed to level up.")
                            extracoins = 0
                        bought4 = True
                        coins2 = checkmoney + extracoins
                else:
                    print(f"Sorry, but you don't have enough coins to buy {offers[3]} :( Why don't you catch some more pokemon to earn more coins?")
                    playsound(resource_path("lose.mp3"))

            elif pick == 4 and bought4 == True:
                print("Sorry, you already bought this pokemon.")

            elif pick == 5 and bought5 == False:
                checkmoney = gems2 - 25
                if checkmoney >= 0:
                    confirm = input(f"Are you sure you want to buy {legend} for 25 gems? Input y to confirm your decision or n otherwise: ")
                    playsound(resource_path("click.mp3"))
                    if confirm == 'y':
                        playsound(resource_path("buy.mp3"))
                        db.execute(f"UPDATE users SET Gems = {checkmoney} WHERE username = '{login1}'")
                        db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{legend}")')
                        print(f"Thanks for buying {legend}! You now have {checkmoney} gems left.")
                        print()
                        expgain = 75
                        print(f"You also got {expgain} exp!")
                        totalexp = exp2 + expgain
                        exp2 = totalexp
                        print(f"You now have {totalexp} exp!")
                        db.execute(f"UPDATE users SET Exp = {totalexp} WHERE username = '{login1}'")
                        level0 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
                        level1 = int(level0[0]["Level"])
                        levelupexp0 = round((50 * (pow(level1 - 1, 1.35))))
                        levelupexp1 = round((50 * (pow(level1, 1.35))))
                        if totalexp >= levelupexp1:
                            level1 = level1 + 1
                            print(f"Congratulations, you are now at level {level1}!")
                            playsound(resource_path("levelup.mp3"))
                            db.execute(f"UPDATE users SET Level = {level1} WHERE username = '{login1}'")
                            extracoins = level1 * 100
                            extragems = int((level1 + 10) / 10)
                            print(f"Here's {extracoins} coins and {extragems} gems as a level up bonus!")
                            totalcoins = checkmoney + extracoins
                            totalgems = checkmoney + extragems
                            db.execute(f"UPDATE users SET Coins = {totalcoins} WHERE username = '{login1}'")
                            db.execute(f"UPDATE users SET Gems = {totalgems} WHERE username = '{login1}'")
                        else:
                            exptonextlvl = levelupexp1 - totalexp
                            print(f"{exptonextlvl} more exp needed to level up.")
                            extragems = 0
                        bought5 = True
                        gems2 = checkmoney + extragems
                else:
                    print(f"Sorry, but you don't have enough gems to buy {legend} :( Why don't you catch some more shiny pokemon or level up to earn more gems?")
                    playsound(resource_path("lose.mp3"))

            elif pick == 5 and bought5 == True:
                print("Sorry, you already bought this pokemon.")

            elif pick == 6:
                print()
                print("Thanks for shopping!")
                break
            else:
                print("",end="")



    elif pref == 2:
        allpokes = db.execute("SELECT * FROM Pokemon")
        allpokestotal = len(allpokes)
        print()
        print(f"{login1}'s stats")
        print()
        print("Total pokemon caught: ", end="")
        total0 = db.execute(f"SELECT MAX(ID) FROM {login1}")
        print(total0[0]["MAX(ID)"])
        print("Unique pokemon caught (Normal): ", end="")
        pretotal1 = db.execute(f"SELECT DISTINCT pokemon FROM {login1} WHERE shiny = 'False'")
        total1 = len(pretotal1)
        print(f"{total1} / {allpokestotal}")
        print("Unique pokemon caught (Shiny): ", end="")
        pretotal6 = db.execute(f"SELECT DISTINCT pokemon FROM {login1} WHERE shiny = 'True'")
        total6 = len(pretotal6)
        print(f"{total6} / {allpokestotal}")
        pretotal2 = db.execute(f"SELECT Coins FROM users WHERE username = '{login1}'")
        total2 = pretotal2[0]["Coins"]
        print(f"Coins: {total2}")
        pretotal3 = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
        total3 = pretotal3[0]["Gems"]
        print(f"Gems: {total3}")
        pretotal4 = db.execute(f"SELECT Exp FROM users WHERE username = '{login1}'")
        total4 = pretotal4[0]["Exp"]
        print(f"Total Exp: {total4}")
        pretotal5 = db.execute(f"SELECT Level FROM users WHERE username = '{login1}'")
        total5 = pretotal5[0]["Level"]
        print(f"Current Level: {total5}")
        levelupexp0 = round((50 * (pow(total5 - 1, 1.35))))
        levelupexp1 = round((50 * (pow(total5, 1.35))))
        total7 = levelupexp1 - total4
        if total7 > 0:
            print(f"Exp needed to level up: {total7}")
        else:
            print(f"Exp needed to level up: Catch / Buy 1 more Pokemon to level up!")
        print()
        wait = input("Press enter to continue: ")
        playsound(resource_path("click.mp3"))
        print()

    elif pref == 3:
        coins = db.execute(f"SELECT Coins FROM users WHERE username = '{login1}'")
        coins2 = int(coins[0]["Coins"])
        gems = db.execute(f"SELECT Gems FROM users WHERE username = '{login1}'")
        gems2 = int(gems[0]["Gems"])
        print()
        print("Welcome to the Bank!")
        playsound(resource_path("buy.mp3"))
        print(f"You currently have {coins2} coins and {gems2} gems.")
        print("Today's exchange rate is: ",end="")
        playsound(resource_path("exchangerate.mp3"))
        exchangerate = random.randrange(100, 251)
        print(f"1 gem = {exchangerate} coins!")
        while True:
            exchange = input("Would you like to exchange your gems for coins? Input y for yes or n otherwise: ")
            playsound(resource_path("click.mp3"))
            if exchange == 'y':
                while True:
                    try:
                        howmany = int(input("How many gems are you willing to exchange? Input it here: "))
                    except ValueError:
                        print("",end="")
                        continue
                    if gems2 - howmany >= 0:
                        coinresult = howmany * exchangerate
                        confirmation = input(f"Are you sure you want to exchange {howmany} gems for {coinresult} coins? Input y for yes or n otherwise: ")
                        if confirmation == 'y':
                            coins2 = coins2 + coinresult
                            gems2 = gems2 - howmany
                            db.execute(f"UPDATE users SET Coins = {coins2} WHERE username = '{login1}'")
                            db.execute(f"UPDATE users SET Gems = {gems2} WHERE username = '{login1}'")
                            print(f"You now have {coins2} coins and {gems2} gems.")
                            playsound(resource_path("buy.mp3"))
                            playsound(resource_path("coins.mp3"))
                            playsound(resource_path("exchangerate2.mp3"))

                            break
                        else:
                            break
                    else:
                        print("Sorry, you don't have enough gems to do that!")
                        playsound(resource_path("outofballs.mp3"))
                        break
            elif exchange == 'n':
                break

    elif pref == 4:
        print()
        print(f"{login1}'s Pokemon Manager")
        playsound(resource_path("pokeshop.mp3"))
        print()
        time.sleep(1)
        while True:
            try:
                print("Press: ")
                print("0 to view all your Pokemon")
                print("1 to check if you own a specific Pokemon")
                print("2 to view your duplicate Pokemon")
                print("3 to release Pokemon into the wild")
                print("4 to view another user's Pokemon")
                print("5 to quit")
                print()
                managerpref = int(input("Input your number here: "))
                playsound(resource_path("click.mp3"))
            except ValueError:
                print("",end="")
                continue
            if managerpref == 0:
                print()
                print("Pokemon                 | Rarity")
                prepokes = db.execute("SELECT pokemon, rarity FROM ? JOIN Pokemon ON ?.pokemon = Pokemon.name ORDER BY rarity", login1, login1)
                prepokes2 = db.execute("SELECT pokemon, rarity FROM ? JOIN Pokemon_shiny ON ?.pokemon = Pokemon_shiny.name ORDER BY rarity", login1, login1)
                for i in range(len(prepokes)):
                    pokemonm = prepokes[i]["pokemon"]
                    raritym = prepokes[i]["rarity"]
                    print(pokemonm,end="")
                    for x in range(24 - len(pokemonm)):
                        print(" ",end="")
                    print("|   ",end="")
                    print(raritym)
                for j in range(len(prepokes2)):
                    pokemonm = prepokes2[j]["pokemon"]
                    raritym = prepokes2[j]["rarity"]
                    print(pokemonm,end="")
                    for x in range(24 - len(pokemonm)):
                        print(" ",end="")
                    print("|   ",end="")
                    print(raritym)
                print()
            elif managerpref == 1:
                print()
                print("Some guidelines: ")
                print("Input is case-sensitive, so please capitalize appropriately")
                print("For Pokemon with types/variants, use the format name_variant Ex. Nidoran_Male or Oricorio_Pa'u")
                print("For Pokemon with apostrophes, include them Ex. Farfetch'd or Sirfetch'd, and for shiny Pokemon, type in Shiny followed by its name Ex. Shiny Pikachu")
                print()
                isitthere = input("Type in the name of the Pokemon you want to check: ")
                thereitis = db.execute('SELECT pokemon FROM ? WHERE pokemon = ?', login1, isitthere)
                if len(thereitis) != 0:
                    print("Pokemon found!")
                    playsound(resource_path("found.mp3"))
                    raritycheck = db.execute(f'SELECT rarity FROM Pokemon_shiny WHERE name LIKE "%{isitthere}"')
                    a = len(thereitis)
                    b = thereitis[0]["pokemon"]
                    c = raritycheck[0]["rarity"]
                    print(f"You have {a} {b}(s) of rarity {c}")
                    print()
                else:
                    print("Sorry, but you don't have this Pokemon.")
                    playsound(resource_path("nopoke.mp3"))
                    print()
            elif managerpref == 2:
                print("Please wait, this may take a while to process...")
                pokes = list()
                duplicates = list()
                raritylist = list()
                file = open(resource_path("allpokes.csv"), "r")
                for line in file:
                    lined = line.rstrip("\n")
                    pokes.append(lined)
                for i in range(len(pokes)):
                    check = db.execute(f'SELECT pokemon, rarity FROM {login1} JOIN Pokemon ON {login1}.pokemon = Pokemon.name WHERE pokemon = "{pokes[i]}" ORDER BY rarity')
                    check2 = db.execute(f'SELECT pokemon, rarity FROM {login1} JOIN Pokemon_shiny ON {login1}.pokemon = Pokemon_shiny.name WHERE pokemon = "{pokes[i]}" ORDER BY rarity')
                    if len(check) > 1:
                        for j in range(len(check)):
                            duplicates.append(check[j]["pokemon"])
                            raritylist.append(check[j]["rarity"])
                    if len(check2) > 1:
                        for l in range(len(check2)):
                            duplicates.append(check2[l]["pokemon"])
                            raritylist.append(check2[l]["rarity"])
                if len(duplicates) != 0:
                    print()
                    print("Thanks for waiting, here are your duplicate pokemon: ")
                    print()
                    print("Pokemon                     | Rarity")
                    for k in range(len(duplicates)):
                        print(f"{k + 1}. ",end="")
                        print(duplicates[k],end="")
                        if k + 1 < 10:
                            for x in range(25 - len(duplicates[k])):
                                print(" ",end="")
                        elif k + 1 >= 10 and k + 1 < 100:
                            for x in range(24 - len(duplicates[k])):
                                print(" ",end="")
                        elif k + 1 >= 100 and k + 1 < 1000:
                            for x in range(23 - len(duplicates[k])):
                                print(" ",end="")
                        else:
                            for x in range(22 - len(duplicates[k])):
                                print(" ",end="")
                        print("|  ",end="")
                        print(raritylist[k])
                else:
                    print("No duplicates found")
                print()

            elif managerpref == 3:
                print()
                print("Some guidelines: ")
                print("Input is case-sensitive, so please capitalize appropriately")
                print("To release the desired Pokemon, first type in its name. For Pokemon with types/variants, use the format name_variant Ex. Nidoran_Male or Oricorio_Pa'u")
                print("For Pokemon with apostrophes, include them Ex. Farfetch'd or Sirfetch'd, and for shiny Pokemon, type in Shiny followed by its name Ex. Shiny Pikachu")
                print()
                release = input("Type in the name of the Pokemon you want to release, or n to cancel: ")
                playsound(resource_path("click.mp3"))
                if release == 'n':
                    print()
                else:
                    checkit = db.execute(f'SELECT pokemon FROM ? WHERE pokemon LIKE ?', login1, release)
                    if len(checkit) == 0:
                        print("Pokemon not found, maybe you typed its name incorrectly?")
                        print()
                    else:
                        checked = checkit[0]["pokemon"]
                        print(f"Are you sure you want to release {checked}? This cannot be undone. Input y for yes or n otherwise: ", end="")
                        playsound(resource_path("legendary.mp3"))
                        releasing = input("")
                        if releasing == 'y':
                            prerelease = db.execute('SELECT ID FROM ? WHERE pokemon LIKE ?', login1, release)
                            ID = prerelease[0]["ID"]
                            released = db.execute(f'DELETE FROM {login1} WHERE pokemon = "{checked}" AND ID = {ID}')
                            print("Pokemon released!")
                            print()

                        else:
                            print()


            elif managerpref == 4:
                print()
                who = input("Input the username to access Pokemon with: ")
                playsound(resource_path("click.mp3"))
                check99 = db.execute("SELECT * FROM users WHERE username = ?", who)
                if len(check99) == 0:
                    print("Sorry, this username does not exist")
                    break
                print()
                print("Pokemon                 | Rarity")
                prepokes = db.execute(f"SELECT pokemon, rarity FROM ? JOIN Pokemon ON ?.pokemon = Pokemon.name ORDER BY rarity", who, who)
                prepokes2 = db.execute(f"SELECT pokemon, rarity FROM ? JOIN Pokemon_shiny ON ?.pokemon = Pokemon_shiny.name ORDER BY rarity", who, who)
                for i in range(len(prepokes)):
                    pokemonm = prepokes[i]["pokemon"]
                    raritym = prepokes[i]["rarity"]
                    print(pokemonm,end="")
                    for x in range(24 - len(pokemonm)):
                        print(" ",end="")
                    print("|   ",end="")
                    print(raritym)
                for j in range(len(prepokes2)):
                    pokemonm = prepokes2[j]["pokemon"]
                    raritym = prepokes2[j]["rarity"]
                    print(pokemonm,end="")
                    for x in range(24 - len(pokemonm)):
                        print(" ",end="")
                    print("|   ",end="")
                    print(raritym)
                print()
            elif managerpref == 5:
                break
    elif pref == 5:
        print()
        print("Trading Section")
        print()
        while True:
            trade0 = input("Type in the username of the player you want to trade with, or n to exit: ")
            playsound(resource_path("click.mp3"))
            if trade0 == 'n':
                break
            else:
                user = db.execute(f'SELECT username FROM users WHERE username = ?', trade0)
                if len(user) != 0:
                    username = str(user[0]["username"])
                    print()
                    print("Some guidelines: ")
                    print("You can only trade 1 pokemon at a time")
                    print("For Pokemon with types/variants, use the format name_variant Ex. Nidoran_Male or Oricorio_Pa'u")
                    print("For Pokemon with apostrophes, include them Ex. Farfetch'd or Sirfetch'd, and for shiny Pokemon, type in Shiny followed by its name Ex. Shiny Pikachu")
                    print()
                    trade1 = input(f"Input the Pokemon you will give to {username}, or n to go back: ")
                    playsound(resource_path("click.mp3"))
                    trade2 = db.execute(f'SELECT pokemon FROM ? WHERE pokemon LIKE ?', login1, trade1)
                    if trade1 == 'n':
                        print("",end="")
                    elif len(trade2) != 0:
                        pokeone = str(trade2[0]["pokemon"])
                        print(f"{pokeone} successfully retrieved from your collection!")
                        print()
                        trade3 = input(f"Input the Pokemon you wish to get in return, or n to go back: ")
                        playsound(resource_path("click.mp3"))
                        trade4 = db.execute(f'SELECT pokemon FROM ? WHERE pokemon LIKE ?', username, trade3)
                        if trade3 == 'n':
                            print("",end="")
                        elif len(trade4) != 0:
                            poketwo = str(trade4[0]["pokemon"])
                            print(f"{poketwo} successfully retrieved from {username}'s collection!")
                            print()
                            while True:
                                confirmation = input(f"Are you sure you want to trade your {pokeone} for {username}'s {poketwo}? Input y to confirm or n otherwise: ")
                                playsound(resource_path("click.mp3"))
                                if confirmation == 'y':
                                    print(f"For added security, please tell {username} to enter his/her account's password")
                                    time.sleep(1)
                                    passw = getpass.getpass(f"{username}, please enter your password to complete the trade (Characters you type are not shown for added security): ")
                                    playsound(resource_path("click.mp3"))
                                    checker = db.execute(f'SELECT username FROM users WHERE username = ? and password = ?', username, passw)
                                    if len(checker) != 0:
                                        checker2 = str(checker[0]["username"])
                                    else:
                                        checker2 = None
                                    if username == checker2:
                                        preexchange0 = db.execute(f'SELECT ID FROM {login1} WHERE pokemon = "{pokeone}"')
                                        ID2 = preexchange0[0]["ID"]
                                        exchange0 = db.execute(f'DELETE FROM {login1} WHERE pokemon = "{pokeone}" AND ID = {ID2}')
                                        exchange1 = db.execute(f'INSERT INTO {login1} (pokemon) VALUES ("{poketwo}")')
                                        preexchange2 = db.execute(f'SELECT ID FROM {username} WHERE pokemon = "{poketwo}"')
                                        ID3 = preexchange2[0]["ID"]
                                        exchange2 = db.execute(f'DELETE FROM {username} WHERE pokemon = "{poketwo}" AND ID = {ID3}')
                                        exchange3 = db.execute(f'INSERT INTO {username} (pokemon) VALUES ("{pokeone}")')
                                        print("Trade successful!")
                                        playsound(resource_path("found.mp3"))
                                        print("Thanks for trading!")
                                        print()
                                    else:
                                        print("Sorry, incorrect password.")
                                        playsound(resource_path("wrongpassword.mp3"))
                                        print("Trade cancelled")
                                        print()
                                    break
                                elif confirmation == 'n':
                                    print("Trade cancelled")
                                    print()
                                    break
                                else:
                                    print("",end="")
                        else:
                            print(f"Sorry, but {username} doesn't have this Pokemon")
                            playsound(resource_path("nopoke.mp3"))
                            print()
                    else:
                        print("Sorry, but you don't have this Pokemon")
                        playsound(resource_path("nopoke.mp3"))
                        print()
                else:
                    print("User not found")
                    print()


    elif pref == 6:
        print()
        print("Leaderboard")
        playsound(resource_path("leaderboard.mp3"))
        while True:
            try:
                print()
                print("Press: ")
                print("0 to update your points")
                print("1 to show users with the most legends")
                print("2 to show the most experienced users")
                print("3 to show the users with the most shiny Pokemon")
                print("4 to see the users with the most Pokemon")
                print("5 to see who's the best collector so far")
                print("6 to quit")
                print()
                boardchoice = int(input("Input your number here: "))
                playsound(resource_path("click.mp3"))
            except ValueError:
                print("",end="")
                continue
            if boardchoice == 0:
                pokesbyrarity = list()
                shinypokesbyrarity = list()
                experience1 = db.execute(f"SELECT Exp FROM users WHERE username = '{login1}'")
                experience = experience1[0]["Exp"]
                print("Updating your points...")
                for c in range(10):
                    onetoten = db.execute("SELECT DISTINCT pokemon FROM ? JOIN Pokemon ON ?.pokemon = Pokemon.name WHERE rarity = ?", login1, login1, c + 1)
                    pokesbyrarity.append(len(onetoten))
                for d in range(10):
                    shinyonetoten = db.execute("SELECT DISTINCT pokemon FROM ? JOIN Pokemon_shiny ON ?.pokemon = Pokemon_shiny.name WHERE rarity = ?", login1, login1, d + 1)
                    shinypokesbyrarity.append(len(shinyonetoten))
                points0 = (4 * pokesbyrarity[0]) + (9 * pokesbyrarity[1]) + (16 * pokesbyrarity[2]) + (25 * pokesbyrarity[3]) + (36 * pokesbyrarity[4]) + (49 * pokesbyrarity[5]) + (64 * pokesbyrarity[6]) + (81 * pokesbyrarity[7]) + (100 * pokesbyrarity[8]) + (150 * pokesbyrarity[9])
                points1 = (54 * shinypokesbyrarity[0]) +  (59 * shinypokesbyrarity[1]) + (66 * shinypokesbyrarity[2]) + (75 * shinypokesbyrarity[3]) + (86 * shinypokesbyrarity[4]) + (99 * shinypokesbyrarity[5]) + (114 * shinypokesbyrarity[6]) + (131 * shinypokesbyrarity[7]) + (150 * shinypokesbyrarity[8]) + (200 * shinypokesbyrarity[9])
                points2 = round(experience / 4)
                TOTALPOINTS = points0 + points1 + points2
                updatepoints = db.execute("UPDATE users SET Points = ? WHERE username = ?", TOTALPOINTS, login1)
                print("Points successfully updated!")
                print()
                print(f"Points gained from Normal Pokemon: {points0}")
                playsound(resource_path("point.mp3"))
                print(f"Points gained from Shiny Pokemon: {points1}")
                playsound(resource_path("point.mp3"))
                print(f"Points gained from Total Exp: {points2}")
                playsound(resource_path("point.mp3"))
                print(f"Giving you a total of {TOTALPOINTS} points")
                playsound(resource_path("found.mp3"))
                print()
            elif boardchoice == 1:
                print()
                print("Top 10 users with the most Legends: ")
                print()
                print("   Username                 |  # of Legendary Pokemon")
                legendusers = dict()
                tables = db.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table'")
                for a in range(len(tables)):
                    name = tables[a]["name"]
                    if "Pokemon" not in name and "sqlite" not in name and "users" not in name:
                        legendperuser0 = db.execute("SELECT pokemon FROM ? JOIN Pokemon_shiny ON ?.pokemon = Pokemon_shiny.name WHERE rarity = 10", name, name)
                        legendperuser1 = db.execute("SELECT pokemon FROM ? JOIN Pokemon ON ?.pokemon = Pokemon.name WHERE rarity = 10", name, name)
                        legendusers[name] = len(legendperuser0) + len(legendperuser1)
                sortedlegendusers = OrderedDict(sorted(legendusers.items(), key = lambda t: t[1], reverse = True))
                count = 0
                for key, value in sortedlegendusers.items():
                    count = count + 1
                    print(f"{count}. ",end="")
                    print(key,end="")
                    for x in range(25 - len(key)):
                        print(" ",end="")
                    print("|            ",end="")
                    print(value)
                    if count == 10:
                        break
                print()
                moveon = input("Press enter to continue: ")
                playsound(resource_path("click.mp3"))
            elif boardchoice == 2:
                print()
                mostexperienced = db.execute("SELECT username, Exp FROM users ORDER BY Exp DESC LIMIT 10")
                print("Top 10 users with the most exp: ")
                print()
                print("   Username                 |  Exp")
                for f in range(len(mostexperienced)):
                    print(f"{f + 1}. ",end="")
                    print(mostexperienced[f]["username"],end="")
                    for x in range(25 - len(mostexperienced[f]["username"])):
                        print(" ",end="")
                    print("|  ", end="")
                    print(mostexperienced[f]["Exp"])
                print()
                moveon = input("Press enter to continue: ")
                playsound(resource_path("click.mp3"))
            elif boardchoice == 3:
                print()
                print("Top 10 users with the most Shiny Pokemon: ")
                print()
                print("   Username                 |  # of Shiny Pokemon")
                topusers = dict()
                tables = db.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table'")
                for a in range(len(tables)):
                    name = tables[a]["name"]
                    if "Pokemon" not in name and "sqlite" not in name and "users" not in name:
                        shinyperuser = db.execute("SELECT pokemon FROM ? JOIN Pokemon_shiny ON ?.pokemon = Pokemon_shiny.name WHERE shiny = 'True'", name, name)
                        topusers[name] = len(shinyperuser)
                sortedtopusers = OrderedDict(sorted(topusers.items(), key = lambda t: t[1], reverse = True))
                count = 0
                for key, value in sortedtopusers.items():
                    count = count + 1
                    print(f"{count}. ",end="")
                    print(key,end="")
                    for x in range(25 - len(key)):
                        print(" ",end="")
                    print("|          ",end="")
                    print(value)
                    if count == 10:
                        break
                print()
                moveon = input("Press enter to continue: ")
                playsound(resource_path("click.mp3"))
            elif boardchoice == 4:
                print()
                print("Top 10 users with the most Pokemon: ")
                print()
                print("   Username                 |  # of Total Pokemon")
                mostpokes = dict()
                tables = db.execute("SELECT name FROM sqlite_master WHERE TYPE = 'table'")
                for a in range(len(tables)):
                    name = tables[a]["name"]
                    if "Pokemon" not in name and "sqlite" not in name and "users" not in name:
                        mostpoke0 = db.execute("SELECT pokemon FROM ? JOIN Pokemon_shiny ON ?.pokemon = Pokemon_shiny.name", name, name)
                        mostpoke1 = db.execute("SELECT pokemon FROM ? JOIN Pokemon ON ?.pokemon = Pokemon.name", name, name)
                        mostpokes[name] = len(mostpoke0) + len(mostpoke1)
                sortedmostpokes = OrderedDict(sorted(mostpokes.items(), key = lambda t: t[1], reverse = True))
                count = 0
                for key, value in sortedmostpokes.items():
                    count = count + 1
                    print(f"{count}. ",end="")
                    print(key,end="")
                    for x in range(25 - len(key)):
                        print(" ",end="")
                    print("|          ",end="")
                    print(value)
                    if count == 10:
                        break
                print()
                moveon = input("Press enter to continue: ")
                playsound(resource_path("click.mp3"))
            elif boardchoice == 5:
                print()
                print("Official Collectemon Leaderboard")
                bestuser = db.execute("SELECT username, Points FROM users ORDER BY Points DESC LIMIT 10")
                print()
                print("   Username                 |  Points")
                for g in range(len(bestuser)):
                    print(f"{g + 1}. ",end="")
                    print(bestuser[g]["username"],end="")
                    for y in range(25 - len(bestuser[g]["username"])):
                        print(" ",end="")
                    print("|  ", end="")
                    print(bestuser[g]["Points"])
                print()
                moveon = input("Press enter to continue: ")
                playsound(resource_path("click.mp3"))
            elif boardchoice == 6:
                break

    elif pref == 7:
        while True:
            try:
                print()
                print("Type in: ")
                print("0 to view the entire help booklet")
                print("1 to view I. INTRODUCTION")
                print("2 to view II. USER INTERFACE")
                print("3 to view III. ACCOUNT CREATION AND LOGIN")
                print("4 to view IV. CURRENCY, LEVELLING, AND RARITY")
                print("5 to view V. CATCHING POKEMON")
                print("6 to view VI. POKESHOP")
                print("7 to view VII. STATS PAGE")
                print("8 to view VIII. BANK")
                print("9 to view IX. POKEMON MANAGER")
                print("10 to view X. TRADING")
                print("11 to view XI. LEADERBOARDS")
                print("12 to view XII. ACCOUNT DELETION")
                print("13 to view XIII. FAQ (Frequently Asked Quesitons)")
                print("14 to view XIV. LIMITATIONS")
                print("15 to view XV. CREDITS")
                print("16 to exit")
                print()
                helping = int(input("Input your number here: "))
                playsound(resource_path("click.mp3"))
            except ValueError:
                print("",end="")
                continue
            if helping == 0:
                print()
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                for line in helpbooklet:
                    print(line)
            elif helping == 1:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 56 and counters < 71:
                        print(line)
            elif helping == 2:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 75 and counters < 99:
                        print(line)
            elif helping == 3:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 104 and counters < 113:
                        print(line)
            elif helping == 4:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 118 and counters < 150:
                        print(line)
            elif helping == 5:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 155 and counters < 175:
                        print(line)
            elif helping == 6:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 180 and counters < 189:
                        print(line)
            elif helping == 7:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 194 and counters < 207:
                        print(line)
            elif helping == 8:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 212 and counters < 219:
                        print(line)
            elif helping == 9:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 224 and counters < 229:
                        print(line)
            elif helping == 10:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 234 and counters < 240:
                        print(line)
            elif helping == 11:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 245 and counters < 265:
                        print(line)
            elif helping == 12:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 270 and counters < 286:
                        print(line)
            elif helping == 13:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 291 and counters < 341:
                        print(line)
            elif helping == 14:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 346 and counters < 358:
                        print(line)
            elif helping == 15:
                counters = 0
                helpbooklet = open(resource_path("helpbooklet.txt"), "r")
                print()
                for line in helpbooklet:
                    counters = counters + 1
                    if counters >= 363 and counters < 373:
                        print(line)
            elif helping == 16:
                break

    elif pref == 8:
        print()
        print("Thanks for playing!")
        playsound(resource_path("goodbye.mp3"))
        print()
        time.sleep(1)
        playsound(resource_path("shutdown.mp3"))
        sys.exit()

    elif pref == 68:
        counting = 1
        delete.append(chr(pref))
        print("", end="")
    elif pref == 69:
        counting = counting + 1
        delete.append(chr(pref))
        if counting == 6:
            DELETE = ''.join(delete)
            if DELETE == "DELETE":
                print()
                print("ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT? YOUR ACCOUNT WILL BE LOST FOREVER AND CANNOT BE RECOVERABLE!")
                playsound(resource_path("legendary.mp3"))
                AREYOUSURE = input("Input your password if you wish to continue, or any other character otherwise: ")
                playsound(resource_path("click.mp3"))
                checkdelete = db.execute(f"SELECT * FROM users WHERE username = ? and password = ?", login1, AREYOUSURE)
                if len(checkdelete) != 0:
                    DELETION1 = db.execute(f"DELETE FROM users WHERE username = ? and password = ?", login1, AREYOUSURE)
                    DELETION2 = db.execute(f"DROP TABLE ?", login1)
                    print("Account permanently deleted.")
                    playsound(resource_path("gameover.mp3"))
                    print()
                    playsound(resource_path("shutdown.mp3"))
                    sys.exit()
                else:
                    print("Deletion cancelled!")
        print("", end="")
    elif pref == 76:
        counting = counting + 1
        delete.append(chr(pref))
        print("", end="")
    elif pref == 84:
        counting = counting + 1
        delete.append(chr(pref))
        print("", end="")
    elif pref == 63:
        print("A wild ? appeared!")
        enter = input("Hurry, press enter to catch it!")
        print("? was caught!")
        playsound(resource_path("caught.mp3"))
        print("Hey, looks like ? wants to sing you a song :)")
        enter2 = input("Press enter to hear it!")
        print()
        for i in range(25):
            print("( ͡° ͜ʖ ͡°) ",end="")
        playsound(resource_path("mystery.mp3"))
    else:
        print("", end="")


print("Thanks for playing!")
playsound(resource_path("goodbye.mp3"))
playsound(resource_path("shutdown.mp3"))
print()
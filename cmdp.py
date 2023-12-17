"""
Command prompt made by Torrez.
To run cmdp, import cmdp and run this line of code:
>>> cmdp.cmdp()

Here is an example of how to login to your account:
>>> sys.login
If you haven\'t already made an account, it asks you to create a new account which is an admin account.
Then you have to login to the new account.
"""

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, "w")


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

from googlesearch import search
import getpass
import sys
from time import sleep
from random import uniform, randint
from datetime import datetime
from typing import Literal
from threading import Thread
import pickle
import os
from string import printable
import smtplib
import pygame

os.system("cls" if os.name == "nt" else "clear")

# from polyarea.polyarea2 import
# import mathsolvers.msv3
from _pformatter import _password_formatter


blockPrint()


def readable_format(num: int | float) -> str:
    abbrs = [
        "",
        "K",
        "M",
        "B",
        "T",
        "Qa",
        "Qt",
        "Sx",
        "Sp",
        "Oc",
        "No",
        "Dc",
        "UDc",
        "DDc",
        "TDc",
        "QaDc",
        "QiDc",
        "SxDc",
        "SpDc",
        "OcDc",
        "NmDc",
        "Vg",
        "UVg",
        "DVg",
        "TVg",
        "QaVg",
        "QiVg",
        "SxVg",
        "SpVg",
        "OcVg",
        "NmVg",
        "Tg",
        "UTg",
        "DTg",
        "TTg",
        "QaTg",
        "QiTg",
        "SxTg",
        "SpTg",
        "OcTg",
        "NmTg",
        "Qa",
        "UQa",
        "DQa",
        "TQa",
        "QaQa",
        "QiQa",
        "SxQa",
        "SpQa",
        "OcQa",
        "NoQa",
        "Qi",
        "UQi",
        "DQi",
        "TQi",
        "QaQi",
        "QiQi",
        "SxQi",
        "SpQi",
        "OcQi",
        "NoQi",
        "Se",
        "USe",
        "DSe",
        "TSe",
        "QaSe",
        "QiSe",
        "SxSe",
        "SpSe",
        "OcSe",
        "NoSe",
        "St",
        "USt",
    ]
    num = float("{:.3g}".format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return "{} {}".format("{:f}".format(num).rstrip("0").rstrip("."), abbrs[magnitude])


class UMM:
    def __init__(self, money) -> None:
        self.money = readable_format(money)

    def open_window(self) -> None:
        pygame.init()

        width = 250
        height = 100

        self.screen = pygame.display.set_mode(size=(width, height))
        pygame.display.set_caption("User Money Monitor")
        self.text_font = pygame.font.Font(
            "assets/Arial.ttf",
            12,
        )
        self.title_font = pygame.font.Font(
            "assets/pixely[1].ttf",
            12,
        )
        title = self.title_font.render("User Money Moniter", True, "#00aa00")
        background = pygame.image.load("assets/cookieclicker_background.jpg").convert()

        clock = pygame.time.Clock()

        self.screen.blit(background, (0, 0))
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.close_window()
                        sleep(1)
                        enablePrint()
                        os.system("cls" if os.name == "nt" else "clear")
                self.screen.blit(title, (50, 15))
                self.render()
                pygame.display.update()
                clock.tick(360)
            except Exception:
                break

    def close_window(self):
        pygame.quit()

    def blit_money(self) -> None:
        self.display_money = self.text_font.render(
            f"Cash: {str(self.money)}", True, "#ffffff"
        )
        self.screen.blit(self.display_money, (25, 50))

    def render(self) -> None:
        self.blit_money()


class cmdp(object):
    def __init__(self) -> None:
        try:
            with open("user_data.dat", "rb") as f:
                loaded_data = pickle.load(f)
            self.user_data = loaded_data
        except Exception:
            self.user_data = {
                "username": "user",
                "password": "",
                "uaps": {},
                "email": "user@example.com",
                "e-password": "",
                "eaps": {},
                "platform": sys.platform,
                "version": {
                    "major": _version_info().major,
                    "minor": _version_info().minor,
                    "micro": _version_info().micro,
                },
                "u-ranks": {},
                "u-google-search-history": {},
                "downloads": {},
                "user-cmdp-times": {},
                "admin": False,
            }
            with open("user_data.dat", "wb") as f:
                pickle.dump(self.user_data, f)

        self.ranks = [
            "alpha",
            "beta",
            "gamma",
            "delta",
            "epsilon",
            "zeta",
            "eta",
            "theta",
            "iota",
            "kappa",
            "lambda",
            "mu",
            "nu",
            "omicron",
            "pi",
            "rho",
            "sigma",
            "tau",
            "upsilon",
            "phi",
            "chi",
            "psi",
            "omega",
        ]

        self.__original_ver_info = _version()
        self.__cmdUseCount = 0
        self.download_packs = [
            "ms",
            "collatz-conjecture",
            "g.cookie-clicker",  # the 'g' means games
            "polyarea",
            "time",
        ]
        self.__initpackages = [
            "ms",
            "collatz-conjecture",
            "g.cookie-clicker",
            "polyarea",
            "time",
        ]
        self._cmdflags = {
            "-d": "downloads <package>",
            "--change": "to force something to change",
        }
        self.__commands = [
            "jit version info",
            "jit --change kip version info",
            "jit pc version",
            "jit pc platform",
            "jit time",
            "jit user info",
            "users",
            "jit create account",
            "jit log out",
            "jit",
            "jit download ",
            "jit -d init",
            "jit help",
            "help",
            "jit ranks",
            "jit google",
            "jit money",
        ]
        self.__notLoggedInCommands = ["users", "commands", "help", "login"]

        self.__login_or_register()
        self.copyright()
        self.tips()
        while True:
            self.reqcmd()

    def reqcmd(self, /) -> None:
        """Requests a command from the active user."""
        if (
            self.user_data["username"] == "user"
            and self.user_data["password"] == ""
            and self.user_data["email"] == "user@example.com"
            and self.user_data["e-password"] == ""
        ):
            if sys.platform.startswith("win32"):
                reqd_cmd = input("PS C:\\Users\\user>")
            elif sys.platform.startswith("darwin"):
                reqd_cmd = input("PS /Users/user>")
            if reqd_cmd == "":
                pass
            elif reqd_cmd in self.__notLoggedInCommands:
                self.load("sc")
                print()
                if reqd_cmd == "users":
                    usernames = []
                    for users in self.user_data["uaps"].keys():
                        usernames.append(users)

                    print("Users: {}".format(usernames))
                if reqd_cmd == "commands":
                    print("Available commands: {}".format(self.__notLoggedInCommands))
                if reqd_cmd == "help":
                    print(
                        'If you want to create an account, you can "jit create account", or\n"jit login <username>" to login to a specific account ("<username>" is the username you want to log into).'
                    )
                if reqd_cmd == "login":
                    self.__login()

        else:
            if sys.platform.startswith("win32"):
                reqd_cmd = input(f"PS C:\\Users\\{self.user_data['username']}>")
            elif sys.platform.startswith("darwin"):
                reqd_cmd = input(f"PS /Users/{self.user_data['username']}>")
            if reqd_cmd == "":
                pass
            elif reqd_cmd in self.__commands:
                self.load("sc")
                print()
                if reqd_cmd.startswith(
                    self.__commands[self.__commands.index("jit download ")]
                ):
                    ucmd = reqd_cmd[13:]
                    if ucmd in self.download_packs:
                        self.user_data["downloads"][self.user_data["username"]] = []
                        self.user_data["downloads"][self.user_data["username"]].append(
                            str(ucmd)
                        )
                        with open("user_data.dat", "wb") as f:
                            pickle.dump(self.user_data, f)
                    else:
                        print(
                            f"Sorry but {ucmd} does not exist as a package or a download. Please retry or not."
                        )
                elif reqd_cmd == "jit -d init":
                    ...
                elif reqd_cmd == self.__commands[1]:
                    major = int(input("major: "))
                    minor = int(input("minor: "))
                    micro = int(input("micro: "))

                    print()

                    _version_info.major = major
                    _version_info.minor = minor
                    _version_info.micro = micro

                    self.user_data["version"]["major"] = major
                    self.user_data["version"]["minor"] = minor
                    self.user_data["version"]["micro"] = micro

                    with open(self.user_data, "wb") as f:
                        pickle.dump(self.user_data, f)
                else:
                    if reqd_cmd == self.__commands[0]:
                        self.pc_ver_info()
                    if reqd_cmd == self.__commands[2]:
                        print(f"Version: {_version()}")
                    if reqd_cmd == self.__commands[3]:
                        print(f"Platform: {sys.platform}")
                    if reqd_cmd == self.__commands[4]:
                        print(Time())
                    if reqd_cmd == "user info":
                        ...
                    if reqd_cmd == "users":
                        usernames = []
                        for users in self.user_data["uaps"].keys():
                            usernames.append(users)

                        print("Users: {}".format(usernames))
                    if reqd_cmd == "jit create account":
                        print("----- Creating account -----")
                        self.user_data["username"] = input("Username: ")
                        while True:
                            sub_p = getpass.getpass()
                            if len(sub_p) < 8:
                                print(
                                    "\nSorry but password must be at least 8 characters."
                                )
                            else:
                                self.user_data["password"] = _password_formatter(
                                    password=sub_p, f="c"
                                )
                                break

                        print()
                        print("--- Creating email and email password ---")
                        while True:
                            print("Email: ", end="")
                            sub_e = input()
                            if "@" in sub_e and sub_e.index("@") > 0:
                                self.user_data["email"] = sub_e
                                break
                            else:
                                print(
                                    "\nSorry but email must be a valid email address. (with an '@' symbol)"
                                )
                        while True:
                            print("Email password: ", end="")
                            sub_ep = input()
                            if len(sub_ep) < 8:
                                print(
                                    "\nSorry but password must be at least 8 characters."
                                )
                            else:
                                self.user_data["e-password"] = _password_formatter(
                                    password=sub_ep, f="c"
                                )
                                break

                        print()
                        print(
                            'Please check your real life gmail and there should be one gmail from "that1.stinkyarmpits@gmail.com".'
                        )

                        self._verification_code = randint(100_000, 999_999)
                        sender_email = "that1.stinkyarmpits@gmail.com"
                        receiver_email = self.user_data["email"]
                        subject = "Email verification"
                        message = f"{self._verification_code} is your one-time email verification code; enter this 6-digit code in the cmdp to continue."
                        text = f"Subject: {subject}\n\n{message}"
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(sender_email, "uxse vldv kqmx ribr")
                        server.sendmail(sender_email, receiver_email, text)
                        while True:
                            user_verifycode = input(
                                "Please enter the code sent to your gmail account: "
                            )
                            if user_verifycode == str(self._verification_code):
                                break
                            else:
                                print(
                                    "This isn't your email verification code. Please retry."
                                )

                        self.user_data["uaps"][
                            self.user_data["username"]
                        ] = self.user_data["password"]
                        self.user_data["eaps"][
                            self.user_data["email"]
                        ] = self.user_data["e-password"]
                        self.user_data["downloads"][self.user_data["username"]] = []

                        self.user_data["user-cmdp-times"][
                            self.user_data["username"]
                        ] = {}
                        self.user_data["user-cmdp-times"][self.user_data["username"]][
                            "online"
                        ] = ...

                        with open("user_data.dat", "wb") as f:
                            pickle.dump(self.user_data, f)

                    if reqd_cmd == "jit log out":
                        resetUserSettings()
                        self.reqcmd()
                    if reqd_cmd == "jit":
                        cmdl = ""
                        for commands in self.__commands:
                            cmdl += commands
                            cmdl += "\n"
                        print(
                            f"Commands: {self.__commands} ({len(self.__commands) + 1} commands)"
                        )
                    if reqd_cmd == "help":
                        print('Perhaps trying the most similar command: "jit help" ?')
                    if reqd_cmd == "jit help":
                        print(
                            "This feature is not available yet in this version, when it is finally made I'll release it."
                        )
                    if reqd_cmd == "jit ranks":
                        print("User ranking or ranks?")

                        ranks_choice = input(
                            '\033[33m[u] user rankings\033[0m  [r] ranks  [q] quit, (default is "u"): '
                        ).lower()
                        if ranks_choice in ["u", ""]:
                            print("User rankings:")
                            print(self.user_data["u-ranks"])
                        elif ranks_choice == "r":
                            print("Ranks:")
                            print(self.ranks)
                        elif ranks_choice == "q":
                            pass
                        else:
                            print("Invalid option...")
                            print()
                    if reqd_cmd == "jit google":
                        print("Public or Incognito mode?")

                        google_choice = input(
                            '\033[33m[p] public google\033[0m  [i] incognito google  [q] quit, (default is "p"): '
                        ).lower()
                        print()
                        if google_choice in ["p", ""]:
                            print(
                                "CAUTION: Each query saved to the history will not be removed, replaced or deleted."
                            )
                            print()
                            sleep(1)
                            query = input("Enter a query: ")
                            self.user_data["u-google-search-history"][
                                self.user_data["username"]
                            ].insert(0, query)

                            with open("user_data.dat", "wb") as f:
                                pickle.dump(self.user_data, f)

                            num_results = input("Number of results to be shown: ")
                            try:
                                eval(num_results)
                            except Exception as e:
                                print("Error: " + str(e))
                            else:
                                num_results = eval(num_results)
                                for url in search(query, num_results=num_results):
                                    print(url)
                        elif google_choice == "i":
                            print(
                                "DISCLAIMER: when using google incognito mode, each search query will not be saved."
                            )
                            sleep(1)
                            print()
                            query = input("Enter a query: ")
                            num_results = input("Number of results to be shown: ")
                            try:
                                eval(num_results)
                            except Exception as e:
                                print("Error: " + str(e))
                            else:
                                num_results = eval(num_results)
                                for url in search(query, num_results=num_results):
                                    print(url)
                        elif google_choice == "q":
                            pass
                        else:
                            print("Invalid option.")
                            print()
                            sleep(0.25)
                    if reqd_cmd == "jit money":
                        print()
                        print("Which user ")
                        sleep(0.499999999999990006969696969696969696969)
                        while True:
                            user_money_review_request = input("Please ")

            else:
                print(
                    "Sorry, it looks like you have entered something that the computer can't understand or identify.\nPerhaps you misspelt something?\n"
                )

    def add_money(
        self,
        on_time: tuple[int, int, int, float],
        off_time: tuple[int, int, int, float],
    ) -> str | float:
        """Format the parameters like \"(days, hours, minutes, seconds)\"
        and of course replace days, hours, minutes, seconds with the actual time but don't put in anything
        type str."""
        if type(on_time) == tuple:
            on_days = on_time[0]
            on_hours = on_time[1]
            on_minutes = on_time[2]
            on_seconds = on_time[3]
            for on_day in on_days:
                on_hours += 24
            for on_hour in on_hours:
                on_minutes += 60
            for on_minute in on_minutes:
                on_seconds += 60
        else:
            raise TypeError("Invalid.")
        if type(off_time) == tuple:
            off_days = off_time[0]
            off_hours = off_time[1]
            off_minutes = off_time[2]
            off_seconds = off_time[3]
            for off_day in off_days:
                off_hours += 24
            for off_hour in off_hours:
                off_minutes += 60
            for on_minute in off_minutes:
                off_seconds += 60
        else:
            raise TypeError("Invalid.")

        # Returns
        return off_seconds - on_seconds

    def __login(self):
        print(
            "\nPlease login in order to use the command prompt since you entered the login command."
        )
        sleep(1.5)
        print("----- Login to created account -----")
        user_u = input("Username: ")
        user_p = input("Password: ")
        sleep(0.5)
        print("--- Log into admin email ---")
        user_e = input("Email: ")
        user_ep = input("E-Password (email password): ")
        print()
        print(
            'Please check your real life gmail and there should be one gmail from "that1.stinkyarmpits@gmail.com".'
        )
        self._verification_code = randint(100_000, 999_999)
        sender_email = "that1.stinkyarmpits@gmail.com"
        receiver_email = self.user_data["email"]
        subject = "Email verification"
        message = f"{self._verification_code} is your one-time email verification code; enter this 6-digit code in the cmdp to continue."
        text = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, "uxse vldv kqmx ribr")
        server.sendmail(sender_email, receiver_email, text)
        while True:
            user_verifycode = input(
                "Please enter the code sent to your gmail account: "
            )
            if user_verifycode == str(self._verification_code):
                break
            else:
                print("This isn't your email verification code. Please retry.")
        if (
            user_u == self.user_data["username"]
            and user_p
            == _password_formatter(password=self.user_data["password"], f="dc")
            and user_e == self.user_data["email"]
            and user_ep
            == _password_formatter(password=self.user_data["e-password"], f="dc")
        ):
            with open("user_data.dat", "wb") as f:
                pickle.dump(self.user_data, f)
            print(
                "\nSuccessfully logged in user {}!".format(self.user_data["username"])
            )
            self.current_account = self.user_data["username"]
            sleep(1)

    def __login_or_register(self) -> dict:
        if (
            self.user_data["username"] == "user"
            and self.user_data["password"] == ""
            and self.user_data["email"] == "user@example.com"
            and self.user_data["e-password"] == ""
        ):
            sleep(1)
            print("\nHello and welcome to TCMDPS (Torrez's Command Prompt Software)!")
            sleep(0.75)
            print(
                "It looks like you're a new user! We just need to help you complete\nsome minor tasks."
            )
            sleep(2)
            print(
                "\nFor security reasons, you need to create a new account and login to the account.\n"
            )
            sleep(2)
            print("----- Creating admin account -----")

            while True:
                sub_u = input("Username:")
                if len(sub_u) <= 15:
                    self.user_data["username"] = sub_u
                    break
                else:
                    print(
                        "\nUsername must be below the length of 15 of lower characters."
                    )
            while True:
                sub_p = getpass.getpass()
                if len(sub_p) < 8:
                    print("\nSorry but password must be at least 8 characters.")
                else:
                    self.user_data["password"] = _password_formatter(
                        password=sub_p, f="c"
                    )
                    break
            self.user_data["uaps"][self.user_data["username"]] = self.user_data[
                "password"
            ]

            print()
            print("--- Creating first admin email and email password ---")
            while True:
                print("Email: ", end="")
                sub_e = input()
                if "@" in sub_e and sub_e.index("@") > 0:
                    self.user_data["email"] = sub_e
                    break
                else:
                    print(
                        "\nSorry but email must be a valid email address. (with an '@' symbol)"
                    )
            while True:
                print("Email password: ", end="")
                sub_ep = input()
                if len(sub_ep) < 8:
                    print("\nSorry but password must be at least 8 characters.")
                else:
                    self.user_data["e-password"] = _password_formatter(
                        password=sub_ep, f="c"
                    )
                    break

            print()
            print(
                'Please check your real life gmail and there should be one gmail from "that1.stinkyarmpits@gmail.com".'
            )

            self._verification_code = randint(100_000, 999_999)
            sender_email = "that1.stinkyarmpits@gmail.com"
            receiver_email = self.user_data["email"]
            subject = "Email verification"
            message = f"{self._verification_code} is your one-time email verification code; enter this 6-digit code in the cmdp to continue."
            text = f"Subject: {subject}\n\n{message}"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, "uxse vldv kqmx ribr")
            server.sendmail(sender_email, receiver_email, text)
            while True:
                user_verifycode = input(
                    "Please enter the code sent to your gmail account: "
                )
                if user_verifycode == str(self._verification_code):
                    break
                else:
                    print("This isn't your email verification code. Please retry.")

            self.user_data["eaps"][self.user_data["email"]] = self.user_data[
                "e-password"
            ]

            print()
            os.system("cls" if os.name == "nt" else "clear")
            print("----- Login to created admin account -----")
            print("--- Log into admin user ---")
            user_u = input("Username: ")
            user_p = input("Password: ")
            sleep(0.5)
            print("--- Log into admin email ---")
            user_e = input("Email: ")
            user_ep = input("E-Password (email password): ")
            if (
                user_u == self.user_data["username"]
                and user_p
                == _password_formatter(password=self.user_data["password"], f="dc")
                and user_e == self.user_data["email"]
                and user_ep
                == _password_formatter(password=self.user_data["e-password"], f="dc")
            ):
                self.user_data["downloads"][user_u]: list = []
                self.user_data["admin"] = True
                print(
                    "\nSuccessfully logged in user {}!".format(
                        self.user_data["username"]
                    )
                )
                self.current_account = self.user_data["username"]
                sleep(1)
                print()
                self.user_data["u-ranks"][self.user_data["username"]] = self.ranks[0]
                print(
                    "Your jit rank is {}! (everybody starts off with this rank)".format(
                        self.user_data["u-ranks"][self.user_data["username"]]
                    )
                )
                self.user_data["u-google-search-history"][
                    self.user_data["username"]
                ] = []
                with open("user_data.dat", "wb") as f:
                    pickle.dump(self.user_data, f)
                sleep(1)
            else:
                print("There was an error so the system will terminate in 3 seconds...")
                sleep(3)
                sys.exit()
        else:
            sleep(1.5)
            print("----- Login to an account -----")
            user_u = input("Username: ")
            user_p = input("Password: ")
            sleep(0.5)
            print("--- Log into email ---")
            user_e = input("Email: ")
            user_ep = input("E-Password (email password): ")
            print()
            print(
                'Please check your real life gmail and there should be one gmail from "that1.stinkyarmpits@gmail.com".'
            )

            self._verification_code = randint(100_000, 999_999)
            sender_email = "that1.stinkyarmpits@gmail.com"
            receiver_email = self.user_data["email"]
            subject = "Email verification"
            message = f"{self._verification_code} is your one-time email verification code; enter this 6-digit code in the cmdp to continue."
            text = f"Subject: {subject}\n\n{message}"
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, "uxse vldv kqmx ribr")
            server.sendmail(sender_email, receiver_email, text)
            while True:
                user_verifycode = input(
                    "Please enter the code sent to your gmail account: "
                )
                if user_verifycode == str(self._verification_code):
                    break
                else:
                    print("This isn't your email verification code. Please retry.")
            if (
                user_u == self.user_data["username"]
                and user_p
                == _password_formatter(password=self.user_data["password"], f="dc")
                and user_e == self.user_data["email"]
                and user_ep
                == _password_formatter(password=self.user_data["e-password"], f="dc")
            ):
                with open("user_data.dat", "wb") as f:
                    pickle.dump(self.user_data, f)
                print(
                    "\nSuccessfully logged in user {}!".format(
                        self.user_data["username"]
                    )
                )
                self.current_account = self.user_data["username"]
                sleep(1)

    def copyright(self):
        print()
        print(
            "\033[0mCopyright (c) 2023-____ Torrez's Command Prompt Software Foundation."
        )
        print("All Rights Reserved.\n")
        sleep(1)

    def tips(self):
        print(
            "We recommend you to run this in the command prompt to enhance you experience\ninto Torrez's command prompt.\n"
        )
        print(
            "If you want to exit the loop, you can just kill the terminal or exit the\ncommand prompt software (not the one made by Torrez) to quit the program.\n"
        )
        sleep(1)
        print(
            "DISCLAIMER: This program does not and has no rights to share personal information online."
        )
        sleep(1)

        print('Type "jit help" or "help" for more information.')
        sleep(2)

        print(
            "# ---------------------------------------------------------------------------- #"
        )
        print(
            "# ---------------------------------------------------------------------------- #\n"
        )

    def load(self, reason: str | Literal["sc"]) -> None:
        if reason == "sc":
            sleep(uniform(0, 1.5))
            print("\033[34m[\033[32m| \033[34m]\033[0m Finding command...")
            sleep(uniform(0, 1.25))
            print("\033[34m[\033[32m||\033[34m]\033[0m Preparing results...\n")

    def pc_ver_info(self):
        vi = _version_info()
        return f"version info: \n\tmajor: {vi.major}\n\tminor: {vi.minor}\n\tmicro: {vi.micro}\n"

    def addUseCount(self, amount: int | None = 1, /):
        self.__cmdUseCount += amount

    def resetUseCount(self, /):
        self.__cmdUseCount = 0


class resetUserSettings(cmdp):
    def __init__(self) -> None:
        super().__init__()
        self.user_data["username"] = "user"
        self.user_data["password"] = ""
        self.user_data["email"] = "user@example.com"
        self.user_data["e-password"] = ""

        with open("user_data.dat", "wb") as f:
            pickle.dump(self.user_data, f)


class Time:
    def __new__(self):
        now = datetime.now()
        return f"Time: {now:%Y-%m-%d %H:%M:%S.%f}"


class _version:
    def __new__(self):
        vi = _version_info()
        return "{}.{}.{}".format(vi.major, vi.minor, vi.micro)


class _version_info:
    def __init__(self) -> None:
        self._major = 0
        self._minor = 0
        self._micro = 1

    @property
    def major(self) -> int:
        return self._major

    @property
    def minor(self) -> int:
        return self._minor

    @property
    def micro(self) -> int:
        return self._micro

    @major.setter
    def major(self, value: int):
        self._major = value

    @minor.setter
    def minor(self, value: int):
        self._minor = value

    @micro.setter
    def micro(self, value: int):
        self._micro = value


def main() -> None:
    cmd = cmdp()
    return None


if __name__ == "__main__":
    main()

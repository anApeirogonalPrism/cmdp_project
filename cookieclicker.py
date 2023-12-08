import pygame
import sys
from threading import Thread
from time import sleep, time


class CookieClicker:
    class description:
        class cursor:
            def __init__(self) -> None:
                self.first = "prod prod"
                self.second = "it... it hurts to click..."
                self.third = "Look ma, both hands!"
                self.fourth = "clickity"

            @property
            def reinforced_index_finger(self):
                return self.first

    def __init__(self) -> None:
        # self.background =
        # self.music =

        self.cookies = 0
        self.cookie_per_click = 1
        self.cookie = pygame.Rect(400 - 150, 400 - 250, 300, 300)
        self.cookie_color = "#522920"
        self.clicked = False

        # ! User Clicks
        self.user_click_upgradeBtn = pygame.Rect(10, 50, 185, 75)
        self.user_click_cost = 15

        # ! Cursors
        self.cursors = 0
        self.cursor_multiplier = 1
        self.cursors_upgradeBtn = pygame.Rect(10, 150, 185, 75)
        self.cursor_assister_cost = 50

        self.tier_cursor_upgradeBtn = pygame.Rect(10, 250, 185, 75)

        self.tiercursorpick = 1

        self.click_efficiency = 0

        # ! Grannies
        self.grannies = 0
        self.grannycost = 100
        self.buy_granny_Btn = pygame.Rect(580, 50, 185, 75)
        self.grannies_upgradeBtn = pygame.Rect(580, 150, 185, 75)
        self.granny_multiplier = 1

        self.grannypick = 1

        # ! Farms
        self.farms = 0
        self.farm_multiplier = 1
        self.farmscost = 1100
        self.buy_farm_Btn = pygame.Rect(580, 250, 185, 75)
        self.farms_upgradeBtn = pygame.Rect(580, 350, 185, 75)

        self.farmpick = 1

        # ! Multi-threading
        self.cursors_A = Thread(target=self.cursor_assist)
        self.cursors_A.start()
        self.grannies_A = Thread(target=self.granny_assist)
        self.grannies_A.start()
        self.farm_A = Thread(target=self.farm_assist)
        self.farm_A.start()

        self.tcursorsc = Thread(target=self.tcursor_cost)
        self.tcursorsc.start()

        self.granniesc = Thread(target=self.grannies_cost)
        self.granniesc.start()

        self.granniestier = Thread(target=self.grannies_needed)
        self.granniestier.start()

        self.farmsc = Thread(target=self.farms_cost)
        self.farmsc.start()

        self.farmstier = Thread(target=self.farms_needed)
        self.farmstier.start()

        self.game_font = pygame.font.Font(None, 28)

    def tcursor_cost(self) -> None:
        while True:
            if self.tiercursorpick == 1:
                self.cursorsneeded = 1
                self.tier_cursor_cost = 100
            elif self.tiercursorpick == 2:
                self.cursorsneeded = 1
                self.tier_cursor_cost = 500
            elif self.tiercursorpick == 3:
                self.cursorsneeded = 10
                self.tier_cursor_cost = 10000
            elif self.tiercursorpick == 4:
                self.cursorsneeded = 25
                self.tier_cursor_cost = 100_000
            elif self.tiercursorpick == 5:
                self.cursorsneeded = 50
                self.tier_cursor_cost = 10_000_000
            elif self.tiercursorpick == 6:
                self.cursorsneeded = 100
                self.tier_cursor_cost = 100_000_000
            elif self.tiercursorpick == 7:
                self.cursorsneeded = 150
                self.tier_cursor_cost = 1_000_000_000
            elif self.tiercursorpick == 8:
                self.cursorsneeded = 200
                self.tier_cursor_cost = 10_000_000_000
            elif self.tiercursorpick == 9:
                self.cursorsneeded = 250
                self.tier_cursor_cost = 10_000_000_000_000
            elif self.tiercursorpick == 10:
                self.cursorsneeded = 300
                self.tier_cursor_cost = 10_000_000_000_000_000
            elif self.tiercursorpick == 11:
                self.cursorsneeded = 350
                self.tier_cursor_cost = 10_000_000_000_000_000_000
            elif self.tiercursorpick == 12:
                self.cursorsneeded = 400
                self.tier_cursor_cost = 10_000_000_000_000_000_000_000
            elif self.tiercursorpick == 13:
                self.cursorsneeded = 450
                self.tier_cursor_cost = 10_000_000_000_000_000_000_000_000
            elif self.tiercursorpick == 14:
                self.cursorsneeded = 500
                self.tier_cursor_cost = 10_000_000_000_000_000_000_000_000_000
            elif self.tiercursorpick == 15:
                self.cursorsneeded = 550
                self.tier_cursor_cost = 10_000_000_000_000_000_000_000_000_000_000
            elif self.tiercursorpick == 16:
                self.cursorsneeded = 600
                self.tier_cursor_cost = 10_000_000_000_000_000_000_000_000_000_000_000

    def grannies_cost(self) -> None:
        while True:
            if self.grannypick == 1:
                self.granny_cost = 1000
            elif self.grannypick == 2:
                self.granny_cost = 5_000
            elif self.grannypick == 3:
                self.granny_cost = 50_000
            elif self.grannypick == 4:
                self.granny_cost = 5_000_000
            elif self.grannypick == 5:
                self.granny_cost = 500_000_000
            elif self.grannypick == 6:
                self.granny_cost = 50_000_000_000
            elif self.grannypick == 7:
                self.granny_cost = 50_000_000_000_000
            elif self.grannypick == 8:
                self.granny_cost = 50_000_000_000_000_000
            elif self.grannypick == 9:
                self.granny_cost = 50_000_000_000_000_000_000
            elif self.grannypick == 10:
                self.granny_cost = 50_000_000_000_000_000_000_000
            elif self.grannypick == 11:
                self.granny_cost = 500_000_000_000_000_000_000_000_000
            elif self.grannypick == 12:
                self.granny_cost = 5_000_000_000_000_000_000_000_000_000_000
            elif self.grannypick == 13:
                self.granny_cost = 50_000_000_000_000_000_000_000_000_000_000_000
            elif self.grannypick == 14:
                self.granny_cost = 500_000_000_000_000_000_000_000_000_000_000_000_000
            elif self.grannypick == 15:
                self.granny_cost = (
                    5_000_000_000_000_000_000_000_000_000_000_000_000_000_000
                )

    def grannies_needed(self) -> None:
        while True:
            if self.grannypick == 1:
                self.granniesneeded = 1
            elif self.grannypick == 2:
                self.granniesneeded = 5
            elif self.grannypick == 3:
                self.granniesneeded = 25
            elif self.grannypick == 4:
                self.granniesneeded = 50
            elif self.grannypick == 5:
                self.granniesneeded = 100
            elif self.grannypick == 6:
                self.granniesneeded = 150
            elif self.grannypick == 7:
                self.granniesneeded = 200
            elif self.grannypick == 8:
                self.granniesneeded = 250
            elif self.grannypick == 9:
                self.granniesneeded = 300
            elif self.grannypick == 10:
                self.granniesneeded = 350
            elif self.grannypick == 11:
                self.granniesneeded = 400
            elif self.grannypick == 12:
                self.granniesneeded = 450
            elif self.grannypick == 13:
                self.granniesneeded = 500
            elif self.grannypick == 14:
                self.granniesneeded = 550
            elif self.grannypick == 15:
                self.granniesneeded = 600

    def farms_cost(self) -> None:
        while True:
            if self.farmpick == 1:
                self.farm_cost = 11_000
            elif self.farmpick == 2:
                self.farm_cost = 55_000
            elif self.farmpick == 3:
                self.farm_cost = 550_000
            elif self.farmpick == 4:
                self.farm_cost = 55_000_000
            elif self.farmpick == 5:
                self.farm_cost = 5500_000_000
            elif self.farmpick == 6:
                self.farm_cost = 550_000_000_000
            elif self.farmpick == 7:
                self.farm_cost = 550_000_000_000_000
            elif self.farmpick == 8:
                self.farm_cost = 550_000_000_000_000_000
            elif self.farmpick == 9:
                self.farm_cost = 550_000_000_000_000_000_000
            elif self.farmpick == 10:
                self.farm_cost = 550_000_000_000_000_000_000_000
            elif self.farmpick == 11:
                self.farm_cost = 5_500_000_000_000_000_000_000_000
            elif self.farmpick == 12:
                self.farm_cost = 55_000_000_000_000_000_000_000_000_000_000
            elif self.farmpick == 13:
                self.farm_cost = 550_000_000_000_000_000_000_000_000_000_000_000
            elif self.farmpick == 14:
                self.farm_cost = 5_500_000_000_000_000_000_000_000_000_000_000_000_000
            elif self.farmpick == 15:
                self.farm_cost = (
                    55_000_000_000_000_000_000_000_000_000_000_000_000_000_000
                )

    def farms_needed(self) -> None:
        while True:
            if self.farmpick == 1:
                self.farmsneeded = 1
            elif self.farmpick == 2:
                self.farmsneeded = 5
            elif self.farmpick == 3:
                self.farmsneeded = 25
            elif self.farmpick == 4:
                self.farmsneeded = 50
            elif self.farmpick == 5:
                self.farmsneeded = 100
            elif self.farmpick == 6:
                self.farmsneeded = 150
            elif self.farmpick == 7:
                self.farmsneeded = 200
            elif self.farmpick == 8:
                self.farmsneeded = 250
            elif self.farmpick == 9:
                self.farmsneeded = 300
            elif self.farmpick == 10:
                self.farmsneeded = 350
            elif self.farmpick == 11:
                self.farmsneeded = 400
            elif self.farmpick == 12:
                self.farmsneeded = 450
            elif self.farmpick == 13:
                self.farmsneeded = 500
            elif self.farmpick == 14:
                self.farmsneeded = 550
            elif self.farmpick == 15:
                self.farmsneeded = 600

    def cursor_assist(self) -> None:
        while True:
            if self.cursors > 0:
                each_sec = 1 / (
                    self.cursors * self.cookie_per_click
                )  # (self.cookie_per_click / self.cursors)
                sleep(each_sec)
                self.cookies += self.cursors * self.cursor_multiplier

    def granny_assist(self) -> None:
        while True:
            if self.grannies > 0:
                each_sec = 1 / (self.grannies * self.cookie_per_click)
                sleep(each_sec)
                self.cookies += self.grannies * self.granny_multiplier

    def farm_assist(self) -> None:
        while True:
            if self.farms > 0:
                each_sec = 1 / (self.farms * self.cookie_per_click)
                sleep(each_sec)
                self.cookies += self.farms * self.farm_multiplier

    def scn(self, new_name: str) -> str:
        """scn stands for "set cursor name".

        Args:
            new_name (str): the new name to be assigned to a variable.

        Returns:
            str: a new name to be assigned.
        """
        return new_name

    def upgrade(self):
        self.user_click = self.game_font.render(
            f"+{round(self.cookie_per_click*1.3, 3)} cookies per click.",
            True,
            "#ffffff",
        )
        if self.cookies >= self.user_click_cost:
            self.user_click_display_cost = text_font.render(
                f"Cost: {str(round(self.user_click_cost, 3))} c.",
                True,
                "#ffffff",
            )
        else:
            self.user_click_display_cost = text_font.render(
                f"Cost: {str(round(self.user_click_cost, 3))} c.",
                True,
                "#ff0000",
            )

        self.click_assist_label = self.game_font.render(
            "+1 cursor(s).", True, "#ffffff"
        )
        if self.cookies >= self.cursor_assister_cost:
            self.click_assist_display_cost = text_font.render(
                f"Cost: {str(round(self.cursor_assister_cost, 2))} c.",
                True,
                "#ffffff",
            )
        else:
            self.click_assist_display_cost = text_font.render(
                f"Cost: {str(round(self.cursor_assister_cost, 2))} c.",
                True,
                "#ff0000",
            )

        if self.tiercursorpick == 1:
            self.tier_cursor_displayer = self.game_font.render(
                "Reinforced Index Finger",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 2:
            self.tier_cursor_displayer = self.game_font.render(
                "Carpal Tunnel Prevention Cream",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 3:
            self.tier_cursor_displayer = self.game_font.render(
                "Ambidextrous",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 4:
            self.tier_cursor_displayer = self.game_font.render(
                "Thousand Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 5:
            self.tier_cursor_displayer = self.game_font.render(
                "Million Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 6:
            self.tier_cursor_displayer = self.game_font.render(
                "Billion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 7:
            self.tier_cursor_displayer = self.game_font.render(
                "Trillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 8:
            self.tier_cursor_displayer = self.game_font.render(
                "Quadrillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 9:
            self.tier_cursor_displayer = self.game_font.render(
                "Quintillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 10:
            self.tier_cursor_displayer = self.game_font.render(
                "Sextillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 11:
            self.tier_cursor_displayer = self.game_font.render(
                "Septillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 12:
            self.tier_cursor_displayer = self.game_font.render(
                "Octillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 13:
            self.tier_cursor_displayer = self.game_font.render(
                "Nonillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 14:
            self.tier_cursor_displayer = self.game_font.render(
                "Decillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 15:
            self.tier_cursor_displayer = self.game_font.render(
                "Undecillion Fingers",
                True,
                "#ffffff",
            )
        elif self.tiercursorpick == 16:
            self.tier_cursor_displayer = self.game_font.render(
                "Duodecillion Fingers",
                True,
                "#ffffff",
            )

        if self.grannypick == 1:
            self.granny_displayer = self.game_font.render(
                "Forwards from grandma",
                True,
                "#ffffff",
            )
        elif self.grannypick == 2:
            self.granny_displayer = self.game_font.render(
                "Steel-plated rolling pins",
                True,
                "#ffffff",
            )
        elif self.grannypick == 3:
            self.granny_displayer = self.game_font.render(
                "Lubricated dentures",
                True,
                "#ffffff",
            )
        elif self.grannypick == 4:
            self.granny_displayer = self.game_font.render(
                "Prune juice",
                True,
                "#ffffff",
            )
        elif self.grannypick == 5:
            self.granny_displayer = self.game_font.render(
                "Double-thick glasses",
                True,
                "#ffffff",
            )
        elif self.grannypick == 6:
            self.granny_displayer = self.game_font.render(
                "Aging agents",
                True,
                "#ffffff",
            )
        elif self.grannypick == 7:
            self.granny_displayer = self.game_font.render(
                "Xtreme walkers",
                True,
                "#ffffff",
            )
        elif self.grannypick == 8:
            self.granny_displayer = self.game_font.render(
                "The Unbridling",
                True,
                "#ffffff",
            )
        elif self.grannypick == 9:
            self.granny_displayer = self.game_font.render(
                "Reverse dementia",
                True,
                "#ffffff",
            )
        elif self.grannypick == 10:
            self.granny_displayer = self.game_font.render(
                "Timeproof hair dyes",
                True,
                "#ffffff",
            )
        elif self.grannypick == 11:
            self.granny_displayer = self.game_font.render(
                "Good manners",
                True,
                "#ffffff",
            )
        elif self.grannypick == 12:
            self.granny_displayer = self.game_font.render(
                "Generation degeneration",
                True,
                "#ffffff",
            )
        elif self.grannypick == 13:
            self.granny_displayer = self.game_font.render(
                "Visits",
                True,
                "#ffffff",
            )
        elif self.grannypick == 14:
            self.granny_displayer = self.game_font.render(
                "Kitchen cabinets",
                True,
                "#ffffff",
            )
        elif self.grannypick == 15:
            self.granny_displayer = self.game_font.render(
                "Foam-tipped canes",
                True,
                "#ffffff",
            )

        if self.farmpick == 1:
            self.farm_displayer = self.game_font.render(
                "Cheap hoes",
                True,
                "#ffffff",
            )
        elif self.farmpick == 2:
            self.farm_displayer = self.game_font.render(
                "Fertilizer",
                True,
                "#ffffff",
            )
        elif self.farmpick == 3:
            self.farm_displayer = self.game_font.render(
                "Cookie trees",
                True,
                "#ffffff",
            )
        elif self.farmpick == 4:
            self.farm_displayer = self.game_font.render(
                "Genetically-modified cookies",
                True,
                "#ffffff",
            )
        elif self.farmpick == 5:
            self.farm_displayer = self.game_font.render(
                "Gingerbread scarecrows",
                True,
                "#ffffff",
            )
        elif self.farmpick == 6:
            self.farm_displayer = self.game_font.render(
                "Pulsar sprinklers",
                True,
                "#ffffff",
            )
        elif self.farmpick == 7:
            self.farm_displayer = self.game_font.render(
                "Fudge fungus",
                True,
                "#ffffff",
            )
        elif self.farmpick == 8:
            self.farm_displayer = self.game_font.render(
                "Wheat triffids",
                True,
                "#ffffff",
            )
        elif self.farmpick == 9:
            self.farm_displayer = self.game_font.render(
                "Humane pesticides",
                True,
                "#ffffff",
            )
        elif self.farmpick == 10:
            self.farm_displayer = self.game_font.render(
                "Barnstars",
                True,
                "#ffffff",
            )
        elif self.farmpick == 11:
            self.farm_displayer = self.game_font.render(
                "Lindworms",
                True,
                "#ffffff",
            )
        elif self.farmpick == 12:
            self.farm_displayer = self.game_font.render(
                "Global seed vault",
                True,
                "#ffffff",
            )
        elif self.farmpick == 13:
            self.farm_displayer = self.game_font.render(
                "Reverse-veganism",
                True,
                "#ffffff",
            )
        elif self.farmpick == 14:
            self.farm_displayer = self.game_font.render(
                "Cookie mulch",
                True,
                "#ffffff",
            )
        elif self.farmpick == 15:
            self.farm_displayer = self.game_font.render(
                "Self-driving tractors",
                True,
                "#ffffff",
            )

        # ---------------------------------------------------------------------------------------------------- #
        # ---------------------------------------------------------------------------------------------------- #
        # ---------------------------------------------------------------------------------------------------- #
        # ---------------------------------------------------------------------------------------------------- #

        if self.cookies >= self.granny_cost:
            self.granny_display_cost = text_font.render(
                f"Cost: {str(round(self.granny_cost, 2))} c.",
                True,
                "#ffffff",
            )
        else:
            self.granny_display_cost = text_font.render(
                f"Cost: {str(round(self.granny_cost, 2))} c.",
                True,
                "#ff0000",
            )

        if self.cookies >= self.farm_cost:
            self.farm_display_cost = text_font.render(
                f"Cost: {str(round(self.farm_cost, 2))} c.",
                True,
                "#ffffff",
            )
        else:
            self.farm_display_cost = text_font.render(
                f"Cost: {str(round(self.farm_cost, 2))} c.",
                True,
                "#ff0000",
            )

        if self.cursors >= self.cursorsneeded:
            if self.cookies >= self.tier_cursor_cost:
                self.tier_cursor_display_cost = text_font.render(
                    f"Cost: {str(round(self.tier_cursor_cost, 2))} c.",
                    True,
                    "#ffffff",
                )
            else:
                self.tier_cursor_display_cost = text_font.render(
                    f"Cost: {str(round(self.tier_cursor_cost, 2))} c.",
                    True,
                    "#ff0000",
                )

        pygame.draw.rect(
            screen, "#488ebd", self.user_click_upgradeBtn, border_radius=15
        )
        pygame.draw.rect(screen, "#488ebd", self.cursors_upgradeBtn, border_radius=15)

        # tier cursor
        if self.cursors >= self.cursorsneeded and self.tiercursorpick in list(
            range(1, 17)
        ):
            pygame.draw.rect(
                screen, "#488ebd", self.tier_cursor_upgradeBtn, border_radius=15
            )
            screen.blit(self.tier_cursor_displayer, (15, 255))
            screen.blit(self.tier_cursor_display_cost, (15, 285))

        # Grannies
        if self.cursors >= 1:
            self.grannies_label = self.game_font.render(
                "+1 granny(s/ies)", True, "#ffffff"
            )
            if self.cookies >= self.grannycost:
                self.grannies_display_cost = text_font.render(
                    f"Cost: {str(round(self.grannycost, 2))} c.",
                    True,
                    "#ffffff",
                )
            else:
                self.grannies_display_cost = text_font.render(
                    f"Cost: {str(round(self.grannycost, 2))} c.",
                    True,
                    "#ff0000",
                )

            pygame.draw.rect(screen, "#488ebd", self.buy_granny_Btn, border_radius=15)
            screen.blit(self.grannies_label, (585, 55))
            screen.blit(self.grannies_display_cost, (585, 85))

        if self.grannies >= self.granniesneeded:
            pygame.draw.rect(
                screen, "#488ebd", self.grannies_upgradeBtn, border_radius=15
            )
            screen.blit(self.granny_displayer, (585, 155))
            screen.blit(self.granny_display_cost, (585, 185))

        # Farms
        if self.grannies >= 1:
            self.farms_label = self.game_font.render(
                "+1 farm(s)",
                True,
                "#ffffff",
            )
            if self.cookies >= self.farmscost:
                self.farms_display_cost = text_font.render(
                    f"Cost: {str(round(self.farmscost, 2))} c.", True, "#ffffff"
                )
            else:
                self.farms_display_cost = text_font.render(
                    f"Cost: {str(round(self.farmscost, 2))} c.", True, "#ff0000"
                )

            pygame.draw.rect(screen, "#488ebd", self.buy_farm_Btn, border_radius=15)
            screen.blit(self.farms_label, (585, 255))
            screen.blit(self.farms_display_cost, (585, 285))

        if self.farms >= self.farmsneeded:
            pygame.draw.rect(screen, "#488ebd", self.farms_upgradeBtn, border_radius=15)
            screen.blit(self.farm_displayer, (585, 355))
            screen.blit(self.farm_display_cost, (585, 385))

        screen.blit(self.user_click, (15, 55))
        screen.blit(self.user_click_display_cost, (15, 85))

        screen.blit(self.click_assist_label, (15, 155))
        screen.blit(self.click_assist_display_cost, (15, 185))

    def draw_cps(self):
        """The word "cps" is used to indicate how many cookies are being generated in a second."""
        if self.cursors > 0:
            self.display_cps = text_font.render(
                f"Cookies per second: {str(round(self.cookie_per_click, 3))}",
                True,
                "#ffffff",
            )
            if self.cursors >= 1:
                if self.grannies >= 1:
                    if self.farms >= 1:
                        screen.blit(self.display_cps, (0, 475))
                    else:
                        screen.blit(self.display_cps, (0, 445))
                else:
                    screen.blit(self.display_cps, (0, 535))

    def draw_click_assisters(self):
        if self.cursors >= 1:
            self.display_click_assisters = text_font.render(
                f"Cursors: {str(self.cursors)}", True, "#ffffff"
            )
            if self.grannies >= 1:
                if self.farms >= 1:
                    screen.blit(self.display_click_assisters, (0, 505))
                else:
                    screen.blit(self.display_click_assisters, (0, 535))
            else:
                screen.blit(self.display_click_assisters, (0, 565))

    def draw_grannies(self):
        if self.grannies >= 1:
            self.display_grannies = text_font.render(
                f"Grannies: {str(self.grannies)}", True, "#ffffff"
            )
            if self.farms >= 1:
                screen.blit(self.display_grannies, (0, 535))
            else:
                screen.blit(self.display_grannies, (0, 565))

    def draw_farms(self):
        if self.farms >= 1:
            self.display_farms = text_font.render(
                f"Farms: {str(self.farms)}", True, "#ffffff"
            )
            screen.blit(self.display_farms, (0, 565))

    def draw_score(self):
        self.display_cookies = text_font.render(
            f"Cookies: {str(round(self.cookies, 2))}", True, "#ffffff"
        )

        if self.cursors == 0:
            screen.blit(self.display_cookies, (0, 565))
        else:
            if self.grannies >= 1:
                if self.farms >= 1:
                    screen.blit(self.display_cookies, (0, 445))
                    self.draw_click_assisters()
                    self.draw_cps()
                else:
                    screen.blit(self.display_cookies, (0, 475))
                    self.draw_click_assisters()
                    self.draw_cps()
            else:
                screen.blit(self.display_cookies, (0, 505))
                self.draw_click_assisters()
                self.draw_cps()

    def click_button(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.cookies += self.cookie_per_click + self.click_efficiency
                    self.clicked = False

        if self.user_click_upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.user_click_cost:
                    self.cookies -= self.user_click_cost

                    upgrade_click.play()

                    self.user_click_cost *= 1.4
                    self.cookie_per_click *= 1.3

        if self.cursors_upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.cursor_assister_cost:
                    self.cookies -= self.cursor_assister_cost

                    upgrade_click.play()
                    self.cursor_assister_cost *= 1.6
                    self.cursors += 1

        if self.tier_cursor_upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cursors >= self.cursorsneeded:
                    if self.cookies >= self.tier_cursor_cost:
                        if self.tiercursorpick in [1, 2, 3]:
                            self.cookie_per_click *= 2
                            self.cursor_multiplier *= 2
                        elif self.tiercursorpick == 4:
                            self.click_efficiency += 0.0001
                        elif self.tiercursorpick == 5:
                            self.click_efficiency *= 5
                        elif self.tiercursorpick == 6:
                            self.click_efficiency *= 10
                        elif self.tiercursorpick in list(range(7, 17)):
                            self.click_efficiency *= 20

                        self.tiercursorpick += 1
                        self.cookies -= self.tier_cursor_cost
                        upgrade_click.play()

        if self.buy_granny_Btn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.grannycost:
                    self.cookies -= self.grannycost

                    upgrade_click.play()
                    self.grannycost *= 1.7
                    self.grannies += 1

        if self.grannies_upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.grannies >= self.granniesneeded:
                    if self.cookies >= self.granny_cost:
                        if self.grannypick in list(range(1, 16)):
                            self.granny_multiplier *= 2

                        self.grannypick += 1
                        self.cookies -= self.granny_cost
                        upgrade_click.play()

        if self.buy_farm_Btn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.cookies >= self.farmscost:
                    self.cookies -= self.grannycost

                    upgrade_click.play()
                    self.farm_cost *= 1.8
                    self.farms += 1

        if self.farms_upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.farms >= self.farmsneeded:
                    if self.cookies >= self.farm_cost:
                        if self.farmpick in list(range(1, 16)):
                            self.farm_multiplier *= 2

                        self.farmpick += 1
                        self.cookies -= self.farm_cost
                        upgrade_click.play()

        pygame.draw.rect(screen, self.cookie_color, self.cookie, border_radius=150)

    def render(self):
        self.click_button()
        self.draw_score()
        self.draw_grannies()
        self.draw_farms()
        self.upgrade()


pygame.init()
cc = CookieClicker()

width = 800
height = 600

screen = pygame.display.set_mode(size=(width, height))
pygame.display.set_caption("Cookie Clicker")
text_font = pygame.font.Font(
    "assets/pixely[1].ttf",
    18,
)
title = text_font.render("Cookie Clicker", True, "#00aa00")
background = pygame.image.load("assets/cookieclicker_background.jpg").convert()

upgrade_click = pygame.mixer.Sound("assets/cookieclicker_upgrade.wav")

clock = pygame.time.Clock()

while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(title, (310, 15))
    cc.render()
    pygame.display.update()
    clock.tick(360)

from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class BurgerShopArchipelagoOptions:
    pass

# Main Class
class PaulBlartMallCopGame(Game):
    name = "Burger Shop"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = BurgerShopArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="No Burgerbot",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="No Cookies",
                data=dict(),
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Get Perfect on AMOUNT RESTAURANT Levels in Story Mode",
                data={
                    "AMOUNT": (self.levels, 1),
                    "RESTAURANT": (self.restaurant_base, 1),         
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Get Perfect on AMOUNT RESTAURANT Levels in Expert Story Mode",
                data={
                    "AMOUNT": (self.levels, 1),
                    "RESTAURANT": (self.restaurant_base, 1),   
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
             GameObjectiveTemplate(
                label="Get a MEDAL medal on RESTAURANT in Relax mode",
                data={
                    "MEDAL": (self.medal_base, 1),
                    "RESTAURANT": (self.restaurant_base, 1),   
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Get a MEDAL medal on RESTAURANT in Challenge mode",
                data={
                    "MEDAL": (self.medal_base, 1),
                    "RESTAURANT": (self.restaurant_base, 1),   
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            )
        ]

    # Datasets
    @staticmethod
    def restaurant_base() -> List[str]:
        return [
            "Diner",
            "Saloon",
            "City",
            "Boardwalk",
            "Sports Bar",
            "Beach Hut",
            "Pagoda",
            "Spaceship"
        ]
    @staticmethod
    def levels() -> range:
        return range(1, 10)
    @staticmethod
    def medal_base() -> List[str]:
        return [
            "Silver",
            "Gold",
            "Bronze"
        ]
from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SeaOfThievesArchipelagoOptions:
    sea_of_thieves_include_athenas_fortune: SeaOfThievesIncludeAthenasFortune
    sea_of_thieves_include_sunken_kingdom: SeaOfThievesIncludeSunkenKingdom
    sea_of_thieves_include_tall_tales: SeaOfThievesIncludeTallTales

class SeaOfThievesGame(Game):
    name = "Sea of Thieves"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
        KeymastersKeepGamePlatforms.XONE,
    ]

    is_adult_only_or_unrated = False

    options_cls = SeaOfThievesArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Set sail as the following ship type: SHIP_TYPE",
                data={
                    "SHIP_TYPE": (self.ship_types, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Sail while flying the Flag Of The Reaper's Mark",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Complete any Emergent Encounters (Skeleton Ship, Meg, Kraken)",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Sell all the loot you collect before moving on to the next voyage",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Don't sell any loot acquired during challenges",
                data=dict(),
            )
        ]
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Complete the following: VOYAGE",
                data={
                    "VOYAGE": (self.voyages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Complete the following: VOYAGES",
                data={
                    "VOYAGES": (self.voyages, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Complete VOYAGES",
                data={
                    "VOYAGES": (self.voyages, 5),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete MEDLEY_VOYAGE",
                data={
                    "MEDLEY_VOYAGE": (self.medley_voyages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete VOYAGE while only using WEAPONS",
                data={
                    "VOYAGE": (self.voyages, 1),
                    "WEAPONS": (self.weapons, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete VOYAGES while only using WEAPONS",
                data={
                    "VOYAGES": (self.voyages, 3),
                    "WEAPONS": (self.weapons, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete VOYAGES while only using WEAPONS",
                data={
                    "VOYAGES": (self.voyages, 5),
                    "WEAPONS": (self.weapons, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete the following world event: WORLD_EVENT",
                data={
                    "WORLD_EVENT": (self.world_events, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete the following world event: WORLD_EVENT while only using WEAPONS",
                data={
                    "WORLD_EVENT": (self.world_events, 1),
                    "WEAPONS": (self.weapons, 2),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Reach Emissary level 5 in the TRADING_COMPANY",
                data={
                    "TRADING_COMPANY": (self.trading_companies, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ]

        return templates

    @property
    def include_athena_voyages(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_athenas_fortune.value)
    
    @property
    def include_sunken_kingdom(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_sunken_kingdom.value)
    
    @property 
    def include_tall_tales(self) -> bool:
        return bool(self.archipelago_options.sea_of_thieves_include_tall_tales.value)
    
    @staticmethod
    def ship_types() -> List[str]:
        return [
            "Sloop",
            "Brigantine",
            "Galleon",
        ]
    
    
    @staticmethod
    def world_events() -> List[str]:
        return [
            "Skeleton Fort",
            "Fort of Fortune",
            "Skeleton Fleet",
            "Ghost Fleet",
            "Ashen Winds",
            "Burning Blade",
            "Fort of Damned",
        ]
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "Cutlass",
            "Flintlock",
            "Blunderbuss",
            "Eye of Reach",
            "Double Barrel Pistol",
            "Throwing Knives",
            "Grapple Gun",
            "Blowpipe",
        ]

    @functools.cached_property
    def trading_companies_base(self) -> List[str]:
        return [
            "Gold Hoarders",
            "Order of Souls",
            "Merchant Alliance",
            "The Hunter's Call",
        ]
    
    @functools.cached_property
    def trading_companies_legend(self) -> List[str]:
        return [
            "Athena's Fortune"
        ]
    
    def trading_companies(self) -> List[str]:
        trading_companies: List[str] = self.trading_companies_base[:]

        if self.include_athena_voyages:
            trading_companies.extend(self.trading_companies_legend[:])

        return sorted(trading_companies)
    
    @functools.cached_property
    def voyages_base(self) -> List[str]:
        return [
            "A Pirate's Treasure Map",
            "A Captain's Treasure Map",
            "An Ashen Pirate's Treasure Map",
            "An Ashen Captain's Treasure Map",
            "A Pirate's Riddle Quest",
            "A Captain's Riddle Quest",
            "An Ashen Pirate's Riddle Quest",
            "An Captain's Riddle Quest",
            "A Pirate's Treasure Vault",
            "A Captain's Treasure Vault",
            "An Ashen Pirate's Treasure Vault",
            "An Ashen Captain's Treasure Vault",
            "A Raid on a Sea Fort",
            "A Raid on a Skeleton Camp",
            "An Adventure to a Sunken Shrine",
            "A Raid on a Sunken Treasury",
            "A Duel with an Ashen Lord",
            "A Raid on a Skeleton Fort",
            "A Battle with a Skeleton Fleet",
            "A Battle with the Burning Blade's Armada",
            "A Bounty for a Skeleton Crew",
            "A Bounty for Skeleton Captains",
            "A Bounty for a Skeleton Lord",
            "An Ashen Bounty for a Skeleton Crew",
            "An Ashen Bounty for Skeleton Captains",
            "An Ashen Bounty for a Skeleton Lord",
            "A Battle with a Ghost Armada",
            "An Ashen Battle with a Ghost Armada",
            "A Founder's Merchant Contract",
            "An Executive's Merchant Contract",
            "A Founder's Cargo Run",
            "An Executive's Cargo Run",
            "An Ashen Founder's Cargo Run",
            "An Ashen Executive's Cargo Run",
            "An Executive's Lost Shipment",
            "An Ashen Executive's Lost Shipment",
            "A Pirate's Fishing Map",
            "A Hunter's Fishing Map",
            "A Pirate's Boar Hunt",
            "A Tracker's Megalodon Hunt",
            "Search for Ancient Secrets",
        ]
    
    @functools.cached_property
    def voyages_athena(self) -> List[str]:
        return [
            "A Legendary Search for Cursed Treasure",
            "A Legendary Search for the Skull of Destiny",
        ]
    
    @functools.cached_property
    def voyages_sunkenKingdom(self) -> List[str]:
        return [
            "The Legend of the Sunken Kingdom"
        ]
    
    @functools.cached_property
    def voyages_tallTales(self) -> List[str]:
        return [
            "Maiden Voyage",
            "The Shroudbreaker",
            "The Cursed Rogue",
            "The Legendary Storyteller",
            "Stars of a thief",
            "Wild Rose",
            "The Art of the Trickster",
            "The Fate of the Morningstar",
            "Revenge of the Morningstar",
            "Shores of Gold",
            "The Seabound Soul icon",
            "A Pirate's Life",
            "The Sunken Pearl",
            "Captains of the Damned",
            "Dark Brethren",
            "Lords of the Sea",
            "The Journey to Melee Island",
            "The Quest for Guybrush",
            "The Lair of LeChuck",
        ]
    
    def voyages(self) -> list[str]:
        voyages: List[str] = self.voyages_base[:]

        if self.include_athena_voyages:
            voyages.extend(self.voyages_athena[:])

        if self.include_sunken_kingdom:
            voyages.extend(self.voyages_sunkenKingdom[:])

        if self.include_tall_tales:
            voyages.extend(self.voyages_tallTales[:])

        return sorted(voyages)

    @functools.cached_property
    def medley_voyages_base() -> List[str]:
        return [
            "A Medley of Gold Hoarders Voyages",
            "An Ashen Medley of Gold Hoarders Voyages",
            "A Medley of Order of Souls Voyages",
            "An Ashen Medley of Order of Souls Voyages",
            "A Medley of Merchant Alliance Voyages",
            "An Ashen Medley of Merchant Alliance Voyages",
        ]
    
    @functools.cached_property
    def medley_voyages_athena() -> List[str]:
        return [
            "A Voyage of Legends",
            "An Ashen Voyage of Legends",
            "Legend of the Veil",
        ]
    
    def medley_voyages(self) -> list[str]:
        medley_voyages: List[str] = self.medley_voyages_base[:]

        if self.include_athena_voyages:
            medley_voyages.extend(self.medley_voyages_athena[:])

        return sorted(medley_voyages)


# Archipelago Options
class SeaOfThievesIncludeAthenasFortune(Toggle):
    """
    If true, Athena's Fortune Voyages will be included in the voyage pool.
    """

    display_name = "Sea of Thieves Include Athena's Fortune Voyages"

class SeaOfThievesIncludeSunkenKingdom(Toggle):
    """
    If true, The Legend of the Sunken Kingdom Voyage will be included in the voyage pool.
    """

    display_name = "Sea of Thieves Include Legend of the Sunken Kingdom"

class SeaOfThievesIncludeTallTales(Toggle):
    """
    If True, Tall Tale Voyages will be included in the voyage pool.
    """

    display_name = "Sea of Thieves Include Tall Tales"

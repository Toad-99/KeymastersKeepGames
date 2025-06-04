from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SidMeiersPiratesArchipelagoOptions:
    pass

class SidMeiersPiratesGame(Game):
    name = "Sid Meier's Pirates"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XBOX,
        KeymastersKeepGamePlatforms.X360,
        KeymastersKeepGamePlatforms.PSP,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.WII,
    ]

    is_adult_only_or_unrated = False

    options_cls = SidMeiersPiratesArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Whenever possible choose WEAPON",
                data={
                    "WEAPON": (self.weapons, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Never use the following cannon shot type: CANNON_TYPE",
                data={
                    "CANNON_TYPE": (self.cannon_types, 1),
                },
            ),
            GameObjectiveTemplate(
                label="If possible, only do business with the following factions: MAIN_FACTION, SUB_FACTION",
                data={
                    "MAIN_FACTION": (self.main_factions, 1),
                    "SUB_FACTION": (self.sub_factions, 1),
                },
            ),
        ]
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Dig up some buried treasure or find a lost city.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Rescue a family member.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Achieve the best outcome in the Dancing Minigame.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Marry a governor's daughter.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Marry a Beautiful governor's daughter.",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Gift a governor's daughter a GIFT.",
                data={
                    "GIFT": (self.gifts, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Best the following pirate in combat: FAMOUS_PIRATE.",
                data={
                    "FAMOUS_PIRATE": (self.famous_pirates, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Best the following pirates in combat: FAMOUS_PIRATE.",
                data={
                    "FAMOUS_PIRATE": (self.famous_pirates, 2),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Become the Most Famous Pirate in the Caribbean.",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Sneak into a city and enter the SNEAK_LOCATION.",
                data={
                    "SNEAK_LOCATION": (self.sneak_locations, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Sack the following city: CITY.",
                data={
                    "CITY": (self.cities, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Sack the following cities: CITIES.",
                data={
                    "CITIES": (self.cities, 3),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Have the following ship type in your fleet: SHIP_TYPES.",
                data={
                    "SHIP_TYPES": (self.ship_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Have the following ship types in your fleet: SHIP_TYPES.",
                data={
                    "SHIP_TYPES": (self.ship_types, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Have the following ship types in your fleet: SHIP_TYPES.",
                data={
                    "SHIP_TYPES": (self.ship_types, 4),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a fencing minigame without taking any hits.",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Have a ship with UPGRADE.",
                data={
                    "UPGRADE": (self.upgrades, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Have a ship with UPGRADE.",
                data={
                    "UPGRADE": (self.upgrades, 3)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Have a ship with UPGRADE.",
                data={
                    "UPGRADE": (self.upgrades, 5)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Recruit a SPECIALIST to join your crew.",
                data={
                    "SPECIALIST": (self.specialists, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Recruit the following specialists: SPECIALIST.",
                data={
                    "SPECIALIST": (self.specialists, 3)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Best the Marquis Montalban in combat.",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
        ]
        
        return templates
    
    @staticmethod
    def weapons() -> List[str]:
        return [
            "Rapier",
            "Longsword",
            "Cutlass",
        ]
    
    @staticmethod
    def cannon_types() -> List[str]:
        return [
            "Round-Shot",
            "Chain-Shot",
            "Grape-Shot",
        ]
    
    @staticmethod
    def main_factions() -> List[str]:
        return [
            "England",
            "France",
            "Dutch",
            "Spain",
        ]
    
    @staticmethod
    def sub_factions() -> List[str]:
        return [
            "Indians",
            "Jesuits",
            "Pirates",
        ]
    
    @staticmethod
    def gifts() -> List[str]:
        return [
            "Ruby Ring",
            "Diamond Necklace",
        ]
    
    @staticmethod
    def famous_pirates() -> List[str]:
        return [
            "Henry Morgan",
            "Blackbeard",
            "Captain Kidd",
            "Jean Lafitte",
            "Stede Bonnet",
            "L'Olennais",
            "Roc Brasiliano",
            "Bart Roberts",
            "Jack Rackham",
        ]
    
    @staticmethod
    def sneak_locations() -> List[str]:
        return [
            "Governor's Mansion",
            "Tavern",
        ]
    
    @staticmethod
    def upgrades() -> List[str]:
        return [
            "Copper Plating",
            "Cotton Sails",
            "Triple Hammocks",
            "Iron Scantlings",
            "Chain-Shot",
            "Grape-Shot",
            "Fine-Grain Powder",
            "Bronze Cannons",
        ]
    
    @staticmethod
    def specialists() -> List[str]:
        return [
            "Carpenter",
            "Cook",
            "Cooper",
            "Gunner",
            "Navigator",
            "Quartermaster",
            "Sailmaker",
            "Surgeon",
        ]
    
    @staticmethod
    def cities() -> List[str]:
        return [
            "St. Eustatius",
            "St. Martin",
            "Curacao",
            "Barbados",
            "Antigua",
            "Nevis",
            "St. Kitts",
            "Eleuthera",
            "Port Royale",
            "Nassau",
            "Grand Bahama",
            "Martinique",
            "Guadelope",
            "Montserrat",
            "Port-de-Paix",
            "Leogane",
            "Tortuga",
            "Petit-Goave",
            "Florida Keys",
            "Trinidad",
            "Margarita",
            "Cumana",
            "San Juan",
            "Caracas",
            "Puerto Cabello",
            "Santo Domingo",
            "Gibraltar",
            "Maracaibo",
            "Rio De La Hacha",
            "Santa Marta",
            "Santiago",
            "Cartenga",
            "Nombre De Dios",
            "Puerto Principe",
            "Puerto Bello",
            "Panama",
            "St. Augustine",
            "Havana",
            "Santa Catalina",
            "Gran Granada",
            "Campeche",
            "Villa Hermosa",
            "Vera Cruz",
        ]
    
    @staticmethod 
    def ship_types() -> List[str]:
        return [
            "Pinnace Class",
            "Sloop Class",
            "Barque Class",
            "Fluyt Class",
            "Brig Class",
            "Merchantman Class",
            "Merchant Galleon Class",
            "Combat Galleon Class",
            "Frigate Class",
        ]

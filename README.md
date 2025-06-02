# KeymastersKeepGames
My game implementations for [Keymasters Keep](https://github.com/SerpentAI/Archipelago/releases?q=keymaster&expanded=true) -
a custom world for [Archipelago](https://archipelago.gg/) - created by SerpentAI.

# Games
- Sea of Thieves
- Sid Meier's Pirates! (2004)
- Burger Shop

## Sea of Thieves
Sea of Thieves is a 2018 action-adventure game developed by Rare and published by Xbox Game Studios. The player assumes the role of a pirate who completes voyages from different trading companies. The multiplayer game sees players explore an open world via a pirate ship from a first-person perspective. Players may encounter each other during their adventures, sometimes forming alliances, and sometimes going head-to-head.

[Steam](https://store.steampowered.com/app/1172620/Sea_of_Thieves_2025_Edition/)

The Keymasters Keep implementation includes trials for each voyage and world events.

### Settings

- **include_difficult_objectives (global option)**: if difficult objectives are enabled, World Event trials will be included in SoT trials.
- **sea_of_thieves_include_athenas_fortune**: Will include the voyages from the Athena's Fortune trading company that are unlocked by having three of the other trading companies to level 50.
- **sea_of_thieves_include_sunken_kingdom**: Will include the voyage "The Legend of the Sunken Kingdom" which requires "The Mysteries of the Sunken Kingdom" commendation.
- **sea_of_thieves_include_tall_tales**: Will include tall tale voyages. These voyages are meant to be done one after the other and tell a linear story, so it is recommended to only enable this if you have already completed all the tall tales.

``` yaml
sea_of_thieves_include_athenas_fortune:
    # If true, Athena's Fortune Voyages will be included in the voyage pool.
    'false': 50
    'true': 0

  sea_of_thieves_include_sunken_kingdom:
    # If true, The Legend of the Sunken Kingdom Voyage will be included in the voyage pool.
    'false': 50
    'true': 0

  sea_of_thieves_include_tall_tales:
    # If True, Tall Tale Voyages will be included in the voyage pool.
    'false': 50
    'true': 0
```

## Sid Meier's Pirates! (2004)
Sid Meier's Pirates! (also known as Sid Meier's Pirates!: Live the Life) is a 2004 strategy, action and adventure video game developed by Firaxis Games. A remake of Sid Meier's earlier 1987 game of the same name. Sail the Caribbean, marauding all on the high seas or ally your ship and crew as a privateer in search of riches - the life you choose is up to you. Face dogged enemies, raid unsuspecting villages, woo fair maidens, avoid capture or dig for buried treasure. Discover what it takes to become one of the most famous pirates in history!

[Steam](https://store.steampowered.com/app/3920/Sid_Meiers_Pirates/)

The Keymasters Keep implementation includes trials for finding buried treasure, besting the famous pirates in battle, giving gifts to governor's daughters, getting wedded, completing minigames, sacking cities, upgrading your ships, recruiting specialist crew members, having specific ship types in your fleet, becoming the most infamous pirate and rescuing family members. 

## Burger Shop
Burger Shop is a time management game where the player serves burgers, fries and other burger-related foods and drinks to customers. It is the first game in the Burger Shop series and was originally released for Windows in 2007.

[Steam](https://store.steampowered.com/app/730840/Burger_Shop/)

The Keymasters Keep implementation includes trials for getting medals in challenge or relax mode, and getting the Perfect rating on levels in story mode.

### Credits
- Keymasters Keep implementation for Burger Shop made by Reign

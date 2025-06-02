# KeymastersKeepGames
My game implementations for [Keymasters Keep](https://github.com/SerpentAI/Archipelago/releases?q=keymaster&expanded=true) -
a custom world for [Archipelago](https://archipelago.gg/) - created by SerpentAI.

# Games
- [Sea of Thieves](https://github.com/Toad-99/KeymasterKeepGames/main/README.md#L10)
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


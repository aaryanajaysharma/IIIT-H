# Assignment 3

All the specifications, including bonus, have been implemented.

## Change log

<!-- Write the changes from branch original to branch master -->

- Modified `Archer` Class to include implementation of the Stealth Archer
- Stealth Archers and Archers have a spawn limit of 7 combined
- Created `Healer` Class to include implementation of the Healer
- Created `spawnHealer` and `move_healers` methods in game.py
- Changed `break` to `exit()` when pressing key `q` in game.py to avoid error
- Implemented levelling of buildings i.e. the building's level can be manually increased
  - Done to building Cannon & Wizard Tower
  - The wall level is set to 1 and on level 3 explosion can be seen
- Decreased the attack radius of Archer from 6 to 3
- Max number of healers capped to 3
- Added a method `findClosestFriendlyTroop`, which takes in the position of the troop and returns the closest friendly troop that is most in need of healing
- The colour of the healers changes as their health decreases, similar to balloons
- The healers can be spawned by `e`, `f` and `g` key.
- The stealth archer can be spawned by `i`, `o` and `p`.
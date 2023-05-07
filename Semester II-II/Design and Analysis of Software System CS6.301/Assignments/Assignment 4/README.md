# Assignment 4: Design & Analysis of Software System

Name: Aaryan Ajay Sharma

Student ID: 2022121001

## Test Cases

### Test Case 1

- **Description** : Testing the movement of troops.
- **Input** : `python3 game.py`
- **Expected Output** : The troops should move according to the movement type chosen by the user.
- **Actual Output** : The troops move according to the movement type chosen by the user.

### Test Case 2

- **Description** : Test if king remains in the same position when dead.
- **Input** : `python3 game.py`
- **Expected Output** : King should remain in the same position when dead.
- **Actual Output** : King remains in the same position when dead.

### Test Case 3

- **Description** : Test if speed is not negative.
- **Input** : `python3 game.py`
- **Expected Output** : Speed should not be negative.
- **Actual Output** : Speed is not negative.

### Test Case 4

- **Description** : Test if other attributes are changed after moving.
- **Input** : `python3 game.py`
- **Expected Output** : Other attributes should not be changed while moving.
- **Actual Output** : Other attributes are not changed while moving.

### Test Case 5

- **Description** : Test if king is facing the right direction after moving.
- **Input** : `python3 game.py`
- **Expected Output** : King should face the right direction after moving.
- **Actual Output** : King faces the right direction after moving.



## Test Cases (Bonus)

### Test Case 1

- **Description** : Test if king is alive after attacking.
- **Input** : `python3 game.py`
- **Expected Output** : King should be alive after attacking.
- **Actual Output** : King is alive after attacking.

### Test Case 2

- **Description** : Test if cannon is destroyed after attacking.
- **Input** : `python3 game.py`
- **Expected Output** : Cannon should be destroyed after attacking.
- **Actual Output** : Cannon is destroyed after attacking.

### Test Case 3

- **Description** : Test if cannon health is not negative.
- **Input** : `python3 game.py`
- **Expected Output** : Cannon health should not be negative.
- **Actual Output** : Cannon health is not negative.

*For Test Case 2 & 3, ideally one should check for all the buildings, but since only attack_target function is being changed in all the test cases, the results of just testing cannon would generalise to all the building.*

### Test Case 4

- **Description** : Test if king's other attributes are not changed after attacking.
- **Input** : `python3 game.py`
- **Expected Output** : King's other attributes should not be changed after attacking.
- **Actual Output** : King's other attributes are not changed after attacking.

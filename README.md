# Higher-or-Lower-Game

A Python-based guessing game where players compare social media follower counts of celebrities, brands, and organizations.

## Description

Players are presented with two social media accounts and must guess which one has more followers. The game continues until a wrong guess is made, with the score increasing for each correct answer.

## Python Concepts Implemented

- **Functions with Return Values**: Using dedicated functions for data formatting and answer checking
- Docstrings for function documentation
- **Dictionary Data Structures**: Storing account information in dictionaries
- **Random Selection**: Using `random.choice()` for account selection
- **Game State Management**: Tracking score and game over conditions
- **String Formatting**: Using f-strings for output formatting
- **Clear Screen Implementation**: Using console clearing for better user experience

## Files

- [`main.py`](Higher-or-Lower-Game/main.py): Core game logic
- [`game_data.py`](Higher-or-Lower-Game/game_data.py): Database of social media accounts
- [`art.py`](Higher-or-Lower-Game/art.py): ASCII art for game visuals
- `README.md`: Documentation
- `LICENSE`: MIT license

## Features

- Large database of social media accounts
- Score tracking
- ASCII art interface
- Clear game progression
- Input validation
- Formatted account display

## How to Play

1. Run `main.py`
2. You will be shown two accounts with their descriptions
3. Type 'A' or 'B' to guess which account has more followers
4. If correct, you get a point and continue with new comparisons
5. If wrong, the game ends and shows your final score

## Example Game

```
Compare A: Instagram, a Social media platform from United States
VS
Compare B: Cristiano Ronaldo, a Footballer from Portugal
Who has more followers?: A
You're right! Current score: 1

Compare A: Cristiano Ronaldo, a Footballer from Portugal
VS
Compare B: Ariana Grande, a Musician and actress from United States
Who has more followers?: 
```

## Data Structure

Each account in the game data contains:
- Name
- Follower count
- Description
- Country of origin

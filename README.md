# Space Invaders Game

This project is a modernized version of the classic **Space Invaders** game built using **Pygame**, a Python library for creating 2D games. It features interactive gameplay, sound effects, and dynamic animations, providing a nostalgic gaming experience with a fresh design.

## 🚀 Features

- **Player Control**: Move the player horizontally and shoot lasers to destroy aliens.
- **Alien Waves**: Multiple rows of aliens with increasing difficulty.
- **Obstacles**: Shields to block alien lasers, but they can be destroyed.
- **Power-ups**: Extra alien appearances for bonus points.
- **Sound Effects**: Laser shooting, explosions, and background music for an immersive experience.
- **Score Tracking**: Keep track of your score and compete for the highest score.
- **Victory Condition**: Win the game by destroying all aliens.

---

## 🖼️ Gameplay Preview

### Main Features:
1. Move left and right to dodge alien lasers.
2. Shoot lasers to destroy enemies and earn points.
3. Protect yourself using destructible obstacles.
4. Watch out for extra alien ships for bonus points!

---

## 🛠️ Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Prathamesh326/Space-Invaders-Game.git
    cd Space-Invaders-Game
    ```

2. **Install Dependencies**:
    Ensure you have Python installed. Then install Pygame using pip:
    ```bash
    pip install pygame
    ```

3. **Run the Game**:
    Execute the `main.py` file:
    ```bash
    python main.py
    ```

---

## 🎮 Controls

| Key         | Action                     |
|-------------|----------------------------|
| **←**       | Move left                  |
| **→**       | Move right                 |
| **Spacebar**| Shoot laser                |
| **ESC**     | Quit the game              |

---

## 🗂️ Project Structure

```
Space-Invaders-Game/
│
├── main.py          # Main game loop and logic
├── player.py        # Player class and controls
├── alien.py         # Alien and extra alien logic
├── obstacles.py     # Obstacles and shield logic
├── laser.py         # Laser behavior for player and aliens
├── Graphics/        # Game assets like player, alien, and extra sprites
├── Audio/           # Sound effects and background music
├── Font/            # Custom pixelated font
└── README.md        # Project documentation
```

---

## 🔧 Dependencies

- **Python 3.7+**
- **Pygame 2.0.0+**

---

## 📚 How It Works

1. **Game Initialization**:
   - The game initializes the player, obstacles, aliens, and extra alien mechanics.
   - Background music and sound effects are loaded.

2. **Gameplay**:
   - Player movement and shooting are controlled via keyboard input.
   - Aliens move horizontally and shoot lasers at intervals.
   - Collision detection checks interactions between lasers, obstacles, and aliens.

3. **Game Over**:
   - The player loses if all lives are depleted or an alien collides with the player.
   - Victory is achieved when all aliens are destroyed.

---

## 🎉 Future Improvements

- Add levels with increasing difficulty.
- Include more alien types and power-ups.
- Implement a leaderboard to track high scores.
- Add a pause and restart functionality.

---

## 🧑‍💻 Author

This project was developed by **[Prathamesh](https://github.com/Prathamesh326)**.

Feel free to contribute or report any issues in the repository!

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as per the license terms.

---

Enjoy the nostalgic gameplay and feel free to share your feedback! 🚀

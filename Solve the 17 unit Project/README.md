# 🎮 Falling Shapes Game:
**Falling Shapes Game** is a simple game when different shapes fall from the top of the screen, and the player controls a paddle to catch them, and each shape gives different points.
## 🎯 Game Rules:
| Shape Type        | Effect           |
| ----------------- | ---------------- |
| 🐢 Turtle (white) | Game Over        |
| 🐢 Turtle (color) | +5 points        |
| ⬜ Square          | +2 points        |
| ⚪ Circle          | +1 point         |
| 🔺 Triangle       | Reset score to 0 |
- Shapes fall faster as the game progresses
- Missing a shape simply spawns a new one
- Catching shapes correctly increases your score
## 🎮 Controls:
| Key           | Action            |
| ------------- | ----------------- |
| ⬅ Left Arrow  | Move paddle left  |
| ➡ Right Arrow | Move paddle right |
## 🧩 File Overview:
### main.py:
- Initializes the game window
- Creates the player paddle, falling shapes, and scoreboard
- Handles keyboard input
- Runs the main game loop
- Controls collisions, scoring, and game speed
### ball.py:
- Represents the falling shape
- Randomly selects:
  - Shape type
  - Color
  - Size
  - Horizontal position
- Moves shapes downward continuously
- Resets shape when caught or missed
**Special Rule**
- A **white turtle** shape is rare and instantly ends the game
### paddle.py:
- Represents the player-controlled paddle
- Moves left and right using keyboard keys
- Prevents the paddle from leaving the screen boundaries
### score.py:
- Displays the current score at the top of the screen
- Updates score based on the caught shape
- Resets score when needed
- Shows **GAME OVER** message when the game ends



# 🏓 Ping Pong Game:
This project is a Ping Pong Game built using Python’s built-in **turtle graphics module**.
## 🎮 Gameplay Overview:
- Two players control paddles on the left and right sides
- A ball moves continuously across the screen
- Players try to hit the ball with their paddles
- The ball bounces off:
  - Top and bottom walls
  - Paddles
- A point is awarded when a player misses the ball
- The ball speed increases slightly after each paddle hit
## ⌨️ Controls:
### Player 1 (Right Paddle):
| Key          | Action    |
| ------------ | --------- |
| ↑ Up Arrow   | Move Up   |
| ↓ Down Arrow | Move Down |
### Player 2 (Left Paddle):
| Key | Action    |
| --- | --------- |
| A   | Move Up   |
| Q   | Move Down |
## 🧠 Main Components:
### main.py:
- Sets up the game window
- Creates paddles, ball, and scoreboard
- Handles:
  - Ball movement
  - Wall collisions
  - Paddle collisions
  - Scoring logic
- Controls game speed and updates the screen
### paddle.py:
- Represents a player paddle
- Uses a stretched square turtle shape
- Can move up and down using keyboard input
- Position is passed during initialization (left or right side)
### ball.py:
- Represents the ball
- Moves diagonally across the screen
- Changes direction when:
  - It hits a wall
  - It collides with a paddle
- Uses x_move and y_move values to control movement speed
### score.py:
- Displays the score at the top of the screen
- Keeps track of:
  - Left player score
  - Right player score
- Updates the scoreboard whenever a point is scored

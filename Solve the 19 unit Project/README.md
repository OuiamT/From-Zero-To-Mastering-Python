# 🗺️ Map Guessing Game:
This project is an interactive map-based guessing game built with **Python**, **Turtle graphics**, and **Pandas**.
The player must guess country names and will see them marked on a map in real time.
## 🎮 How the Game Works:
- A map image is displayed on the screen.
- The player types the name of a country.
- If the answer is correct:
  - A red marker appears on the map at the country’s coordinates.
  - The country name is written next to the marker.
- The game continues until:
  - All countries are guessed, or
  - The player types Exit.
- When the player exits, all missing countries are saved to a **notgussed.CSV file**.
## 📁 Project:
### coordinates.csv:
Must contain these columns:
| country | x   | y   |
| ------- | --- | --- |
| Morocco | -50 | 120 |
| Egypt   | 80  | 100 |
- **country** → country name
- **x**, **y** → screen coordinates for placement

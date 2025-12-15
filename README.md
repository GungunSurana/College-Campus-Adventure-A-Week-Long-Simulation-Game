# 🎓 College Campus Adventure: A Week-Long Simulation Game  

This project is an interactive Python game that simulates a full week of college life.  
Players make daily choices that affect four main stats:

- **Grades (G)**
- **Money (M)**
- **Reputation (R)**
- **Attendance (A)**

Every choice impacts these stats differently, and a 30% random event system adds unpredictability.  
At the end of the week, the game evaluates the final stats and generates a personalized ending.

---

## Features:

- Five-round gameplay (one day per round)
- Choice-based decision system using **a/b/c** inputs
- Four tracked stats updated dynamically throughout the game
- Random events with both positive and negative outcomes
- Input validation using loops for error-free gameplay
- Multiple unique endings depending on final performance
- Modular and clean code structure with functions for each round

---

## Technologies Used:

- **Python 3.x**
- **IDLE** (Python’s official IDE)
- No external libraries required

---

## Data Structures Used:

- **Dictionary (`stats`)** → Stores player stats  
- **List of dictionaries (`random_events`)** → Holds random event data  
- **Functions** → One per round + helpers like `apply_changes()` and `show_stats()`  
- **While loops** → Ensure correct input (a/b/c)  
- **If/elif statements** → Apply stat changes based on choices  

---

How to Run the Game

-Clone this repository or download the Python file:

college_game.py

-Open the file using Python IDLE or any Python editor.

-Run the program using:

python college_game.py

-Follow the on-screen instructions.

-Enter your choices using a, b, or c when prompted.

---


## Game Flow:

```text
Start → Round 1 → Random Event → Round 2 → Random Event → Round 3 → Random Event → Round 4 → Random Event → Round 5 → Random Event → Final Results



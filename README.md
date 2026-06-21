# 🎯 Guess the Number — Flask Mini Game

A simple Flask web app where the user tries to guess a randomly generated number between **0 and 9**. The app responds with visual feedback based on the guess.

---

## 🚀 Overview

- A random number is generated when the server starts.
- The home route displays the game instructions.
- A dynamic route receives the user's guess and returns:
  - **Too high**  
  - **Too low**  
  - **Correct guess**  

Each response includes a themed GIF for a more playful experience.

---

## 🧩 Routes

- **Home route** — Shows the game introduction.  
- **Guess route** — Compares the user’s number with the secret one and returns feedback.

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask**
- **random** module

---

## ▶️ How to Run

1. Install Flask:
   ```bash
   pip install flask
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Open in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## 📌 Purpose

This project demonstrates:
- Basic Flask routing  
- Handling dynamic URL parameters  
- Returning HTML responses  
- Simple backend logic with conditionals  

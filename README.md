# 📅 Habit Tracker Web App

## 🚀 Overview
**Habit Tracker** is a simple Flask-based web application that helps users track their daily habits. Users can add any number of habits, which will be displayed on the homepage daily from the day they were added. Clicking on a habit marks it as complete, making it easier to stay consistent and accountable.

## ✨ Features
+ ➕ **Add New Habits** – Users can add multiple habits to track
+ 📌 **Daily Habit Display** – Habits appear on the main page daily from their creation date
+ ✅ **Mark Habits as Complete** – Click on a habit to mark it as completed for the day
+ 🗄 **MongoDB Integration** – Stores habit data in two separate collections:
  + **Habit List Collection** – Keeps track of all added habits
  + **Completed Habits Collection** – Stores completed habits for tracking progress
+ 🎯 **Simple & User-Friendly** – Minimalistic design with an intuitive interface

## 🛠️ Tech Stack
+ **Backend**: Python, Flask
+ **Frontend**: HTML, CSS
+ **Database**: MongoDB

## 📌 How to Run
1. Clone the repository:
   `git clone https://github.com/yourusername/Habit-Tracker.git`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Set up MongoDB and update the database connection in the Flask app
4. Run the Flask app:
   `flask run`
5. Open in browser: `http://127.0.0.1:5000/`




### This project was made as part of a Udemy Web development course by [Jose Salvatierra](https://www.udemy.com/user/josesalvatierra/).

# 🚀 Smart Civic Issue Reporting System

## 📌 Overview
This is a full-stack civic issue reporting application that allows users to report problems such as potholes, water leakage, and electrical issues by tagging their location on a map.

The system helps authorities monitor and resolve issues efficiently through a centralized dashboard.

---

## 🎯 Features

- 📍 Location tagging using map
- 🛠️ Issue categories:
  - Pothole
  - Electric Line Problem
  - Water Leakage
  - Other (custom input)
- 📤 Submit complaints
- 📊 Dashboard to view all reported issues
- 🗺️ Map-based visualization of complaints

---

## 🏗️ Tech Stack

- Frontend: HTML, CSS, JavaScript (Leaflet Map)
- Backend: Python (Flask)
- Database: SQLite

---

## 🔄 How It Works

1. User selects a location on the map  
2. Chooses issue type  
3. Submits the complaint  
4. Backend stores data in database  
5. Dashboard displays issues on map  

---

## 📂 Project Structure

---

## ▶️ How to Run the Project

### Step 1: Clone the repository
```bash
git clone https://github.com/dhanyamg/civic-issue-reporting-app.git
cd civic-issue-reporting-app

---

## ▶️ How to Run the Project

### Step 1: Clone the repository
```bash
git clone https://github.com/dhanyamg/civic-issue-reporting-app.git
cd civic-issue-reporting-app
the dashboard link says access denined
Running on http://127.0.0.1:5000%                                                                                                                                        
(base) dhanyamg@Dhanyas-MacBook cvic_app % Running on http://127.0.0.1:5000
zsh: command not found: Running
(base) dhanyamg@Dhanyas-MacBook cvic_app % 

Running on http://127.0.0.1:5000%                                                                                                                                        
(base) dhanyamg@Dhanyas-MacBook cvic_app % Running on http://127.0.0.1:5000
zsh: command not found: Running
(base) dhanyamg@Dhanyas-MacBook cvic_app % python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 125-150-385
python app.py

python app.py
http://127.0.0.1:5000/dashboard
^C%                                                                                                                                                                      
(base) dhanyamg@Dhanyas-MacBook cvic_app % http://127.0.0.1:5000/dashboard
zsh: no such file or directory: http://127.0.0.1:5000/dashboard
(base) dhanyamg@Dhanyas-MacBook cvic_app % 
Access to 127.0.0.1 was denied
You don't have authorization to view this page.
HTTP ERROR 403
Access to 127.0.0.1 was denied
You don't have authorization to view this page.
HTTP ERROR 403
from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lat REAL,
            lng REAL,
            issue_type TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    lat = request.form['lat']
    lng = request.form['lng']
    issue_type = request.form['issue_type']
    description = request.form.get('description', '')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO issues (lat, lng, issue_type, description) VALUES (?, ?, ?, ?)",
              (lat, lng, issue_type, description))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM issues")
    data = c.fetchall()
    conn.close()

    return render_template('dashboard.html', issues=data)

@app.route('/api/issues')
def api_issues():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT lat, lng, issue_type, description FROM issues")
    rows = c.fetchall()
    conn.close()

    issues = [
        {"lat": r[0], "lng": r[1], "type": r[2], "desc": r[3]}
        for r in rows
    ]
    return jsonify(issues)

if __name__ == '__main__':
    app.run(debug=True)
/usr/local/bin/python3 /Users/dhanyamg/cvic_app/app.py
(base) dhanyamg@Dhanyas-MacBook cvic_app % /usr/local/bin/python3 /Users/dhanyamg/cvic_app/app.py
Traceback (most recent call last):
  File "/Users/dhanyamg/cvic_app/app.py", line 1, in <module>
    from flask import Flask, render_template, request, redirect, jsonify
ModuleNotFoundError: No module named 'flask'
(base) dhanyamg@Dhanyas-MacBook cvic_app % 
#results

<img width="1436" height="625" alt="Screenshot 2026-05-13 at 2 08 41 PM" src="https://github.com/user-attachments/assets/6411ffe4-7d2d-4937-b7e1-1697f6d0770b" />
<img width="1436" height="625" alt="Screenshot 2026-05-13 at 2 08 41 PM" src="https://github.com/user-attachments/assets/542da36c-9acb-4156-b508-3c116b3af186" />



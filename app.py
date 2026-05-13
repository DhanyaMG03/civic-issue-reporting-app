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
    # User page: http://127.0.0.1:5000
#Dashboard: http://127.0.0.1:5000/dashboard
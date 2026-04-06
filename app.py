from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('database.db', timeout=10, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       uni_id TEXT NOT NULL,
                       class TEXT NOT NULL,
                       email TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS registrations
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id INTEGER NOT NULL,
                       event TEXT NOT NULL,
                       UNIQUE(user_id, event))''')
    conn.commit()
    conn.close()

init_db()

def get_or_create_user(cursor, name, uni_id, user_class, email):
    cursor.execute("SELECT id FROM users WHERE name=? AND uni_id=?", (name, uni_id))
    user = cursor.fetchone()
    if user:
        return user["id"]
    cursor.execute(
        "INSERT INTO users (name, uni_id, class, email) VALUES (?, ?, ?, ?)",
        (name, uni_id, user_class, email)
    )
    return cursor.lastrowid

@app.route('/')
def home():
    message = request.args.get('message')
    return render_template('index.html', page="home", message=message)

@app.route('/hackathon', methods=['GET', 'POST'])
def hackathon():
    if request.method == 'POST':
        name = request.form['name']
        uni_id = request.form['uni_id']
        user_class = request.form['class']
        email = request.form['email']

        if not name or not uni_id or not user_class or not email:
            return render_template("index.html", page="hackathon", message="Fill in all fields")

        conn = get_db()
        cursor = conn.cursor()

        user_id = get_or_create_user(cursor, name, uni_id, user_class, email)

        try:
            cursor.execute(
                "INSERT INTO registrations (user_id, event) VALUES (?, ?)",
                (user_id, "hackathon")
            )
        except:
            pass

        conn.commit()
        conn.close()

        return redirect('/?message=success')

    return render_template("index.html", page="hackathon")

@app.route('/workshop', methods=['GET', 'POST'])
def workshop():
    if request.method == 'POST':
        name = request.form['name']
        uni_id = request.form['uni_id']
        user_class = request.form['class']
        email = request.form['email']

        if not name or not uni_id or not user_class or not email:
            return render_template("index.html", page="workshop", message="Fill in all fields")

        conn = get_db()
        cursor = conn.cursor()

        user_id = get_or_create_user(cursor, name, uni_id, user_class, email)

        try:
            cursor.execute(
                "INSERT INTO registrations (user_id, event) VALUES (?, ?)",
                (user_id, "workshop")
            )
        except:
            pass

        conn.commit()
        conn.close()

        return redirect('/?message=success')

    return render_template("index.html", page="workshop")

@app.route('/admin')
def admin():
    password = request.args.get('password')

    if password != 'Aawez123!':
        return render_template("index.html", page="admin", message="Incorrect password")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT users.id, users.name, users.uni_id, users.class, users.email,
               GROUP_CONCAT(registrations.event)
        FROM users
        LEFT JOIN registrations ON users.id = registrations.user_id
        GROUP BY users.id
    ''')

    users = cursor.fetchall()
    conn.close()

    return render_template("index.html", page="admin", users=users)

@app.route('/delete/<int:user_id>')
def delete(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM registrations WHERE user_id=?", (user_id,))
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    conn.commit()
    conn.close()

    return redirect('/admin?password=Aawez123!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
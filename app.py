from flask import Flask, request, redirect, render_template
import sqlite3 as sql

app = Flask(__name__)

def get_db_connection():
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       uni_id TEXT NOT NULL,
                       event TEXT NOT NULL)''')
    conn.commit()
    conn.close()

get_db_connection()

@app.route('/')
def type_test():
    return render_template('index.html', page="home")

@app.route('/hackathon', methods=['GET', 'POST'])
def hackathon():
    if request.method == 'POST':
        name = request.form['name']
        uni_id = request.form['uni_id']

        if not name or not uni_id:
            return render_template("index.html", page="hackathon", message="Fill in all fields")

        conn = sql.connect('database.db')
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT event FROM users WHERE name=? AND uni_id=?",
            (name, uni_id)
        )
        result = cursor.fetchone()

        if result:
            existing_events = result[0]

            if "hackathon" not in existing_events:
                updated_events = existing_events + ", hackathon"

                cursor.execute(
                    "UPDATE users SET event=? WHERE name=? AND uni_id=?",
                    (updated_events, name, uni_id)
                )
        else:
            cursor.execute(
                "INSERT INTO users (name, uni_id, event) VALUES (?, ?, ?)",
                (name, uni_id, "hackathon")
            )
        conn.commit()
        conn.close()

        return render_template("index.html", page="home", message="Registered successfully")

    else:
        return render_template("index.html", page="hackathon")

@app.route('/workshop', methods=['GET', 'POST'])
def workshop():
    if request.method == 'POST':
        name = request.form['name']
        uni_id = request.form['uni_id']

        if not name or not uni_id:
            return render_template("index.html", page="workshop", message="Fill in all fields")

        conn = sql.connect('database.db')
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT event FROM users WHERE name=? AND uni_id=?",
            (name, uni_id)
        )
        result = cursor.fetchone()

        if result:
            existing_events = result[0]

            if "workshop" not in existing_events:
                updated_events = existing_events + ", workshop"

                cursor.execute(
                    "UPDATE users SET event=? WHERE name=? AND uni_id=?",
                    (updated_events, name, uni_id)
                )
        else:
            cursor.execute(
                "INSERT INTO users (name, uni_id, event) VALUES (?, ?, ?)",
                (name, uni_id, "workshop")
            )

        conn.commit()
        conn.close()

        return render_template("index.html", page="home", message="Registered successfully")

    else:
        return render_template("index.html", page="workshop")
    
@app.route('/admin')
def admin():
    password = request.args.get('password')

    if password != 'Aawez123!':
        return render_template("index.html", page="admin", message="Incorrect password")
    
    conn = sql.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("index.html", page="admin", users=users)

@app.route('/delete/<int:user_id>')
def delete(user_id):
    conn = sql.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    conn.commit()
    conn.close()

    return redirect('/admin?password=Aawez123!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

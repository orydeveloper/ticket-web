from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():

    conn = sqlite3.connect("../tickets.db")
    cursor = conn.cursor()

    # leaderboard
    cursor.execute("""
        SELECT user_name, COUNT(*) as total
        FROM claims
        GROUP BY user_id
        ORDER BY total DESC
    """)
    leaderboard = cursor.fetchall()

    # historie
    cursor.execute("""
        SELECT user_name, ticket_name, claimed_at
        FROM claims
        ORDER BY claimed_at DESC
    """)
    history = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        leaderboard=leaderboard,
        history=history
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
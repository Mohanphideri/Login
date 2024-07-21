from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'root',  # your MySQL username
    'password': 'Monuyadav2@',  # your MySQL password
    'host': 'localhost',
    'database': 'july21'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_uid = request.form['student_uid']
        password = request.form['password']

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if the user exists
        query = "SELECT * FROM NCHA WHERE student_uid=%s AND password=%s"
        cursor.execute(query, (student_uid, password))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return f"Login successful! Welcome, {result[0]}."
        else:
            return "Invalid UID or password."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

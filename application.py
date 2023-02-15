from flask import Flask, render_template
import psycopg2

application = Flask(__name__)

app = application

# Set up the PostgreSQL database connection
def connect_to_database():
    conn = psycopg2.connect(
        user='jasonadmin',
        password='qwerty123',
        host='cardb-1.cbbge8pluyf7.eu-central-1.rds.amazonaws.com',
        port='5432',
        database='cardb'
    )
    return conn



@app.route("/")
def index():
    conn = connect_to_database()
    conn.close()
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
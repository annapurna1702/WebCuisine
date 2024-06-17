from flask import Flask, render_template, request, redirect
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname='myproj',
            user='myuser',
            password='mypassword',
            host='localhost'
        )
        return conn
    except OperationalError as e:
        print(f"Unable to connect to the database: {e}")
        return None


@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM foods")
            records = cur.fetchall()
            cur.close()
            conn.close()
            return render_template('index.html', records=records)
        except psycopg2.Error as e:
            print(f"Error fetching data from database: {e}")
            conn.close()
            return "Error fetching data from database"
    else:
        return "Database connection failed"


@app.route('/indian')
def indian():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM foods WHERE cuisine='Indian'")
            records = cur.fetchall()
            cur.close()
            conn.close()
            return render_template('indian.html', records=records)
        except psycopg2.Error as e:
            print(f"Error fetching Indian cuisine data: {e}")
            conn.close()
            return "Error fetching Indian cuisine data"
    else:
        return "Database connection failed"


@app.route('/arabic')
def arabic():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM foods WHERE cuisine='Arabian'")
            records = cur.fetchall()
            cur.close()
            conn.close()
            return render_template('arabic.html', records=records)
        except psycopg2.Error as e:
            print(f"Error fetching Arabian cuisine data: {e}")
            conn.close()
            return "Error fetching Arabian cuisine data"
    else:
        return "Database connection failed"


@app.route('/chinese')
def chinese():
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM foods WHERE cuisine='Chinese'")
            records = cur.fetchall()
            cur.close()
            conn.close()
            return render_template('chinese.html', records=records)
        except psycopg2.Error as e:
            print(f"Error fetching Chinese cuisine data: {e}")
            conn.close()
            return "Error fetching Chinese cuisine data"
    else:
        return "Database connection failed"


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        cuisine = request.form['cuisine']
        img = request.form['img']
        describe = request.form['describe']
        conn = get_db_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute('INSERT INTO foods (name, cuisine, img, describe) VALUES (%s, %s, %s, %s)', (name, cuisine, img, describe))
                conn.commit()
                cur.close()
                conn.close()
                return redirect('/')
            except psycopg2.Error as e:
                print(f"Error inserting data into database: {e}")
                conn.close()
                return "Error inserting data into database"
        else:
            return "Database connection failed"
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)

from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host="db",          # Docker networking
        user="root",
        password="root",
        database="testdb"
    )

@app.get("/")
def home():
    return {"message": "Backend running with MySQL"}

@app.get("/data")
def get_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    conn.close()
    return {"data": result}
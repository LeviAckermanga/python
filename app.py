# app.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'app.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/items', methods=['GET'])
def get_items():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, description) VALUES (?, ?)', (data['name'], data['description']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item created successfully'})

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000)

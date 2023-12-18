import sqlite3
import flask
from flask import Flask, render_template
from sqlite3 import *

app = Flask(__name__)


con = sqlite3.connect('TarAi_Data.db', check_same_thread=False)
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
                id INTEGER,
                login TEXT,
                password TEXT
                )""")
con.commit()

@app.route('/')
def Reg():
    return render_template('Reg.html')








if __name__ == '__main__':
    app.run()
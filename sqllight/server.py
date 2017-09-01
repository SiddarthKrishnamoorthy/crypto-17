from flask import Flask, request, render_template
import sqlite3
import random
app = Flask(__name__)

conn = sqlite3.connect('database.sql')

@app.route('/',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
       username = request.form['username']
       password = request.form['password']
       query = 'SELECT * FROM users WHERE NAME = \'' + username + '\' AND PASSWORD = \'' + password + '\''
       rows = conn.execute(query)
       rows = [row for row in rows]
       rows_num = len(rows)
       if rows_num == 0:
           answer = "Oops! Wrong username and password. You are denied entry into the vale!"
       elif rows_num == 1:
           usr_grp = rows[0][2]
           if usr_grp != "user_guest":
               answer = "Hmm... I seem to know you, but you are not a guest! You belong to the USER_GROUP = user_protector. I was looking for user_guest"
           else:
               answer = "Your attempt was successful. Your flag: flag{lysa_arryn_killed_herself}"
       else:
          answer = "Hmm... You name and password have identified you as MANY users, not just ONE. Suspicious..."
       return render_template("index.html", answer = answer)
    else:
       return render_template("index.html", answer = "Hello!")


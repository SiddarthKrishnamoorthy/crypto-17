from flask import Flask, request, render_template
import sqlite3
import random
import os
app = Flask(__name__)

conn = sqlite3.connect('weirddb' + os.environ['FILENUM'] + '.sql')

@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['query']
      answer = ""
      if "sqlite_master" in result.lower() or "master" in result.lower() or result.lower().strip()[0] == '.':
         answer = "LOL not so easy"
      elif "drop" in result.lower() or "delete" in result.lower():
         answer = "Warning: if you delete the flag it's your fault ;)"
      elif "pragma" in result.lower():
         answer = "Going deep, but not deep enough yet!"
      else:
         try:
            for row in conn.execute(result):
               answer += ' | '.join([str(r) for r in row if r != None])
            conn.commit()
            print(answer)
            if answer.strip() == "": answer = "Executed query successfully in " + str(random.random()) + " seconds."
         except RuntimeError:
            answer = "SQL Error!"
      return render_template("index.html", answer = answer)
   else:
      return render_template("index.html")

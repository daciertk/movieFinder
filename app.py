from flask import Flask, render_template, request
import mysql.connector
from io import StringIO
app = Flask(__name__)

con = mysql.connector.connect(host="localhost", user="root", password="grannygear1952", database="moviefiner")
cur = con.cursor()

@app.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
       # result = request.args.get("text")
        values = list(request.args.values())
        if len(values) == 0:
            return render_template("home.jinja")
        type = values[0]
        rating = values[-1]
        genres = values[1:-1]
        print(genres)
        print(values)
        out = StringIO()
        out.write(f"SELECT title, type, genres, averageRating, numVotes, releaseYear FROM `moviefiner`.`data` WHERE type = '{type}' AND genres LIKE ")
        last = genres[-1]
        rest = genres[:-1]
        for genre in rest:
            out.write(f'"%{genre}%" AND genres LIKE ')
        out.write(f'"%{last}%" ')
        out.write(f"AND averageRating > {int(rating) * 0.1} ")
        out.write("ORDER BY averageRating DESC")
    
        print(out.getvalue())
        cur.execute(out.getvalue())
        data = cur.fetchall()
       
        return render_template("home.jinja", data=data)
        
    return render_template("home.jinja")


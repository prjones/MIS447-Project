from flask import Flask, render_template, request, redirect
import markdown as md
import csv, os
import sqlite3
import psycopg2

'''
    Will have to change the host, database, user, and password for Flask connection
'''

app = Flask(__name__)
conn = psycopg2.connect(host="ec2-174-129-214-193.compute-1.amazonaws.com",database="d245l8lq8fvt3k", user="jptsqrcgcolpzw", password="68ba5ad64cadf6d0b7f387da474436dfbd3dca326fd914db29d2b35a59690ef9", port="5432")
c = conn.cursor()



WEB_APP_NAME = "Meals on Wheels Signup"

'''
    Main NavBar Methods
'''

@app.route('/')
@app.route('/home')
@app.route('/home/<name>')
def home(name=WEB_APP_NAME):
    return render_template("practicewindow.html", content=name)

@app.route('/about/')
@app.route('/about/<name>')  # be sure to include both forward slashes
def about(name=WEB_APP_NAME):
    return render_template("about.html", content=name)

@app.route('/contact/')
@app.route('/contact/<name>')  # be sure to include both forward slashes
def contact(name=WEB_APP_NAME):
    return render_template("contact.html", content=name)


@app.route('/account', methods=['GET'])
def accountPage():
    return render_template("account.html", content=user)



@app.route('/logout', methods=['GET'])
def logoutPage():
    return render_template('logout.html')

# run the Flask app (which will launch a local webserver)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)



 
conn.commit()

from flask import Flask, render_template, request, redirect


'''
    Will need to change the host, database, user, and password for Flask connection
'''

app = Flask(__name__)



WEB_APP_NAME = "Meals on Wheels Signup"

'''
    Main NavBar Methods
'''

@app.route('/')
@app.route('/home')
def home():
    return render_template("RegistrationHomePage.html")

@app.route('/registration/')
def registration():
    return render_template("RegistrationForm.html")

# run the Flask app (which will launch a local webserver)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


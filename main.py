from flask import Flask,render_template
from favorite_elements import create_blogger_card
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
PORT_ENV = os.getenv('PORT')
print(PORT_ENV)

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("./index.html")

@app.route("/search")
def search():
    return render_template('./search.html')

@app.route("/profile")
def profile():
    return render_template('./profile.html')


@app.route("/favorite")
def favorite():
    blogger_card = create_blogger_card()
    return render_template('./favorite.html',blogger_card = blogger_card)

@app.route("/sign")
def sign():
    return render_template('./sign.html')

@app.route("/login")
def login():
    return render_template('./login.html')

@app.route("/blogger_profile")
def blogger_profile():
    return render_template('/blogger-profile.html')

if __name__ == '__main__':
  app.run(port=5000)
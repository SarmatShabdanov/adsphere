from flask import Flask,render_template, request
from favorite_elements import create_blogger_card
from left_menu import create_left_menu,left_menu_create_script
from header import create_header
from dotenv import load_dotenv
import os
import sqlite3

# Load environment variables from .env file
load_dotenv()

# Access environment variables
PORT_ENV = os.getenv('PORT')
print(PORT_ENV)

def get_bloggers():
    conn = sqlite3.connect("ad_sphere.db")
    cursor = conn.cursor()
    q = "SELECT * from bloggers"
    cursor.execute(q)
    result = cursor.fetchall()
    conn.close()
    return result 

def get_history():
    conn = sqlite3.connect("ad_sphere.db")
    cursor = conn.cursor()
    q = "SELECT * from history INNER JOIN bloggers ON bloggers.id = history.blogger_id "
    cursor.execute(q)
    result = cursor.fetchall()
    conn.close()
    return result 



def get_favorite():
    conn = sqlite3.connect("ad_sphere.db")
    cursor = conn.cursor()
    q = "SELECT * from favorite INNER JOIN bloggers ON bloggers.id = favorite.blogger_id "
    cursor.execute(q)
    result = cursor.fetchall()
    conn.close()
    return result 


app = Flask(__name__)
@app.route("/")
def home():
    left_menu = create_left_menu()
    left_menu_script = left_menu_create_script()
    header = create_header()
    return render_template("./index.html",left_menu = left_menu,left_menu_script = left_menu_script,header = header)

@app.route("/search")
def search():
    left_menu = create_left_menu()
    left_menu_script = left_menu_create_script()
    header = create_header()
    bloggers = get_bloggers()
    return render_template('./search.html',left_menu = left_menu,left_menu_script = left_menu_script,header = header,bloggers = bloggers)

@app.route("/profile")
def profile():
    left_menu = create_left_menu()
    left_menu_script = left_menu_create_script()
    header = create_header()
    return render_template('./profile.html',left_menu = left_menu,left_menu_script = left_menu_script,header = header)


@app.route("/favorite")
def favorite():
    left_menu = create_left_menu()
    left_menu_script = left_menu_create_script()
    header = create_header()
    blogger_card = create_blogger_card()
    return render_template('./favorite.html',blogger_card = blogger_card,left_menu = left_menu,left_menu_script = left_menu_script,header = header)

@app.route("/add_favorite", methods=['POST'])
def add_favorite():
    blogger_id = request.form.get('bloggerId')
    print(blogger_id)

    
    
    
@app.route("/sign")
def sign():
    return render_template('./sign.html')

@app.route("/login")
def login():
    return render_template('./login.html')

@app.route("/blogger_profile")
def blogger_profile():
    left_menu = create_left_menu()
    left_menu_script = left_menu_create_script()
    header = create_header()
    return render_template('/blogger-profile.html',left_menu = left_menu,left_menu_script = left_menu_script,header = header)

if __name__ == '__main__':
  app.run(port=5000)
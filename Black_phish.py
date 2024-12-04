from flask import Flask, render_template, request
from termcolor import colored
from pyfiglet import Figlet

app = Flask(__name__)

# ASCII Art Setup
ascii_art = Figlet(font="slant")  # Isticmaal font-ka slant ama mid kale
title = ascii_art.renderText("BLACK1446")
colored_title = colored(title, "blue")  # Midabka buluugga ah

# Home route: wuxuu soo bandhigayaa bogga login
@app.route('/')
def home():
    return render_template('login.html')  # Foomka login-ka

# Login route: wuxuu aqbalaa xogta loo soo diro foomka
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']  # Qaad xogta username
    password = request.form['password']  # Qaad xogta password
    # Halkan waxaad ku qori kartaa koodhka xaqiijinta (validation)
    return f"{colored_title}\n\nWelcome {username}, your password is {password}"

if __name__ == "__main__":
    print(colored_title)  # Daabac ASCII art ee title-ka
    print("##### CODED BY BLACK1446 #####")  # Qorista qoraalka "coded by Black1446"
    app.run(debug=True, host="0.0.0.0", port=5000)  # Flask server-ka ku orod port 5000

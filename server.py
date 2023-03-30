from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)


def display(function):
    def wrapper():
        return "<h1>" + function() + "</h1>"
    return wrapper


@app.route("/")
@display
def home():
    return "Guess a number between 0 and 9" \
           "<p><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></p>"


@app.route("/<int:guess>")
def choice(guess):
    if guess == random_number:
        return f"<h1 style='color:green'>{guess} is just right.</h1>" \
               f"<p><img src='https://media.giphy.com/media/26ufq9mryvc5HI27m/giphy.gif'></p>"
    elif guess > random_number:
        return f"<h1 style='color:purple'>{guess} is too high</h1>" \
               f"<p><img src='https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy-downsized-large.gif'></p>"
    elif guess < random_number:
        return f"<h1 style='color:red'>{guess} is too low</h1>" \
               f"<p><img src='https://media.giphy.com/media/dKpEvFHdGsZBRuszpv/giphy.gif'></p>"


if __name__ == "__main__":
    app.run(debug=True)




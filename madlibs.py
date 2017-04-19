"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)




@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the <a href='/hello'> home page. </a> </html>"


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""


    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
        'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
        'smashing', 'lovely',
    ]

    c1 = choice(AWESOMENESS)

    AWESOMENESS = list( set(AWESOMENESS) - {c1} )
    
    c2 = choice(AWESOMENESS)

    AWESOMENESS = list( set(AWESOMENESS) - {c2} )
    
    c3 = choice(AWESOMENESS)

    AWESOMENESS = list( set(AWESOMENESS) - {c3} )





    player = request.args.get("person")

    compliments= [c1, c2, c3 ]

    return render_template("compliment.html",
                           person=player,
                           compliment=compliments)


@app.route('/game')
def show_madlib_form():
    """Play the mad lib game."""

    game_response = request.args.get("yesno")

    nouns = ["Dog", "Cat", "Balloonicorn", "hedgehog", "yak"]



    if game_response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html", nouns= nouns)


@app.route('/madlib')
def show_madlib():
    """Responses to the MadLib game."""

    player = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    if not noun:
        noun = "CAT"
    adjective = request.args.get("adjective")

    file_name = choice(["madlib.html", "madlib2.html"])

    return render_template(file_name,
                           person=player,
                           color=color,
                           noun=noun,
                           adjective=adjective
                           )


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)

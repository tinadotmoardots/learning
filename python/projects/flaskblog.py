from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Kristina Hunter',
        'title': 'Look What I Can Do!',
        'content': 'I can make a blog using Flask',
        'date_posted': 'October 6'
    },
    {
        'author': 'Kristina Hunter',
        'title': 'Who is the best mentor?',
        'content': 'Obvs Sarah. Her theme song is x.co/imdabes',
        'date_posted': 'October 6'
    },
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
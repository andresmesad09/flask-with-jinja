from flask import Flask, render_template
import random
from datetime import datetime
from utils import APIGuesser, BlogGetter

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    api_guesser = APIGuesser(name)
    return render_template(template_name_or_list="guess.html", api_guesser=api_guesser)


@app.route("/blogs")
def get_blogs():
    blog_client = BlogGetter()
    return render_template("blogs.html", blogs=blog_client.blogs)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

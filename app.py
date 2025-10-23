from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif", 
    "https://media.giphy.com/media/3o72FfM5HJydzafgUE/giphy.gif",
    "https://media.giphy.com/media/3o6Zt6KHxJTbXC3wfC/giphy.gif",
    "https://media.giphy.com/media/OmK8lulOMQ9XO/giphy.gif",
    "https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask
from stories import story

app = Flask(__name__)

@app.route('/')
def questions():
    words = story.prompts

    return render_template('index.html', words= words)

@app.route('/story')
def add_story():
    text = story.generate(request.args)

    return render_template('story.html', text= text)

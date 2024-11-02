from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

jobs = [
    "Professional Cloud Observer",
    "Unicorn Trainer",
    "Space Pizza Delivery Driver",
    "Astro-Architect",
    "Galactic Ambassador",
    "Time Travel Tour Guide",
    "Alien Language Interpreter",
    "Chief Happiness Officer",
    "Dream Weaver",
    "Interstellar Farmer"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_job')
def get_job():
    job = random.choice(jobs)
    return jsonify(job=job)

if __name__ == '__main__':
    app.run(debug=True)

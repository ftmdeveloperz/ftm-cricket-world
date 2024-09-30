from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

API_KEY = 'd670fa9a-8d0b-4afd-93a6-d99d2047983f'  # Your CricAPI key

@app.route('/')
def home():
    scores = get_live_scores()  # Function to fetch live scores
    return render_template('index.html', scores=scores)

def get_live_scores():
    url = f'https://cricapi.com/api/cricket/?apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data.get('data', [])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

from flask import Flask, render_template
import requests

app = Flask(__name__)

# Your CricAPI key
CRIC_API_KEY = 'd670fa9a-8d0b-4afd-93a6-d99d2047983f'
BASE_URL = 'https://cricapi.com/api/'

def get_live_scores():
    try:
        response = requests.get(f"{BASE_URL}cricketScore?apikey={CRIC_API_KEY}")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        # Check if data is not empty
        if data:
            return data
        else:
            return "No live scores available."
    except requests.exceptions.RequestException as e:
        print(f"Error fetching live scores: {e}")
        return "Error fetching live scores."

@app.route('/')
def home():
    scores = get_live_scores()  # Fetch live scores
    return render_template('scores.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Specify the port here

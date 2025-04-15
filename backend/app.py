from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# Update CORS for production
CORS(app, resources={r"/api/*": {"origins": ["", "http://localhost:3000"]}})

# Get API key from environment variable
API_KEY = os.getenv('OPENWEATHER_API_KEY')
if not API_KEY:
    raise ValueError("No OpenWeather API key found. Please set OPENWEATHER_API_KEY in .env file")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route('/')
def index():
    return 'The API is working'

@app.route('/api/weather', methods=['GET'])
def get_weather():
    print("Received request for weather data")
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location parameter is required'}), 400
    
    try:
        print(f"Fetching weather for location: {location}")
        params = {
            'q': location,
            'appid': API_KEY,
            'units': 'metric'  # Use metric units
        }   
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather_data = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed'],
                'city': data['name'],
                'country': data['sys']['country']
            }
            print(f"Weather data fetched successfully for {location}")
            return jsonify(weather_data)
        else:
            print(f"Error fetching weather data: {response.status_code}")
            return jsonify({'error': 'Failed to fetch weather data'}), response.status_code
            
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Use environment variables for production settings
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 
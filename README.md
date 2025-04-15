# Weather App

A simple weather application built with React frontend and Flask backend that displays weather information for any location.

## Features

- Search weather by city name
- Display temperature, humidity, weather description, and wind speed
- Show location information (city and country)
- Modern and responsive UI

## Prerequisites

- Python 3.7+
- Node.js 14+
- OpenWeatherMap API key

## Setup

1. Clone the repository
2. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
3. Backend setup:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
   Edit the `.env` file and add your OpenWeatherMap API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

4. Frontend setup:
   ```bash
   cd frontend
   npm install
   ```

## Running the Application

1. Start the backend server:
   ```bash
   cd backend
   python app.py
   ```

2. Start the frontend development server:
   ```bash
   cd frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Enter a city name in the search box
2. Click "Get Weather" or press Enter
3. View the weather information for the specified location

## Technologies Used

- Frontend: React.js
- Backend: Flask (Python)
- API: OpenWeatherMap
- Styling: CSS 
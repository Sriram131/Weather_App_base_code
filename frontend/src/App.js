import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

// const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';
const API_URL = 'https://weather-app-base-code.onrender.com' || 'http://localhost:5000';


function App() {
  const [location, setLocation] = useState('');
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchWeather = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.get(`${API_URL}/api/weather?location=${location}`);
      setWeather(response.data);
      setError('');
    } catch (err) {
      setError('Failed to fetch weather data. Please try again.');
      setWeather(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1>Weather App</h1>
        <form onSubmit={fetchWeather}>
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            placeholder="Enter city name"
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Loading...' : 'Get Weather'}
          </button>
        </form>

        {error && <p className="error">{error}</p>}

        {weather && (
          <div className="weather-info">
            <h2>{weather.city}, {weather.country}</h2>
            <div className="weather-details">
              <p>Temperature: {weather.temperature}°C</p>
              <p>Humidity: {weather.humidity}%</p>
              <p>Weather: {weather.description}</p>
              <p>Wind Speed: {weather.wind_speed} m/s</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App; 

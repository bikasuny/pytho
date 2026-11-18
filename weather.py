import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText('Enter city name')
        layout.addWidget(self.city_input)

        self.get_weather_button = QPushButton('Get Weather', self)
        self.get_weather_button.clicked.connect(self.get_weather)
        layout.addWidget(self.get_weather_button)

        self.weather_label = QLabel('', self)
        self.weather_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.weather_label)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text()
        if city:
            api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                self.weather_label.setText(f'Temperature: {temp}°C\nDescription: {description}')
            else:
                self.weather_label.setText('City not found or API error.')
        else:
            self.weather_label.setText('Please enter a city name.')
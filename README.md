# IoT Temperature and Humidity Monitor

This project is a simple IoT system to monitor temperature and humidity using a sensor and a microcontroller. Data is sent to a server using MQTT and stored in a database for analysis and visualization.

## Components
- Microcontroller (e.g., Raspberry Pi, ESP8266/ESP32)
- Temperature and Humidity Sensor (e.g., DHT22)
- MQTT Broker
- Python

## Setup
### Hardware
1. Connect the sensor to the microcontroller.
2. Ensure the microcontroller is connected to the internet.

### Software
1. Install dependencies:
    ```bash
    pip install Adafruit_DHT paho-mqtt sqlite3 matplotlib
    ```
2. Run the sensor script on the microcontroller:
    ```bash
    python sensor/sensor_script.py
    ```
3. Run the server script to receive and store data:
    ```bash
    python server/server_script.py
    ```
4. Run the visualization script to see the collected data:
    ```bash
    python server/visualize_data.py
    ```
## Running the Test Script
To test the system without actual hardware, you can run the `main.py` script which generates and publishes fake temperature and humidity data.

1. Ensure you have installed the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the test script:
    ```bash
    python main.py
    ```

This script will generate and publish fake data every 10 seconds.

## License
This project is licensed under the MIT License.

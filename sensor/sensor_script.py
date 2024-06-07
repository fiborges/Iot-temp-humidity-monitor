import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import json
from config.mqtt_config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

# Define o tipo de sensor e o pino GPIO ao qual está conectado
sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO4

# Configuração do MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        print("Falha ao ler os dados do sensor")
        return None, None

def publish_data(humidity, temperature):
    payload = json.dumps({'temperature': temperature, 'humidity': humidity})
    client.publish(MQTT_TOPIC, payload)
    print(f"Publicado: {payload}")

# Loop principal
while True:
    humidity, temperature = read_sensor()
    if humidity is not None and temperature is not None:
        publish_data(humidity, temperature)
    time.sleep(60)  # Publica a cada 60 segundos

import paho.mqtt.client as mqtt
import time
import json
import random
from config.mqtt_config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

# Configuração do MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def generate_fake_data():
    # Gera dados fictícios de temperatura e umidade
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(30.0, 60.0), 2)
    return humidity, temperature

def publish_data(humidity, temperature):
    payload = json.dumps({'temperature': temperature, 'humidity': humidity})
    client.publish(MQTT_TOPIC, payload)
    print(f"Publicado: {payload}")

# Loop principal
while True:
    humidity, temperature = generate_fake_data()
    publish_data(humidity, temperature)
    time.sleep(10)  # Publica a cada 10 segundos para testes

import sys
import os

# Adicionar o diretório do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import paho.mqtt.client as mqtt
import sqlite3
import json
from config.mqtt_config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

# Configuração do banco de dados
conn = sqlite3.connect('server/sensor_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS data
             (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, temperature REAL, humidity REAL)''')
conn.commit()

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    temperature = payload['temperature']
    humidity = payload['humidity']
    c.execute("INSERT INTO data (temperature, humidity) VALUES (?, ?)", (temperature, humidity))
    conn.commit()
    print(f"Dados inseridos: Temperatura={temperature}, Humidade={humidity}")

# Configuração do MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.on_message = on_message

client.loop_forever()

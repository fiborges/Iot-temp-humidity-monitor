import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# Conecta ao banco de dados
conn = sqlite3.connect('server/sensor_data.db')
c = conn.cursor()

# Busca os dados
c.execute("SELECT timestamp, temperature, humidity FROM data")
rows = c.fetchall()

# Processa os dados
timestamps = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in rows]
temperatures = [row[1] for row in rows]
humidities = [row[2] for row in rows]

# Plota os dados
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(timestamps, temperatures, label='Temperature (°C)')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(timestamps, humidities, label='Humidity (%)')
plt.xlabel('Timestamp')
plt.ylabel('Humidity (%)')
plt.legend()

plt.tight_layout()
plt.show()

import network
import ssl
import time
import ubinascii
import ujson
import upip
from simple import MQTTClient
from machine import Pin, I2C, Timer
import dht
from DHT11 import InvalidChecksum, InvalidPulseCount
from blink import blink, fast_blink, attention_blink

# MQTT client and broker constants / PEM encoded data (Privacy-Enhanced Mail)
MQTT_CLIENT_KEY = "*****************************************-private.pem.key"
MQTT_CLIENT_CERT = "*****************************************-certificate.pem.crt"
MQTT_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
MQTT_BROKER = "**************-ats.iot.us-east-1.amazonaws.com"
MQTT_BROKER_CA = "*****************************************-ca1.pem"
# Certificate Authority

MQTT_DHT11 = "pico/w/dht11"

# Read PEM file and return byte array of data.
def read_pem(file):
    with open(file) as input:
        text = input.read().strip()
        split_text = text.split("\n")
        base64_text = "".join(split_text[1:-1])
        return ubinascii.a2b_base64(base64_text)

# Read the data in the private key, public certificate, and root CA files.
key = read_pem(MQTT_CLIENT_KEY)
cert = read_pem(MQTT_CLIENT_CERT)
ca = read_pem(MQTT_BROKER_CA)

# Create MQTT client that use TLS/SSL for a secure connection.
mqtt_client = MQTTClient(
    MQTT_CLIENT_ID,
    MQTT_BROKER,
    keepalive=60,
    ssl = True,
    ssl_params= {
        "key": key,
        "cert": cert,
        "server_hostname": MQTT_BROKER,
        "cert_reqs": ssl.CERT_REQUIRED,
        "cadata": ca
    }
)

# Wi-Fi network constants
WIFI_SSID = "xxxxxxxxxxxxx"
WIFI_PWD = "***********"

# Initialize the Wi-Fi interface
wlan = network.WLAN(network.STA_IF)
print(f"Connecting to Wi-Fi SSID: {WIFI_SSID}")

# Activate and connect to the Wi-Fi network:
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PWD)

while not wlan.isconnected():
    time.sleep(0.5)

print(f"Connected to Wi-Fi SSID: {WIFI_SSID}")

# Register callback for MQTT messages and connect to broker.
print(f"Connecting to MQTT Broker: {MQTT_BROKER}")
mqtt_client.connect()
print(f"Connected to MQTT broker: {MQTT_BROKER}")
fast_blink(3)

# Callback function periodically send MQTT ping messages to the broker.
def send_mqtt_ping(t):
    print("TX: ping")
    mqtt_client.ping()

# Create timer for periodic MQTT ping messages for keeping the connection alive.
mqtt_ping_timer = Timer(
    mode=Timer.PERIODIC, period=mqtt_client.keepalive * 1000, callback=send_mqtt_ping)

# Dht sensor
pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)
from timestamp import format_timestamp

while True:
    try:
        time.sleep(5)
        temp = (sensor.temperature)
        hum = (sensor.humidity)
        timestamp = time.time()
        formatted_time = format_timestamp(timestamp)
        data = {
            "temperature": temp,
            "humidity": hum,
            "timestamp": formatted_time
        }
        payload = json.dumps(data)
        mqtt_client.publish("picow/dht11", payload)
        print("Sent", payload)
        blink()
    except InvalidPulseCount as e:
        print(e)
        attention_blink()
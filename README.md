# Solar-Powered Smart Sensing System

This project involves the design and implementation of a solar-powered smart sensing system using the Raspberry Pi Pico W microcontroller and Amazon Web Services (AWS) IoT platform. The system collects environmental data using a DHT11 temperature and humidity sensor and sends the data to AWS IoT Core for further processing and storage.

## Introduction

The demand for energy-efficient and sustainable solutions has led to the development of smart systems based on renewable energy sources. This project presents the design and implementation of a solar-powered smart sensing system using the Raspberry Pi Pico W and AWS IoT platform. The system is powered by a solar panel and a 18650 lithium battery, and it periodically collects sensor data, which is sent to AWS for analysis.

## Components

- Raspberry Pi Pico W
- DHT11 temperature and humidity sensor
- 6V 250mA solar panel
- 3.7V 2200mAh 18650 lithium battery
- TP4056 charging module
- Schottky diodes
- Various connecting wires and resistors

## Setup

1. **Hardware Setup:**
   - Connect the solar panel and battery to the TP4056 charging module.
   - Connect the DHT11 sensor to the Raspberry Pi Pico W (Pin 28).
   - Connect the TP4056 charging module to the Raspberry Pi Pico W for power supply.
   - Add Schottky diodes to protect the solar panel and battery.

2. **Software Setup:**
   - Install MicroPython on the Raspberry Pi Pico W.
   - Install required libraries (e.g., `umqtt.simple`, `machine`, `dht`).

3. **AWS Setup:**
   - Create an AWS IoT Core account and set up a new "Thing".
   - Download the necessary certificates and keys.
   - Configure AWS IoT Core, AWS Lambda, and DynamoDB for data storage and analysis.

## Code Overview

The main components of the code are as follows:

- **WiFi Connection:** Connects to a specified WiFi network.
- **MQTT Client:** Configures and connects to the MQTT broker using TLS/SSL for secure communication.
- **Sensor Data Collection:** Reads temperature and humidity data from the DHT11 sensor.
- **Data Transmission:** Publishes the sensor data to the MQTT broker.
- **LED Indications:** Uses onboard LED to indicate different statuses (connection, data sent, error).

### `blink.py`
Defines three LED blink modes:
- `attention_blink`: Infinite fast blink to indicate a problem.
- `blink`: Normal blink to indicate data has been successfully sent.
- `fast_blink`: Quick blink to indicate a successful connection.

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/picow-smart-sensing.git

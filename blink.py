from machine import Pin
import time

# Define the LED pin
LED_PIN = 25

# Initialize the LED pin
led = Pin(LED_PIN, Pin.OUT)

def attention_blink():
    """Blink the LED infinitely fast to indicate a problem."""
    while True:
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)

def blink():
    """Normal blink to indicate data has been successfully sent."""
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

def fast_blink(count):
    """Blink quickly to indicate a successful connection."""
    for _ in range(count):
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
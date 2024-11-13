from machine import Pin
import time
import dht

# Set up the DHT22 sensor on GPIO 15 (or your chosen pin)
dht_sensor = dht.DHT22(Pin(14))

while True:
    try:
        # Trigger the DHT22 to take a reading
        dht_sensor.measure()
        
        # Read temperature and humidity from the sensor
        temperature_c = dht_sensor.temperature()  # in Celsius
        humidity = dht_sensor.humidity()          # in %
        
        # Convert Celsius to Fahrenheit
        temperature_f = temperature_c * 9 / 5 + 32
        
        # Print the values to the terminal
        print("Temperature: {:.2f}°C / {:.2f}°F, Humidity: {}%".format(temperature_c, temperature_f, humidity))
        
    except OSError as e:
        # Handle any sensor read errors
        print("Failed to read sensor:", e)
        
    # Wait for 2 seconds before taking another reading
    time.sleep(2)


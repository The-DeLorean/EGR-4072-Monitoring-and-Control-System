from machine import ADC, Pin
import time

# Initialize ADC on Pin 26
adc = ADC(Pin(26))  # Corrected initialization

def read_voltage(adc):
    raw_value = adc.read_u16()  # Read the raw 16-bit ADC value
    return (raw_value / 65535) * 3.3  # Convert to voltage (assuming 3.3V reference)

def voltage_to_irradiance(voltage, max_voltage=2.5, max_irradiance=1800):
    if voltage < 0:
        return 0
    elif voltage > max_voltage:
        return max_irradiance
    else:
        return (voltage / max_voltage) * max_irradiance

# Main loop
while True:
    voltage = read_voltage(adc)  # Read voltage from ADC
    irradiance = voltage_to_irradiance(voltage)  # Convert to irradiance
    print(f"Voltage: {voltage:.2f} V, Irradiance: {irradiance:.2f} W/m²")
    time.sleep(1)

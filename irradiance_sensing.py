from machine import ADC, Pin
import time

ADC_converter = 65535
max_irradiance = 2000
min_voltage = 0.66
max_voltage = 3.3

adc = ADC(Pin(26))

def read_irradiance():
    ADC_value = adc.read_u16()
    voltage = ADC_value * (max_voltage / ADC_converter)
    irradiance = (voltage - min_voltage) * (max_irradiance / (max_voltage - min_voltage))
    return irradiance

while True:
    irradiance = read_irradiance()
    print("Irradiance:", irradiance, "W/m²")
    time.sleep(1)

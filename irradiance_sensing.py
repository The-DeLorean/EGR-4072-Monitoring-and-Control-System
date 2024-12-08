import machine
import time

adc_pin = 26
adc = machine.ADC(adc_pin)
resistor = 220

v_ref = 3.3

#Pyranometer specifications
i_min = 4    # Minimum current (mA)
i_max = 20   # Maximum current (mA)
irradiance_range = 1800

def read_irradiance():
    adc_value = adc.read_u16()
    v_measured = (adc_value / 65535) * v_ref

    # Convert voltage to irradiance (W/m²)
    irradiance = ((v_measured / shunt_resistor) * 1000 - i_min) * (irradiance_range / (i_max - i_min))

    return irradiance

while True:
    irradiance = read_irradiance()
    print("Irradiance: {:.2f} W/m²".format(irradiance))
    time.sleep(1)
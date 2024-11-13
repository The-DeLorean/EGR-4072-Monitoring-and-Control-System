from machine import Pin
import time

# Define pins for the A4988 driver
STEP_PIN = 16  # STEP pin
DIR_PIN = 17   # Direction pin
ENABLE_PIN = 18  # Enable pin (optional)

# Set up the pins
step_pin = Pin(STEP_PIN, Pin.OUT)
dir_pin = Pin(DIR_PIN, Pin.OUT)
enable_pin = Pin(ENABLE_PIN, Pin.OUT)

# Enable the driver (LOW is active for A4988 enable pin)
enable_pin.value(0)

# Steps for a 180-degree turn (200 steps per revolution)
steps_180_degrees = 200

def step_motor(steps, direction, delay=0.001):
    """
    Control the stepper motor.
    
    :param steps: Number of steps to move the motor.
    :param direction: Set direction - 1 for one direction, 0 for the other.
    :param delay: Delay between steps in seconds (adjust for speed).
    """
    # Set the direction
    dir_pin.value(direction)
    
    # Loop to send pulses
    for _ in range(steps):
        # Generate pulse for step
        step_pin.value(1)
        time.sleep(delay)
        step_pin.value(0)
        time.sleep(delay)

# Example usage:
try:
    # Rotate the motor 180 degrees clockwise
    step_motor(steps_180_degrees, direction=1, delay=0.001)

finally:
    # Disable the driver (set ENABLE high to turn off motor)
    enable_pin.value(1)


import time
import board
import busio
import adafruit_vl6180x

# Initialize I2C bus
i2c = busio.I2C(board.GP1, board.GP0)  # SCL=GP1, SDA=GP0

# Initialize the VL6180X sensor
sensor = adafruit_vl6180x.VL6180X(i2c)

while True:
    # Read range value in millimeters
    range_mm = sensor.range
    print("Range: {} mm".format(range_mm))
    
    time.sleep(1)

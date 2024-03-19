import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]

# period = float(input("Введите период треугольного сигнала в секундах: "))
try:
    period = float(input("Введите период треугольного сигнала в секундах: "))
    while True:
        for i in range(256):
            binary_value = dec2bin(i)
            GPIO.output(dac, binary_value)
            time.sleep(period / (256 * 2))
        
        for i in range(255, -1, -1):
            binary_value = dec2bin(i)
            GPIO.output(dac, binary_value)
            time.sleep(period * 0.5 / 256)

except KeyboardInterrupt:
    pass

finally:
    GPIO.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    GPIO.cleanup()
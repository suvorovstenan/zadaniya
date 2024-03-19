import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]  # GPIO pins for DAC

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal_to_binary_list(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]

try:
    while True:
        user_input = input("Введите число от 0 до 255 (q - для выхода): ")
        
        if user_input.lower() == 'q':
            break
        
        try:
            number = int(user_input)
            if number < 0 or number > 255:
                print("Пожалуйста, введите число от 0 до 255.")
                continue
        except ValueError:
            print("Пожалуйста, введите целое числo от 0 до 255.")
            continue

        binary_value = decimal_to_binary_list(number)
        GPIO.output(dac, binary_value)

        voltage = number * (3.3 / 255)
        print(f"Предполагаемое напряжение на ЦАП: {voltage:.2f} В")

except KeyboardInterrupt:
    pass

finally:
    GPIO.output(dac, [0, 0, 0, 0, 0, 0, 0, 0])
    GPIO.cleanup()
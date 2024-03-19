import RPi.GPIO as GPIO

GPIO.setwarnings(False)


pwm_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

pwm = GPIO.PWM(pwm_pin, 1000)
pwm.start(0)

try:
    while True:
        user_input = input("Введите коэффициент заполнения ШИМ (от 0 до 100, q - для выхода): ")
        
        if user_input.lower() == 'q':
            break
        
        try:
            duty_cycle = float(user_input)
            if duty_cycle < 0 or duty_cycle > 100:
                print("Пожалуйста, введите число от 0 до 100.")
                continue
        except ValueError:
            print("Пожалуйста, введите числовое значение от 0 до 100.")
            continue

        pwm.ChangeDutyCycle(duty_cycle)

        # Calculate and print the expected voltage on the RC circuit output
        voltage = round((3.3 * duty_cycle / 100), 2)
        print(f"Предполагаемое напряжение на выходе RC-цепи: {voltage} В")

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
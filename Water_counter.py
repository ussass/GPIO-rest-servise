import RPi.GPIO as GPIO


class Water_counter:
    hot = 0
    cold = 0


hot_key = 4
cold_key = 17
hot_flag = False
cold_flag = False

GPIO.setmode(GPIO.BCM)

GPIO.setup(hot_key, GPIO.IN)
GPIO.setup(cold_key, GPIO.IN)

try:
    while True:
        if GPIO.input(hot_key) == False and hot_flag == True:
            Water_counter.hot += 1
        if GPIO.input(cold_key) == False and cold_flag == True:
            Water_counter.cold += 1
        hot_flag = GPIO.input(hot_key)
        cold_flag = GPIO.input(cold_flag)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('Exit')
finally:
    GPIO.cleanup()
    print('End')

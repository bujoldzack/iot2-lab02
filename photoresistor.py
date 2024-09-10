#!/usr/bin/env python
import ADC0832
import time
import RPi.GPIO as GPIO

MAX_VOLTAGE = 3.3
MAX_ADC_VALUE = 255
LED_PIN = 26

def init():
    ADC0832.setup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

def get_lux(adc_value):
    voltage = MAX_VOLTAGE / MAX_ADC_VALUE * adc_value
    lux = voltage * 100
    return lux

def loop():
    while True:
        res = ADC0832.getADC(0)
        vol = 3.3/255 * res
        lux = get_lux(res)
        print('analog value: %03d  ||  voltage: %.2fV || lux: %.2f' %(res, vol, lux))
        
        if lux < 10:
            print("Dark")
            GPIO.output(LED_PIN, GPIO.LOW)
        else:
            print("Light")
            GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.2)

if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt: 
        ADC0832.destroy()
        GPIO.cleanup()
        print ('The end !')

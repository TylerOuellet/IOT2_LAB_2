#!/usr/bin/env python
import ADC0832
import time
import RPi.GPIO as GPIO
mode = "debug"
LED_PIN = 24
def init():
    ADC0832.setup()
    
    GPIO.setup(LED_PIN,  GPIO.OUT)

def loop():
    while True:
        res = ADC0832.getADC(0)
        vol = 3.3/255 * res
        if mode == "test" or mode == "debug":
            print ('analog value: %03d || voltage: %.2fV' %(res, vol))
        

        if mode == "log" or mode == "debug":
            if res >= 128:
                print("Light")
            else:
                print("Dark")
        time.sleep(0.2)

        if mode == "alert" or mode == "debug":
            if res >= 128:
                GPIO.output(LED_PIN,True)
            else:
                GPIO.output(LED_PIN,False)
                
                

if __name__ == '__main__':
    init()
    print("Modes:")
    print("test: displays in console analog and voltage values")
    print("log: displays in console if it is light or dark")
    print("alert: toggles led if light, off if dark")
    print("debug: all of them at once")
    mode = input("Mode: ")
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.output(LED_PIN,False)
        ADC0832.destroy()
        print ('The end !')

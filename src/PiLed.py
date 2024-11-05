# use "killall python" in the console to end the program

from hal import hal_input_switch as switch
from hal import hal_led as led



import socket
import time
from time import sleep

def setup():

    led.init()
    switch.init()
    print("hello")





def main():
    i = 0
    runTime = 20
    print("1111")
    setup()
    while i < runTime:
        setup()
        swState = switch.read_slide_switch()
        while swState == 1:
            print("on")
            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)
            time.sleep(0.1)
            swState = switch.read_slide_switch()
            i = i+1
            if i > runTime:
                break

        while swState == 0:
            led.set_output(0, 0)
            print("off")
            swState = switch.read_slide_switch()
            time.sleep(0.5)
            i = i+1
            if i > runTime:
                break

if __name__ == "__main__":
    main()
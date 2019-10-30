import RPi.GPIO as GPIO
import time
class hcsr04:
    def __init__(self,pin,pout):
      GPIO.setmode(GPIO.BCM)
      self.pin=pin
      self.pout=pout
      GPIO.setup(self.pin, GPIO.IN)
      GPIO.setup(self.pout, GPIO.OUT)

    def measure(self):
        GPIO.output(self.pout, GPIO.HIGH)
        time.sleep(0.000001)
        GPIO.output(self.pout, GPIO.LOW)

        while GPIO.input(self.pin) == 0:
          pulse_start = time.time()
        while GPIO.input(self.pin) == 1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 34000 / 2.0

        return distance




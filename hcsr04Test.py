import hcsr04class
import time
hc=hcsr04class.hcsr04(27,17)
while True:
    print(hc.measure())
    time.sleep(0.1)
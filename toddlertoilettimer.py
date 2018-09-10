print("Initializing...")
from gpiozero import TrafficHat
from time import sleep
redtime=10
ambertime=3
greentime=30
buzzertime=3
a = TrafficHat()
a.lights.red.blink(0.1,0.2,10)
sleep(0.1)
a.lights.amber.blink(0.1,0.2,10)
sleep(0.1)
a.lights.green.blink(0.1,0.2,10,False)
while True:
  print("Waiting for button press...")
  a.button.wait_for_press()
  #turn on red light and periodic beep
  a.lights.red.on()
  a.buzzer.beep(0.1,1.9,int(redtime/2),False)
  a.lights.red.off()
  #switch to amber light and faster beep
  a.lights.amber.on()
  a.buzzer.beep(0.1,0.9,ambertime,False)
  a.lights.amber.off()
  #switch to green light and fast beep
  a.lights.green.on()
  a.buzzer.beep(0.1,0.1,int(buzzertime/0.2),False)
  sleep(greentime-buzzertime)
  a.off()

#sample main.py for testing Microphyton for ESP32 for Sparkfun TB6612FNG Motor Drive for two motors
from machine import Pin, PWM
from time import sleep
from TB6612FNG import Motor

frequency = 50

BIN2 = 14 
BIN1 = 27 
STBY = 26
AIN1 = 32
AIN2 = 33
PWMA = 12
PWMB = 13
ofsetA = 1
ofsetB = 1

motor = Motor(BIN2,BIN1,STBY,AIN1,AIN2,PWMA,PWMB,ofsetA,ofsetB)

motor.forward(400)
sleep(10)

motor.backward(600)
sleep(10)

motor.right(700)
sleep(10)

motor.left(800)
sleep(10)

motor.brake()
sleep(5)

motor.stop()
sleep(5)

motor.standby()
sleep(5)

motor.run()
sleep(5)





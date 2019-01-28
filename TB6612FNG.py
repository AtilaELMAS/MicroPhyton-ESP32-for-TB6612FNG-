"""
Microphyton for ESP32 for Sparkfun TB6612FNG Motor Drive for two motors
by Atila ELMAS, atila.alpagut@gmail.com
the following functions implemented forward, backward, right, left,
brake, stor, standby

please note that only some Pin available for PWM and OUT for DOIT ESP32 dev.R1 36 pins
PWM pins : 0, 2, 4, 5, 10, 12, 13, 22
OUT pins : 0, 2, 4, 5, 10, 12, 13-19, 21-27,32,33


"""
from machine import Pin,PWM
from time import sleep

class Motor():
    def __init__(self, BIN2,BIN1,STBY,AIN1,AIN2,PWMA,PWMB,ofsetA,ofsetB):
        
        self.bin2 = Pin(BIN2, mode=Pin.OUT, pull=None)
        self.bin1 = Pin(BIN1, mode=Pin.OUT, pull=None)
        self.ain2 = Pin(AIN2, mode=Pin.OUT, pull=None)
        self.ain1 = Pin(AIN1, mode=Pin.OUT, pull=None)
        self.stby = Pin(STBY, mode=Pin.OUT, pull=None)
        self.apwm = PWM(Pin(PWMA),50)
        self.bpwm = PWM(Pin(PWMB),50)
        self.stby.value(1)
        if ofsetA==1:
            self.aofset=True
        else:
            self.aofset=False
        if  ofsetB==1:
            self.bofset=True
        else:
            self.bofset=False
        
    def forward(self,speed):
        
        if self.aofset:
            self.ain1.value(1)
            self.ain2.value(0)
        else: 
            self.ain1.value(0)
            self.ain2.value(1)
                      
        if self.bofset:
            self.bin1.value(1)
            self.bin2.value(0)
        else: 
            self.bin1.value(0)
            self.bin2.value(1)
            
        self.apwm.duty(speed)
        self.bpwm.duty(speed)
    
    def backward(self,speed):
        
        if self.aofset:
            self.ain1.value(0)
            self.ain2.value(1)
        else: 
            self.ain1.value(1)
            self.ain2.value(0)
            
        if self.bofset:
            self.bin1.value(0)
            self.bin2.value(1)
        else: 
            self.bin1.value(1)
            self.bin2.value(0)
            
        self.apwm.duty(speed)
        self.bpwm.duty(speed)
        
    def right(self,speed):
        
        if self.aofset:
            self.ain1.value(1)
            self.ain2.value(0)
        else: 
            self.ain1.value(0)
            self.ain2.value(1)
                      
        if self.bofset:
            self.bin1.value(0)
            self.bin2.value(1)
        else: 
            self.bin1.value(1)
            self.bin2.value(0)
            
        self.apwm.duty(speed)
        self.bpwm.duty(speed)
    
    
    def left(self,speed):
        
        if self.aofset:
            self.ain1.value(0)
            self.ain2.value(1)
        else: 
            self.ain1.value(1)
            self.ain2.value(0)
                      
        if self.bofset:
            self.bin1.value(1)
            self.bin2.value(0)
        else: 
            self.bin1.value(0)
            self.bin2.value(1)
            
        self.apwm.duty(speed)
        self.bpwm.duty(speed)
        
    def brake(self):
        
        self.ain1.value(1)
        self.ain2.value(1)        
        self.bin1.value(1)
        self.bin2.value(1)
        self.apwm.duty(0)
        self.bpwm.duty(0)
        
    def stop(self):
        
        self.ain1.value(0)
        self.ain2.value(0)        
        self.bin1.value(0)
        self.bin2.value(0)
        self.apwm.duty(1000)
        self.bpwm.duty(1000)
        
    def standby(self):
        self.ain1.value(0)
        self.ain2.value(0)        
        self.bin1.value(0)
        self.bin2.value(0)
        self.apwm.duty(1000)
        self.bpwm.duty(1000)
        
        self.stby.value(0)
        
    def run(self):
        self.ain1.value(0)
        self.ain2.value(0)        
        self.bin1.value(0)
        self.bin2.value(0)
        self.apwm.duty(1000)
        self.bpwm.duty(1000)
        self.stby.value(1)
        
        

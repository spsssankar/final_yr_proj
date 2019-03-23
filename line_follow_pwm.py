import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2,IO.IN) #GPIO 2 -> Right IR out
IO.setup(3,IO.IN) #GPIO 3 -> Left IR out

IO.setup(4,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(14,IO.OUT) #GPIO 14 -> Motor 1 terminal B

IO.setup(17,IO.OUT) #GPIO 17 -> Motor Left terminal A
IO.setup(18,IO.OUT) #GPIO 18 -> Motor Left terminal B

IO.setup(12,IO.OUT) #GPIO 12 -> Pin 32 pwm -> ENA
IO.setup(13,IO.OUT) #GPIO 13 -> Pin 33 pwm -> ENB

def left(value):
    IO.output(4,False) #1A+
    IO.output(14,False) #1B-

    IO.output(17,True) #2A+
    IO.output(18,False) #2B-

    IO.output(12,value)

def right(value):
    IO.output(4,False) #1A+
    IO.output(14,True) #1B-

    IO.output(17,False) #2A+
    IO.output(18,False) #2B-

    IO.output(13,value)

def forward(value):
    IO.output(4,False) #1A+
    IO.output(14,True) #1B-

    IO.output(17,True) #2A+
    IO.output(18,False) #2B-
    IO.output(12,value)
    IO.output(13,value)


def still():
    IO.output(4,False) #1A+
    IO.output(14,False) #1B-

    IO.output(17,False) #2A+
    IO.output(18,False) #2B-


while 1:

 

    if(IO.input(2)==False and IO.input(3)==False): #both while move forward     
        
        forward()

    elif(IO.input(2)==True and IO.input(3)==False): #turn right
        
        right()

    elif(IO.input(2)==False and IO.input(3)==True): #turn left
        
        left()      

    else:  #stay still
        
        still()

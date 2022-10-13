from machine import Pin, PWM,ADC
from time import sleep

servo_x = PWM(Pin(16))
servo_x.freq(50)

servo_y = PWM(Pin(15)) 
servo_y.freq(50)
def movimentar_servos(eixo_x, eixo_y):
   
    trab_max=9000
    trab_min=1000
        
    trabalho_y=trab_min+(trab_max-trab_min)*(eixo_y/180)
    trabalho_x=trab_min+(trab_max-trab_min)*(eixo_x/180)
    servo_y.duty_u16(int(trabalho_y))
    servo_x.duty_u16(int(trabalho_x))


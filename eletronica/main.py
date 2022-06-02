from machine import Pin, PWM,ADC
from time import sleep

potx = ADC(Pin(28))
servo_x = PWM(Pin(16))
servo_x.freq(50)
poty = ADC(Pin(27))
servo_y = PWM(Pin(15)) 
servo_y.freq(50)
def movimentar_servos(eixo_x, eixo_y):
    if eixo_x > 80: eixo_x =80
    if eixo_x  < 10: eixo_x =10
    if eixo_y  > 60: eixo_y =60
    if eixo_y  < 10: eixo_y =10
    
    trab_max=9000
    trab_min=1000
    
    try:
        
        trabalho_y=trab_min+(trab_max-trab_min)*(eixo_y/180)
        trabalho_x=trab_min+(trab_max-trab_min)*(eixo_x/180)
        servo_y.duty_u16(int(trabalho_y))
        servo_x.duty_u16(int(trabalho_x))

    except Exception as e:
        print(e)

try:
    while True:
        poty_value=poty.read_u16() 
        potx_value=potx.read_u16()
        poty_value = 0 if poty_value < 0 else poty_value
        potx_value = 0 if potx_value < 0 else potx_value
        grau_x=potx_value*180/65500 
        grau_y=poty_value*180/65500 -40
        movimentar_servos(grau_x,grau_y)
        sleep(0.1)
except Exception as e:
    print(e)

from machine import Pin, PWM

frecuencia = 5000

velocidad = int(65535/3)

sensor_izq = Pin(15, Pin.IN)
sensor_der = Pin(14, Pin.IN)

motor_1 = Pin(1, Pin.OUT)
motor_2 = Pin(0, Pin.OUT)

motor_izq = PWM(motor_1)
motor_der = PWM(motor_2)

motor_izq.freq(50)
motor_der.freq(50)

def girar_izq():
    motor_izq.duty_u16(0)
    motor_der.duty_u16(velocidad)
    
def girar_der():
    motor_izq.duty_u16(velocidad)
    motor_der.duty_u16(0)

def caminar():
    motor_izq.duty_u16(velocidad)
    motor_der.duty_u16(velocidad)

def parar():
    motor_izq.duty_u16(0)
    motor_der.duty_u16(0)
    
while True:
    if sensor_izq.value() == 0 and sensor_der.value() == 0:
        caminar()
    
    elif sensor_izq.value() == 1 and sensor_der.value() == 0:
        girar_izq()
    
    elif sensor_izq.value() == 0 and sensor_der.value() == 1:
        girar_der()
    else:
        parar()

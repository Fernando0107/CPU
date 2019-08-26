import time
class Clock():
    
    def __init__(self, clock, name, brand):
        self.clock = clock
        self.name = name
        self.brand = brand
    def Hz(clock_speed):
        time.sleep(float(clock_speed))         # La velocidad del reloj esta definida por el archivo bios.yaml
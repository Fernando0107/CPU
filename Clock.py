from IC import *


class Clock(IC):
    
    def Hz():
        time.sleep(float(CU.read_file('bios.yml')[1]))        # La velocidad del reloj esta definida por el archivo bios.yaml
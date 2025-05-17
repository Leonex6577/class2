#Tapia Hernandez Jose Alejandro 
class Computadoras:
    def __init__ (self, cpu, ram,  grafica, placa_madre):
        self.cpu = cpu
        self.ram = ram
        self.grafica = grafica
        self.placa_madre = placa_madre

gaimer = Computadoras("AMD Ryzen 5 3600X", "ddr4", "Nvidia1660", "Asus")

print(gaimer.cpu)
print(gaimer.ram)
print(gaimer.grafica)
print(gaimer.placa_madre)
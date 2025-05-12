class Computadoras:
    cpu = "Ryzen_6500"
    tarjeta_grafica = "Nvidia_1660"
    ram = "drra4"
    placa_madre = "Asus" 
    
gaimer = Computadoras()
print(gaimer.cpu)
gaimer.cpu = "Intel Core i9"
print(gaimer.cpu)

print(gaimer.tarjeta_grafica)
gaimer.tarjeta_grafica = "Nvidia_6090"
print(gaimer.tarjeta_grafica)
print(gaimer.ram)
gaimer.ram = "ddr3"
print(gaimer.ram)
print(gaimer.placa_madre)
gaimer.placa_madre = "Asus pro"
print(gaimer.placa_madre)
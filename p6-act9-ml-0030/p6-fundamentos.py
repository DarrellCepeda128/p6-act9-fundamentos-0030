# Cepeda Darrell
# NC 0030
print("/*/*/*/* VARIABLES MULTIPLES */*/*/*")

x, y, z = "Carro", "Bicicleta", "Yate"
print(x)
print(y)
print(z)

x = y = z = "Carro"
print(x)
print(y)
print(z)

vehiculos = ["Carro", "Bicicleta", "Yate"]
x, y, z = vehiculos
print(x)
print(y)
print(z)

print("*+*+*+*+* OPERADORES LOGICOS +*+*+*+*")

vehiculo = "Carro"

if vehiculo == "Carro" and vehiculo != "Yate":
    print("Es un carro terrestre")

vehiculo = "Bicicleta"

if vehiculo == "Carro" or vehiculo == "Bicicleta":
    print("Es un vehículo terrestre")

vehiculo = "Yate"

if not vehiculo == "Carro":
    print("No es un carro")

print("-*-*-*-*-* OPERADORES ARITMETICOS *-*-*-*-*-*-")

carro = 50000
bicicleta = 5000

total = carro + bicicleta

print("Total:", total)

yate = 100000
cantidad = 2

total = yate * cantidad

print("Costo de los yates:", total)

carro = 80000
descuento = 10000

precio = carro - descuento

print("Precio final del carro:", precio)

print("Programa realizado por Cepeda Darrell NC 0030")
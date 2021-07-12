# importar modulos
from datetime import date
from conversiones import *


# variables
fecha = date.today()
""""
moneda = input("nombre de la Criptomoneda: ")
valor = float(input("cantidad de Cripto: "))
preciomoneda = float(input("cotizacion de la moneda: "))
monedolar = (valor*preciomoneda)
"""
consulta = 0

#####   CONSULTAS

# Capital
consulta = input("cuantas divisas desea calcular: (0 = salir)")
if consulta.isdigit():
    resultado = sumatotal(int(consulta))
    print("Total: $" + str(resultado))
else:
    print("intente nuevamente")
print("Hasta luego...")
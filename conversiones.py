import requests
_ENDPOINT = "https://api.binance.com"
def _url(api):
    return _ENDPOINT+api


# FUNCIONES
def precio(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

def validador(nombre):
   criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
   if nombre in criptos:
      return True


def sumacriptos(cant):
   nombre = input("nombre de la divisa: ")
   if validador(nombre) == True:
      cripto = cant * precio(nombre)
      print("Usted posee USD $" + str(cripto) + " en " + nombre)
      return(cripto, nombre)
   else:
      return(False)
   

def sumatotal(x):
   total = 0
   cont = 0
   while cont < x:
      divisa = sumacriptos(float(input("ingrese cantidad: ")))
      total = total + divisa[0]
      cont +=1
   return(total)

nombre = "BTC"
asd = precio(nombre)
print(str(asd))
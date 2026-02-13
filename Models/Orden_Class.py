
from .Menu_Class import   Menu
from utileria import *


class Orden(Menu):
    def __init__(self) -> None:
        super().__init__()
        pass
    def pedido (self) ->None:
        self.orden_Diccionario = {"Consumo": [[], []]}
        lista_productos = self.listaAlimentos + self.listaBebidas  #lista que contiene todos los productos (alimentos y bebidas)
        lista_precios = self.listaPrecios + self.listaPreciosBebidas

        while True: #agregar un try catch por si se elige algo que no sea 1 o 2

            print("Eliga lo que desee realizar \n 1.Ordenar\n 2.Mostrar el menu\n 3.Pedir la cuenta")
            accion = int(input("Ingrese la accion : "))
            if accion == 2:
                self.mostraMenu()
            elif accion ==3:
                break
            print("Ingrese su orden: ")

            orden = input() #Agregar trycatch para que no se elija nada que no este en el menu


            #for productos in lista_productos:

            try: #Este try Catch lo usamos para saber el indice en la lista de precios del producto que buscamos, seguro hay una forma mas facil pero no se me ocurre nada


                posicion = lista_productos.index(orden)

                self.orden_Diccionario["Consumo"][0].append(orden)
                self.orden_Diccionario["Consumo"][1].append(lista_precios[posicion])
            except ValueError:
                    print("El producto no existe")


            crearJson(self.orden_Diccionario)




from Models import *
from utileria import *


def main():
    prueba = Menu()
    prueba.mostraMenu()

    Orden1 = Orden()
    Orden1.pedido()

    Cuenta1 = Cuenta()
    print(Cuenta1.total())
    print( Cuenta1.subtotal())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  main()


# Creamos la clase Vendedor
class Vendedor:
    # Creamos el constructor
    def __init__(self, nombre: str, ventas: list[float]) -> None: 
        self.__nombre =  nombre
        self.__ventas = ventas
    # Creamos el metodo getter
    def getVentasDelUsuario(self) -> list[float]:
        return self.__ventas
    def setVentas(self, indice: int, valor: float) -> None:
        # Nos ubicamos en el indice que nos proporcionaron dentro de la lista y colocamos el valor entregado
        self.__ventas[indice] = valor
    # Un setter comun y corriente
    def setNombre(self, n: str) -> None:
        self.__nombre =  n
    # Recorremos la lista e imprimos cada valor
    def imprimeVentasAnuales(self) -> None:
        for venta in self.__ventas:
            print(venta)
    # Recorremos la lista de ventas y vamos sumando cada valor a una variable contadora, dspues se imprime la variable.
    def totalVentasAnuales(self) -> float: 
        aux = 0.0
        for venta in self.__ventas:
            aux += venta
        return aux

vendedores = [] # Utilizamos esta lista para guardar los objetos que crearemos a continuacion
# Utilizamos un bucle while ya que es el usuario es el que decide en que momento detener el programa
while True:
    nombre = input('Nombre del vendedor: ')
    # Creamos un generador para facilitar la recoleccion de datos de venta anual
    ventas = [float(input(f'Valor de venta del mes {i+1}: ')) for i in range(2)] # El numero dentro del range es la cantidad de peticiones, en este caso el numero de meses en un año
    vendedor = Vendedor(nombre, ventas) # El objeto de clase Vendedor
    vendedores.append(vendedor)
    decicion = int(input('Desea continuar el programa? Si(1) No(0)\n> '))
    if decicion == 0:
        break
valor_acumulado = 0.0
for vendedor in vendedores:
    valor_acumulado += vendedor.totalVentasAnuales()
print(f'Ventas totales durante la ejecucion del programa: ${valor_acumulado} ')

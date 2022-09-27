# Creamos la clase Vendedor
class Vendedor:
    # Creamos el constructor
    def __init__(self, nombre: str, ventas: list[float]) -> None: 
        self.__nombre =  nombre
        self.__ventas = ventas
    # Creamos el metodo getter
    def getVentasDelUsuario(self) -> None:
        return self.__ventas
    def setVentas(self, indice: int, valor: float) -> None:
        # Nos ubicamos en el indice que nos proporcionaron dentro de la lista y colocamos el valor entregado
        self.__ventas[indice] = valor
    # Un setter comun y corriente
    def setNombre(self, n: str):
        self.__nombre =  n
    # Recorremos la lista e imprimos cada valor
    def __str__(self) -> str:
        return f"""
        Enero: {self.__ventas[0]}
        Febrero: {self.__ventas[1]}
        Marzo: {self.__ventas[2]}
        Mayo: {self.__ventas[3]}
        Abril: {self.__ventas[4]}
        Junio: {self.__ventas[5]}
        Julio: {self.__ventas[6]}
        Agosto: {self.__ventas[7]}
        Septiembre: {self.__ventas[8]}
        Octubre: {self.__ventas[9]}
        Noviembre: {self.__ventas[10]}
        Diciembre: {self.__ventas[11]}
        """
    # Retornamos la suma de la lista ventas
    def totalVentasAnuales(self) -> float: 
        return sum(self.__ventas)

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
print(f'Ventas totales durante la ejecucion del programa: ${valor_acumulado}')

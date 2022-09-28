class Persona:
    # Iniciamos el constructor
    def __init__(self, identidad: int, nombreCompleto: str) -> None:
        self.__identidad = identidad
        self.__nombreCompleto = nombreCompleto
    # Creamos los getter's
    def getNombre(self) -> None:
        return self.__nombreCompleto
    def getID(self) -> None:
        return self.__identidad
    # Creamos los setter's
    def setPersona(self, identidad: int, nombreCompleto: str) -> None:
        self.__identidad = identidad
        self.__nombreCompleto = nombreCompleto
    def setNombre(self, nombreCompleto: str) -> None:
        self.__nombreCompleto = nombreCompleto
    def setId(self, identidad: int) -> None:
        self.__identidad = identidad
    def setPersona(self, identidad: int, nombreCompleto: str) -> None:
        self.__identidad = identidad
        self.__nombreCompleto = nombreCompleto
    # Utilizamos el metodo magico _str_
    def __str__(self) -> None:
        return f'Nombre: {self.__nombreCompleto}\nID: {self.__identidad}'

class Tiempo:
    # Iniciamos el constructor
    def __init__(self, hora: int, minuto: int, segundo: int) -> None:
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
    # Creamos los getter's
    def getSegundo(self) -> None:
        return self.__segundo
    def getMinuto(self) -> None:
        return self.__minuto
    def getHora(self) -> None:
        return self.__minuto
    # Creamos los setter's
    def setSegundo(self, segundo: int) -> None:
        self.__segundo = segundo
    def setMinuto(self, minuto: int) -> None:
        self.__minuto = minuto
    def setHora(self, hora: int) -> None:
        self.__hora = hora
    def setTiempo(self, hora: int, minuto: int, segundo: int) -> None:
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
    # Formatos
    def imprimirEstandar(self) -> None:
    # se suman 6 horas teniendo en cuenta a colombia como el lugar donde se tomó la hora a convertir
        hora = self.__hora + 6 if self.__hora + 6 < 24 else (self.__hora + 6) - 24
        # hora es igual a self.__hora + 6 si esa suma no es mayor a 12, de lo contrario, se hace la suma y se le restan 12
        print(f'{hora}:{self.__minuto}:{self.__segundo}')

    def imprimirUniversal(self) -> None:
    # se suman 5 horas
        hora = self.__hora + 5 if self.__hora + 5 < 24 else (self.__hora + 5) - 24
        print(f'{hora}:{self.__minuto}:{self.__segundo}')

class Empleado(Persona, Tiempo):
    # Iniciamos el constructor
    def __init__(self, horaEntrada: list[int], horaSalida: list[int]) -> None:
        self.__horaEntrada = horaEntrada
        self.__horaSalida = horaSalida
    # Definimos los setter's
    def setEmpleado(self, horaEntrada: list[int], horaSalida: list[int]) -> None:
        self.__horaEntrada = horaEntrada
        self.__horaSalida = horaSalida
    def setHoraEntrada(self, horaEntrada: list[int]) -> None:
        self.__horaEntrada = horaEntrada
    def setHoraSalida(self, horaSalida: list[int]) -> None:
        self.__horaSalida = horaSalida
    # Definimos los getter's
    def getHoraEntrada(self) -> str:
        return f'{self.__horaEntrada[0]}:{self.__horaEntrada[1]}:00'
    def getHoraSalida(self) -> str:
        return f'{self.__horaSalida[0]}:{self.__horaSalida[1]}:00'
    # Metodo magico __str__
    def __str__(self) -> str:
        return f'Hora de entrada {self.__horaEntrada}, hora de salida {self.__horaSalida}'
    # Capturamos objetos externos al propio objeto y los integramos en forma de tupla
    def capturar(self, *vendedores):
        self.__capturarVendedores = vendedores

# Una funcin estetica para imprimir formato 24: (12:9) -> (12:09) 
def x(hora: list[int]) -> str:
    hora = list[0] if len(str(list[0])) == 2 else f'0{list[0]}'
    minutos = list[1] if len(str([list[1]])) == 2 else f'0{list[1]}'
    return f'{hora}:{minutos}'

# Formato Hora / Minuto / Segundo
entradaEstipulada = [7,00,00]  
salidaEstipulada = [17,00,00]

palabrasTiempo, palabraGenero = ['hora', 'minuto',], ['la', 'el']
entradaTrabajador = [int(input(f'Ingrese {palabraGenero[i]} {palabrasTiempo[i]} de entrada: ')) for i in range(len(palabrasTiempo))]
salidaTrabajador = [int(input(f'Ingrese {palabraGenero[i]} {palabrasTiempo[i]} de salida: ')) for i in range(len(palabrasTiempo))] 
empleado = Empleado(entradaTrabajador, salidaTrabajador)
horaTemprano = True if entradaTrabajador[0] - entradaEstipulada[0] < 0 else False
horaPuntual = True if entradaTrabajador[0] - entradaEstipulada[0] == 0 and entradaTrabajador[1] - entradaEstipulada[1] == 0 else False
horaTarde = True if entradaTrabajador[0] - entradaEstipulada[0] > 0 else False
operacion = (entradaEstipulada[0] - entradaTrabajador[0]) + (salidaTrabajador[0] - salidaEstipulada[0])
horaExtra = True if operacion > 0 else False
print(f'Hora de entrada estipulada: {x(entradaEstipulada)}\nHora de salida estipulada: {x(salidaEstipulada)} ')

if horaTemprano:
    print('Llego temprano')
elif horaPuntual:
    print('Llego Puntual')
elif horaTarde:
    print('Llego Tarde')
minutos = 0
if horaExtra:
    for _ in range(operacion):
        minutos += 60
    print('Los minutos a pagar por horas extra son: ' + str(minutos))
else:
    print('No hubo horas extra')

import random
import os

# Obtener el directorio donde se encuentra el script actual
# Esto asegura que los archivos generados se guarden en la misma ubicación que el script.
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

class JuegoAdivinanza:
    """
    Clase que representa el juego de adivinanza de números.
    """
    def __init__(self):
        """
        Constructor que inicializa el número secreto aleatorio entre 1 y 100,
        el contador de intentos en 0, y establece un límite de 10 intentos.
        """
        self.numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100.
        self.intentos = 0  # Inicializa el contador de intentos.
        self.limite_intentos = 10  # Límite máximo de intentos permitidos.

    def validarNumero(self, numero):
        """
        Valida si el número ingresado por el jugador es mayor, menor o igual al número secreto.

        Args:
            numero (int): Número ingresado por el jugador.

        Returns:
            str: Mensaje indicando si el número es mayor, menor o igual al número que se debe adivinar.
        """
        self.intentos += 1  # Incrementa el contador de intentos.
        if numero < self.numero_secreto:
            return "El número es mayor."
        elif numero > self.numero_secreto:
            return "El número es menor."
        else:
            return "¡Felicidades es correcto! Adivinaste el número."

    def alcanzadoLimite(self):
        """
        Verifica si el jugador alcanzó el límite de intentos permitidos por el programa.

        Returns:
            bool: True si se alcanzó el límite, False en caso contrario.
        """
        return self.intentos >= self.limite_intentos

    def reiniciar(self):
        """
        Reinicia el juego generando un nuevo número secreto y resetea el contador de intentos.
        """
        self.numero_secreto = random.randint(1, 100)  # Genera un nuevo número secreto.
        self.intentos = 0  # Resetea el contador de intentos.


class Jugador:
    """
    Clase que representa al jugador y su historial de partidas.
    """
    def __init__(self, nombre):
        """
        Constructor que inicializa el nombre del jugador y su historial de partidas.

        Args:
            nombre (str): Nombre del jugador.
        """
        self.nombre = nombre  # Nombre del jugador.
        self.partidas = []  # Lista de tuplas (intentos, ganó), que representan las partidas jugadas.

    def registrarPartida(self, intentos, gano):
        """
        Registra una partida en el historial del jugador.

        Args:
            intentos (int): Número de intentos realizados en la partida.
            gano (bool): Indica si el jugador ganó la partida.
        """
        self.partidas.append((intentos, gano))

    def mostrarEstadisticas(self):
        """
        Muestra las estadísticas del jugador, incluyendo:
        - Número total de partidas jugadas.
        - Número de partidas ganadas.
        - Porcentaje de partidas ganadas.
        """
        partidas_jugadas = len(self.partidas)  # Total de partidas jugadas.
        partidas_ganadas = sum(1 for _, gano in self.partidas if gano)  # Total de partidas ganadas.
        porcentaje = (partidas_ganadas / partidas_jugadas) * 100 if partidas_jugadas > 0 else 0  # Calcula el porcentaje de éxito.

        print(f"\nEstadísticas de {self.nombre}:")
        print(f"- Partidas jugadas: {partidas_jugadas}")
        print(f"- Partidas ganadas: {partidas_ganadas}")
        print(f"- Porcentaje de aciertos: {porcentaje:.2f}%\n")


def cargarEstadisticas():
    """
    Carga las estadísticas del jugador desde el archivo 'estadísticas.txt'.

    Returns:
        Jugador: Objeto jugador con las estadísticas cargadas.
        None: Si no existe el archivo o no se pueden cargar las estadísticas.
    """
    ruta_archivo = os.path.join(DIRECTORIO_ACTUAL, "estadisticas.txt")  # Ruta completa del archivo.
    if os.path.exists(ruta_archivo):  # Verifica si el archivo existe.
        with open(ruta_archivo, "r") as archivo:
            nombre = archivo.readline().strip()  # Lee el nombre del jugador.
            partidas = [tuple(map(int, linea.split(','))) for linea in archivo]  # Carga las partidas como tuplas.
            jugador = Jugador(nombre)  # Crea un objeto Jugador con el nombre.
            jugador.partidas = partidas  # Asigna las partidas al jugador.
            return jugador
    return None  # Si no existe el archivo, retorna None.


def guardarEstadisticas(jugador):
    """
    Guarda las estadísticas del jugador en el archivo 'estadísticas.txt'.

    Args:
        jugador (Jugador): Objeto jugador cuyas estadísticas se van a guardar.
    """
    try:
        ruta_archivo = os.path.join(DIRECTORIO_ACTUAL, "estadísticas.txt")  # Ruta completa del archivo.
        with open(ruta_archivo, "w") as archivo:
            # Escribe las estadísticas del jugador al principio del archivo
            partidas_jugadas = len(jugador.partidas)
            partidas_ganadas = sum(1 for _, gano in jugador.partidas if gano)
            porcentaje = (partidas_ganadas / partidas_jugadas) * 100 if partidas_jugadas > 0 else 0
            archivo.write(f"Estadisticas de {jugador.nombre}:\n")
            archivo.write(f"- Partidas jugadas: {partidas_jugadas}\n")
            archivo.write(f"- Partidas ganadas: {partidas_ganadas}\n")
            archivo.write(f"- Porcentaje de aciertos: {porcentaje:.2f}%\n\n")
            
            # Guarda el historial de partidas
            archivo.write("Historial de partidas (Intentos, Resultado):\n")
            for intentos, gano in jugador.partidas:
                archivo.write(f"{intentos},{int(gano)}\n")
            # 1= Gano 0=Perdio
        
        print("\nEstadísticas guardadas correctamente en 'estadísticas.txt'.")
    except Exception as e:
        print(f"\nOcurrió un error al guardar las estadísticas: {e}")


def menu():
    """
    Función principal que muestra el menú interactivo del juego.
    Permite al usuario:
    1. Comenzar una nueva partida.
    2. Ver estadísticas del jugador.
    3. Salir del juego y guardar estadísticas.
    """
    jugador = cargarEstadisticas()  # Intenta cargar las estadísticas desde el archivo.

    if not jugador:  # Si no hay estadísticas previas, pide al usuario su nombre.
        nombre = input("Ingrese su nombre: ").strip()
        jugador = Jugador(nombre)

    while True:
        # Muestra el menú principal.
        print("\nMenú:")
        print("1. Comenzar nueva partida")
        print("2. Ver estadísticas del jugador")
        print("3. Salir del juego")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # Comienza una nueva partida.
            juego = JuegoAdivinanza()
            print("\n¡Nueva partida iniciada! Adivina el número entre 1 y 100. Tienes 10 intentos.")

            while True:
                try:
                    # Solicita al jugador que ingrese un número.
                    numero = int(input(f"Intento {juego.intentos + 1}/10 - Ingresa tu número: "))
                    resultado = juego.validarNumero(numero)
                    print(resultado)

                    if resultado == "¡Felicidades es correcto! Adivinaste el número.":
                        jugador.registrarPartida(juego.intentos, True)
                        break

                    if juego.alcanzadoLimite():
                        print(f"¡Has alcanzado el límite de 10 intentos! El número era {juego.numero_secreto}.")
                        jugador.registrarPartida(juego.intentos, False)
                        break

                except ValueError:
                    print("Por favor, ingresa un número válido.")

        elif opcion == "2":
            # Muestra las estadísticas del jugador.
            jugador.mostrarEstadisticas()

        elif opcion == "3":
            # Guarda las estadísticas y sale del juego.
            guardarEstadisticas(jugador)
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida, intenta nuevamente.")


if __name__ == "__main__":
    # Punto de entrada del programa.
    menu()
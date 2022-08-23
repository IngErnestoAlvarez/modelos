from algoritmo import lavados_con
from parsear import parsear_archivo


def main():
    # Parsear archivo
    tiempos, incompatibilidades = parsear_archivo()

    # Algoritmo
    lavados = lavados_con(tiempos, incompatibilidades)

    # Salida


if __name__ == '__main__':
    main()

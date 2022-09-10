from algoritmo import lavados_con
from parsear import parsear_archivo


def main():
    # Parsear archivo
    tiempos, incompatibilidades = parsear_archivo()

    # Algoritmo
    lavados = lavados_con(tiempos, incompatibilidades)

    f = open("respuesta", "w+")
    for lavado, prendas in lavados.items():
        for prenda in prendas:
            f.write(f"{prenda} {lavado}\n")

    imprimir_gasto_total(lavados, tiempos)


def imprimir_gasto_total(lavados, tiempos):
    suma_total = 0
    for lavado, prendas in lavados.items():
        suma_total += max(map(lambda x: tiempos.get(x), prendas))
    print(suma_total)


if __name__ == '__main__':
    main()

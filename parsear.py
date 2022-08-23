from typing import Dict


def parsear_archivo():
    tiempos = {}
    incompatibilidades = {}
    f = open("primer_problema.txt", "r")
    for linea in f.readlines():
        linea = linea.strip()
        comando, *args = linea.split(" ")
        dic[comando](args, tiempos, incompatibilidades)

    return tiempos, incompatibilidades


def comando_c(args, tiempos={}, incompatibilidades={}):
    pass


def comando_p(args, tiempos={}, incompatibilidades={}):
    pass


def comando_e(args, _tiempos, incompatibilidades: Dict[object, list]):
    prenda1, prenda2 = args
    if prenda1 not in incompatibilidades:
        incompatibilidades.setdefault(prenda1, [])

    incompatibilidades[prenda1].append(prenda2)

    print(f"{prenda1} es incompatible con {prenda2}")


def comando_n(args, tiempos, _incompatibilidades):
    prenda, tiempo = args
    tiempos[prenda] = int(tiempo)
    print(f"prenda {prenda} tarda {tiempo}s")


dic = {
    'c': comando_c,
    'p': comando_p,
    'e': comando_e,
    'n': comando_n,
}

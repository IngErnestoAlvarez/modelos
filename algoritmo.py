def lavados_con(tiempos, incompatibilidades):
    tiempos_ordenados = {k: v for k, v in sorted(tiempos.items(), key=lambda item: -item[1])}
    resultado = {}

    for prenda, _ in tiempos_ordenados.items():
        numero_de_lavado = 1
        entro = False
        while not entro:
            puede = True
            for prenda_del_lavado in resultado.setdefault(numero_de_lavado, []):
                if prenda_del_lavado in incompatibilidades[prenda]:
                    puede = False
                    break
            if puede:
                resultado[numero_de_lavado].append(prenda)
                entro = True
            else:
                numero_de_lavado += 1

    return resultado

# limpar_producoes_inuteis.py


def limpar_producoes_inuteis(gramatica: list) -> list:
    variaveis = gramatica[0].split()
    terminais = gramatica[1].split()
    inicial = gramatica[2].strip()
    producoes_raw = gramatica[3:]

    producoes = []
    for linha in producoes_raw:
        parte = linha.split()
        lado_esq = parte[0]
        lado_dir = parte[1]
        producoes.append((lado_esq, lado_dir))

    # Encontrar variáveis GERADORAS
    geradoras = set()

    mudou = True
    while mudou:
        mudou = False
        for A, rhs in producoes:
            # Se todos os símbolos no RHS forem terminais ou já forem geradores
            if all((x in terminais) or (x in geradoras) for x in rhs):
                if A not in geradoras:
                    geradoras.add(A)
                    mudou = True

    # Filtrar produções que usam apenas geradoras
    producoes_somente_geradoras = [
        (A, rhs)
        for (A, rhs) in producoes
        if A in geradoras and all((x in terminais) or (x in geradoras) for x in rhs)
    ]

    # Encontrar variáveis ALCANÇÁVEIS
    alcancaveis = set([inicial])

    mudou = True
    while mudou:
        mudou = False
        for A, rhs in producoes_somente_geradoras:
            if A in alcancaveis:
                for simbolo in rhs:
                    if simbolo in variaveis and simbolo not in alcancaveis:
                        alcancaveis.add(simbolo)
                        mudou = True

    # Filtrar produções úteis (geradoras + alcançáveis)
    producoes_finais = [
        (A, rhs) for (A, rhs) in producoes_somente_geradoras if A in alcancaveis
    ]

    # Montar nova gramática limpa
    novas_variaveis = sorted(list(alcancaveis))
    nova_gramatica = []

    nova_gramatica.append(" ".join(novas_variaveis))
    nova_gramatica.append(" ".join(terminais))
    nova_gramatica.append(inicial)

    for A, rhs in producoes_finais:
        nova_gramatica.append(f"{A} {rhs}")

    return nova_gramatica


if __name__ == "__main__":
    from time import time
    from utils import ler_arquivo, exibir_gramatica
    from limpar_producoes_nulas import limpar_producoes_nulas
    from limpar_producoes_unidade import limpar_producoes_unidade
    import os

    start = time()
    os.system("cls" if os.name == "nt" else "clear")

    diretorio = "gramaticas/"
    arquivo = "gramatica_portal.txt"
    gramatica = ler_arquivo(os.path.join(diretorio, arquivo))
    exibir_gramatica(gramatica, True)
    gramatica = limpar_producoes_nulas(gramatica)
    gramatica = limpar_producoes_unidade(gramatica)
    gramatica = limpar_producoes_inuteis(gramatica)
    exibir_gramatica(gramatica, True)

    print(f"\nTempo: {time() - start:.8f} segundos")

# limpar_producoes_nulas.py


def limpar_producoes_nulas(gramatica: list):
    gramatica_limpa = []
    indice_primeira_producao = 3
    n_producoes = len(gramatica) - indice_primeira_producao
    # buscar producoes nulas (A -> ε)
    variaveis_nulas = []
    for producao in gramatica[3:]:
        parte_esq, parte_dir = producao.split()
        if parte_dir == "eps":
            variaveis_nulas.append(parte_esq)

    # buscar producoes que levam em producoes nulas (A -> * -> ε)
    while True:
        re_verificar = False
        for i in range(n_producoes):
            indice = indice_primeira_producao + i
            parte_esq, parte_dir = gramatica[indice].split()
            diferenca = set(parte_dir) - set(variaveis_nulas)

            if diferenca:
                continue

            if parte_esq in variaveis_nulas:
                continue

            variaveis_nulas.append(parte_esq)
            re_verificar = True

        if not re_verificar:
            break

    # reescrever gramatica
    gramatica_limpa.append(gramatica[0])  # variaveis
    gramatica_limpa.append(gramatica[1])  # terminais
    gramatica_limpa.append(gramatica[2])  # variavel de partida
    # producoes
    for i in range(n_producoes):
        indice = indice_primeira_producao + i
        parte_esq, parte_dir = gramatica[indice].split()

        visitados = set([parte_dir])
        fila = [parte_dir]

        while fila:
            atual = fila.pop(0)
            if parte_dir != "eps" and atual != "":
                producao = f"{parte_esq} {atual}"
                gramatica_limpa.append(producao)

            for j, c in enumerate(atual):
                if c in variaveis_nulas:
                    nova = atual[:j] + atual[j + 1 :]
                    if nova not in visitados:
                        visitados.add(nova)
                        fila.append(nova)

    return gramatica_limpa


if __name__ == "__main__":
    from time import time
    from utils import ler_arquivo, exibir_gramatica
    import os

    start = time()
    os.system("cls" if os.name == "nt" else "clear")

    diretorio = "gramaticas"
    arquivo = "gramatica_portal.txt"
    gramatica = ler_arquivo(os.path.join(diretorio, arquivo))
    exibir_gramatica(gramatica, True)
    gramatica_limpa = limpar_producoes_nulas(gramatica)
    exibir_gramatica(gramatica_limpa, True)
    print(f"\nTempo: {time() - start:.8f} segundos")

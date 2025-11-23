# limpar_producoes_nulas.py


def limpar_producoes_nulas(gramatica: list):
    gramatica_limpa = []

    # buscar producoes nulas (A -> ε)
    variaveis_nulas = []
    for producao in gramatica[3:]:
        prod_partes = producao.split()
        if prod_partes[1] == "eps":
            variaveis_nulas.append(prod_partes[0])

    # busca producoes que levam em producoes nulas (A -> * -> ε)
    while True:
        re_verificar = False
        for i in range(3, len(gramatica)):
            prod_partes = gramatica[i].split()
            diferenca = set(prod_partes[1]) - set(variaveis_nulas)

            if diferenca:
                continue

            if prod_partes[0] in variaveis_nulas:
                continue

            variaveis_nulas.append(prod_partes[0])
            re_verificar = True

        if not re_verificar:
            break

    # reescrever gramatica
    gramatica_limpa.append(gramatica[0])  # variaveis
    gramatica_limpa.append(gramatica[1])  # terminais
    gramatica_limpa.append(gramatica[2])  # variavel de partida

    for i in range(3, len(gramatica)):
        prod_partes = gramatica[i].split()

        visitados = set([prod_partes[1]])
        fila = [prod_partes[1]]

        while fila:
            atual = fila.pop(0)
            if prod_partes[1] != "eps" and atual != "":
                producao = f"{prod_partes[0]} {atual}"
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
    from utils import ler_arquivo
    import os

    start = time()
    os.system("cls" if os.name == "nt" else "clear")

    diretorio = "gramaticas"
    arquivo = "gramatica_complexa.txt"
    gramatica = ler_arquivo(os.path.join(diretorio, arquivo))
    gramatica_limpa = limpar_producoes_nulas(gramatica)

    print(gramatica_limpa)
    print(f"\nTempo: {time() - start:.8f} segundos")

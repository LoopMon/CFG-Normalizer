# limpar_producoes_unidade.py


def limpar_producoes_unidade(gramatica: list):
    gramatica_limpa = []
    pares_unidade = []

    # pares unidade diretos (S, A)
    for producao in gramatica[3:]:
        prod_partes = producao.split()
        if prod_partes[1] in gramatica[0] and prod_partes[0] != prod_partes[1]:
            pares_unidade.append(producao)

    if len(pares_unidade) == 0:
        gramatica_limpa = gramatica[:]
        return gramatica_limpa

    # pares por transitividade (S, A), (A, B) -> (S, B)
    i = 0
    while i < len(pares_unidade):
        par_partes = pares_unidade[i].split()
        j = 0
        resetou = False
        while j < len(pares_unidade):
            prod_partes = pares_unidade[j].split()
            if par_partes[1] == prod_partes[0] and par_partes[0] != prod_partes[1]:
                aux = f"{par_partes[0]} {prod_partes[1]}"
                if aux not in pares_unidade:
                    pares_unidade.append(aux)
                    j = 0
                    resetou = True
            if resetou:
                resetou = False
            else:
                j += 1
        i += 1

    # Criar gramatica limpa sem os pares unidade
    gramatica_limpa.append(gramatica[0])  # variaveis
    gramatica_limpa.append(gramatica[1])  # terminais
    gramatica_limpa.append(gramatica[2])  # variavel de partida

    for i in range(0, len(pares_unidade)):
        par_partes = pares_unidade[i].split()
        for j in range(3, len(gramatica)):
            prod_partes = gramatica[j].split()

            if gramatica[j] in pares_unidade or prod_partes[0] == prod_partes[1]:
                continue

            if gramatica[j] not in gramatica_limpa:
                gramatica_limpa.append(gramatica[j])

            if par_partes[1] == prod_partes[0]:
                aux = f"{par_partes[0]} {prod_partes[1]}"
                if aux in gramatica_limpa:
                    continue
                gramatica_limpa.append(aux)

    return gramatica_limpa


if __name__ == "__main__":
    from time import time
    from limpar_producoes_nulas import limpar_producoes_nulas
    from utils import ler_arquivo, exibir_gramatica
    import os

    start = time()
    os.system("cls" if os.name == "nt" else "clear")

    diretorio = "gramaticas"
    arquivo = "gramatica_complexa.txt"
    gramatica = ler_arquivo(os.path.join(diretorio, arquivo))
    gramatica = limpar_producoes_nulas(gramatica)
    gramatica_limpa = limpar_producoes_unidade(gramatica)
    gramatica_limpa[3:] = sorted(gramatica_limpa[3:])

    exibir_gramatica(gramatica_limpa)
    print(f"\nTempo: {time() - start:.8f} segundos")

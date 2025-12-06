# limpar_producoes_unidade.py


def limpar_producoes_unidade(gramatica: list):
    gramatica_limpa = []
    pares_unidade = []
    indice_primeira_producao = 3

    # pares unidade diretos (S, A)
    for producao in gramatica[indice_primeira_producao:]:
        parte_esq, parte_dir = producao.split()
        if parte_dir in gramatica[0] and parte_esq != parte_dir:
            pares_unidade.append(producao)

    # se nao existe pares unidades, mantem a G original
    n_pares_unidade = len(pares_unidade)
    if n_pares_unidade == 0:
        return gramatica

    # pares por transitividade (S, A), (A, B) -> (S, B)
    i = 0
    while i < n_pares_unidade:
        par_unidade_esq_i, par_unidade_dir_i = pares_unidade[i].split()
        # par_partes = pares_unidade[i].split()
        j = 0
        while j < n_pares_unidade:
            par_unidade_esq_j, par_unidade_dir_j = pares_unidade[j].split()
            # prod_partes = pares_unidade[j].split()
            if (
                par_unidade_dir_i == par_unidade_esq_j
                and par_unidade_esq_i != par_unidade_dir_j
            ):
                nova_par_unidade = f"{par_unidade_esq_i} {par_unidade_dir_j}"
                if nova_par_unidade not in pares_unidade:
                    pares_unidade.append(nova_par_unidade)
                    # recomecar a verificacao dos pares unidade
                    j = -1
            j += 1
        i += 1

    # Criar gramatica limpa sem os pares unidade
    gramatica_limpa.append(gramatica[0])  # variaveis
    gramatica_limpa.append(gramatica[1])  # terminais
    gramatica_limpa.append(gramatica[2])  # variavel de partida

    for par_unidade in pares_unidade:
        var_esq, var_dir = par_unidade.split()
        for j in range(3, len(gramatica)):
            parte_esq, parte_dir = gramatica[j].split()

            if (
                gramatica[j] not in gramatica_limpa
                and gramatica[j] not in pares_unidade
            ):
                gramatica_limpa.append(gramatica[j])

            if var_dir == parte_esq:
                nova_producao = f"{var_esq} {parte_dir}"
                if (
                    nova_producao in gramatica_limpa
                    or var_esq == parte_dir
                    or nova_producao in pares_unidade
                ):
                    continue
                gramatica_limpa.append(nova_producao)

    return gramatica_limpa


if __name__ == "__main__":
    from time import time
    from utils import ler_arquivo, exibir_gramatica
    from limpar_producoes_nulas import limpar_producoes_nulas
    import os

    start = time()
    os.system("cls" if os.name == "nt" else "clear")

    diretorio = "gramaticas"
    arquivo = "gramatica_portal.txt"

    gramatica = ler_arquivo(os.path.join(diretorio, arquivo))
    exibir_gramatica(gramatica, True)
    gramatica = limpar_producoes_nulas(gramatica)
    exibir_gramatica(gramatica, True)
    gramatica = limpar_producoes_unidade(gramatica)
    exibir_gramatica(gramatica, True)

    print(f"\nTempo: {time() - start:.8f} segundos")

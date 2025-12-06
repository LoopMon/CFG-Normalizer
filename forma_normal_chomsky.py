# forma_chomsky.py
import re


def forma_normal_chomsky(gramatica: list[str]) -> list[str]:
    gramatica_normalizada = gramatica[:]
    indice_primeira_producao = 3

    # Procurar e Trocar terminais por novas variaveis Tn
    producoes_para_terminais = []
    cont_terminal = 1
    for i, producao in enumerate(gramatica_normalizada[indice_primeira_producao:]):
        parte_esq, parte_dir = producao.split()
        sentenca = list(parte_dir)

        if len(sentenca) == 1:
            continue

        # Cada item da producao[i]
        achou_terminal = False
        setenca_atualizada = ""
        for j, item in enumerate(sentenca):
            variavel_tn = ""

            # verifica se ja existe uma producao Tn para o terminal
            for prod_terminal in producoes_para_terminais:
                if item in prod_terminal:
                    variavel_tn = prod_terminal.split()[0]
                    break

            # cria producao para o terminal caso nao exista
            if item in gramatica_normalizada[1] and not variavel_tn:
                achou_terminal = True
                nova_variavel = f"T{cont_terminal}"
                nova_producao = f"{nova_variavel} {item}"
                sentenca[j] = nova_variavel  # trocar o terminal por Tn
                setenca_atualizada = "".join(sentenca)

                # adicionando Tn a gramatica
                gramatica_normalizada[0] += f" {nova_variavel}"
                gramatica_normalizada.append(nova_producao)
                producoes_para_terminais.append(nova_producao)
                # indice = i + indice_primeira_producao
                # gramatica_normalizada[indice] = f"{parte_esq} {setenca_atualizada}"

                cont_terminal += 1
                continue

            # atualizar producao caso ja exista producao para terminal
            if variavel_tn:
                achou_terminal = True
                sentenca[j] = variavel_tn
                setenca_atualizada = "".join(sentenca)
                # indice = i + indice_primeira_producao
                # gramatica_normalizada[indice] = f"{parte_esq} {setenca_atualizada}"

        if not achou_terminal:
            continue

        indice = i + indice_primeira_producao
        gramatica_normalizada[indice] = f"{parte_esq} {setenca_atualizada}"

    # Procurar producoes com mais de 2 variaveis e criar novas producoes Vn
    producoes_para_duas_variaveis = []
    cont_variavel = 1
    verificar = True
    while verificar:
        for i, producao in enumerate(gramatica_normalizada[indice_primeira_producao:]):
            parte_esq, parte_dir = producao.split()
            sentenca = list(parte_dir)

            sentenca_sem_digitos = re.sub(r"[^A-Z]", "", parte_dir)
            if len(sentenca_sem_digitos) <= 2:
                verificar = False
                continue

            cont = 0  # vai fatiando da esq -> dir
            tamanho_sentenca = 0
            achou_proxima_variavel = False
            variavel_vn = ""
            aux = ""
            while not achou_proxima_variavel:
                aux = parte_dir[:cont]

                # final da sentenca
                if cont == len(parte_dir):
                    break

                # encontrou 2 variaveis nao TV
                if tamanho_sentenca == 2:
                    break

                if parte_dir[cont].isalpha():
                    if parte_dir[cont] not in "TV":
                        tamanho_sentenca += 1
                        cont += 1

                    elif parte_dir[cont] in "TV":
                        # variavel nao TV com variavel TV: AT1
                        if tamanho_sentenca == 1:
                            while parte_dir[cont + 1].isdigit():
                                cont += 1
                            aux = parte_dir[: cont + 1]
                            achou_proxima_variavel = True

                        # comeca em TV
                        else:
                            termina_em_TV = False
                            while True:
                                if parte_dir[cont + 1].isdigit():
                                    cont += 1

                                elif parte_dir[cont + 1] in "TV":
                                    termina_em_TV = True
                                    cont += 1

                                elif parte_dir[cont + 1].isalpha():
                                    if termina_em_TV:
                                        cont -= 1
                                    else:
                                        cont += 1
                                    achou_proxima_variavel = True
                                    break

            for producao_vn in producoes_para_duas_variaveis:
                if aux in producao_vn:
                    variavel_vn = producao_vn.split()[0]

            if variavel_vn:
                indice = i + indice_primeira_producao
                producao_atual_atualizada = gramatica_normalizada[indice].replace(
                    aux, variavel_vn, 1
                )
                gramatica_normalizada[indice] = producao_atual_atualizada
                verificar = True
                continue

            nova_variavel = f"V{cont_variavel}"
            nova_producao = f"{nova_variavel} {aux}"

            indice = i + indice_primeira_producao
            producao_atual_atualizada = gramatica_normalizada[indice].replace(
                aux, nova_variavel, 1
            )

            gramatica_normalizada[0] += f" {nova_variavel}"
            gramatica_normalizada[indice] = producao_atual_atualizada
            gramatica_normalizada.append(nova_producao)

            producoes_para_duas_variaveis.append(nova_producao)
            cont_variavel += 1
            verificar = True

    return gramatica_normalizada


if __name__ == "__main__":
    from time import time
    import os
    from utils import ler_arquivo, escrever_arquivo, exibir_gramatica, ordenar_producoes
    from limpar_producoes_nulas import limpar_producoes_nulas
    from limpar_producoes_unidade import limpar_producoes_unidade
    from limpar_producoes_inuteis import limpar_producoes_inuteis

    start = time()
    os.system("cls" if os.name == "nt" else "clear")

    diretorio = "gramaticas/"
    arquivo = "gramatica_portal.txt"

    gramatica = ler_arquivo(os.path.join(diretorio, arquivo))
    gramatica = limpar_producoes_nulas(gramatica)
    gramatica = limpar_producoes_unidade(gramatica)
    gramatica = limpar_producoes_inuteis(gramatica)
    exibir_gramatica(gramatica, True)

    gramatica = forma_normal_chomsky(gramatica)
    exibir_gramatica(gramatica, True)

    gramatica = ordenar_producoes(gramatica)
    escrever_arquivo("saida/gramatica_normalizada.txt", gramatica)

    print(f"\nTempo: {time() - start:.8f} segundos")

# forma_chomsky.py
import re


def forma_normal_chomsky(gramatica: list[str]) -> list[str]:
    gramatica_normalizada = gramatica[:]

    # Procurar e Trocar terminais por novas variaveis
    producoes_para_terminais = []
    cont_terminal: int = 1
    for i, producao in enumerate(gramatica_normalizada[3:]):
        parte_esq, parte_dir = producao.split()
        sentenca = list(parte_dir)

        if len(sentenca) == 1:
            continue

        # Cada item da producao[i]
        achou_terminal = False
        producao_atual_atualizada = ""
        for j, item in enumerate(sentenca):
            existe_producao_terminal = False
            variavel_terminal_existente = ""

            # verificar se ja existe uma producao para o terminal
            for prod_terminal in producoes_para_terminais:
                if item in prod_terminal:
                    existe_producao_terminal = True
                    variavel_terminal_existente = prod_terminal.split()[0]
                    break

            # criar producao para o terminal caso nao exista
            if item in gramatica_normalizada[1] and not existe_producao_terminal:
                achou_terminal = True
                nova_variavel = f"T{cont_terminal}"
                nova_producao = f"{nova_variavel} {item}"
                sentenca[j] = nova_variavel
                producao_atual_atualizada = "".join(sentenca)

                gramatica_normalizada[0] += f" {nova_variavel}"
                producoes_para_terminais.append(nova_producao)
                gramatica_normalizada[i + 3] = (
                    f"{parte_esq} {producao_atual_atualizada}"
                )
                gramatica_normalizada.append(nova_producao)

                cont_terminal += 1
                continue

            # atualizar producao caso ja exista producao para terminal
            if existe_producao_terminal:
                sentenca[j] = variavel_terminal_existente
                producao_atual_atualizada = "".join(sentenca)
                gramatica_normalizada[i + 3] = (
                    f"{parte_esq} {producao_atual_atualizada}"
                )

        if not achou_terminal:
            continue

        gramatica_normalizada[i + 3] = f"{parte_esq} {producao_atual_atualizada}"

    # Procurar producoes com mais de 2 variaveis e criar novas producoes
    producoes_para_duas_variaveis = []
    cont_variavel: int = 1
    verificar = True
    while verificar:
        for i, producao in enumerate(gramatica_normalizada[3:]):
            parte_esq, parte_dir = producao.split()
            sentenca_sem_digitos = re.sub(r"[^A-Z]", "", parte_dir)
            sentenca = list(parte_dir)

            if len(sentenca_sem_digitos) <= 2:
                verificar = False
                continue

            cont = 0
            sequencia_T = 0
            achou_proxima_variavel = False
            achou_variaveis_TV = False
            aux = ""
            while not achou_proxima_variavel:
                aux = parte_dir[: cont + 1]

                if cont == len(parte_dir):
                    break
                if parte_dir[cont].isalpha() and cont == 0:
                    if parte_dir[cont] == "T":
                        sequencia_T += 1
                    cont += 1
                elif (
                    parte_dir[cont].isalpha()
                    and parte_dir[cont] not in "TV"
                    and cont != 0
                ):
                    if achou_variaveis_TV:
                        cont -= 1
                        aux = parte_dir[: cont + 1]
                    achou_proxima_variavel = True
                elif parte_dir[cont].isdigit():
                    cont += 1
                elif parte_dir[cont] in "TV":
                    if sequencia_T < 2:
                        achou_variaveis_TV = True
                        sequencia_T += 1
                        cont += 1
                    else:
                        cont -= 1
                        aux = parte_dir[: cont + 1]
                        achou_proxima_variavel = True

            nova_variavel = f"V{cont_variavel}"
            nova_producao = f"{nova_variavel} {aux}"
            producoes_para_duas_variaveis.append(nova_producao)

            producao_atual_atualizada = gramatica_normalizada[i + 3].replace(
                aux, nova_variavel
            )
            gramatica_normalizada[0] += f" {nova_variavel}"
            gramatica_normalizada[i + 3] = producao_atual_atualizada
            gramatica_normalizada.append(nova_producao)
            cont_variavel += 1
            verificar = True

    return gramatica_normalizada


if __name__ == "__main__":
    from utils import ler_arquivo, escrever_arquivo

    gramatica = ler_arquivo("gramaticas/limpa/gramatica_2.txt")

    fnc_gramatica = forma_normal_chomsky(gramatica)
    escrever_arquivo("saida/gramatica_normalizada.txt", fnc_gramatica)

    # print(fnc_gramatica)
    for i in fnc_gramatica:
        print(i)

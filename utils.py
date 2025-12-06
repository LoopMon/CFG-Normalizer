def ler_arquivo(caminho_arquivo: str) -> list:
    """
    Lê todas as linhas de um arquivo .txt e retorna seu conteúdo como uma lista de strings.

    Parametros:
        caminho_arquivo (str): Caminho absoluto ou relativo para o arquivo a ser lido.

    Retorna:
        list: Lista contendo cada linha do arquivo sem o caractere de quebra de linha.
    """

    lista = []
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            aux = linha.replace("\n", "")
            lista.append(aux)
    return lista


def escrever_arquivo(caminho_arquivo: str, conteudo: list) -> None:
    """
    Escreve uma lista de strings em um arquivo .txt, adicionando quebras de linha automaticamente.

    Parametros:
        caminho_arquivo (str): Caminho absoluto ou relativo do arquivo de destino.
        conteudo (list): Lista de linhas a serem gravadas no arquivo.
    """

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in conteudo:
            aux = f"{linha}\n"
            arquivo.write(aux)


def exibir_gramatica(gramatica: list, agrupar=False) -> None:
    """
    Exibe uma gramatica no terminal em formato legivel, com ou sem agrupamento das producoes.

    Parametros:
        gramatica (list): Estrutura contendo variaveis, terminais, simbolo inicial e producoes.
        agrupar (bool, opcional): Se True, agrupa producoes por variavel. Padrao: False.
    """

    print()
    print("=-=-=-=-= GRAMATICA =-=-=-=-=")
    print("Variaveis:", gramatica[0])
    print("Terminais:", gramatica[1])
    print("Var. de partida:", gramatica[2])
    print("Producoes:")
    if not agrupar:
        for producao in gramatica[3:]:
            parte_esq, parte_dir = producao.split()
            print(f"{'-' * 4} {parte_esq} -> {parte_dir}")
        print()
        return

    variaveis = gramatica[0].split()
    for variavel in variaveis:
        producao_agrupada = f"{'-' * 4} {variavel} ->"
        for producao in gramatica[3:]:
            parte_esq, parte_dir = producao.split()

            if variavel == parte_esq:
                producao_agrupada += f" {parte_dir} |"
        producao_agrupada = producao_agrupada[:-1]
        print(producao_agrupada)
    print()


def ordenar_producoes(gramatica: list) -> list:
    """
    Retorna uma copia da gramatica com as producoes ordenadas lexicograficamente.

    Parametros:
        gramatica (list): Lista representando a gramatica completa.

    Retorna:
        list: Nova gramatica com suas producoes ordenadas.
    """

    gramatica_copia = gramatica[:]
    producoes = gramatica_copia[3:]
    producoes.sort()
    gramatica_copia[3:] = producoes[:]

    return gramatica_copia


if __name__ == "__main__":
    caminho = "gramaticas/gramatica_trabalho.txt"
    gramatica = ler_arquivo(caminho)
    exibir_gramatica(gramatica)

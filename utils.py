def ler_arquivo(caminho_arquivo: str) -> list:
    """Lê o conteúdo de um arquivo e retorna como um array.

    Args:
    caminho_arquivo (str): O caminho para o arquivo a ser lido.

    Returns:
    list: O conteúdo do arquivo como uma lista de linhas.
    """
    lista = []
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            aux = linha.replace("\n", "")
            lista.append(aux)
    return lista


def escrever_arquivo(caminho_arquivo: str, conteudo: list) -> None:
    """Escreve o conteúdo em um arquivo.

    Args:
    caminho_arquivo (str): O caminho para o arquivo a ser escrito.
    conteudo (list): O conteúdo a ser escrito no arquivo, como uma lista de linhas.
    """
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for linha in conteudo:
            aux = f"{linha}\n"
            arquivo.write(aux)


def exibir_gramatica(gramatica: list, agrupar=False) -> None:
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


if __name__ == "__main__":
    caminho = "gramaticas/gramatica_trabalho.txt"
    gramatica = ler_arquivo(caminho)
    exibir_gramatica(gramatica)

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
        arquivo.writelines(conteudo)


def exibir_gramatica(gramatica: list) -> None:
    print("=-=-=-=-= GRAMATICA =-=-=-=-=")
    print("Variaveis:", gramatica[0].replace("\n", ""))
    print("Terminais:", gramatica[1].replace("\n", ""))
    print("Var. de partida:", gramatica[2].replace("\n", ""))
    print("Producoes:")
    for linha in gramatica[3:]:
        print(f"\t{linha.replace('\n', '')}")


if __name__ == "__main__":
    caminho = "gramatica.txt"
    linhas = ler_arquivo(caminho)
    for linha in linhas:
        print(linha.strip())

def ler_arquivo(caminho_arquivo: str) -> list:
    """Lê o conteúdo de um arquivo e retorna como um array.

    Args:
    caminho_arquivo (str): O caminho para o arquivo a ser lido.

    Returns:
    list: O conteúdo do arquivo como uma lista de linhas.
    """
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.readlines()
    return conteudo


def escrever_arquivo(caminho_arquivo: str, conteudo: list) -> None:
    """Escreve o conteúdo em um arquivo.

    Args:
    caminho_arquivo (str): O caminho para o arquivo a ser escrito.
    conteudo (list): O conteúdo a ser escrito no arquivo, como uma lista de linhas.
    """
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(conteudo)


if __name__ == "__main__":
    caminho = "gramatica.txt"
    linhas = ler_arquivo(caminho)
    for linha in linhas:
        print(linha.strip())

# limpar_producoes_nulas.py


def limpar_producoes_nulas(gramatica: list):
    pass


if __name__ == "__main__":
    from utils import ler_arquivo

    gramatica = ler_arquivo("gramaticas/gramatica_simples.txt")
    gramatica_limpa = limpar_producoes_nulas(gramatica)
    print(gramatica_limpa)

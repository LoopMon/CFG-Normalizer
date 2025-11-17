# main.py
from utils import ler_arquivo

if __name__ == "__main__":
    lista = ler_arquivo("gramaticas/gramatica_simples.txt")
    caracteres = lista[0].split()
    print(lista)
    print(caracteres)

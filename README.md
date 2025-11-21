# 📘 **Limpador e Normalizador de Gramáticas Livres de Contexto**

## 📝 **Descrição do Projeto**

Este projeto recebe uma **Gramática Livre de Contexto (GLC) “bruta”** e realiza automaticamente todo o processo de **limpeza, simplificação e normalização**.
O sistema aplica de forma sequencial as principais transformações utilizadas em Teoria da Computação para preparar uma gramática para análise formal:

1. **Remoção de produções nulas (ε-produções)**
2. **Remoção de produções-unidade**
3. **Remoção de símbolos e produções inúteis**
4. **Conversão da gramática para a Forma Normal de Chomsky (CNF)**

O objetivo é transformar qualquer GLC arbitrária em uma versão equivalente, porém totalmente limpa, padronizada.

## 🚀 **Funcionalidades**

* 📥 Recebe uma gramática escrita de forma simples (texto bruto).
* 🧹 Realiza automaticamente todas as etapas de limpeza:
  * remoção de ε-produções
  * remoção de produções-unidade
  * eliminação de símbolos inúteis (inalcançáveis ou improdutivos)
* 🧩 Normaliza a gramática para **Forma Normal de Chomsky**.
* 📤 Retorna a gramática final já padronizada e pronta para uso.
* 🛠️ Oferece funções independentes para cada etapa (útil para estudos ou debugging).

## 📚 **Tecnologias Utilizadas**

* Linguagem usada: **Python** (ou coloque a sua linguagem real)
* Estrutura modular para facilitar testes e reutilização
* Algoritmos baseados em teoria clássica de linguagens formais

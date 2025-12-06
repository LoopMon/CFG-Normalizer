# Resolução da Gramática do Portal

Este arquivo pretende ajudar e usar de comparação com os resultados do algoritmo.

A gramática segue o padrão abaixo:
* Primeira linha: Variáveis da gramática
* Segunda linha: Terminais 
* Terceira linha: Variável de partida
* Quarta em diante: Produções $A \to \alpha$

## Gramática:

$
X\ Y\ Z\ K\ W\ T \newline
a\ b\ c \newline
X \newline
X \to KW \ |\ aK \newline
Y \to eps \ |\ XWb \newline
Z \to XK \ |\ Y \ |\ cK \newline
K \to b \ |\ XWa \newline
W \to Y \ |\ XbY \newline
T \to cZY \ |\ YbZ \newline
$
Obs: eps = $\lambda$

## Limpar produções Nulas ( $A \to \epsilon$ / $\lambda$ / eps )

$V_n = \{ Y, Z, W\}$

$
X\ Y\ Z\ K\ W\ T \newline
a\ b\ c \newline
X \newline
X \to KW \ |\ K \ |\ aK \newline
Y \to XWb \ |\ Xb \newline
Z \to XK \ |\ Y \ |\ cK \newline
K \to b \ |\ XWa \ |\ Xa \newline
W \to Y \ |\ XbY \ |\ Xb \newline
T \to cZY \ |\ YbZ \ |\ cZ \ |\ cY \ |\ c \ |\ Yb \ |\ bZ \ |\ b \newline
$

## Limpar produções unidade ($A \to B$)

Pares Unidade: $(X, K) \quad (Z, Y) \quad (W, Y)$

$
X\ Y\ Z\ K\ W\ T \newline
a\ b\ c \newline
X \newline
X \to KW \ |\ aK \ |\ b \ |\ XWa \ |\ Xa \newline
Y \to XWb \ |\ Xb \newline
Z \to XK \ |\ cK \ |\ XWb \ |\ Xb \newline
K \to b \ |\ XWa \ |\ Xa \newline
W \to XbY \ |\ XWb \ |\ Xb \newline
T \to cZY \ |\ YbZ \ |\ cZ \ |\ cY \ |\ c \ |\ Yb \ |\ bZ \ |\ b \newline
$

## Limpar produções inúteis ($S \to A \quad B \to A_{\text{inútil}}$)

$V_{geradoras} = \{X, K, T, Y, Z, W\}$

$V_{alcancaveis} = \{X, K, W, Y\}$

$V_{inalcancavel} = \{T, Z\}$

$
X\ Y\ K\ W \newline
a\ b\ c \newline
X \newline
X \to KW \ |\ aK \ |\ b \ |\ XWa \ |\ Xa \newline
Y \to XWb \ |\ Xb \newline
K \to b \ |\ XWa \ |\ Xa \newline
W \to XbY \ |\ XWb \ |\ Xb \newline
$

## Forma Normal de Chomsky ($A \to BC \ \text{ou} \ B \to a$)

$
X\ Y\ K\ W \newline
a\ b\ c \newline
X \newline
X \to KW \ |\ T_1K \ |\ b \ |\ V_1T_1 \ |\ XT_1 \newline
Y \to V_1T_2 \ |\ XT_2 \newline
K \to b \ |\ V_1T_1 \ |\ XT_1 \newline
W \to V_2Y \ |\ V_1T_2 \ |\ XT_2 \newline
T_1 \to a \newline
T_2 \to b \newline
V_1 \to XW \newline
V_2 \to XT_2 \newline
$
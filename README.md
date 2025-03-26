Algoritmo Guloso para Busca de Caminho entre Cidades

Este projeto implementa um algoritmo guloso para encontrar o caminho mais curto entre duas cidades com base em um mapa representado em um arquivo JSON.

📌 Funcionalidades

Carrega dados de um mapa a partir de um arquivo JSON

Evita loops armazenando cidades visitadas

Escolhe sempre o vizinho mais próximo (estratégia gulosa)

Gera um log detalhado das decisões do algoritmo

📁 Estrutura do Projeto

📂 projeto-algoritmo-guloso
 ├── cidades.json  # Arquivo contendo o mapa das cidades e distâncias
 ├── algoritmo.py  # Implementação do algoritmo guloso
 ├── README.md     # Documentação do projeto

📜 Formato do Arquivo cidades.json

O arquivo JSON deve conter um dicionário onde as chaves são os nomes das cidades e os valores são dicionários com os vizinhos e a distância até eles. Exemplo:

{
    "A": {"B": 10, "C": 20},
    "B": {"A": 10, "C": 5, "D": 15},
    "C": {"A": 20, "B": 5, "D": 30},
    "D": {"B": 15, "C": 30}
}

🚀 Como Executar

Clone este repositório:

git clone https://github.com/Alchini/Algoritmo_Guloso.git
cd projeto-algoritmo-guloso

Certifique-se de ter o Python instalado.

Execute o programa:

python algoritmo.py

Insira as cidades de origem e destino quando solicitado.

🛠 Tecnologias Utilizadas

Python 3

JSON para representar o mapa das cidades

🔍 Exemplo de Uso

Cidade origem: A
Cidade destino: D

=== LOG DE DECISÕES ===
Iniciando busca de A para D
Visitando cidade: A
Vizinhos disponíveis: B (10 km), C (20 km)
Decisão gulosa: escolhendo B (menor distância: 10 km)
...
Distância total percorrida: 25 km

📌 Observações

O algoritmo usa uma estratégia gulosa, escolhendo sempre a cidade vizinha mais próxima.

Na maioria das vezes, não será encontrado o caminho ideal, pois o algoritmo não explora todas as possibilidades, explora apenas o caminho das cidades mais curtas.

Se não houver caminho possível, ele retornará uma mensagem de erro.
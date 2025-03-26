# 🏙️ Algoritmo Guloso para Busca de Caminho entre Cidades

Este projeto implementa um **algoritmo guloso** para encontrar o **caminho mais curto** entre duas cidades, utilizando um **mapa representado em JSON**.

---

## 📌 Funcionalidades

✅ **Carrega dados de um mapa a partir de um arquivo JSON**  
✅ **Evita loops armazenando cidades visitadas**  
✅ **Escolhe sempre o vizinho mais próximo** (estratégia gulosa)  
✅ **Gera um log detalhado das decisões do algoritmo**  

---

## 📂 Estrutura do Projeto

```
📂 projeto-algoritmo-guloso
 ├── 🗺️ cidades.json  # Arquivo contendo o mapa das cidades e distâncias
 ├── 🖥️ algoritmo.py  # Implementação do algoritmo guloso
 ├── 📜 README.md     # Documentação do projeto
```

---

## 📜 Formato do Arquivo `cidades.json`

O arquivo JSON deve conter um dicionário onde as **chaves** são os nomes das cidades e os **valores** são dicionários com os vizinhos e a distância até eles. **Exemplo:**

```json
{
    "A": {"B": 10, "C": 20},
    "B": {"A": 10, "C": 5, "D": 15},
    "C": {"A": 20, "B": 5, "D": 30},
    "D": {"B": 15, "C": 30}
}
```

---

## 🚀 Como Executar

1️⃣ Clone este repositório:
   ```sh
   git clone https://github.com/Alchini/Algoritmo_Guloso.git
   cd projeto-algoritmo-guloso
   ```
2️⃣ Certifique-se de ter o **Python 3** instalado.
3️⃣ Execute o programa:
   ```sh
   python algoritmo.py
   ```
4️⃣ Insira as **cidades de origem e destino** quando solicitado.

---

## 🛠 Tecnologias Utilizadas

- 🐍 **Python 3**
- 📂 **JSON** para representar o mapa das cidades

---

## 🔍 Exemplo de Uso

```
Cidade origem: A
Cidade destino: D

=== LOG DE DECISÕES ===
Iniciando busca de A para D
Visitando cidade: A
Vizinhos disponíveis: B (10 km), C (20 km)
Decisão gulosa: escolhendo B (menor distância: 10 km)
...
Distância total percorrida: 25 km
```

---

## ⚠️ Observações

⚡ O algoritmo usa uma estratégia **gulosa**, escolhendo sempre a cidade vizinha mais próxima.  
⚡ Ele pode **não encontrar o caminho ideal** em todos os casos, pois não explora todas as possibilidades.  
⚡ Se **não houver caminho possível**, ele retornará uma **mensagem de erro**.  

---

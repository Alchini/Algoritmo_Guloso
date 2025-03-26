import json

def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def algoritmo_guloso(dados, origem, destino):
    """
    - Evita loops pq armazena a cidade ja visitada
    - Escolhe o vizinho mais próximo
    - Retorna o caminho, distância total e logs de decisão
    """
    caminho = []
    cidades_visitadas = set()
    cidade_atual = origem
    distancia_total = 0
    logs = []
    
    logs.append(f"Iniciando busca de {origem} para {destino}")
    
    while cidade_atual != destino:
        if cidade_atual not in dados:
            logs.append(f"Erro: Cidade {cidade_atual} não encontrada no mapa!")
            return None, None, logs
        
        caminho.append(cidade_atual)
        cidades_visitadas.add(cidade_atual)
        logs.append(f"\nVisitando cidade: {cidade_atual}")
        
        vizinhos = dados[cidade_atual]
        
        vizinhos_disponiveis = {k: v for k, v in vizinhos.items() if k not in cidades_visitadas}
        logs.append(f"Vizinhos disponíveis: {', '.join(f'{k} ({v} km)' for k, v in vizinhos_disponiveis.items())}")
        
        if destino in vizinhos_disponiveis:
            distancia = vizinhos_disponiveis[destino]
            logs.append(f"Destino {destino} encontrado como vizinho da cidade atual | Distância: {distancia} km")
            caminho.append(destino)
            distancia_total += distancia
            logs.append(f"Distância total: {distancia_total} km")
            return caminho, distancia_total, logs
        
        if not vizinhos_disponiveis:
            logs.append("Nenhum vizinho disponível - caminho impossível!")
            return None, None, logs
        
        proxima_cidade = min(vizinhos_disponiveis.keys(), key=lambda x: vizinhos_disponiveis[x])
        distancia = vizinhos_disponiveis[proxima_cidade]
        
        logs.append(f"Decisão gulosa: escolhendo {proxima_cidade} (menor distância: {distancia} km)")
        logs.append(f"Distância parcial adicionada: {distancia} km")
        
        cidade_atual = proxima_cidade
        distancia_total += distancia
        
        logs.append(f"Próxima cidade: {cidade_atual} | Distância total acumulada: {distancia_total} km")
        
        if len(caminho) > len(dados):
            logs.append("Número máximo de cidades excedido - abortando busca!")
            return None, None, logs
    
    return caminho, distancia_total, logs

def main():
    dados = carregar_dados('cidades.json')
    origem = input("Cidade origem: ").strip()
    destino = input("Cidade destino: ").strip()
    
    if origem not in dados:
        print(f"Erro: Cidade de origem '{origem}' não encontrada no mapa!")
        return
    if destino not in dados:
        print(f"Erro: Cidade de destino '{destino}' não encontrada no mapa!")
        return
    
    caminho, distancia_total, logs = algoritmo_guloso(dados, origem, destino)
    
    print("\n=== LOG DE DECISÕES ===")
    for log in logs:
        print(log)
    
    if not caminho:
        print(f"\nNão foi possível encontrar um caminho entre {origem} e {destino}.")
        return
    
    print("\n=== CAMINHO ENCONTRADO ===")
    for i in range(len(caminho)-1):
        cidade_atual = caminho[i]
        proxima_cidade = caminho[i+1]
        distancia = dados[cidade_atual][proxima_cidade]
        print(f"{cidade_atual} -> {proxima_cidade}: {distancia} km")
    
    print(f"\nDistância total percorrida: {distancia_total} km")

if __name__ == "__main__":
    main()
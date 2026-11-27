#Imprima as cidades que têm exatamente 1 estrada (resposta: Giurgiu, Eforie e Neamt).

#Imprima as cidades com h(n) menor que 200 km. Dica: for cidade in heuristica_bucareste: e 
# um ifDescubra qual é a estrada mais longa do mapa (resposta: Fagaras–Bucharest, 211 km).

from mapa import mapa_romenia, heuristica_bucareste

for cidades in mapa_romenia:
    # Uso len() porque mapa_romenia[cidades] devolve uma lista de tuplas com os vizinhos,
    # então preciso contar quantas estradas (tuplas) existem dentro dessa lista.
    if len(mapa_romenia[cidades]) == 1:
        print(cidades)

print()

for cidades in heuristica_bucareste:
    # Executei com len() e deu TypeError: object of type 'int' has no len().
    # Aqui não uso len() porque estou comparando diretamente um valor do tipo inteiro (int).
    if heuristica_bucareste[cidades] < 200:
        print(cidades)

print()

maior_distancia = 0
origem = ""
destino = ""

# O primeiro for percorre todas as cidades (chaves) do mapa
for cidade in mapa_romenia:
    # O segundo for usa duas variáveis para desempacotar cada tupla (vizinho, distancia) da lista
    for vizinho, distancia in mapa_romenia[cidade]:
        if distancia > maior_distancia:
            maior_distancia = distancia
            origem = cidade
            destino = vizinho

print(f"{origem}–{destino}, {maior_distancia} km")


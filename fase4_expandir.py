# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: função que mostra a fronteira de forma resumida -----
def mostrar_fronteira(fronteira):
    """Imprime cada nó da fronteira como Cidade(f=...)."""
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    print('   fronteira:', ', '.join(partes))

# astar-romenia

Implementação passo a passo do algoritmo de **Busca A\*** (*A-Star*) em Python para encontrar o caminho de menor custo entre **Arad** e **Bucareste** (*Bucharest*).

Projeto desenvolvido em 6 fases na disciplina de **Engenharia de Software**.

---

## Pré-requisitos

- **Python 3.x** instalado na máquina
- **Git** (opcional, caso queira clonar o repositório).

## Como rodar o projeto

### 1. Clonar o repositório e entrar na pasta
```bash
git clone https://github.com/AnthonyCastroDev/astar-romenia.git
cd astar-romenia
```

### 2. Executar o programa completo (Fase 6)
```bash
python a_estrela.py
```

### 3. Executar as fases intermediárias (opcional)
Cada fase é independente e importa os dados de `mapa.py`. Você pode rodar qualquer uma delas para acompanhar a evolução do algoritmo:

```bash
python fase1_explorar.py   # Exploração do grafo e da heurística
python fase2_caminhos.py   # Cálculo de custos g(n), h(n) e f(n)
python fase3_fronteira.py  # Expansão manual de Arad e ordenação da fronteira
python fase4_expandir.py   # Três rodadas de expansão usando conjunto de explorados
python fase5_busca.py      # Laço while completo da busca A*
```

---

## Resultado Esperado

Ao executar `python a_estrela.py`, o algoritmo encontra a rota ótima entre Arad e Bucareste:

```text
Caminho: Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
Custo  : 418 km
Passos : 4 estradas
```

## Estrutura das Fases

| Fase | Arquivo | Descrição | Conceitos abordados |
| :--- | :--- | :--- | :--- |
| **Dados** | `mapa.py` | Grafo rodoviário da Romênia e tabela heurística | `dict`, `list`, `tuple` |
| **Fase 1** | `fase1_explorar.py` | Leitura e navegação nos dicionários do mapa | `import`, `len`, `for`, desempacotamento |
| **Fase 2** | `fase2_caminhos.py` | Cálculo de custo de estradas e caminhos completos | `def`, `return`, `range`|
| **Fase 3** | `fase3_fronteira.py` | Criação do nó `(f, g, cidade, caminho)` e ordenação | `append`, `pop(0)`, `sort`, `lambda` |
| **Fase 4** | `fase4_expandir.py` | Função `expandir()` e controle de cidades visitadas | `in`, `continue` |
| **Fase 5** | `fase5_busca.py` | Algoritmo A\* completo com laço de repetição | `while`, teste de objetivo ao remover nó |
| **Fase 6** | `a_estrela.py` | Programa final com rastro detalhado e validação | `main()`, `if __name__ == '__main__'`, `dict.get` |

---

## Como funciona o A\* neste problema

Para achar o caminho mais curto sem testar todas as estradas do mapa, o algoritmo calcula uma pontuação para cada cidade usando esta fórmula:

$$f(n) = g(n) + h(n)$$

- **$g(n)$ (Custo):** Quantos km você **já andou** de verdade desde a saída (`Arad`).
- **$h(n)$ (Heurística):** Quantos km **ainda faltam** (estimativa em linha reta) até o destino (`Bucharest`).
- **$f(n)$ (Custo total):** A soma dos dois ($g + h$).

Em cada passo, o algoritmo olha as cidades vizinhas e escolhe sempre a que tiver o menor valor, garantindo o caminho mais barato sem perder tempo em rotas ruins.

## O que aprendi neste projeto

### Engenharia de Software, Git e GitHub
- **Fluxo com Branches e Pull Requests:** Aprendi a isolar cada fase do desenvolvimento em branches separadas (`fase-1` a `fase-6`) e integrar tudo na `main` de forma organizada via Pull Requests.
- **Controle de Versão na Prática:** Pratiquei commits semânticos (*Conventional Commits*), visualização do histórico com `git log --oneline --graph` e recuperação de erros usando `git reset` e `git restore`.
- **Leitura de Diagramas UML:** Entendi como acompanhar diagramas de atividades, sequência, classes, objetos e estados para compreender o funcionamento do sistema antes de escrever o código.

### Lógica de Programação e Python
- **Estruturas de Dados:** Aprendi a diferença prática entre dicionários (`dict`), listas (`list`) e tuplas (`tuple`) escolhendo cada um conforme a necessidade do algoritmo.

- **Depuração com Breakpoints:** Utilizei *breakpoints* no VS Code para pausar a execução dentro dos laços `for` e acompanhar passo a passo como as variáveis e as listas mudavam a cada volta.


Desenvolvido por **Anthony de Castro Santos** — Análise e Desenvolvimento de Sistemas (FATEC Araraquara).

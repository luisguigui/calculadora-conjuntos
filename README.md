# 🔢 CALCULADORA DE TEORIA DOS CONJUNTOS — Completo

> Um software educacional abrangente desenvolvido em Python com CustomTkinter que implementa operações de teoria dos conjuntos do básico ao avançado. Apresenta 16 operações distintas, categorizadas por dificuldade, com explicações teóricas passo a passo, visualização clara de fórmulas matemáticas e interface profissional.

[![Python](https://img.shields.io/badge/python-3.7+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Math](https://img.shields.io/badge/Math-Set%20Theory-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Educational-brightgreen.svg)]()
[![Academic](https://img.shields.io/badge/Academic-Complete-success.svg)]()

<div align="center">

**[🚀 Instalação](#-instalação-e-execução) • [🎮 Como Usar](#-como-usar) • [📖 Documentação](#-arquitetura-completa) • [🧮 Operações](#-16-operações-disponíveis) • [📚 Teoria](#-teoria-dos-conjuntos)**

</div>

---

## 🌟 Visão Geral

**CALCULADORA DE TEORIA DOS CONJUNTOS** é uma ferramenta educacional completa que implementa todas as operações fundamentais de teoria dos conjuntos com **suporte a explicações detalhadas**, **fórmulas matemáticas**, **passo a passo** e **exemplos práticos**.

### ✨ Destaques Principais

- 🔢 **16 Operações**: Do básico ao avançado
- 📂 **5 Categorias**: Básicas, Complemento, Relações, Avançadas
- 📚 **Teoria Completa**: Explicações passo a passo para cada operação
- 🎨 **Interface Clara**: Dark mode profissional com CustomTkinter
- ⌨️ **Entrada Flexível**: Suporta números, letras e caracteres especiais
- 📊 **Fórmulas Matemáticas**: Visualização de fórmulas em notação matemática
- 🎯 **Feedback Visual**: Resultados destacados e categorizados por cor
- 🔄 **Filtro Dinâmico**: Alterne entre categorias de operações
- ✅ **Validação**: Tratamento robusto de erros e entradas
- 🖥️ **Responsivo**: Ajusta-se a diferentes resoluções

---

## 🧮 16 Operações Disponíveis

### 📂 CATEGORIA 1: Operações Básicas (5 operações)

#### 1️⃣ **União (A ∪ B)**

```
DEFINIÇÃO:
A ∪ B = { x | x ∈ A ou x ∈ B }

Reúne TODOS os elementos de A e B.
Em conjuntos não existem duplicatas.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A ∪ B = {1, 2, 3, 4, 5, 6, 7}

FÓRMULA: |A∪B| = |A| + |B| − |A∩B|
```

**Código Python**:
```python
case "uniao":
    r = set_a | set_b  # Operador | faz a união
    # Resultado: todos elementos de ambos os conjuntos
```

---

#### 2️⃣ **Interseção (A ∩ B)**

```
DEFINIÇÃO:
A ∩ B = { x | x ∈ A e x ∈ B }

Contém APENAS os elementos comuns.
Elementos que estão SIMULTANEAMENTE em A e B.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A ∩ B = {3, 4, 5}

Caso especial: A ∩ B = ∅ (vazio) → conjuntos disjuntos
```

**Código Python**:
```python
case "intersecao":
    r = set_a & set_b  # Operador & faz a interseção
    # Resultado: apenas elementos que existem em AMBOS
```

---

#### 3️⃣ **Diferença A − B**

```
DEFINIÇÃO:
A − B = { x | x ∈ A e x ∉ B }

Remove de A tudo que também está em B.
Resultado: elementos EXCLUSIVOS de A.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A − B = {1, 2}  (o que sobra de A)

Interpretação: "A menos B"
```

**Código Python**:
```python
case "dif_ab":
    r = set_a - set_b  # Operador - faz a diferença
    # Resultado: elementos em A que não estão em B
    
removidos = set_a & set_b  # Quais foram removidos
# Exemplo: removidos = {3, 4, 5}
```

---

#### 4️⃣ **Diferença B − A**

```
DEFINIÇÃO:
B − A = { x | x ∈ B e x ∉ A }

Remove de B tudo que também está em A.
Resultado: elementos EXCLUSIVOS de B.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
B − A = {6, 7}  (o que sobra de B)
```

---

#### 5️⃣ **Diferença Simétrica (A △ B)**

```
DEFINIÇÃO:
A △ B = (A−B) ∪ (B−A)

Reúne elementos EXCLUSIVAMENTE em A ou EXCLUSIVAMENTE em B.
Exclui a interseção.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
A−B = {1, 2}
B−A = {6, 7}
A △ B = {1, 2, 6, 7}

Interpretação: "O que distingue os dois conjuntos"
```

**Código Python**:
```python
case "dif_sim":
    r = set_a.symmetric_difference(set_b)
    # Equivalente a: (set_a - set_b) | (set_b - set_a)
    
so_a = set_a - set_b  # Exclusivos de A
so_b = set_b - set_a  # Exclusivos de B
# Resultado: so_a ∪ so_b
```

---

### 📂 CATEGORIA 2: Operações com Complemento (3 operações)

#### 6️⃣ **Complemento de A (Aᶜ)**

```
DEFINIÇÃO:
Aᶜ = U − A

U (universo) = A ∪ B (localmente)
Aᶜ contém tudo do universo que NÃO está em A.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
U = A ∪ B = {1, 2, 3, 4, 5, 6, 7}
Aᶜ = U − A = {6, 7}

Interpretação: "Tudo exceto A"
```

**Código Python**:
```python
case "comp_a":
    U = set_a | set_b  # Universo local = A ∪ B
    r = U - set_a       # Complemento = tudo menos A
```

---

#### 7️⃣ **Complemento de B (Bᶜ)**

```
DEFINIÇÃO:
Bᶜ = U − B

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
U = {1, 2, 3, 4, 5, 6, 7}
Bᶜ = U − B = {1, 2}
```

---

#### 8️⃣ **Complemento da União (A∪B)ᶜ**

```
LEI DE DE MORGAN:
(A∪B)ᶜ = Aᶜ ∩ Bᶜ

Significa: "Nem A nem B"
O que não pertence a NENHUM dos dois.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
U = A ∪ B = {1, 2, 3, 4, 5, 6, 7}
(A∪B)ᶜ = ∅  (vazio, pois U = A∪B)

Verificação:
Aᶜ = {6, 7}
Bᶜ = {1, 2}
Aᶜ ∩ Bᶜ = {6, 7} ∩ {1, 2} = ∅  ✓
```

**Código Python**:
```python
case "comp_uniao":
    r = U - (set_a | set_b)  # Tudo menos (A∪B)
    # Como U = A∪B, resultado é sempre ∅
    
ac = U - set_a  # Complemento de A
bc = U - set_b  # Complemento de B
# Verifica: ac & bc == r  (Lei de De Morgan)
```

---

#### 9️⃣ **Complemento da Interseção (A∩B)ᶜ**

```
LEI DE DE MORGAN:
(A∩B)ᶜ = Aᶜ ∪ Bᶜ

Significa: "Não (A e B ao mesmo tempo)"
Tudo exceto a interseção.

EXEMPLO:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
U = A ∪ B = {1, 2, 3, 4, 5, 6, 7}
A ∩ B = {3, 4, 5}
(A∩B)ᶜ = U − {3, 4, 5} = {1, 2, 6, 7}

Verificação:
Aᶜ = {6, 7}
Bᶜ = {1, 2}
Aᶜ ∪ Bᶜ = {6, 7} ∪ {1, 2} = {1, 2, 6, 7}  ✓
```

---

### 📂 CATEGORIA 3: Relações Entre Conjuntos (4 operações)

#### 🔟 **Subconjunto A ⊆ B?**

```
DEFINIÇÃO:
A ⊆ B quando todo elemento de A também pertence a B.

EXEMPLO 1 (Verdadeiro):
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
A ⊆ B ?  SIM ✓
Todos elementos de A estão em B.

EXEMPLO 2 (Falso):
A = {1, 2, 3}
B = {1, 2, 4, 5}
A ⊆ B ?  NÃO ✗
Elemento 3 está em A mas não em B.

Propriedades:
- Todo conjunto é subconjunto de si: A ⊆ A
- Conjunto vazio é subconjunto de qualquer coisa: ∅ ⊆ A
```

**Código Python**:
```python
case "subconjunto_ab":
    ok = set_a.issubset(set_b)  # Verifica se A ⊆ B
    
if ok:
    # Todos elementos de A estão em B
    resultado = "SIM — A ⊆ B"
else:
    # Encontra elementos de A ausentes em B
    nao_em_b = set_a - set_b
    resultado = f"NÃO — A ⊄ B (ausentes: {nao_em_b})"
```

---

#### 1️⃣1️⃣ **Subconjunto B ⊆ A?**

```
Verifica se todo elemento de B pertence a A.
(Operação inversa da anterior)
```

---

#### 1️⃣2️⃣ **Igualdade de Conjuntos (A = B?)**

```
DEFINIÇÃO:
A = B quando A ⊆ B E B ⊆ A

Ou seja: possuem EXATAMENTE os mesmos elementos.
A ordem não importa.

EXEMPLO 1 (Verdadeiro):
A = {1, 2, 3}
B = {3, 1, 2}
A = B ?  SIM ✓
Mesmos elementos, ordem diferente.

EXEMPLO 2 (Falso):
A = {1, 2, 3}
B = {1, 2, 3, 4}
A = B ?  NÃO ✗
B tem elemento 4 que A não tem.
```

**Código Python**:
```python
case "igualdade":
    ok = set_a == set_b  # Verifica se são iguais
    
    # Análise:
    exc_a = set_a - set_b  # Exclusivos de A
    exc_b = set_b - set_a  # Exclusivos de B
    
    # Se ambos vazios, são iguais
    if not exc_a and not exc_b:
        resultado = "SIM — A = B"
    else:
        resultado = "NÃO — A ≠ B"
```

---

#### 1️⃣3️⃣ **Conjuntos Disjuntos (A ∩ B = ∅?)**

```
DEFINIÇÃO:
Dois conjuntos são DISJUNTOS quando não têm nenhum
elemento em comum: A ∩ B = ∅.

EXEMPLO 1 (Disjuntos):
A = {1, 2, 3}
B = {4, 5, 6}
A ∩ B = ∅  ?  SIM ✓
Nenhum elemento em comum.

EXEMPLO 2 (Não disjuntos):
A = {1, 2, 3}
B = {3, 4, 5}
A ∩ B = {3}  ✗ (não vazio)
Compartilham o elemento 3.
```

**Código Python**:
```python
case "disjuntos":
    inter = set_a & set_b
    ok = len(inter) == 0
    
    if ok:
        resultado = "SIM — A ∩ B = ∅ (disjuntos)"
    else:
        resultado = f"NÃO — A ∩ B = {inter} (não disjuntos)"
```

---

### 📂 CATEGORIA 4: Operações Avançadas (3 operações)

#### 1️⃣4️⃣ **Cardinalidade (|A|, |B|)**

```
DEFINIÇÃO:
|X| = número de elementos DISTINTOS em X

PRINCÍPIO DA INCLUSÃO-EXCLUSÃO:
|A∪B| = |A| + |B| − |A∩B|

Subtrai-se a interseção porque seus elementos
seriam contados duas vezes.

EXEMPLO:
A = {1, 2, 3, 4, 5}        |A| = 5
B = {3, 4, 5, 6, 7}        |B| = 5
A ∩ B = {3, 4, 5}          |A∩B| = 3
A ∪ B = {1,2,3,4,5,6,7}    |A∪B| = 7

Verificação:
|A∪B| = 5 + 5 − 3 = 7  ✓

Também calcula:
|A△B| = |A∪B| − |A∩B| = 7 − 3 = 4
(elementos na diferença simétrica)
```

**Código Python**:
```python
case "cardinalidade":
    inter = set_a & set_b
    uniao = set_a | set_b
    
    r = {
        f"|A| = {len(set_a)}",
        f"|B| = {len(set_b)}",
        f"|A∩B| = {len(inter)}",
        f"|A∪B| = {len(uniao)}",  # Aplicando fórmula
    }
    
    # Verifica:
    calc = len(set_a) + len(set_b) - len(inter)
    assert len(uniao) == calc  # Deve bater
```

---

#### 1️⃣5️⃣ **Produto Cartesiano (A × B)**

```
DEFINIÇÃO:
A × B = { (a, b) | a ∈ A e b ∈ B }

Todos os PARES ORDENADOS (a, b).
A ordem importa: (a,b) ≠ (b,a).

EXEMPLO:
A = {1, 2}
B = {a, b, c}
A × B = {(1,a), (1,b), (1,c), (2,a), (2,b), (2,c)}
|A × B| = 6

FÓRMULA:
|A × B| = |A| × |B| = 2 × 3 = 6 pares

Aplicações:
- Coordenadas (x, y)
- Relações matemáticas
- Funções
```

**Código Python**:
```python
case "prod_cart":
    MAX = 30  # Limita para não travar UI
    
    pares = [
        (a, b) for a in sorted(str(x) for x in set_a)
                for b in sorted(str(x) for x in set_b)
    ]
    
    r = {f"({a},{b})" for a, b in pares[:MAX]}
    
    total = len(set_a) * len(set_b)
    # Se total > MAX, mostra aviso
    
    # Resultado: exibe primeiros pares
    # Total: total pares possíveis
```

---

#### 1️⃣6️⃣ **Conjunto das Partes (℘(A))**

```
DEFINIÇÃO:
℘(A) = conjunto de TODOS os subconjuntos possíveis de A
(incluindo ∅ e o próprio A)

FÓRMULA:
|℘(A)| = 2^|A|

Cada elemento pode estar ou não → 2 escolhas por elemento

EXEMPLO:
A = {1, 2, 3}
|A| = 3
|℘(A)| = 2^3 = 8 subconjuntos

Subconjuntos:
1. ∅           (nenhum elemento)
2. {1}         (só 1)
3. {2}         (só 2)
4. {3}         (só 3)
5. {1, 2}      (1 e 2)
6. {1, 3}      (1 e 3)
7. {2, 3}      (2 e 3)
8. {1, 2, 3}   (todos)

Interpretação:
Para cada elemento: "incluir ou não?"
3 elementos × 2 opções = 2^3 = 8
```

**Código Python**:
```python
case "partes":
    from itertools import combinations
    
    MAX_ELEM = 4  # Evita explosão combinatória
    lista = sorted(str(x) for x in set_a)[:MAX_ELEM]
    n = len(lista)
    
    # Gera todos os subconjuntos
    subconj = []
    for r_size in range(n + 1):  # 0 a n elementos
        for combo in combinations(lista, r_size):
            subconj.append("{" + ", ".join(combo) + "}")
    
    # Resultado: lista de subconjuntos
    total_teorico = 2 ** len(set_a)
    
    # Se A > 4 elementos, mostra apenas subconjuntos dos 4 primeiros
```

---

## 🏗️ Arquitetura Completa

### 📊 Fluxo Geral

```
┌─────────────────────────────────┐
│   Usuário inicia App()          │
└────────────┬────────────────────┘
             │
    ┌────────▼────────────────────┐
    │ Constrói Interface (_build) │
    ├────────────────────────────┤
    │ ├─ Título e descrição      │
    │ ├─ Inputs A e B            │
    │ ├─ Filtros de categoria    │
    │ ├─ Grid de operações       │
    │ ├─ Label resultado         │
    │ ├─ Label fórmula           │
    │ └─ Textbox teoria          │
    └────────┬────────────────────┘
             │
    ┌────────▼────────────────────┐
    │ Aguarda interação do usuário│
    └────────┬────────────────────┘
             │
    ┌────────┴─────────────────────────┐
    │                                  │
┌───▼───────────────┐      ┌──────────▼─────┐
│ Clica categoria   │      │ Clica operação │
├───────────────────┤      ├────────────────┤
│ _filtrar_cat()    │      │ _calcular()    │
│                   │      │                │
│ 1. Define cat     │      │ 1. Parse A, B  │
│ 2. Renderiza ops  │      │ 2. Calcula op  │
│ 3. Destaca botão  │      │ 3. Exibe resul │
│ 4. Volta ao loop  │      │ 4. Mostra teor │
└───────────────────┘      └────────────────┘
```

---

### 🧩 Estrutura de Classes

```
conjuntos.py
│
├── 📊 ESTRUTURA DE DADOS
│   ├── CATEGORIAS (dict[str, str|None])
│   │   ├─ "Todas": None
│   │   ├─ "Básicas": "basico"
│   │   ├─ "Complemento": "complemento"
│   │   ├─ "Relações": "relacao"
│   │   └─ "Avançadas": "avancado"
│   │
│   └── OPERACOES (list[dict])
│       ├─ Cada operação tem:
│       │   ├─ "id": identificador único
│       │   ├─ "cat": categoria
│       │   ├─ "simbolo": símbolo matemático
│       │   ├─ "nome": nome descritivo
│       │   ├─ "descricao": breve descrição
│       │   └─ "formula": fórmula formal
│       │
│       └─ 16 operações total (5+3+4+3)
│
├── 🔧 FUNÇÕES UTILITÁRIAS
│   ├── formatar(s: set) → str
│   │   └─ Converte {1,2,3} → "{ 1, 2, 3 }"
│   │
│   └── calcular(op_id: str, set_a, set_b) → (str, str)
│       ├─ (1) Valida operação via match/case
│       ├─ (2) Aplica lógica de conjuntos
│       ├─ (3) Retorna (resultado_formatado, teoria)
│       └─ 16 cases para cada operação
│
└── 🎮 CLASSE: App(ctk.CTk)
    │
    ├── INICIALIZAÇÃO
    │   ├── __init__()
    │   │   ├─ Cria janela 860x720
    │   │   ├─ Inicializa estado (_cat_atual, _op_atual)
    │   │   └─ Chama _build_ui()
    │   │
    │   └── _build_ui()
    │       ├─ Cria títulos
    │       ├─ Cria inputs A e B
    │       ├─ Cria filtros categoria
    │       ├─ Cria grid operações
    │       ├─ Cria labels resultado/fórmula
    │       └─ Cria textbox teoria
    │
    ├── INTERATIVIDADE
    │   ├── _filtrar_cat(chave, nome)
    │   │   ├─ Atualiza _cat_atual
    │   │   ├─ Destaca botão
    │   │   └─ Chama _render_ops()
    │   │
    │   ├── _calcular(op: dict)
    │   │   ├─ Parse inputs via _parse()
    │   │   ├─ Chama calcular(op_id, set_a, set_b)
    │   │   ├─ Atualiza labels
    │   │   ├─ Atualiza textbox
    │   │   └─ Destaca botão operação
    │   │
    │   └── _render_ops()
    │       ├─ Limpa grid anterior
    │       ├─ Filtra operações por categoria
    │       ├─ Cria botões em grid 4 colunas
    │       └─ Reaplica destaque se houver
    │
    ├── UTILITÁRIOS
    │   └── _parse(texto: str) → set
    │       ├─ Split por vírgula
    │       ├─ Strip cada item
    │       ��─ Retorna set
    │       └─ Trata strings vazias
    │
    └── PROPRIEDADES
        ├── _cat_atual: str|None (categoria selecionada)
        ├── _op_atual: str|None (operação selecionada)
        ├── _btn_ops: dict (referências aos botões)
        ├── _btn_cats: dict (referências aos filtros)
        ├── entry_a: CTkEntry (entrada conjunto A)
        ├── entry_b: CTkEntry (entrada conjunto B)
        ├── lbl_resultado: CTkLabel (resultado)
        ├── lbl_formula: CTkLabel (fórmula)
        └── textbox: CTkTextbox (teoria)
```

---

## 📚 Explicação Detalhada do Código

### 1. Estrutura de Dados

```python
CATEGORIAS = {
    "Todas":       None,              # Mostra todas as operações
    "Básicas":     "basico",          # 5 operações
    "Complemento": "complemento",     # 3 operações
    "Relações":    "relacao",         # 4 operações
    "Avançadas":   "avancado",        # 3 operações
}

OPERACOES = [
    {
        "id": "uniao",                # Identificador único
        "cat": "basico",              # Categoria
        "simbolo": "A ∪ B",           # Símbolo para display
        "nome": "União",              # Nome descritivo
        "descricao": "...",           # Descrição breve
        "formula": "A ∪ B = ...",     # Fórmula matemática
    },
    # ... mais 15 operações
]
```

**Propósito**: Organiza todas as operações com metadados
**Vantagem**: Fácil adicionar novas operações mantendo padrão

---

### 2. Função `formatar()`

```python
def formatar(s: set) -> str:
    """Exibe um set como { a, b, c } ou ∅ se vazio."""
    if not s:
        return "∅"  # Símbolo de conjunto vazio
    return "{ " + ", ".join(sorted(str(x) for x in s)) + " }"

# EXEMPLOS:
formatar({1, 2, 3})  # "{ 1, 2, 3 }"
formatar({})         # "∅"
formatar({'a','b'})  # "{ a, b }"
```

**Propósito**: Padronizar exibição de conjuntos
**Processo**:
1. Se vazio → retorna "∅"
2. Converte cada elemento para string
3. Ordena (para resultado consistente)
4. Junta com ", "
5. Envolve em "{ ... }"

---

### 3. Função `calcular()` — Motor Central

```python
def calcular(op_id: str, set_a: set, set_b: set) -> tuple[str, str]:
    """
    Retorna (resultado_str, teoria_str) para a operação solicitada.
    """
    U = set_a | set_b  # Universo local = A ∪ B
    
    match op_id:  # Python 3.10+ pattern matching
        case "uniao":
            r = set_a | set_b
            teoria = (
                "DEFINIÇÃO\n"
                "  A ∪ B reúne TODOS os elementos de A e de B.\n"
                "  Em conjuntos não existem duplicatas...\n\n"
                "PASSO A PASSO\n"
                f"  A = {formatar(set_a)}  ({len(set_a)} elemento(s))\n"
                # ... mais linhas de teoria
                f"RESULTADO\n"
                f"  A ∪ B = {formatar(r)}"
            )
        
        case "intersecao":
            # ... outro case
            pass
        
        # ... 16 cases total
        
        case _:  # Default
            r = set()
            teoria = "Operação não reconhecida."
    
    return formatar(r), teoria
```

**Arquitetura**:
- **match/case**: Estrutura switch/case do Python 3.10+
- **U = set_a | set_b**: Calcula universo local
- **Cada case**:
  1. Calcula resultado (r)
  2. Monta explicação teórica (teoria)
  3. Usa f-strings para interpolar valores
  4. Retorna (resultado, teoria)

**Exemplo Prático**:
```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}

resultado, teoria = calcular("uniao", set_a, set_b)

# resultado = "{ 1, 2, 3, 4, 5 }"
# teoria = """DEFINIÇÃO
#   A ∪ B reúne TODOS os elementos...
#   
#   PASSO A PASSO
#   A = { 1, 2, 3 }  (3 elemento(s))
#   B = { 3, 4, 5 }  (3 elemento(s))
#   Em comum: { 3 }
#   
#   RESULTADO
#   A ∪ B = { 1, 2, 3, 4, 5 }"""
```

---

### 4. Classe `App` — Interface Principal

#### **Inicialização**

```python
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Teoria dos Conjuntos — Completo")
        self.geometry("860x720")
        self.resizable(True, True)
        
        # Estado
        self._cat_atual = None      # Categoria ativa (None = Todas)
        self._op_atual = None       # Operação ativa
        self._btn_ops = {}          # Dicionário de botões operações
        self._btn_cats = {}         # Dicionário de botões categorias
        
        self._build_ui()  # Constrói interface
```

**Estado Mantido**:
- `_cat_atual`: Qual categoria está selecionada
- `_op_atual`: Qual operação foi escolhida
- `_btn_*`: Referências para manipular botões dinamicamente

---

#### **Método `_build_ui()` — Construção da Interface**

```python
def _build_ui(self):
    # 1. TÍTULO
    ctk.CTkLabel(
        self,
        text="Calculadora de Teoria dos Conjuntos",
        font=("Georgia", 22, "bold"),
    ).pack(pady=(20, 4))
    
    # 2. INPUTS A E B
    frame_inp = ctk.CTkFrame(self, fg_color="transparent")
    frame_inp.pack(padx=30, fill="x")
    
    for col, (label, attr) in enumerate([
        ("Conjunto A (ex: 1, 2, 3, a):", "entry_a"),
        ("Conjunto B (ex: 3, 4, b, c):", "entry_b")
    ]):
        ctk.CTkLabel(frame_inp, text=label).grid(row=0, column=col)
        entry = ctk.CTkEntry(frame_inp, width=360, placeholder_text="...")
        entry.grid(row=1, column=col, padx=8)
        setattr(self, attr, entry)  # Armazena como self.entry_a, self.entry_b
    
    # Valores padrão
    self.entry_a.insert(0, "1, 2, 3, 4, 5")
    self.entry_b.insert(0, "3, 4, 5, 6, 7")
    
    # 3. FILTRO DE CATEGORIAS
    frame_cat = ctk.CTkFrame(self, fg_color="transparent")
    frame_cat.pack(pady=(18, 6))
    
    for nome_cat, chave_cat in CATEGORIAS.items():
        btn = ctk.CTkButton(
            frame_cat,
            text=nome_cat,
            command=lambda c=chave_cat, n=nome_cat: self._filtrar_cat(c, n)
        )
        btn.pack(side="left", padx=3)
        self._btn_cats[nome_cat] = btn  # Armazena referência
    
    # Destaca "Todas" por padrão
    self._btn_cats["Todas"].configure(fg_color=("#2563EB", "#1d4ed8"))
    
    # 4. GRID DE OPERAÇÕES
    self.frame_ops = ctk.CTkScrollableFrame(self, height=170)
    self.frame_ops.pack(padx=30, pady=(4, 10), fill="x")
    self._render_ops()  # Renderiza operações iniciais
    
    # 5. LABELS DE RESULTADO
    self.lbl_resultado = ctk.CTkLabel(
        self,
        text="Resultado: selecione uma operação",
        font=("Courier New", 17, "bold"),
        text_color="#22c55e"
    )
    self.lbl_resultado.pack(pady=(4, 2))
    
    self.lbl_formula = ctk.CTkLabel(
        self,
        text="",
        font=("Courier New", 13),
        text_color="gray"
    )
    self.lbl_formula.pack()
    
    # 6. TEXTBOX PARA TEORIA
    self.textbox = ctk.CTkTextbox(
        self,
        font=("Courier New", 13),
        height=200,
        state="disabled",
        wrap="word"
    )
    self.textbox.pack(padx=30, pady=(0, 20), fill="both", expand=True)
```

**Estrutura Visual**:
```
┌─────────────────────────────────────────────┐
│  Calculadora de Teoria dos Conjuntos        │
│  Do básico ao avançado...                   │
├─────────────────────────────────────────────┤
│ Conjunto A (ex: 1, 2, 3, a):               │
│ [1, 2, 3, 4, 5________________]             │
│ Conjunto B (ex: 3, 4, b, c):               │
│ [3, 4, 5, 6, 7________________]             │
├─────────────────────────────────────────────┤
│ Categoria: [Todas] [Básicas] [...]          │
├─────────────────────────────────────────────┤
│ [União] [Interseção] [Dif A-B] ...          │
│ [Dif B-A] [Dif Simétrica]                   │
├─────────────────────────────────────────────┤
│   A ∪ B  =  { 1, 2, 3, 4, 5, 6, 7 }        │
│ A ∪ B = { x | x ∈ A ou x ∈ B }             │
├─────────────────────────────────────────────┤
│ Passo a Passo (Teoria):                     │
│ [Textbox com explicação detalhada...]       │
│ [Pode fazer scroll]                         │
└─────────────────────────────────────────────┘
```

---

#### **Método `_render_ops()` — Renderiza Grid de Operações**

```python
def _render_ops(self):
    # 1. LIMPAR WIDGETS ANTIGOS
    for w in self.frame_ops.winfo_children():
        w.destroy()
    self._btn_ops.clear()
    
    # 2. FILTRAR OPERAÇÕES POR CATEGORIA
    ops = [
        op for op in OPERACOES
        if self._cat_atual is None or op["cat"] == self._cat_atual
    ]
    
    # 3. CRIAR BOTÕES EM GRID (4 COLUNAS)
    cols = 4
    for i, op in enumerate(ops):
        # Frame para cada botão
        frm = ctk.CTkFrame(self.frame_ops, corner_radius=8)
        frm.grid(row=i // cols, column=i % cols, padx=5, pady=5, sticky="nsew")
        
        # Botão
        btn = ctk.CTkButton(
            frm,
            text=f"{op['simbolo']}\n{op['nome']}",
            font=("Arial", 12),
            height=54,
            command=lambda o=op: self._calcular(o)
        )
        btn.pack(fill="both", expand=True)
        self._btn_ops[op["id"]] = btn  # Armazena referência
        
        self.frame_ops.columnconfigure(i % cols, weight=1)
    
    # 4. REAPLICA DESTAQUE SE HOUVER OPERAÇÃO ATIVA
    if self._op_atual and self._op_atual in self._btn_ops:
        self._btn_ops[self._op_atual].configure(
            fg_color=("#1e40af", "#1e3a8a")  # Azul destaque
        )
```

**Dinâmica**:
- **Filtragem**: Se categoria "Básicas", mostra apenas 5 operações
- **Grid Responsivo**: 4 colunas, quantas linhas forem necessárias
- **Destaque**: Operação selecionada fica azul
- **Reutilização**: Ao trocar categoria, recria botões

---

#### **Método `_calcular()` — Executa Cálculo**

```python
def _calcular(self, op: dict):
    # 1. ARMAZENA OPERAÇÃO ATIVA
    self._op_atual = op["id"]
    
    # 2. DESTACA BOTÃO
    for b in self._btn_ops.values():
        b.configure(fg_color=("gray75", "gray30"))  # Desativa todos
    if op["id"] in self._btn_ops:
        self._btn_ops[op["id"]].configure(
            fg_color=("#1e40af", "#1e3a8a")  # Ativa selecionado
        )
    
    # 3. PARSE DOS CONJUNTOS
    set_a = self._parse(self.entry_a.get())
    set_b = self._parse(self.entry_b.get())
    
    # 4. CALCULA
    resultado_str, teoria_str = calcular(op["id"], set_a, set_b)
    
    # 5. ATUALIZA UI
    # Resultado
    self.lbl_resultado.configure(
        text=f"  {op['simbolo']}  =  {resultado_str}"
    )
    
    # Fórmula
    self.lbl_formula.configure(text=op["formula"])
    
    # Teoria
    self.textbox.configure(state="normal")
    self.textbox.delete("1.0", "end")
    self.textbox.insert("1.0", teoria_str)
    self.textbox.configure(state="disabled")
```

**Fluxo**:
1. Marca operação como ativa
2. Destaca visualmente o botão
3. Parse: "1, 2, 3" → {1, 2, 3}
4. Chama função calcular()
5. Atualiza 3 labels simultaneamente

---

#### **Método `_parse()` — Converte String para Set**

```python
@staticmethod
def _parse(texto: str) -> set:
    """Converte "1, 2, 3, a" em {1, 2, 3, 'a'}"""
    if not texto.strip():
        return set()  # String vazia → set vazio
    
    # Split por vírgula, strip espaços, filtra vazios
    return {
        item.strip()
        for item in texto.split(",")
        if item.strip()
    }

# EXEMPLOS:
_parse("1, 2, 3")        # {'1', '2', '3'}  (strings!)
_parse("a, b, c")        # {'a', 'b', 'c'}
_parse("  1  ,  2  ")    # {'1', '2'}
_parse("")               # set()
_parse("1,2,3,2,1")      # {'1', '2', '3'}  (sem duplicatas)
```

**Nota**: Armazena como **strings**, não inteiros!
- "1" ∈ {'1', '2', '3'}
- 1 ∉ {'1', '2', '3'}

---

#### **Método `_filtrar_cat()` — Alterna Categorias**

```python
def _filtrar_cat(self, chave: str | None, nome: str):
    # 1. ATUALIZA ESTADO
    self._cat_atual = chave  # None = Todas, "basico" = Básicas, etc
    
    # 2. DESATIVA TODOS OS FILTROS
    for n, b in self._btn_cats.items():
        b.configure(fg_color=("gray75", "gray30"))
    
    # 3. ATIVA SELECIONADO
    self._btn_cats[nome].configure(fg_color=("#2563EB", "#1d4ed8"))
    
    # 4. RECONSTRÓI GRID DE OPERAÇÕES
    self._render_ops()
    
    # 5. PRESERVA DESTAQUE DE OPERAÇÃO (se houver)
    if self._op_atual and self._op_atual in self._btn_ops:
        self._btn_ops[self._op_atual].configure(
            fg_color=("#1e40af", "#1e3a8a")
        )
```

**Exemplo**:
```
Clica "Básicas":
_cat_atual = "basico"
_render_ops() muda filtro
Grid agora mostra apenas 5 operações
```

---

## 🎮 Como Usar

### Passo 1: Inserir Conjuntos

```
Conjunto A: 1, 2, 3, 4, 5
Conjunto B: 3, 4, 5, 6, 7

Sistema converte para:
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
```

### Passo 2: Selecionar Categoria

```
Clica "Básicas":
├─ União (A ∪ B)
├─ Interseção (A ∩ B)
├─ Diferença A−B
├─ Diferença B−A
└─ Diferença Simétrica (A △ B)
```

### Passo 3: Escolher Operação

```
Clica "União":
├─ Calcula: {1, 2, 3, 4, 5, 6, 7}
├─ Mostra fórmula: A ∪ B = { x | x ∈ A ou x ∈ B }
└��� Exibe teoria com passo a passo
```

---

## 🚀 Como Rodar

### ✅ Pré-requisitos

- Python 3.10+
- pip

### 🔧 Passos

```bash
# 1. Clone
git clone https://github.com/luisguigui/calculadora-conjuntos.git
cd calculadora-conjuntos

# 2. Ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 3. Instale CustomTkinter
pip install customtkinter

# 4. Execute
python conjuntos.py
```

---

## 📄 requirements.txt

```
customtkinter>=5.0.0
```

---

## 🐛 Troubleshooting

### ❌ Problema: "ModuleNotFoundError: customtkinter"
**Solução**: `pip install customtkinter`

### ❌ Problema: Operações retornam vazio
**Causa**: Inputs em branco  
**Solução**: Preencha ambos A e B

### ❌ Problema: Caracteres especiais não funcionam
**Causa**: Parse apenas split por vírgula  
**Solução**: Use aspas se necessário, ex: `"#", "$", "%"`

### ❌ Problema: Textbox não atualiza
**Causa**: Pode estar disabled  
**Solução**: Código já trata (disable→insert→disable)

---

## ⚙️ Extensões Possíveis

- [ ] **Suporte a 3+ conjuntos**: A, B, C, D
- [ ] **Salvar operações**: Histórico de cálculos
- [ ] **Export PDF**: Relatório completo
- [ ] **Temas**: Light/Dark customizáveis
- [ ] **Operações lógicas**: Quantificadores, implicações
- [ ] **Visualização Venn**: Diagramas visuais
- [ ] **Modo avançado**: Variáveis simbólicas
- [ ] **Quiz**: Testes de conhecimento

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedor Python Full-Stack
- 📧 Contato: Abra uma issue

---

## 📄 Licença

MIT — Use livremente!

---

## 🌟 Se gostou, deixe uma ⭐!

```
   🔢 TEORIA DOS CONJUNTOS NUNCA FOI TÃO FÁCIL

   16 operações, categorias, explicações completas

   ⭐ APRENDA E PRATIQUE ⭐
```

---

**Versão**: 1.0 — Complete Edition  
**Status**: ✅ Production Ready  
**Foco**: Educação, Clareza, Completude
```

---

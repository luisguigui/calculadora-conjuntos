import customtkinter as ctk
from itertools import combinations

# ──────────────────────────────────────────────
#  Configuração visual
# ──────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ──────────────────────────────────────────────
#  Definição das operações
# ──────────────────────────────────────────────
CATEGORIAS = {
    "Todas":       None,
    "Básicas":     "basico",
    "Complemento": "complemento",
    "Relações":    "relacao",
    "Avançadas":   "avancado",
}

OPERACOES = [
    # ── BÁSICAS ──────────────────────────────────────────────────────────
    {
        "id": "uniao",
        "cat": "basico",
        "simbolo": "A ∪ B",
        "nome": "União",
        "descricao": "Todos os elementos de A e de B (sem repetição).",
        "formula": "A ∪ B  =  { x | x ∈ A  ou  x ∈ B }",
    },
    {
        "id": "intersecao",
        "cat": "basico",
        "simbolo": "A ∩ B",
        "nome": "Interseção",
        "descricao": "Apenas os elementos que existem em A e em B ao mesmo tempo.",
        "formula": "A ∩ B  =  { x | x ∈ A  e  x ∈ B }",
    },
    {
        "id": "dif_ab",
        "cat": "basico",
        "simbolo": "A − B",
        "nome": "Diferença A − B",
        "descricao": "O que está em A mas não está em B.",
        "formula": "A − B  =  { x | x ∈ A  e  x ∉ B }",
    },
    {
        "id": "dif_ba",
        "cat": "basico",
        "simbolo": "B − A",
        "nome": "Diferença B − A",
        "descricao": "O que está em B mas não está em A.",
        "formula": "B − A  =  { x | x ∈ B  e  x ∉ A }",
    },
    {
        "id": "dif_sim",
        "cat": "basico",
        "simbolo": "A △ B",
        "nome": "Diferença Simétrica",
        "descricao": "O que está exclusivamente em A ou exclusivamente em B.",
        "formula": "A △ B  =  (A−B) ∪ (B−A)",
    },
    # ── COMPLEMENTO ──────────────────────────────────────────────────────
    {
        "id": "comp_a",
        "cat": "complemento",
        "simbolo": "Aᶜ",
        "nome": "Complemento de A",
        "descricao": "Tudo em U = A∪B que não está em A.",
        "formula": "Aᶜ  =  U − A",
    },
    {
        "id": "comp_b",
        "cat": "complemento",
        "simbolo": "Bᶜ",
        "nome": "Complemento de B",
        "descricao": "Tudo em U = A∪B que não está em B.",
        "formula": "Bᶜ  =  U − B",
    },
    {
        "id": "comp_uniao",
        "cat": "complemento",
        "simbolo": "(A∪B)ᶜ",
        "nome": "Complemento da União",
        "descricao": "Lei de De Morgan: (A∪B)ᶜ = Aᶜ ∩ Bᶜ  (nem A nem B).",
        "formula": "(A∪B)ᶜ  =  Aᶜ ∩ Bᶜ",
    },
    {
        "id": "comp_int",
        "cat": "complemento",
        "simbolo": "(A∩B)ᶜ",
        "nome": "Complemento da Interseção",
        "descricao": "Lei de De Morgan: (A∩B)ᶜ = Aᶜ ∪ Bᶜ.",
        "formula": "(A∩B)ᶜ  =  Aᶜ ∪ Bᶜ",
    },
    # ── RELAÇÕES ─────────────────────────────────────────────────────────
    {
        "id": "subconjunto_ab",
        "cat": "relacao",
        "simbolo": "A ⊆ B ?",
        "nome": "A é subconjunto de B?",
        "descricao": "Verifica se todo elemento de A também pertence a B.",
        "formula": "A ⊆ B  ⟺  ∀x (x∈A → x∈B)",
    },
    {
        "id": "subconjunto_ba",
        "cat": "relacao",
        "simbolo": "B ⊆ A ?",
        "nome": "B é subconjunto de A?",
        "descricao": "Verifica se todo elemento de B também pertence a A.",
        "formula": "B ⊆ A  ⟺  ∀x (x∈B → x∈A)",
    },
    {
        "id": "igualdade",
        "cat": "relacao",
        "simbolo": "A = B ?",
        "nome": "Igualdade",
        "descricao": "Verifica se A e B têm exatamente os mesmos elementos.",
        "formula": "A = B  ⟺  (A⊆B)  e  (B⊆A)",
    },
    {
        "id": "disjuntos",
        "cat": "relacao",
        "simbolo": "A ∩ B = ∅ ?",
        "nome": "Conjuntos Disjuntos",
        "descricao": "Verifica se A e B não têm nenhum elemento em comum.",
        "formula": "Disjuntos  ⟺  A ∩ B = ∅",
    },
    # ── AVANÇADAS ─────────────────────────────────────────────────────────
    {
        "id": "cardinalidade",
        "cat": "avancado",
        "simbolo": "|A|, |B|",
        "nome": "Cardinalidade",
        "descricao": "Número de elementos e princípio da inclusão-exclusão.",
        "formula": "|A∪B|  =  |A| + |B| − |A∩B|",
    },
    {
        "id": "prod_cart",
        "cat": "avancado",
        "simbolo": "A × B",
        "nome": "Produto Cartesiano",
        "descricao": "Todos os pares ordenados (a, b) com a∈A e b∈B.",
        "formula": "A×B  =  { (a,b) | a∈A  e  b∈B }",
    },
    {
        "id": "partes",
        "cat": "avancado",
        "simbolo": "℘(A)",
        "nome": "Conjunto das Partes de A",
        "descricao": "Todos os subconjuntos possíveis de A (incluindo ∅ e A).",
        "formula": "|℘(A)|  =  2ⁿ,  onde n = |A|",
    },
]


# ──────────────────────────────────────────────
#  Funções de cálculo
# ──────────────────────────────────────────────
def formatar(s: set) -> str:
    """Exibe um set como { a, b, c } ou ∅ se vazio."""
    if not s:
        return "∅"
    return "{ " + ", ".join(sorted(str(x) for x in s)) + " }"


def calcular(op_id: str, set_a: set, set_b: set) -> tuple[str, str]:
    """
    Retorna (resultado_str, teoria_str) para a operação solicitada.
    """
    U = set_a | set_b  # universo local = A ∪ B

    match op_id:
        # ── BÁSICAS ──────────────────────────────────────────────
        case "uniao":
            r = set_a | set_b
            teoria = (
                "DEFINIÇÃO\n"
                "  A ∪ B reúne TODOS os elementos de A e de B.\n"
                "  Em conjuntos não existem duplicatas: elementos repetidos\n"
                "  aparecem uma única vez no resultado.\n\n"
                "PASSO A PASSO\n"
                f"  A = {formatar(set_a)}  ({len(set_a)} elemento(s))\n"
                f"  B = {formatar(set_b)}  ({len(set_b)} elemento(s))\n"
                f"  Em comum: {formatar(set_a & set_b)}\n"
                f"  Cardinalidade: |A∪B| = |A|+|B|−|A∩B| = "
                f"{len(set_a)}+{len(set_b)}−{len(set_a&set_b)} = {len(r)}\n\n"
                f"RESULTADO\n"
                f"  A ∪ B = {formatar(r)}"
            )

        case "intersecao":
            r = set_a & set_b
            teoria = (
                "DEFINIÇÃO\n"
                "  A ∩ B contém apenas os elementos que pertencem\n"
                "  SIMULTANEAMENTE a A e a B.\n\n"
                "PASSO A PASSO\n"
                f"  A = {formatar(set_a)}\n"
                f"  B = {formatar(set_b)}\n"
                "  Percorremos cada elemento de A e verificamos se ele\n"
                "  também está em B.\n"
            )
            if r:
                teoria += f"  Elementos em comum encontrados: {formatar(r)}\n"
            else:
                teoria += "  Nenhum elemento em comum → conjuntos DISJUNTOS.\n"
            teoria += f"\nRESULTADO\n  A ∩ B = {formatar(r)}"

        case "dif_ab":
            r = set_a - set_b
            removidos = set_a & set_b
            teoria = (
                "DEFINIÇÃO\n"
                "  A − B remove de A tudo o que também pertence a B.\n"
                "  Resultado: elementos EXCLUSIVOS de A.\n\n"
                "PASSO A PASSO\n"
                f"  Partimos de A = {formatar(set_a)}\n"
                f"  Removemos os elementos presentes em B: {formatar(removidos)}\n\n"
                f"RESULTADO\n"
                f"  A − B = {formatar(r)}"
            )

        case "dif_ba":
            r = set_b - set_a
            removidos = set_a & set_b
            teoria = (
                "DEFINIÇÃO\n"
                "  B − A remove de B tudo o que também pertence a A.\n"
                "  Resultado: elementos EXCLUSIVOS de B.\n\n"
                "PASSO A PASSO\n"
                f"  Partimos de B = {formatar(set_b)}\n"
                f"  Removemos os elementos presentes em A: {formatar(removidos)}\n\n"
                f"RESULTADO\n"
                f"  B − A = {formatar(r)}"
            )

        case "dif_sim":
            r = set_a.symmetric_difference(set_b)
            so_a = set_a - set_b
            so_b = set_b - set_a
            teoria = (
                "DEFINIÇÃO\n"
                "  A △ B (diferença simétrica) reúne os elementos que\n"
                "  pertencem EXCLUSIVAMENTE a A ou EXCLUSIVAMENTE a B.\n"
                "  É equivalente a (A−B) ∪ (B−A). Exclui a interseção.\n\n"
                "PASSO A PASSO\n"
                f"  Exclusivos de A (A−B): {formatar(so_a)}\n"
                f"  Exclusivos de B (B−A): {formatar(so_b)}\n"
                f"  Interseção excluída: {formatar(set_a & set_b)}\n\n"
                f"RESULTADO\n"
                f"  A △ B = {formatar(r)}"
            )

        # ── COMPLEMENTO ──────────────────────────────────────────
        case "comp_a":
            r = U - set_a
            teoria = (
                "DEFINIÇÃO\n"
                "  Aᶜ contém tudo do conjunto universo U que NÃO está em A.\n"
                "  Aqui U = A ∪ B (universo local).\n\n"
                "PASSO A PASSO\n"
                f"  U = A ∪ B = {formatar(U)}\n"
                f"  A = {formatar(set_a)}\n"
                f"  Aᶜ = U − A\n\n"
                f"RESULTADO\n"
                f"  Aᶜ = {formatar(r)}"
            )

        case "comp_b":
            r = U - set_b
            teoria = (
                "DEFINIÇÃO\n"
                "  Bᶜ contém tudo do conjunto universo U que NÃO está em B.\n"
                "  Aqui U = A ∪ B (universo local).\n\n"
                "PASSO A PASSO\n"
                f"  U = A ∪ B = {formatar(U)}\n"
                f"  B = {formatar(set_b)}\n"
                f"  Bᶜ = U − B\n\n"
                f"RESULTADO\n"
                f"  Bᶜ = {formatar(r)}"
            )

        case "comp_uniao":
            r = U - (set_a | set_b)  # = ∅ quando U = A∪B
            ac = U - set_a
            bc = U - set_b
            teoria = (
                "LEI DE DE MORGAN\n"
                "  (A∪B)ᶜ = Aᶜ ∩ Bᶜ\n"
                "  'Nem A nem B' — o que não pertence a nenhum dos dois.\n\n"
                "PASSO A PASSO\n"
                f"  U = A ∪ B = {formatar(U)}\n"
                f"  Aᶜ = U−A = {formatar(ac)}\n"
                f"  Bᶜ = U−B = {formatar(bc)}\n"
                f"  Aᶜ ∩ Bᶜ = {formatar(ac & bc)}\n"
                "  Como U = A∪B, não existem elementos fora de A∪B,\n"
                "  portanto (A∪B)ᶜ = ∅ neste universo.\n\n"
                f"RESULTADO\n"
                f"  (A∪B)ᶜ = {formatar(r)}"
            )

        case "comp_int":
            inter = set_a & set_b
            r = U - inter
            ac = U - set_a
            bc = U - set_b
            teoria = (
                "LEI DE DE MORGAN\n"
                "  (A∩B)ᶜ = Aᶜ ∪ Bᶜ\n"
                "  'Não (A e B ao mesmo tempo)' — tudo exceto a interseção.\n\n"
                "PASSO A PASSO\n"
                f"  A ∩ B = {formatar(inter)}\n"
                f"  U = {formatar(U)}\n"
                f"  (A∩B)ᶜ = U − (A∩B)\n"
                f"  Verificação: Aᶜ∪Bᶜ = {formatar(ac|bc)}\n\n"
                f"RESULTADO\n"
                f"  (A∩B)ᶜ = {formatar(r)}"
            )

        # ── RELAÇÕES ─────────────────────────────────────────────
        case "subconjunto_ab":
            ok = set_a.issubset(set_b)
            nao_em_b = set_a - set_b
            r = {"SIM — A ⊆ B"} if ok else {"NÃO — A ⊄ B"}
            teoria = (
                "DEFINIÇÃO\n"
                "  A ⊆ B quando todo elemento de A também pertence a B.\n"
                "  Todo conjunto é subconjunto de si mesmo.\n"
                "  ∅ é subconjunto de qualquer conjunto.\n\n"
                "VERIFICAÇÃO\n"
                f"  A = {formatar(set_a)}  ({len(set_a)} elemento(s))\n"
                f"  B = {formatar(set_b)}  ({len(set_b)} elemento(s))\n"
            )
            if ok:
                teoria += f"  Todos os elementos de A estão em B. ✓\n\nRESPOSTA\n  SIM — A ⊆ B"
            else:
                teoria += (
                    f"  Elemento(s) de A ausentes em B: {formatar(nao_em_b)}\n\n"
                    f"RESPOSTA\n  NÃO — A ⊄ B"
                )

        case "subconjunto_ba":
            ok = set_b.issubset(set_a)
            nao_em_a = set_b - set_a
            r = {"SIM — B ⊆ A"} if ok else {"NÃO — B ⊄ A"}
            teoria = (
                "DEFINIÇÃO\n"
                "  B ⊆ A quando todo elemento de B também pertence a A.\n\n"
                "VERIFICAÇÃO\n"
                f"  B = {formatar(set_b)}  ({len(set_b)} elemento(s))\n"
                f"  A = {formatar(set_a)}  ({len(set_a)} elemento(s))\n"
            )
            if ok:
                teoria += f"  Todos os elementos de B estão em A. ✓\n\nRESPOSTA\n  SIM — B ⊆ A"
            else:
                teoria += (
                    f"  Elemento(s) de B ausentes em A: {formatar(nao_em_a)}\n\n"
                    f"RESPOSTA\n  NÃO — B ⊄ A"
                )

        case "igualdade":
            ok = set_a == set_b
            r = {"SIM — A = B"} if ok else {"NÃO — A ≠ B"}
            teoria = (
                "DEFINIÇÃO\n"
                "  A = B quando A ⊆ B E B ⊆ A, ou seja,\n"
                "  possuem exatamente os mesmos elementos.\n\n"
                "VERIFICAÇÃO\n"
                f"  |A| = {len(set_a)},  |B| = {len(set_b)}\n"
                f"  A−B = {formatar(set_a-set_b)}  (exclusivos de A)\n"
                f"  B−A = {formatar(set_b-set_a)}  (exclusivos de B)\n\n"
                "RESPOSTA\n"
            )
            teoria += "  SIM — A = B  (conjuntos idênticos)" if ok else "  NÃO — A ≠ B"

        case "disjuntos":
            inter = set_a & set_b
            ok = len(inter) == 0
            r = {"SIM — disjuntos"} if ok else {"NÃO — têm interseção"}
            teoria = (
                "DEFINIÇÃO\n"
                "  Dois conjuntos são DISJUNTOS quando não têm nenhum\n"
                "  elemento em comum: A ∩ B = ∅.\n\n"
                "VERIFICAÇÃO\n"
                f"  A ∩ B = {formatar(inter)}\n\n"
                "RESPOSTA\n"
            )
            teoria += (
                "  SIM — A ∩ B = ∅, portanto são disjuntos."
                if ok else
                f"  NÃO — A ∩ B = {formatar(inter)}, não são disjuntos."
            )

        # ── AVANÇADAS ─────────────────────────────────────────────
        case "cardinalidade":
            inter = set_a & set_b
            uniao = set_a | set_b
            r = {
                f"|A| = {len(set_a)}",
                f"|B| = {len(set_b)}",
                f"|A∩B| = {len(inter)}",
                f"|A∪B| = {len(uniao)}",
            }
            teoria = (
                "DEFINIÇÃO\n"
                "  A cardinalidade |X| é o número de elementos distintos\n"
                "  de um conjunto X.\n\n"
                "PRINCÍPIO DA INCLUSÃO-EXCLUSÃO\n"
                "  |A∪B| = |A| + |B| − |A∩B|\n"
                "  Subtrai-se a interseção pois seus elementos seriam\n"
                "  contados duas vezes.\n\n"
                "CÁLCULO\n"
                f"  |A|   = {len(set_a)}\n"
                f"  |B|   = {len(set_b)}\n"
                f"  |A∩B| = {len(inter)}\n"
                f"  |A∪B| = {len(set_a)} + {len(set_b)} − {len(inter)} = {len(uniao)}\n"
                f"  |A△B| = |A∪B| − |A∩B| = {len(uniao)} − {len(inter)} = {len(uniao)-len(inter)}"
            )

        case "prod_cart":
            # Limita exibição para não travar a UI
            MAX = 30
            pares = [(a, b) for a in sorted(str(x) for x in set_a)
                              for b in sorted(str(x) for x in set_b)]
            r = {f"({a},{b})" for a, b in pares[:MAX]}
            cortado = len(pares) > MAX
            teoria = (
                "DEFINIÇÃO\n"
                "  A×B é o conjunto de todos os PARES ORDENADOS (a, b)\n"
                "  onde a ∈ A e b ∈ B. A ordem importa: (a,b) ≠ (b,a).\n\n"
                "CÁLCULO\n"
                f"  |A×B| = |A| × |B| = {len(set_a)} × {len(set_b)} = {len(pares)} par(es)\n\n"
                "EXEMPLO\n"
                f"  Primeiros pares: { {f'({a},{b})' for a,b in pares[:6]} }\n"
            )
            if cortado:
                teoria += f"\n  ⚠ Exibindo apenas os primeiros {MAX} de {len(pares)} pares."

        case "partes":
            MAX_ELEM = 4  # evita explosão combinatória na UI
            lista = sorted(str(x) for x in set_a)[:MAX_ELEM]
            n = len(lista)
            subconj = []
            for r_size in range(n + 1):
                for combo in combinations(lista, r_size):
                    subconj.append("{" + ", ".join(combo) + "}" if combo else "∅")
            r = set(subconj)
            teoria = (
                "DEFINIÇÃO\n"
                "  ℘(A) (lê-se 'conjunto das partes de A') contém TODOS\n"
                "  os possíveis subconjuntos de A, incluindo ∅ e o próprio A.\n\n"
                "FÓRMULA\n"
                f"  |℘(A)| = 2^|A| = 2^{len(set_a)} = {2**len(set_a)} subconjunto(s)\n"
                "  Cada elemento pode estar ou não em cada subconjunto:\n"
                "  2 escolhas × n elementos = 2ⁿ combinações.\n\n"
                "SUBCONJUNTOS\n"
            )
            if len(set_a) > MAX_ELEM:
                teoria += (
                    f"  ⚠ A tem {len(set_a)} elementos; exibindo apenas os\n"
                    f"  subconjuntos dos {MAX_ELEM} primeiros para não sobrecarregar.\n"
                )
            teoria += f"  {', '.join(sorted(subconj))}"

        case _:
            r = set()
            teoria = "Operação não reconhecida."

    return formatar(r), teoria


# ──────────────────────────────────────────────
#  Interface principal
# ──────────────────────────────────────────────
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Teoria dos Conjuntos — Completo")
        self.geometry("860x720")
        self.resizable(True, True)
        self._cat_atual = None          # None = todas
        self._op_atual = None
        self._btn_ops: dict[str, ctk.CTkButton] = {}
        self._btn_cats: dict[str, ctk.CTkButton] = {}
        self._build_ui()

    # ── construção da UI ──────────────────────────────────────────
    def _build_ui(self):
        # Título
        ctk.CTkLabel(
            self,
            text="Calculadora de Teoria dos Conjuntos",
            font=("Georgia", 22, "bold"),
        ).pack(pady=(20, 4))
        ctk.CTkLabel(
            self,
            text="Do básico ao avançado — com explicações passo a passo",
            font=("Arial", 13),
            text_color="gray",
        ).pack(pady=(0, 16))

        # ── Inputs A e B ─────────────────────────────────────────
        frame_inp = ctk.CTkFrame(self, fg_color="transparent")
        frame_inp.pack(padx=30, fill="x")

        for col, (label, attr) in enumerate(
            [("Conjunto A (ex: 1, 2, 3, a):", "entry_a"),
             ("Conjunto B (ex: 3, 4, b, c):", "entry_b")]
        ):
            ctk.CTkLabel(frame_inp, text=label, font=("Arial", 13)).grid(
                row=0, column=col, padx=8, pady=(0, 4), sticky="w"
            )
            entry = ctk.CTkEntry(
                frame_inp,
                width=360,
                placeholder_text="Elementos separados por vírgula",
                font=("Arial", 13),
            )
            entry.grid(row=1, column=col, padx=8)
            setattr(self, attr, entry)
            frame_inp.columnconfigure(col, weight=1)

        self.entry_a.insert(0, "1, 2, 3, 4, 5")
        self.entry_b.insert(0, "3, 4, 5, 6, 7")

        # ── Filtro por categoria ──────────────────────────────────
        frame_cat = ctk.CTkFrame(self, fg_color="transparent")
        frame_cat.pack(pady=(18, 6))
        ctk.CTkLabel(frame_cat, text="Categoria:", font=("Arial", 12)).pack(
            side="left", padx=(0, 8)
        )
        for nome_cat, chave_cat in CATEGORIAS.items():
            btn = ctk.CTkButton(
                frame_cat,
                text=nome_cat,
                width=100,
                height=28,
                font=("Arial", 12),
                command=lambda c=chave_cat, n=nome_cat: self._filtrar_cat(c, n),
            )
            btn.pack(side="left", padx=3)
            self._btn_cats[nome_cat] = btn
        self._btn_cats["Todas"].configure(fg_color=("#2563EB", "#1d4ed8"))

        # ── Grid de operações ─────────────────────────────────────
        self.frame_ops = ctk.CTkScrollableFrame(self, height=170)
        self.frame_ops.pack(padx=30, pady=(4, 10), fill="x")
        self._render_ops()

        # ── Resultado ─────────────────────────────────────────────
        self.lbl_resultado = ctk.CTkLabel(
            self,
            text="Resultado: selecione uma operação",
            font=("Courier New", 17, "bold"),
            text_color="#22c55e",
            wraplength=800,
        )
        self.lbl_resultado.pack(pady=(4, 2))

        self.lbl_formula = ctk.CTkLabel(
            self,
            text="",
            font=("Courier New", 13),
            text_color="gray",
        )
        self.lbl_formula.pack()

        # ── Teoria / passo a passo ────────────────────────────────
        ctk.CTkLabel(
            self,
            text="Passo a Passo (Teoria):",
            font=("Arial", 14, "bold"),
            anchor="w",
        ).pack(padx=30, pady=(12, 2), anchor="w")

        self.textbox = ctk.CTkTextbox(
            self,
            font=("Courier New", 13),
            height=200,
            state="disabled",
            wrap="word",
        )
        self.textbox.pack(padx=30, pady=(0, 20), fill="both", expand=True)

    # ── renderiza botões de operação filtrados ────────────────────
    def _render_ops(self):
        for w in self.frame_ops.winfo_children():
            w.destroy()
        self._btn_ops.clear()

        ops = [
            op for op in OPERACOES
            if self._cat_atual is None or op["cat"] == self._cat_atual
        ]
        cols = 4
        for i, op in enumerate(ops):
            frm = ctk.CTkFrame(self.frame_ops, corner_radius=8)
            frm.grid(row=i // cols, column=i % cols, padx=5, pady=5, sticky="nsew")
            self.frame_ops.columnconfigure(i % cols, weight=1)

            btn = ctk.CTkButton(
                frm,
                text=f"{op['simbolo']}\n{op['nome']}",
                font=("Arial", 12),
                height=54,
                corner_radius=8,
                command=lambda o=op: self._calcular(o),
            )
            btn.pack(fill="both", expand=True)
            self._btn_ops[op["id"]] = btn

        # Reaplica destaque se já havia operação selecionada
        if self._op_atual and self._op_atual in self._btn_ops:
            self._btn_ops[self._op_atual].configure(
                fg_color=("#1e40af", "#1e3a8a")
            )

    # ── filtra categoria ──────────────────────────────────────────
    def _filtrar_cat(self, chave: str | None, nome: str):
        self._cat_atual = chave
        for n, b in self._btn_cats.items():
            b.configure(fg_color=("gray75", "gray30"))
        self._btn_cats[nome].configure(fg_color=("#2563EB", "#1d4ed8"))
        self._render_ops()

    # ── executa cálculo ───────────────────────────────────────────
    def _calcular(self, op: dict):
        self._op_atual = op["id"]
        # Destaca botão ativo
        for b in self._btn_ops.values():
            b.configure(fg_color=("gray75", "gray30"))
        if op["id"] in self._btn_ops:
            self._btn_ops[op["id"]].configure(fg_color=("#1e40af", "#1e3a8a"))

        set_a = self._parse(self.entry_a.get())
        set_b = self._parse(self.entry_b.get())
        resultado_str, teoria_str = calcular(op["id"], set_a, set_b)

        self.lbl_resultado.configure(
            text=f"  {op['simbolo']}  =  {resultado_str}"
        )
        self.lbl_formula.configure(text=op["formula"])

        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", teoria_str)
        self.textbox.configure(state="disabled")

    # ── converte string → set ─────────────────────────────────────
    @staticmethod
    def _parse(texto: str) -> set:
        if not texto.strip():
            return set()
        return {item.strip() for item in texto.split(",") if item.strip()}


# ──────────────────────────────────────────────
#  Entry point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    app = App()
    app.mainloop()
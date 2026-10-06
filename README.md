# ROV-MB — Gerenciamento de Projetos

Documentação acadêmica do **Projeto ROV-MB — Aquisição, Integração e Validação de um ROV Modular**, desenvolvida no Curso GDP 2026 — Gerenciamento de Projetos, com orientação do Cmdt Huback.

**Site publicado (GitHub Pages):** https://ighorribeiro.github.io/Projeto_GDP/

> **Premissa do projeto:** a obtenção contratual (pesquisa de mercado, definição da solução e contratação) é considerada concluída. O projeto não possui conteúdo contratual e compreende somente o recebimento, a integração, a validação e a capacitação.

O repositório registra a cadeia documental do projeto:

```text
Tarefa 1 — TAP  →  Tarefa 2 — EAP + Dicionário  →  Tarefa 3 — Gerenciamento da Qualidade  →  Documentação HTML
```

## Conteúdo

| Tarefa | Documento final | Observação |
|---|---|---|
| Tarefa 1 — TAP | [`entregas/tarefa-1-revisada.md`](entregas/tarefa-1-revisada.md) · [`.docx`](entregas/tarefa-1-revisada.docx) | **Versão consolidada** (fonte-base do escopo), sem conteúdo contratual, com registro das alterações de consistência A1 a A25. A versão original está preservada em [`tarefas/Tarefa 01 - TAP.docx`](tarefas/Tarefa%2001%20-%20TAP.docx). |
| Tarefa 2 — EAP + Dicionário | [`entregas/tarefa-2-revisada.md`](entregas/tarefa-2-revisada.md) · [`.docx`](entregas/tarefa-2-revisada.docx) | **Versão oficial (congelada)**, reconstruída após a orientação. A versão original está preservada em [`tarefas/Tarefa 02 - EAP e Dicionário.docx`](tarefas/Tarefa%2002%20-%20EAP%20e%20Dicion%C3%A1rio.docx). |
| Tarefa 3 — Gerenciamento da Qualidade | [`entregas/tarefa-3-qualidade.md`](entregas/tarefa-3-qualidade.md) · [`.docx`](entregas/tarefa-3-qualidade.docx) | Matriz de Rastreabilidade de Requisitos e Matriz da Qualidade. Dados em [`matriz-rastreabilidade.csv`](entregas/matriz-rastreabilidade.csv) e [`matriz-qualidade.csv`](entregas/matriz-qualidade.csv). |
| Auditoria cruzada | [`entregas/auditoria-cruzada.md`](entregas/auditoria-cruzada.md) | Verificação TAP → EAP → Dicionário → Rastreabilidade → Qualidade, com conflitos registrados. |
| Documentação HTML | [`index.html`](index.html) | Registro acadêmico interativo das três tarefas. |

### EAP revisada (versão oficial)

```text
PROJETO ROV-MB
├── 1. GERENCIAMENTO DO PROJETO
├── 2. NECESSIDADES E REQUISITOS
├── 3. RECEBIMENTO DO ROV
│   ├── 3.1 TAF
│   ├── 3.2 TAM
│   ├── 3.3 Aprovação das planilhas de testes
│   └── 3.4 Recebimento de sobressalentes e consumíveis
└── 4. CAPACITAÇÃO
    ├── 4.1 Cursos e piloto operacional
    └── 4.2 Documentação técnica e gestão do conhecimento
```

Mudanças determinadas pelo orientador em relação à EAP original (7 elementos de primeiro nível e 23 pacotes): Fornecedor eliminado; V&V/Testes absorvido pelo Recebimento do ROV; Encerramento absorvido pelo Gerenciamento do Projeto; Gerenciamento consolidado em um único pacote; Capacitação com documentação técnica e gestão do conhecimento. O detalhamento está no Dicionário e no histórico da Tarefa 2 revisada.

## Estrutura do repositório

```text
.
├── index.html                  # documentação HTML (arquivo único, CSS e JS embutidos)
├── README.md
├── .nojekyll                   # publica os arquivos sem processamento Jekyll no GitHub Pages
├── CLAUDE.md                   # regras de trabalho do repositório
├── entregas/                   # versões finais das Tarefas 2 e 3
│   ├── tarefa-1-revisada.md / .docx   # TAP consolidado
│   ├── tarefa-2-revisada.md / .docx
│   ├── tarefa-3-qualidade.md / .docx
│   ├── matriz-rastreabilidade.csv
│   ├── matriz-qualidade.csv
│   ├── auditoria-cruzada.md
│   └── eap-revisada.png        # diagrama da EAP revisada
├── tarefas/                    # documentos originais (preservados)
├── material de apoio/          # material da disciplina
└── skills/                     # instruções de execução de cada tarefa
```

## Visualização local

O `index.html` não depende de servidor, internet ou bibliotecas externas: basta abri-lo no navegador (duplo clique ou arrastar para a janela do navegador).

Para que os links relativos para os documentos (`.md`, `.csv`, `.docx`, `.pdf`) se comportem como no GitHub Pages, é possível usar um servidor local simples:

```bash
python3 -m http.server 8000
# abrir http://localhost:8000
```

## Publicação no GitHub Pages

O site é servido diretamente da raiz da branch `main` (`index.html`), sem etapa de build:

- **Endereço:** https://ighorribeiro.github.io/Projeto_GDP/
- **Configuração (uma única vez):** **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `/ (root)` → Save**.
- A cada novo push na `main`, o GitHub Pages republica o site automaticamente em cerca de um minuto.

O arquivo `.nojekyll` faz o GitHub Pages servir os arquivos como estão, de modo que os links do `index.html` para `entregas/` e `tarefas/` funcionem também no site publicado.

## Observações de consistência

- **C1 — obtenção contratual (resolvido).** A EAP revisada não contém estudo de mercado, seleção de fornecedor nem contratação (decisão do orientador). Para eliminar a divergência com o TAP, a obtenção contratual passou a ser premissa concluída e o TAP foi consolidado em [`entregas/tarefa-1-revisada.md`](entregas/tarefa-1-revisada.md), com cada alteração registrada (A1 a A25). Os 17 requisitos de alto nível do TAP consolidado são todos rastreados na Tarefa 3.
- As demais observações (C2 a C6) estão registradas em [`entregas/auditoria-cruzada.md`](entregas/auditoria-cruzada.md) e na seção Histórico do `index.html`.

## Regras de manutenção

- O TAP consolidado é a fonte do escopo; a Tarefa 2 deve permanecer compatível com ele; a Tarefa 3 usa somente os códigos da EAP revisada.
- O `index.html` representa os documentos finais de `entregas/` e não constitui nova versão do projeto. Qualquer alteração nas tarefas deve ser feita primeiro nos documentos de `entregas/` e então refletida no HTML, nos CSV e na auditoria.
- Conflitos entre tarefas são identificados e registrados antes de qualquer correção; nenhuma tarefa anterior é alterada silenciosamente.

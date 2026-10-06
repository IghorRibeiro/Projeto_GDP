# ROV-MB — Gerenciamento de Projetos

Documentação acadêmica do **Projeto ROV-MB — Aquisição, Integração e Validação de um ROV Modular**, desenvolvida no Curso GDP 2026 — Gerenciamento de Projetos, com orientação do Cmdt Huback.

O repositório registra a cadeia documental do projeto:

```text
Tarefa 1 — TAP  →  Tarefa 2 — EAP + Dicionário  →  Tarefa 3 — Gerenciamento da Qualidade  →  Documentação HTML
```

## Conteúdo

| Tarefa | Documento final | Observação |
|---|---|---|
| Tarefa 1 — TAP | [`tarefas/Tarefa 01 - TAP.docx`](tarefas/Tarefa%2001%20-%20TAP.docx) | Fonte-base do escopo. Não alterada. |
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

1. No GitHub, abra **Settings → Pages**.
2. Em **Build and deployment**, selecione **Source: Deploy from a branch**.
3. Escolha a branch (por exemplo, `main`) e a pasta **/ (root)** e salve.
4. Após a publicação, a documentação fica disponível em `https://<usuário>.github.io/<repositório>/`.

O arquivo `.nojekyll` faz o GitHub Pages servir os arquivos como estão, de modo que os links do `index.html` para `entregas/` e `tarefas/` funcionem também no site publicado.

## Observações de consistência

- **C1 — obtenção contratual.** Por decisão do orientador, a EAP revisada não contém estudo de mercado, seleção de fornecedor nem contratação. O TAP ainda descreve esses itens (objetivo 2, entregas 5 e 7, requisito 16, marcos M-04 a M-06, seção 13). O TAP **não foi alterado**; a correção está proposta como alteração de consistência, e o requisito 16 não é rastreado na Tarefa 3.
- As demais observações (C2 a C6) estão registradas em [`entregas/auditoria-cruzada.md`](entregas/auditoria-cruzada.md) e na seção Histórico do `index.html`.

## Regras de manutenção

- O TAP é a fonte do escopo; a Tarefa 2 deve permanecer compatível com ele; a Tarefa 3 usa somente os códigos da EAP revisada.
- O `index.html` representa os documentos finais de `entregas/` e não constitui nova versão do projeto. Qualquer alteração nas tarefas deve ser feita primeiro nos documentos de `entregas/` e então refletida no HTML, nos CSV e na auditoria.
- Conflitos entre tarefas são identificados e registrados antes de qualquer correção; nenhuma tarefa anterior é alterada silenciosamente.

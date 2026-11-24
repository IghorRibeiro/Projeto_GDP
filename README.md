# ROV-MB — Gerenciamento de Projetos

Documentação acadêmica do **Projeto ROV-MB — Recebimento, Integração e Validação de um ROV Modular** (Grupo I), Curso GDP 2026 — Gerenciamento de Projetos, professor CMG (RM1-EN) Gian Karlo Huback Macedo de Almeida.

> **Premissa do projeto:** não há conteúdo de aquisição ou contratação. O projeto compreende o recebimento, a integração, a validação do ROV e a capacitação do pessoal.

## Conteúdo

| Documento | Arquivo |
|---|---|
| **Documento único (Tarefas 1, 2 e 3)**, incorporando as correções do Cmdt Huback | [`entregas/GDP - Grupo I - ROV-MB - Tarefas 1 a 3.docx`](entregas/) · [`.pdf`](entregas/) |
| Versões enviadas e revisadas pelo Cmdt Huback (registro) | [`tarefas/revisao-huback/`](tarefas/revisao-huback/) |
| Documentos originais das Tarefas 1 e 2 | [`tarefas/`](tarefas/) |

> O site (`index.html`) ainda reflete a versão anterior e será atualizado a partir do documento único.

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

Mudanças determinadas pelo orientador em relação à EAP original (7 elementos de primeiro nível e 23 pacotes): Fornecedor eliminado; V&V/Testes absorvido pelo Recebimento do ROV; Encerramento absorvido pelo Gerenciamento do Projeto; Gerenciamento consolidado em um único pacote; Capacitação com documentação técnica e gestão do conhecimento. O detalhamento está no Dicionário da EAP (documento único).

## Estrutura do repositório

```text
.
├── index.html                  # documentação HTML (a atualizar)
├── README.md
├── .nojekyll
├── CLAUDE.md
├── entregas/                   # documento único das Tarefas 1 a 3 (.docx e .pdf)
├── tarefas/                    # originais e revisao-huback/
├── material de apoio/
└── skills/
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

## Regras de manutenção

- O TAP consolidado é a fonte do escopo; a Tarefa 2 deve permanecer compatível com ele; a Tarefa 3 usa somente os códigos da EAP revisada.
- O `index.html` representa os documentos finais de `entregas/` e não constitui nova versão do projeto. Qualquer alteração nas tarefas deve ser feita primeiro nos documentos de `entregas/` e então refletida no HTML, nos CSV e na auditoria.
- Conflitos entre tarefas são identificados e registrados antes de qualquer correção; nenhuma tarefa anterior é alterada silenciosamente.

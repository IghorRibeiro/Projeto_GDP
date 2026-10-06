# Auditoria cruzada — TAP → EAP → Dicionário → Rastreabilidade → Qualidade

**Projeto:** ROV-MB — Aquisição, Integração e Validação de um ROV Modular  
**Escopo:** Fase 8 — verificação da cadeia documental TAP consolidado → EAP → Dicionário → Rastreabilidade → Qualidade e dos arquivos publicados.

> Resultado: **todas as verificações aprovadas** (51/51). As verificações abaixo foram executadas de forma automatizada sobre os dados das tarefas e sobre os arquivos gerados (`entregas/*.md`, `entregas/*.csv`, `index.html`).

## Verificações

| # | Grupo | Verificação | Resultado | Evidência |
|---|---|---|---|---|
| 1 | TAP consolidado | Registro de alterações fiel: todo texto original citado existe no DOCX original | Aprovado | 25/25 conferidas; divergentes: nenhuma |
| 2 | TAP consolidado | Nenhuma alteração silenciosa: todo item é idêntico ao original ou consta do registro de alterações | Aprovado | 102 itens verificados; sem correspondência: nenhum |
| 3 | TAP consolidado | Sem conteúdo contratual (exceto a própria premissa e o título do projeto) | Aprovado | ocorrências: nenhuma |
| 4 | TAP consolidado | Premissa de obtenção contratual concluída explicitada | Aprovado | seção 1, 3º parágrafo |
| 5 | EAP | Estrutura final com os 10 elementos previstos | Aprovado | 1, 2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2 |
| 6 | EAP | Relação pai-filho válida (todo pai existe; códigos coerentes com o pai) | Aprovado | verificado para os 10 elementos |
| 7 | EAP | Nenhum elemento com filho único (Mandamento IX) | Aprovado | 3: 4 filho(s); 4: 2 filho(s) |
| 8 | EAP | Gerenciamento do Projeto é um único pacote, sem subpacotes por grupo de processo | Aprovado | 1 sem filhos |
| 9 | EAP | Dicionário do pacote 1 contempla os cinco grupos de processo e o PMBOK | Aprovado | termos presentes na especificação |
| 10 | EAP | Recebimento do ROV = TAF, TAM, Aprovação das planilhas de testes, Recebimento de sobressalentes e consumíveis | Aprovado | TAF · TAM · Aprovação das planilhas de testes · Recebimento de sobressalentes e consumíveis |
| 11 | EAP | Capacitação contempla operadores, mantenedores, documentação técnica, manuais (operação, manutenção, técnico) e gestão do conhecimento | Aprovado | operadores, mantenedores, documentação técnica, manuais de operação, manuais de manutenção, manual técnico, gestão do conhecimento |
| 12 | EAP | Nenhum elemento denominado Fornecedor, V&V/Testes, Encerramento ou grupo de processo | Aprovado | nenhum |
| 13 | EAP | Nenhum conteúdo do antigo bloco Fornecedor reintroduzido no Dicionário (busca por termos) | Aprovado | ocorrências: nenhuma |
| 14 | EAP | Todos os elementos com especificação e critério de aceitação | Aprovado | 10/10 |
| 15 | EAP | Nomes orientados à entrega (nenhum iniciado por verbo) | Aprovado | nenhum |
| 16 | Correspondência | Os 23 pacotes originais possuem destino registrado uma única vez | Aprovado | 23 registros |
| 17 | Correspondência | Todos os destinos citados existem na EAP revisada | Aprovado | 1, 2, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2 |
| 18 | Correspondência | Somente o antigo 3.1 e a parcela de contratação de 3.3 foram eliminados | Aprovado | 3.1 (eliminado); 3.3 (parcialmente) |
| 19 | TAP → EAP | Entregas-chave 1–10 do TAP consolidado cobertas | Aprovado | 10/10 |
| 20 | TAP → EAP | Objetivos 1–7 do TAP consolidado cobertos | Aprovado | 7/7 |
| 21 | TAP → EAP | Restrições 1–9 do TAP observadas | Aprovado | 9/9 |
| 22 | TAP → EAP | Conflito C1 (obtenção contratual) resolvido pela consolidação do TAP | Aprovado | Resolvido — TAP consolidado |
| 23 | TAP → EAP | Códigos citados na validação existem na EAP revisada | Aprovado | 1, 2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2 |
| 24 | Rastreabilidade | IDs únicos e sequenciais | Aprovado | RQ-01 a RQ-30 |
| 25 | Rastreabilidade | Todo requisito possui origem no TAP | Aprovado | 30/30 |
| 26 | Rastreabilidade | Nenhum código EAP inexistente ou da EAP original | Aprovado | 1, 2, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2 |
| 27 | Rastreabilidade | Todos os pacotes de trabalho possuem requisito rastreado | Aprovado | 1: 3; 2: 4; 3.1: 7; 3.2: 7; 3.3: 2; 3.4: 1; 4.1: 3; 4.2: 3 |
| 28 | Rastreabilidade | Stakeholders pertencem à lista do TAP | Aprovado | Autoridades de segurança e áreas de teste, Distritos e grupamentos, Engenharia e manutenção, Força de Submarinos, Logística e cadeia de suprimento, Mergulhadores e especialistas SAR, Militares especializados, Patrocinador do projeto, Áreas de ciência, tecnologia e inovação |
| 29 | Rastreabilidade | Prioridade, tipo e status com valores válidos | Aprovado | prioridade 1: 29; prioridade 2: 1; status NI: 30 |
| 30 | Rastreabilidade | Nenhuma descrição duplicada | Aprovado | 30 descrições distintas |
| 31 | Rastreabilidade | Todos os requisitos de alto nível do TAP consolidado rastreados | Aprovado | 17/17 rastreados |
| 32 | Rastreabilidade | Mapa TAP → RQ coerente com a coluna Origem | Aprovado | verificado |
| 33 | Qualidade | Matriz da Qualidade completa (9 campos em todas as linhas) | Aprovado | 30 linhas |
| 34 | Qualidade | Cada requisito da Matriz da Qualidade existe na Matriz de Rastreabilidade com a mesma redação | Aprovado | mesma fonte por ID (verificado nos CSV abaixo) |
| 35 | Qualidade | Metas identificadas como do TAP ou como proposta de controle | Aprovado | (TAP)/referência do TAP: 18; proposta de controle: 12 |
| 36 | Qualidade | Indicador distinto do requisito e da meta | Aprovado | 30/30 |
| 37 | Qualidade | Quem mede e Responsável são funções do TAP (gerente, Força de Submarinos, frentes de testes/capacitação, partes interessadas) | Aprovado | Engenharia e manutenção, Equipe de testes do projeto, Força de Submarinos, Frente de capacitação do projeto, Gerente do projeto, Logística e cadeia de suprimento, Mergulhadores e especialistas SAR, Militares especializados, Patrocinador do projeto |
| 38 | Qualidade | Nenhum conteúdo de fornecedor reintroduzido nas matrizes (busca por termos) | Aprovado | ocorrências: nenhuma |
| 39 | Qualidade | Nenhum conteúdo do exemplo de calçados | Aprovado | ocorrências: nenhuma |
| 40 | Qualidade | Nenhuma seção V&V ou Encerramento nas matrizes; TAF/TAM sob 3 | Aprovado | 3.1 (TAF): 7; 3.2 (TAM): 7 |
| 41 | Arquivos | CSV de rastreabilidade idêntico aos dados | Aprovado | 30 linhas |
| 42 | Arquivos | CSV da qualidade idêntico aos dados e com a mesma redação de requisito | Aprovado | 30 linhas |
| 43 | Arquivos | tarefa-1-revisada.md contém o TAP consolidado completo e o registro de alterações | Aprovado | 17 requisitos · 25 alterações |
| 44 | Arquivos | tarefa-2-revisada.md contém todos os elementos do Dicionário | Aprovado | 10/10 |
| 45 | Arquivos | tarefa-3-qualidade.md contém as duas matrizes completas | Aprovado | 30 × 2 |
| 46 | Arquivos | index.html: dados embutidos idênticos às matrizes e ao Dicionário | Aprovado | JSON comparado campo a campo |
| 47 | Arquivos | index.html: árvore da EAP reflete exatamente a EAP final | Aprovado | 1, 2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2 |
| 48 | Arquivos | index.html: 30 linhas em cada matriz | Aprovado | 60 linhas (30 + 30) |
| 49 | Arquivos | index.html: todos os links relativos apontam para arquivos existentes | Aprovado | 21 links; ausentes: nenhum |
| 50 | Arquivos | index.html: todas as âncoras internas existem | Aprovado | 8 âncoras; ausentes: nenhuma |
| 51 | Preservação | Tarefas originais, material de apoio, skills e CLAUDE.md sem alteração | Aprovado | git status limpo para esses caminhos |

## Itens verificados pela pergunta da auditoria

- **Nenhum requisito sem origem:** todos os 30 requisitos indicam a seção do TAP consolidado de origem.
- **Nenhum código EAP inexistente:** somente os códigos 1, 2, 3.1, 3.2, 3.3, 3.4, 4.1 e 4.2 são usados nas matrizes.
- **Nenhuma duplicidade:** cada conteúdo da EAP original tem um único destino; nenhum requisito repetido.
- **Nenhuma contradição:** restrições, objetivos e partes interessadas do TAP não foram alterados.
- **Nenhuma reintrodução de elementos eliminados:** sem Fornecedor, V&V ou Encerramento independentes; busca de termos sem ocorrências na EAP e nas matrizes.
- **Nenhuma alteração silenciosa do escopo:** a supressão da obtenção contratual decorre da decisão do orientador (D2) e da decisão do responsável pelo projeto (C1); o TAP consolidado registra cada alteração (A1 a A25) e a versão original está preservada.

## Conflitos e observações registrados

| ID | Tipo | Assunto | Situação | Tratamento |
|---|---|---|---|---|
| C1 | Conflito TAP × decisão do orientador | Obtenção contratual (antigo bloco Fornecedor) | Resolvido — TAP consolidado | TAP consolidado em entregas/tarefa-1-revisada.md, com premissa explícita e registro das alterações A1 a A25; versão original preservada em tarefas/Tarefa 01 - TAP.docx. Com a supressão do antigo requisito 16, os 17 requisitos de alto nível do TAP consolidado são todos rastreados na Tarefa 3. |
| C2 | Observação de interpretação | Sequência dos marcos M-05 a M-07 | Registrado — não exige alteração | Sem alteração. O cronograma detalhado, no pacote 1, deverá refinar a ordem dos marcos. |
| C3 | Observação | Consumíveis no pacote 3.4 | Registrado — não exige alteração | Mantido conforme a orientação. Sem alteração do TAP. |
| C4 | Observação de forma | Numeração dos indicadores-chave | Resolvido — TAP consolidado | Corrigida para 10.1 a 10.5 no TAP consolidado (alteração A20). |
| C5 | Limitação de fonte | Registro da reunião com o orientador | Registrado | O histórico usa exclusivamente esse registro, sem justificativas adicionais. |
| C6 | Limitação de fonte | Enunciado e modelo da Tarefa 3 | Registrado | Matrizes construídas com os campos definidos; nenhum conteúdo do exemplo de calçados utilizado. |

**Pendências que dependem de alteração das fontes:** nenhuma. O conflito C1 foi resolvido pela consolidação do TAP (`entregas/tarefa-1-revisada.md`); as demais observações não exigem alteração.


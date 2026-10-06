# Auditoria cruzada — TAP → EAP → Dicionário → Rastreabilidade → Qualidade

**Projeto:** ROV-MB — Aquisição, Integração e Validação de um ROV Modular  
**Escopo:** Fase 8 — verificação da cadeia documental antes da documentação HTML, repetida após a geração dos arquivos finais.

> Resultado: **todas as verificações aprovadas** (46/46). As verificações abaixo foram executadas de forma automatizada sobre os dados das tarefas e sobre os arquivos gerados (`entregas/*.md`, `entregas/*.csv`, `index.html`).

## Verificações

| # | Grupo | Verificação | Resultado | Evidência |
|---|---|---|---|---|
| 1 | EAP | Estrutura final com os 10 elementos previstos | Aprovado | 1, 2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2 |
| 2 | EAP | Relação pai-filho válida (todo pai existe; códigos coerentes com o pai) | Aprovado | verificado para os 10 elementos |
| 3 | EAP | Nenhum elemento com filho único (Mandamento IX) | Aprovado | 3: 4 filho(s); 4: 2 filho(s) |
| 4 | EAP | Gerenciamento do Projeto é um único pacote, sem subpacotes por grupo de processo | Aprovado | 1 sem filhos |
| 5 | EAP | Dicionário do pacote 1 contempla os cinco grupos de processo e o PMBOK | Aprovado | termos presentes na especificação |
| 6 | EAP | Recebimento do ROV = TAF, TAM, Aprovação das planilhas de testes, Recebimento de sobressalentes e consumíveis | Aprovado | TAF · TAM · Aprovação das planilhas de testes · Recebimento de sobressalentes e consumíveis |
| 7 | EAP | Capacitação contempla operadores, mantenedores, documentação técnica, manuais (operação, manutenção, técnico) e gestão do conhecimento | Aprovado | operadores, mantenedores, documentação técnica, manuais de operação, manuais de manutenção, manual técnico, gestão do conhecimento |
| 8 | EAP | Nenhum elemento denominado Fornecedor, V&V/Testes, Encerramento ou grupo de processo | Aprovado | nenhum |
| 9 | EAP | Nenhum conteúdo do antigo bloco Fornecedor reintroduzido no Dicionário (busca por termos) | Aprovado | ocorrências: nenhuma |
| 10 | EAP | Todos os elementos com especificação e critério de aceitação | Aprovado | 10/10 |
| 11 | EAP | Nomes orientados à entrega (nenhum iniciado por verbo) | Aprovado | nenhum |
| 12 | Correspondência | Os 23 pacotes originais possuem destino registrado uma única vez | Aprovado | 23 registros |
| 13 | Correspondência | Todos os destinos citados existem na EAP revisada | Aprovado | 1, 2, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2 |
| 14 | Correspondência | Somente o antigo 3.1 e a parcela de contratação de 3.3 foram eliminados | Aprovado | 3.1 (eliminado); 3.3 (parcialmente) |
| 15 | TAP → EAP | Entregas-chave 1–11 do TAP avaliadas | Aprovado | fora da EAP: 5 |
| 16 | TAP → EAP | Objetivos 1–8 do TAP avaliados | Aprovado | fora da EAP: 2 |
| 17 | TAP → EAP | Restrições 1–9 do TAP observadas | Aprovado | 9/9 |
| 18 | TAP → EAP | Itens do TAP fora da EAP restritos à obtenção contratual (C1) | Aprovado | entrega 5 e objetivo 2 (C1); partes das entregas 7 e objetivo 3 |
| 19 | TAP → EAP | Códigos citados na validação existem na EAP revisada | Aprovado | 1, 2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2 |
| 20 | Rastreabilidade | IDs únicos e sequenciais | Aprovado | RQ-01 a RQ-30 |
| 21 | Rastreabilidade | Todo requisito possui origem no TAP | Aprovado | 30/30 |
| 22 | Rastreabilidade | Nenhum código EAP inexistente ou da EAP original | Aprovado | 1, 2, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2 |
| 23 | Rastreabilidade | Todos os pacotes de trabalho possuem requisito rastreado | Aprovado | 1: 3; 2: 4; 3.1: 7; 3.2: 7; 3.3: 2; 3.4: 1; 4.1: 3; 4.2: 3 |
| 24 | Rastreabilidade | Stakeholders pertencem à lista do TAP | Aprovado | Autoridades de segurança e áreas de teste, Distritos e grupamentos, Engenharia e manutenção, Força de Submarinos, Logística e cadeia de suprimento, Mergulhadores e especialistas SAR, Militares especializados, Patrocinador do projeto, Áreas de ciência, tecnologia e inovação |
| 25 | Rastreabilidade | Prioridade, tipo e status com valores válidos | Aprovado | prioridade 1: 29; prioridade 2: 1; status NI: 30 |
| 26 | Rastreabilidade | Nenhuma descrição duplicada | Aprovado | 30 descrições distintas |
| 27 | Rastreabilidade | Requisitos de alto nível do TAP rastreados (exceto o 16 — C1) | Aprovado | 17/18 rastreados; requisito 16 sem pacote (C1) |
| 28 | Rastreabilidade | Mapa TAP → RQ coerente com a coluna Origem | Aprovado | verificado |
| 29 | Qualidade | Matriz da Qualidade completa (9 campos em todas as linhas) | Aprovado | 30 linhas |
| 30 | Qualidade | Cada requisito da Matriz da Qualidade existe na Matriz de Rastreabilidade com a mesma redação | Aprovado | mesma fonte por ID (verificado nos CSV abaixo) |
| 31 | Qualidade | Metas identificadas como do TAP ou como proposta de controle | Aprovado | (TAP)/referência do TAP: 18; proposta de controle: 12 |
| 32 | Qualidade | Indicador distinto do requisito e da meta | Aprovado | 30/30 |
| 33 | Qualidade | Quem mede e Responsável são funções do TAP (gerente, Força de Submarinos, frentes de testes/capacitação, partes interessadas) | Aprovado | Engenharia e manutenção, Equipe de testes do projeto, Força de Submarinos, Frente de capacitação do projeto, Gerente do projeto, Logística e cadeia de suprimento, Mergulhadores e especialistas SAR, Militares especializados, Patrocinador do projeto |
| 34 | Qualidade | Nenhum conteúdo de fornecedor reintroduzido nas matrizes (busca por termos) | Aprovado | ocorrências: nenhuma |
| 35 | Qualidade | Nenhum conteúdo do exemplo de calçados | Aprovado | ocorrências: nenhuma |
| 36 | Qualidade | Nenhuma seção V&V ou Encerramento nas matrizes; TAF/TAM sob 3 | Aprovado | 3.1 (TAF): 7; 3.2 (TAM): 7 |
| 37 | Arquivos | CSV de rastreabilidade idêntico aos dados | Aprovado | 30 linhas |
| 38 | Arquivos | CSV da qualidade idêntico aos dados e com a mesma redação de requisito | Aprovado | 30 linhas |
| 39 | Arquivos | tarefa-2-revisada.md contém todos os elementos do Dicionário | Aprovado | 10/10 |
| 40 | Arquivos | tarefa-3-qualidade.md contém as duas matrizes completas | Aprovado | 30 × 2 |
| 41 | Arquivos | index.html: dados embutidos idênticos às matrizes e ao Dicionário | Aprovado | JSON comparado campo a campo |
| 42 | Arquivos | index.html: árvore da EAP reflete exatamente a EAP final | Aprovado | 1, 2, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 4.2 |
| 43 | Arquivos | index.html: 30 linhas em cada matriz | Aprovado | 60 linhas (30 + 30) |
| 44 | Arquivos | index.html: todos os links relativos apontam para arquivos existentes | Aprovado | 19 links; ausentes: nenhum |
| 45 | Arquivos | index.html: todas as âncoras internas existem | Aprovado | 8 âncoras; ausentes: nenhuma |
| 46 | Preservação | Tarefas originais, material de apoio, skills e CLAUDE.md sem alteração | Aprovado | git status limpo para esses caminhos |

## Itens verificados pela pergunta da auditoria

- **Nenhum requisito sem origem:** todos os 30 requisitos indicam a seção do TAP de origem.
- **Nenhum código EAP inexistente:** somente os códigos 1, 2, 3.1, 3.2, 3.3, 3.4, 4.1 e 4.2 são usados nas matrizes.
- **Nenhuma duplicidade:** cada conteúdo da EAP original tem um único destino; nenhum requisito repetido.
- **Nenhuma contradição:** restrições, objetivos e partes interessadas do TAP não foram alterados.
- **Nenhuma reintrodução de elementos eliminados:** sem Fornecedor, V&V ou Encerramento independentes; busca de termos sem ocorrências na EAP e nas matrizes.
- **Nenhuma alteração silenciosa do escopo:** a única redução de escopo (obtenção contratual) decorre da decisão do orientador e está registrada no conflito C1, sem alteração do TAP.

## Conflitos e observações registrados

| ID | Tipo | Assunto | Situação | Tratamento |
|---|---|---|---|---|
| C1 | Conflito TAP × decisão do orientador | Obtenção contratual (antigo bloco Fornecedor) | Aberto — depende de alteração da fonte (Tarefa 1) | TAP preservado sem alteração. Proposta de alteração de consistência do TAP, a submeter pelo controle integrado de mudanças (pacote 1) à aprovação da Força de Submarinos: (a) registrar a obtenção contratual como processo institucional externo ao escopo da EAP; (b) ajustar o objetivo 2, as entregas 5 e 7, os marcos M-04 a M-06 e a seção 13; (c) reavaliar o requisito 16, que, na redação atual, é critério de seleção de fornecedor. Na Tarefa 3, o requisito 16 não é rastreado a pacote da EAP. |
| C2 | Observação de interpretação | Sequência dos marcos M-07 a M-09 | Registrado — não exige alteração | Sem alteração do TAP. O cronograma detalhado, no pacote 1, deverá refinar a ordem dos marcos. |
| C3 | Observação | Consumíveis no pacote 3.4 | Registrado — não exige alteração | Mantido conforme a orientação. Sem alteração do TAP. |
| C4 | Observação de forma | Numeração dos indicadores-chave | Registrado — não exige alteração | Indicadores citados com a numeração original (8.1 a 8.5). |
| C5 | Limitação de fonte | Registro da reunião com o orientador | Registrado | O histórico usa exclusivamente esse registro, sem justificativas adicionais. |
| C6 | Limitação de fonte | Enunciado e modelo da Tarefa 3 | Registrado | Matrizes construídas com os campos definidos; nenhum conteúdo do exemplo de calçados utilizado. |

**Pendência que depende de alteração da fonte:** C1 — o TAP (Tarefa 1) ainda descreve estudo de mercado, solução de fornecimento, contratação e priorização de fornecedores nacionais (objetivo 2, entregas 5 e 7, requisito 16, marcos M-04 a M-06, seção 13). A correção pertence ao TAP e foi apenas proposta, conforme a regra de não alterar silenciosamente uma tarefa anterior.


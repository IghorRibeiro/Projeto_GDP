# Tarefa 3 — Gerenciamento da Qualidade

**Projeto:** ROV-MB — Aquisição, Integração e Validação de um ROV Modular  
**Disciplina:** Curso GDP 2026 — Gerenciamento de Projetos · Gerenciamento da Qualidade do Projeto  
**Entregas:** Matriz de Rastreabilidade de Requisitos · Matriz da Qualidade

> **Base documental:** Tarefa 1 — TAP (origem dos requisitos) e Tarefa 2 — EAP e Dicionário **revisados e congelados** ([`entregas/tarefa-2-revisada.md`](tarefa-2-revisada.md)). Nenhum código da EAP original é utilizado. A EAP não foi alterada para facilitar as matrizes.

Arquivos de dados: [`matriz-rastreabilidade.csv`](matriz-rastreabilidade.csv) · [`matriz-qualidade.csv`](matriz-qualidade.csv)

## 1. Cadeia documental

```text
TAP (Tarefa 1)            → necessidade, objetivos, requisitos, partes interessadas e limites
EAP + Dicionário (Tarefa 2) → organização do escopo em pacotes e definição das entregas
Matriz de Rastreabilidade → requisito ↔ pacote da EAP
Matriz da Qualidade       → indicador, meta, medição e resposta a não conformidades
```

Relação adotada em cada linha: **Requisito → Código EAP → Indicador → Meta → Técnica de medição → Resposta**.

## 2. EAP de referência (códigos válidos)

| Código | Elemento | Tipo | Requisitos rastreados |
|---|---|---|---|
| 1 | Gerenciamento do Projeto | Pacote de trabalho | RQ-01, RQ-02, RQ-03 |
| 2 | Necessidades e Requisitos | Pacote de trabalho | RQ-04, RQ-05, RQ-06, RQ-07 |
| 3 | Recebimento do ROV | Elemento de agregação | — (agregação: ver filhos) |
| 3.1 | TAF | Pacote de trabalho | RQ-08, RQ-09, RQ-10, RQ-11, RQ-12, RQ-13, RQ-14 |
| 3.2 | TAM | Pacote de trabalho | RQ-15, RQ-16, RQ-17, RQ-18, RQ-19, RQ-20, RQ-21 |
| 3.3 | Aprovação das planilhas de testes | Pacote de trabalho | RQ-22, RQ-23 |
| 3.4 | Recebimento de sobressalentes e consumíveis | Pacote de trabalho | RQ-24 |
| 4 | Capacitação | Elemento de agregação | — (agregação: ver filhos) |
| 4.1 | Cursos e piloto operacional | Pacote de trabalho | RQ-25, RQ-26, RQ-27 |
| 4.2 | Documentação técnica e gestão do conhecimento | Pacote de trabalho | RQ-28, RQ-29, RQ-30 |

## 3. Convenções

- **ID** e **Origem no TAP** são colunas auxiliares acrescentadas aos campos do modelo para tornar explícita a ligação entre as duas matrizes e a origem de cada requisito.
- **Código EAP:** somente códigos da EAP revisada; vários requisitos podem apontar para o mesmo pacote. Requisitos de produto apontam para o pacote em que são comprovados (TAF ou TAM); requisitos de gerenciamento (registros, prazo e encerramento) apontam para o pacote 1; todos são definidos e aprovados na linha de base do pacote 2.
- **Prioridade:** 1 = imprescindível; 2 = desejável; 3 = opcional. Regra aplicada: prioridade 1 para requisitos da seção 3 do TAP (todos redigidos com “deverá”) e para itens que constam dos indicadores-chave (seção 10) ou dos critérios de término (seção 15); prioridade 2 para objetivo do TAP cujo não atendimento não impede o encerramento segundo a seção 15.
- **Tipo do requisito:** *Funcional* — capacidade ou comportamento que o sistema ROV deve executar; *Não funcional* — desempenho, condição ambiental, restrição, qualidade, suporte (treinamento, documentação, sobressalentes, manutenção) ou requisito de gerenciamento.
- **Status:** NI = Não Iniciada (projeto em planejamento; nenhuma execução é declarada).
- **Metas:** a marcação “(TAP)” indica valor ou condição extraída do TAP; “(proposta de controle)” indica parâmetro proposto nesta Tarefa 3 para tornar o requisito mensurável, não constante do TAP.
- **Quem mede / Responsável:** funções do TAP — gerente do projeto (seção 12), Força de Submarinos (autoridade de aprovação), frentes de testes e de capacitação integradas pelo gerente (seção 12) e partes interessadas da seção 8. A composição das frentes é definida na governança do projeto (pacote 1).
- **TAF e TAM** permanecem dentro do Recebimento do ROV (3.1 e 3.2); não há seção ou pacote de V&V nem de Encerramento.

## 4. Matriz de Rastreabilidade de Requisitos

| ID | Código EAP | Descrição | Stakeholder | Prioridade | Tipo do requisito | Status | Origem no TAP |
|------|------|---------------------------|------------|------|---------|------|---------------|
| RQ-01 | 1 | Registros de premissas, riscos, decisões e mudanças mantidos atualizados e desempenho do projeto reportado à Força de Submarinos | Patrocinador do projeto | 1 | Não funcional | NI | TAP, seção 12 |
| RQ-02 | 1 | MVP recebido, integrado e configurado dentro do prazo aprovado | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 10 (indicador 8.1); seção 11 (M-07) |
| RQ-03 | 1 | Encerramento formal aprovado pela Força de Submarinos, com pendências aceitas ou transferidas, lições aprendidas registradas e recomendação de continuidade | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 4 (entrega 11); seção 15 |
| RQ-04 | 2 | Necessidade operacional dos Distritos e grupamentos consolidada e mapa de usuários definido | Distritos e grupamentos | 1 | Não funcional | NI | TAP, seção 2 (objetivo 1); seção 4 (entrega 2); seção 11 (M-02) |
| RQ-05 | 2 | CONOPS e envelope operacional definidos e aprovados, com limites de correnteza, rebojo e visibilidade explicitados e interpretação do valor de 30 cm confirmada | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 4 (entrega 3); seção 6 (itens 3 a 5); seção 9 (risco 1.6); seção 11 (M-02 e M-03) |
| RQ-06 | 2 | Arquitetura modular especificada com núcleo, interfaces e critérios verificáveis, e configuração do MVP definida | Áreas de ciência, tecnologia e inovação | 1 | Não funcional | NI | TAP, seção 4 (entrega 6); seção 9 (risco 1.2) |
| RQ-07 | 2 | Requisitos rastreáveis aos critérios de aceitação e aprovados pela autoridade competente | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 3 (requisito 18); seção 6 (item 9) |
| RQ-08 | 3.1 | Arquitetura modular que permita a instalação ou substituição de aparatos e acessórios conforme a faina | Engenharia e manutenção | 1 | Não funcional | NI | TAP, seção 3 (requisito 1) |
| RQ-09 | 3.1 | MVP com câmera e iluminação, sem sonar e sem garra/manipulador | Força de Submarinos | 1 | Funcional | NI | TAP, seção 3 (requisito 8); seção 6 (item 6) |
| RQ-10 | 3.1 | Autonomia mínima de 2h30 em condição nominal de operação | Distritos e grupamentos | 1 | Não funcional | NI | TAP, seção 2 (objetivo 6); seção 3 (requisito 5); seção 10 (indicador 8.3) |
| RQ-11 | 3.1 | Umbilical com alcance mínimo de 50 m | Militares especializados | 1 | Não funcional | NI | TAP, seção 3 (requisito 6); seção 6 (item 7) |
| RQ-12 | 3.1 | Mecanismo de recuperação e gestão dinâmica do umbilical | Militares especializados | 1 | Funcional | NI | TAP, seção 3 (requisito 6); seção 6 (item 7) |
| RQ-13 | 3.1 | Produção e armazenamento de imagens e vídeos em 1080p a 30 fps e 4K a 15 fps | Distritos e grupamentos | 1 | Funcional | NI | TAP, seção 2 (objetivo 6); seção 3 (requisito 7) |
| RQ-14 | 3.1 | Comportamentos de proteção para situações de impacto, perda de comunicação ou carga anormal associada ao umbilical | Engenharia e manutenção | 1 | Funcional | NI | TAP, seção 3 (requisito 11); seção 9 (risco 1.5) |
| RQ-15 | 3.2 | Operação por uma única pessoa treinada, a partir de terra, em cais ou margem | Militares especializados | 1 | Não funcional | NI | TAP, seção 2 (objetivo 4); seção 3 (requisito 2); seção 6 (item 1) |
| RQ-16 | 3.2 | Operação em água doce e salgada, preferencialmente em ambientes abrigados | Distritos e grupamentos | 1 | Não funcional | NI | TAP, seção 3 (requisito 3); seção 6 (item 3) |
| RQ-17 | 3.2 | Profundidade nominal de operação de até 10 m e profundidade máxima de projeto de 30 m | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 2 (objetivo 5); seção 3 (requisito 4); seção 10 (indicador 8.3) |
| RQ-18 | 3.2 | Apoio à inspeção visual de ferro, casco, hélice e demais estruturas submersas definidas no CONOPS | Distritos e grupamentos | 1 | Funcional | NI | TAP, seção 3 (requisito 9) |
| RQ-19 | 3.2 | Localização visual de objetos no fundo ou leito, sem requisito de recuperação física no MVP | Mergulhadores e especialistas SAR | 1 | Funcional | NI | TAP, seção 3 (requisito 10) |
| RQ-20 | 3.2 | Imagens e registros associados às missões de inspeção e busca como resultados principais do MVP | Distritos e grupamentos | 1 | Funcional | NI | TAP, seção 3 (requisito 17) |
| RQ-21 | 3.2 | Observância dos limites de emprego: vedação de rebojo perigoso e de correnteza acima de 5 nós e interrupção fora do limite de visibilidade aprovado | Autoridades de segurança e áreas de teste | 1 | Não funcional | NI | TAP, seção 6 (itens 4 e 5) |
| RQ-22 | 3.3 | Testes de bancada e de campo, em água doce e salgada, com critérios de aceitação previamente definidos | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 3 (requisito 15); seção 6 (item 9) |
| RQ-23 | 3.3 | 100% dos testes críticos aprovados antes do piloto operacional | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 10 (indicador 8.2); seção 15 |
| RQ-24 | 3.4 | Entrega de sobressalentes iniciais | Logística e cadeia de suprimento | 1 | Não funcional | NI | TAP, seção 3 (requisito 13); seção 10 (indicador 8.4); seção 15 |
| RQ-25 | 4.1 | Treinamento básico de operadores e mantenedores | Militares especializados | 1 | Não funcional | NI | TAP, seção 3 (requisito 13); seção 10 (indicador 8.4); seção 15 |
| RQ-26 | 4.1 | Piloto operacional avaliado e aprovado pela Força de Submarinos, com relatório de resultados, desempenho, limites e benefícios | Força de Submarinos | 1 | Não funcional | NI | TAP, seção 4 (entrega 10); seção 10 (indicador 8.5); seção 15 |
| RQ-27 | 4.1 | Avaliação do benefício de redução da exposição humana em reconhecimentos preliminares | Mergulhadores e especialistas SAR | 2 | Não funcional | NI | TAP, seção 2 (objetivo 8); seção 5 (justificativa 2) |
| RQ-28 | 4.2 | Procedimentos de operação, lançamento, gestão do fio, recuperação, lavagem, dessalinização, armazenamento e transporte | Militares especializados | 1 | Não funcional | NI | TAP, seção 3 (requisito 12) |
| RQ-29 | 4.2 | Documentação técnica entregue, aprovada e disponibilizada às organizações usuárias | Engenharia e manutenção | 1 | Não funcional | NI | TAP, seção 2 (objetivo 7); seção 3 (requisito 13); seção 10 (indicador 8.4); seção 15 |
| RQ-30 | 4.2 | Vida útil de projeto de 10 anos e apoio de manutenção por cinco anos, com plano de manutenção entregue | Logística e cadeia de suprimento | 1 | Não funcional | NI | TAP, seção 3 (requisito 14); seção 10 (indicador 8.4); seção 15 |

**Resumo:** 30 requisitos · 7 funcionais e 23 não funcionais · 29 de prioridade 1 e 1 de prioridade 2 · todos com status NI.  
Distribuição por pacote: 1 — 3; 2 — 4; 3.1 — 7; 3.2 — 7; 3.3 — 2; 3.4 — 1; 4.1 — 3; 4.2 — 3.

## 5. Matriz da Qualidade

| ID | Código EAP | Requisito | Indicador | Meta | Técnica de medição | Frequência | Quem mede | Ação | Quando | Responsável |
|------|------|---------------|------------|------------|---------------|---------|---------|---------------|------------|---------|
| RQ-01 | 1 | Registros de premissas, riscos, decisões e mudanças mantidos atualizados e desempenho do projeto reportado à Força de Submarinos | Atualização dos registros de gerenciamento e emissão dos relatórios de desempenho | 100% dos relatórios de desempenho previstos no plano de gerenciamento emitidos e registros atualizados em cada ciclo (proposta de controle) | Auditoria documental dos registros de premissas, riscos, decisões e mudanças e dos relatórios emitidos, contra o plano de gerenciamento | Em cada ciclo de reporte definido no plano de gerenciamento | Patrocinador do projeto | Atualizar os registros, emitir o relatório pendente e registrar a questão no registro de questões | Registro desatualizado ou relatório não emitido no ciclo previsto | Gerente do projeto |
| RQ-02 | 1 | MVP recebido, integrado e configurado dentro do prazo aprovado | Desvio de prazo do marco de recebimento do MVP | Desvio nulo em relação à data aprovada na linha de base do cronograma (referência preliminar do TAP: M-07, T0 + 12 meses) | Comparação entre datas previstas e realizadas no cronograma de marcos (linha de base) | Em cada ciclo de reporte e na data do marco | Gerente do projeto | Analisar a causa do desvio, elaborar plano de recuperação de prazo e, se necessário, submeter solicitação de mudança à Força de Submarinos | Tendência de atraso identificada ou marco não atingido na data aprovada | Gerente do projeto (decisão sobre mudança: Força de Submarinos) |
| RQ-03 | 1 | Encerramento formal aprovado pela Força de Submarinos, com pendências aceitas ou transferidas, lições aprendidas registradas e recomendação de continuidade | Atendimento aos critérios de término do projeto | 100% dos critérios de término da seção 15 do TAP atendidos ou formalmente aceitos e encerramento aprovado pela Força de Submarinos (TAP) | Lista de verificação dos critérios de término e análise do relatório final | Na fase de encerramento, antes da submissão à Força de Submarinos | Gerente do projeto | Complementar os itens pendentes, obter aceite formal ou transferir as pendências às organizações usuárias e submeter novamente | Critério de término não atendido ou pendência sem destinação | Gerente do projeto (aprovação: Força de Submarinos) |
| RQ-04 | 2 | Necessidade operacional dos Distritos e grupamentos consolidada e mapa de usuários definido | Validação do relatório de necessidade operacional e do mapa de usuários | Relatório validado pelos usuários representativos até o marco aprovado (referência do TAP: T0 + 2 meses) | Revisão do relatório em oficinas com os usuários e registro formal da validação | Em cada revisão do relatório, até a validação | Gerente do projeto | Consolidar as divergências em nova oficina, revisar o relatório e submetê-lo novamente | Usuário representativo não valida o relatório ou registra divergência | Gerente do projeto |
| RQ-05 | 2 | CONOPS e envelope operacional definidos e aprovados, com limites de correnteza, rebojo e visibilidade explicitados e interpretação do valor de 30 cm confirmada | Aprovação do CONOPS com todos os limites operacionais definidos | CONOPS aprovado pela Força de Submarinos com 100% dos limites da seção 6 do TAP explicitados, inclusive a interpretação confirmada do limite de visibilidade (referência do TAP: M-03, T0 + 3 meses) | Análise documental do CONOPS por lista de verificação dos limites da seção 6 do TAP | Em cada revisão do CONOPS, até a aprovação | Gerente do projeto, com militares especializados | Revisar o CONOPS, consultar as autoridades de segurança para confirmar a interpretação do limite de visibilidade e submeter novamente | Limite ausente, ambíguo ou não aprovado | Gerente do projeto |
| RQ-06 | 2 | Arquitetura modular especificada com núcleo, interfaces e critérios verificáveis, e configuração do MVP definida | Interfaces da arquitetura modular com critério de verificação definido | 100% das interfaces do núcleo (MVP e aparatos futuros) com critério de verificação definido (proposta de controle) | Revisão técnica da especificação da arquitetura modular | Em cada revisão da especificação, até a aprovação | Engenharia e manutenção | Complementar a especificação e repetir a revisão técnica | Interface sem critério verificável ou configuração do MVP indefinida | Gerente do projeto |
| RQ-07 | 2 | Requisitos rastreáveis aos critérios de aceitação e aprovados pela autoridade competente | Percentual de requisitos com critério de aceitação rastreável e aprovado | 100% (TAP) | Verificação da matriz de rastreabilidade (requisito → critério de aceitação → teste) | Na aprovação da linha de base de requisitos e a cada mudança aprovada | Gerente do projeto | Definir o critério do requisito sem rastreio e submeter à aprovação da Força de Submarinos | Requisito sem critério de aceitação ou sem aprovação | Gerente do projeto |
| RQ-08 | 3.1 | Arquitetura modular que permita a instalação ou substituição de aparatos e acessórios conforme a faina | Instalação e substituição de aparatos e acessórios por meio das interfaces especificadas | Instalação e substituição demonstradas em 100% das interfaces previstas para o MVP nas planilhas do TAF (proposta de controle) | Ensaio de montagem, desmontagem e verificação funcional no TAF | Em cada execução do TAF, inclusive retestes | Equipe de testes do projeto | Registrar não conformidade, analisar a causa, corrigir e repetir o ensaio | Interface não permite a instalação ou substituição, ou não atende ao critério da planilha | Gerente do projeto |
| RQ-09 | 3.1 | MVP com câmera e iluminação, sem sonar e sem garra/manipulador | Conformidade da configuração entregue com a configuração aprovada do MVP | 100% dos itens da configuração aprovada conferidos; câmera e iluminação funcionais; ausência de sonar e de garra/manipulador (TAP) | Auditoria de configuração (inventário, números de série e versões de software) e teste funcional de câmera e iluminação | No início do TAF | Equipe de testes do projeto | Registrar não conformidade, adequar a configuração e repetir a verificação | Item ausente, divergente ou não funcional | Gerente do projeto |
| RQ-10 | 3.1 | Autonomia mínima de 2h30 em condição nominal de operação | Tempo de autonomia operacional | ≥ 2h30 (TAP) | Ensaio de autonomia em operação contínua na condição nominal definida na planilha do TAF, com registro dos horários de início e término | Em cada execução do TAF, inclusive retestes | Equipe de testes do projeto | Registrar não conformidade, analisar a causa, corrigir ou ajustar a configuração, repetir o ensaio e submeter novamente à aceitação | Autonomia inferior a 2h30 | Gerente do projeto |
| RQ-11 | 3.1 | Umbilical com alcance mínimo de 50 m | Alcance útil do umbilical | ≥ 50 m (TAP) | Medição do comprimento útil e verificação da continuidade de comunicação e de energia ao longo do umbilical | Em cada execução do TAF, inclusive retestes | Equipe de testes do projeto | Registrar não conformidade, adequar ou substituir o umbilical e repetir o ensaio | Alcance inferior a 50 m ou falha de continuidade | Gerente do projeto |
| RQ-12 | 3.1 | Mecanismo de recuperação e gestão dinâmica do umbilical | Funcionamento do mecanismo de recuperação e gestão dinâmica | Lançamento e recolhimento do umbilical em toda a extensão sem falha nos ciclos previstos na planilha do TAF (proposta de controle) | Ensaio funcional de lançamento e recolhimento | Em cada execução do TAF, inclusive retestes | Equipe de testes do projeto | Registrar não conformidade, analisar a causa, corrigir e repetir o ensaio | Falha, travamento ou enrosco durante o ciclo | Gerente do projeto |
| RQ-13 | 3.1 | Produção e armazenamento de imagens e vídeos em 1080p a 30 fps e 4K a 15 fps | Resolução e taxa de quadros dos vídeos gravados e integridade dos arquivos armazenados | 1080p a 30 fps e 4K a 15 fps, com arquivos armazenados e reproduzíveis (TAP) | Gravação de amostras em cada modo e verificação das propriedades e da reprodução dos arquivos | Em cada execução do TAF, inclusive retestes | Equipe de testes do projeto | Registrar não conformidade, ajustar a configuração de câmera e software e repetir o ensaio | Modo de gravação não atingido ou arquivo corrompido | Gerente do projeto |
| RQ-14 | 3.1 | Comportamentos de proteção para situações de impacto, perda de comunicação ou carga anormal associada ao umbilical | Resposta do sistema às condições simuladas de impacto, perda de comunicação e carga anormal no umbilical | 100% das condições simuladas com acionamento do comportamento de proteção especificado (proposta de controle) | Ensaio de bancada com simulação de cada condição | Em cada execução do TAF, inclusive retestes | Equipe de testes do projeto | Registrar não conformidade, analisar a causa, corrigir e repetir o ensaio; se a falha persistir, submeter à decisão da Força de Submarinos | Comportamento de proteção ausente ou diferente do especificado | Gerente do projeto |
| RQ-15 | 3.2 | Operação por uma única pessoa treinada, a partir de terra, em cais ou margem | Fases de operação (preparação, lançamento, operação e recuperação) conduzidas por um único operador | Todas as fases conduzidas por um único operador treinado, a partir de cais ou margem (TAP) | Observação direta com lista de verificação nas sessões do TAM | Em cada sessão do TAM | Equipe de testes do projeto | Registrar não conformidade, analisar o procedimento ou a configuração, ajustar e repetir a sessão | Alguma fase exige mais de um operador ou operação fora de cais ou margem | Gerente do projeto |
| RQ-16 | 3.2 | Operação em água doce e salgada, preferencialmente em ambientes abrigados | Testes do TAM concluídos em cada meio | 100% dos testes previstos executados e aprovados em água doce e em água salgada (TAP) | Verificação das planilhas executadas do TAM, por meio | Ao término de cada bateria do TAM | Equipe de testes do projeto | Reprogramar a bateria não realizada (área, meios e autorização) ou registrar não conformidade, corrigir e repetir | Meio não testado ou teste reprovado | Gerente do projeto |
| RQ-17 | 3.2 | Profundidade nominal de operação de até 10 m e profundidade máxima de projeto de 30 m | Profundidade atingida com operação estável | Operação a 10 m demonstrada; profundidade máxima de projeto de 30 m demonstrada ou formalmente aceita pela Força de Submarinos (TAP) | Ensaio em água com registro da profundidade pelo sistema, conferido com a referência de profundidade da área de teste | Em cada bateria do TAM | Equipe de testes do projeto | Registrar não conformidade, analisar a causa, corrigir e repetir o ensaio, ou submeter a evidência à aceitação formal | Profundidade não atingida ou operação instável | Gerente do projeto |
| RQ-18 | 3.2 | Apoio à inspeção visual de ferro, casco, hélice e demais estruturas submersas definidas no CONOPS | Alvos de inspeção concluídos com imagem útil | 100% dos alvos previstos na planilha do TAM inspecionados com imagens aceitas pelos usuários (proposta de controle) | Demonstração prática das tarefas de inspeção e avaliação das imagens pelos usuários | Em cada bateria do TAM | Equipe de testes do projeto, com Distritos e grupamentos | Registrar não conformidade, ajustar iluminação, câmera ou procedimento e repetir a demonstração | Alvo não inspecionado ou imagem não aceita | Gerente do projeto |
| RQ-19 | 3.2 | Localização visual de objetos no fundo ou leito, sem requisito de recuperação física no MVP | Objetos-alvo localizados e registrados em imagem | 100% dos objetos-alvo posicionados para o teste localizados e registrados (proposta de controle) | Demonstração de busca com objetos posicionados no fundo ou leito da área de teste | Em cada bateria do TAM | Equipe de testes do projeto, com mergulhadores e especialistas SAR | Registrar não conformidade, ajustar procedimento ou configuração e repetir a demonstração | Objeto não localizado | Gerente do projeto |
| RQ-20 | 3.2 | Imagens e registros associados às missões de inspeção e busca como resultados principais do MVP | Missões com imagens e registros associados armazenados e recuperáveis | 100% das missões de teste com registros recuperáveis (proposta de controle) | Verificação dos arquivos de cada missão do TAM | Ao término de cada sessão do TAM | Equipe de testes do projeto | Registrar não conformidade, corrigir o procedimento de registro ou armazenamento e repetir a missão | Missão sem registro recuperável | Gerente do projeto |
| RQ-21 | 3.2 | Observância dos limites de emprego: vedação de rebojo perigoso e de correnteza acima de 5 nós e interrupção fora do limite de visibilidade aprovado | Operações realizadas fora dos limites aprovados | Zero (TAP) | Registro das condições de correnteza, rebojo e visibilidade antes e durante cada sessão, conforme o CONOPS | Antes e durante cada sessão do TAM | Equipe de testes do projeto, com as autoridades de segurança da área de teste | Interromper imediatamente a operação, registrar a ocorrência, analisar e reprogramar a sessão | Condição ambiental fora do limite aprovado | Gerente do projeto |
| RQ-22 | 3.3 | Testes de bancada e de campo, em água doce e salgada, com critérios de aceitação previamente definidos | Planilhas de testes aprovadas antes da execução | 100% das planilhas do TAF e do TAM aprovadas pela Força de Submarinos antes do início da respectiva bateria (TAP) | Verificação documental do registro de aprovação de cada planilha | Antes de cada bateria de testes | Gerente do projeto | Não iniciar a bateria; revisar a planilha e submetê-la novamente | Planilha não aprovada ou sem critério de aceitação | Gerente do projeto |
| RQ-23 | 3.3 | 100% dos testes críticos aprovados antes do piloto operacional | Percentual de testes críticos aprovados | 100% aprovados ou formalmente dispensados antes do início do piloto (TAP) | Consolidação das planilhas executadas do TAF e do TAM | Ao término do TAF e do TAM, antes do início do piloto | Gerente do projeto | Não iniciar o piloto; tratar as não conformidades com correção e reteste ou submeter dispensa formal à Força de Submarinos | Teste crítico reprovado ou pendente | Gerente do projeto (dispensa: Força de Submarinos) |
| RQ-24 | 3.4 | Entrega de sobressalentes iniciais | Itens recebidos conforme a lista aprovada | 100% dos itens recebidos e conferidos em quantidade, identificação e estado (proposta de controle) | Conferência física contra a lista aprovada e registro no inventário inicial | No recebimento de cada remessa | Logística e cadeia de suprimento | Registrar a divergência, solicitar complementação ou substituição e repetir a conferência | Item faltante, divergente ou avariado | Gerente do projeto |
| RQ-25 | 4.1 | Treinamento básico de operadores e mantenedores | Operadores e mantenedores aprovados na avaliação de competência mínima | 100% dos militares designados aprovados (proposta de controle) | Avaliação teórica e prática ao final do curso básico | Ao final de cada turma | Frente de capacitação do projeto | Reforçar a instrução e reavaliar; revisar o conteúdo do curso em caso de reprovação recorrente | Militar reprovado na avaliação | Gerente do projeto |
| RQ-26 | 4.1 | Piloto operacional avaliado e aprovado pela Força de Submarinos, com relatório de resultados, desempenho, limites e benefícios | Aprovação do relatório de avaliação do piloto | Relatório aprovado pela Força de Submarinos (TAP) | Análise do relatório, comparando os resultados do piloto com os critérios de aceitação | Ao término do piloto | Força de Submarinos | Complementar o piloto ou o relatório, tratar as limitações identificadas e submeter novamente | Relatório não aprovado ou resultado abaixo dos critérios de aceitação | Gerente do projeto |
| RQ-27 | 4.1 | Avaliação do benefício de redução da exposição humana em reconhecimentos preliminares | Reconhecimentos preliminares realizados com o ROV antes do emprego de mergulhadores durante o piloto | Benefício avaliado e registrado no relatório do piloto (proposta de controle) | Registro das missões do piloto e avaliação pelos mergulhadores e especialistas SAR | Durante o piloto operacional | Mergulhadores e especialistas SAR | Complementar os registros e a avaliação antes da submissão do relatório | Relatório do piloto sem a avaliação do benefício | Gerente do projeto |
| RQ-28 | 4.2 | Procedimentos de operação, lançamento, gestão do fio, recuperação, lavagem, dessalinização, armazenamento e transporte | Procedimentos exigidos contemplados nos manuais aprovados | 100% dos procedimentos do requisito 12 do TAP contemplados e aprovados (TAP) | Lista de verificação documental e confirmação prática dos procedimentos empregados no TAM | Na submissão de cada revisão dos manuais | Militares especializados | Revisar o manual, repetir a confirmação prática e submeter novamente | Procedimento ausente, incorreto ou não confirmado | Gerente do projeto |
| RQ-29 | 4.2 | Documentação técnica entregue, aprovada e disponibilizada às organizações usuárias | Manuais aprovados e disponibilizados | Manuais de operação, de manutenção e técnico aprovados e disponibilizados a 100% das organizações usuárias (proposta de controle) | Verificação dos registros de aprovação e de disponibilização da documentação | Na entrega de cada manual e no encerramento | Engenharia e manutenção | Revisar o manual com observações, submetê-lo novamente e completar a disponibilização | Manual reprovado, desatualizado em relação à configuração final ou não disponibilizado | Gerente do projeto |
| RQ-30 | 4.2 | Vida útil de projeto de 10 anos e apoio de manutenção por cinco anos, com plano de manutenção entregue | Cobertura do plano de manutenção | Plano de manutenção entregue, com apoio de manutenção por 5 anos e compatível com a vida útil de projeto de 10 anos (TAP) | Análise documental do plano de manutenção e da documentação técnica | Na entrega do plano de manutenção | Engenharia e manutenção, com logística e cadeia de suprimento | Revisar o plano e, se a lacuna persistir, submeter a pendência à Força de Submarinos | Apoio previsto inferior a 5 anos ou incompatibilidade com a vida útil de 10 anos | Gerente do projeto |

Respostas a não conformidades adotadas, conforme o requisito: registro de não conformidade, análise de causa, correção, adequação de configuração, repetição do teste, avaliação técnica, nova submissão à aceitação e, quando previsto no TAP, aceite ou dispensa formal pela Força de Submarinos.

## 6. Exemplo de leitura da cadeia

```text
REQUISITO   RQ-10 — Autonomia mínima de 2h30 em condição nominal de operação  (TAP, seção 2 (objetivo 6); seção 3 (requisito 5); seção 10 (indicador 8.3))
PACOTE EAP  3.1 TAF  (subordinado a 3 Recebimento do ROV)
INDICADOR   Tempo de autonomia operacional
META        ≥ 2h30 (TAP)
MEDIÇÃO     Ensaio de autonomia em operação contínua na condição nominal definida na planilha do TAF, com registro dos horários de início e término — em cada execução do taf, inclusive retestes; mede: Equipe de testes do projeto
RESPOSTA    Registrar não conformidade, analisar a causa, corrigir ou ajustar a configuração, repetir o ensaio e submeter novamente à aceitação — quando: autonomia inferior a 2h30; responsável: Gerente do projeto
```

## 7. Cobertura

### Requisitos de alto nível do TAP (seção 3) → Tarefa 3

| Req. TAP | Tema | Requisitos (ID) | Código EAP |
|---|---|---|---|
| 1 | Modularidade | RQ-06, RQ-08 | 2, 3.1 |
| 2 | Operação por uma pessoa | RQ-15 | 3.2 |
| 3 | Água doce e salgada | RQ-16 | 3.2 |
| 4 | Profundidade | RQ-17 | 3.2 |
| 5 | Autonomia | RQ-10 | 3.1 |
| 6 | Umbilical | RQ-11, RQ-12 | 3.1 |
| 7 | Imagem e vídeo | RQ-13 | 3.1 |
| 8 | Configuração do MVP | RQ-09 | 3.1 |
| 9 | Inspeção visual | RQ-18 | 3.2 |
| 10 | Localização visual | RQ-19 | 3.2 |
| 11 | Proteção | RQ-14 | 3.1 |
| 12 | Procedimentos | RQ-28 | 4.2 |
| 13 | Treinamento, documentação e sobressalentes | RQ-24, RQ-25, RQ-29 | 3.4, 4.1, 4.2 |
| 14 | Vida útil e manutenção | RQ-30 | 4.2 |
| 15 | Testes | RQ-22 | 3.3 |
| 16 | Cadeia nacional | — | Não rastreado (C1) |
| 17 | Resultados do MVP | RQ-20 | 3.2 |
| 18 | Rastreabilidade | RQ-07 | 2 |

17 dos 18 requisitos de alto nível estão rastreados. O requisito 16 (priorização de fornecedores e cadeia de suprimentos nacionais) é, na redação do TAP, critério de seleção de fornecedor; como a obtenção contratual foi excluída da EAP pelo orientador, não há pacote ao qual rastreá-lo sem reintroduzir o antigo bloco Fornecedor. Registrado no conflito C1, com proposta de alteração de consistência do TAP.

Os demais requisitos da matriz decorrem de objetivos (seção 2), entregas-chave (seção 4), restrições (seção 6), riscos (seção 9), indicadores-chave (seção 10), responsabilidades do gerente (seção 12) e critérios de término (seção 15) do TAP.

### Pacotes de trabalho da EAP → requisitos

Todos os 8 pacotes de trabalho possuem ao menos um requisito rastreado; os elementos de agregação (3 e 4) são cobertos por meio de seus filhos.

## 8. Auditoria da Tarefa 3

| Dimensão | Verificação | Resultado |
|---|---|---|
| Tarefa 1 | Requisito possui fundamento no TAP? | Sim — 30/30 com origem indicada. |
| Tarefa 1 | Stakeholder coerente com o TAP? | Sim — somente partes interessadas da seção 8 do TAP. |
| Tarefa 1 | Restrição ou objetivo contradito? | Não. |
| Tarefa 2 | Código EAP existe na versão final? | Sim — todos os códigos pertencem à EAP revisada. |
| Tarefa 2 | Algum código excluído foi utilizado? | Não — nenhum código da EAP original (3.x Fornecedor, 5.x V&V, 7.x Encerramento, 1.x). |
| Tarefa 2 | A matriz respeita a compactação da EAP? | Sim — nenhum pacote foi criado; vários requisitos apontam para o mesmo pacote. |
| Tarefa 2 | TAF/TAM estão sob Recebimento? | Sim — 3.1 e 3.2. |
| Tarefa 2 | Existe V&V ou Encerramento separado? | Não. |
| Rastreabilidade | Requisitos mensuráveis ou verificáveis? | Sim — cada requisito possui indicador e técnica de medição. |
| Rastreabilidade | Prioridades e tipos consistentes? | Sim — regras explícitas na seção 3. |
| Rastreabilidade | Status correto? | Sim — NI para todos (planejamento). |
| Qualidade | Indicador, meta, técnica, frequência, quem mede, ação, quando e responsável preenchidos? | Sim — 30/30 linhas completas. |
| Qualidade | Metas não presentes no TAP identificadas? | Sim — marcadas como “proposta de controle”. |
| Qualidade | Conteúdo do exemplo de calçados reutilizado? | Não. |
| Coerência | Cada requisito da Matriz da Qualidade existe na Matriz de Rastreabilidade com a mesma redação? | Sim — mesmo ID e mesma descrição. |
| Coerência | Algum conteúdo eliminado na Tarefa 2 reapareceu? | Não — verificação automática registrada em `auditoria-cruzada.md`. |

## 9. Observações

- **C1 — Obtenção contratual (antigo bloco Fornecedor):** Por decisão do orientador (D2), a EAP revisada não contém esses elementos. O texto do TAP, entretanto, continua a descrevê-los como parte do projeto. TAP preservado sem alteração. Proposta de alteração de consistência do TAP, a submeter pelo controle integrado de mudanças (pacote 1) à aprovação da Força de Submarinos: (a) registrar a obtenção contratual como processo institucional externo ao escopo da EAP; (b) ajustar o objetivo 2, as entregas 5 e 7, os marcos M-04 a M-06 e a seção 13; (c) reavaliar o requisito 16, que, na redação atual, é critério de seleção de fornecedor. Na Tarefa 3, o requisito 16 não é rastreado a pacote da EAP.
- **C6 — Enunciado e modelo da Tarefa 3:** O enunciado oficial da Tarefa 3 e o modelo de Gerenciamento da Qualidade da disciplina (exemplo de calçados) não constam do repositório. Matrizes construídas com os campos definidos; nenhum conteúdo do exemplo de calçados utilizado.
- **Partes interessadas sem requisito rastreado:** “Setores de aquisição e assessoria jurídica” e “Fornecedores nacionais e integradores” permanecem no TAP, mas não originam requisitos rastreados, pela mesma razão do C1.


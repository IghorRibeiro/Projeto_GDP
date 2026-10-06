# SKILL 2 — TAREFA 2: EAP + DICIONÁRIO DO PROJETO ROV-MB
## Redesenho obrigatório a partir das críticas do Cmdt Huback e dos 10 Mandamentos da EAP

### Objetivo desta skill

Esta é a etapa principal do trabalho atual.

A IA deve **redesenhar a EAP e o Dicionário da EAP** do ROV-MB, usando:
1. a Tarefa 1 (TAP) como fonte do escopo;
2. a EAP/Dicionário original como ponto de partida;
3. as críticas e decisões registradas na reunião com o Cmdt Huback;
4. os Dez Mandamentos da EAP como critérios de auditoria.

O objetivo NÃO é enriquecer a EAP com mais pacotes.

O objetivo é **compactar, reorganizar, eliminar duplicidades e transferir detalhamento para o Dicionário**, sem perder a cobertura de 100% do escopo.

---

# 1. PRINCIPAL ORIENTAÇÃO DO ORIENTADOR

A EAP original estava excessivamente fragmentada.

A orientação é:
- diminuir a quantidade de pacotes;
- concentrar entregas correlatas;
- evitar separar processos que já pertencem a uma mesma entrega;
- usar o Dicionário para explicar o conteúdo abrangido;
- manter a EAP em um nível que permita planejamento e controle, sem decomposição excessiva.

A palavra-chave é:

**COMPACTAR.**

---

# 2. DECISÕES QUE JÁ ESTÃO FECHADAS

Estas decisões devem ser consideradas obrigatórias.

## 2.1 Gerenciamento do Projeto vira UM ÚNICO pacote

O pacote 1 não deve ser dividido em:
- 1.1 Iniciação;
- 1.2 Planejamento;
- 1.3 Execução;
- 1.4 Monitoramento e Controle;
- 1.5 Encerramento.

Tudo isso fica absorvido em:

**1. GERENCIAMENTO DO PROJETO**

No Dicionário, a descrição deve deixar explícito que o pacote contempla as práticas relacionadas aos grupos de processo de:
- iniciação;
- planejamento;
- execução;
- monitoramento e controle;
- encerramento;

em consonância com o preconizado no PMBOK.

A forma conceitual já definida pelo orientador é:

> “Entrega de todas as práticas correlacionadas aos grupos de processo: iniciação, planejamento, execução, monitoramento e controle e encerramento em consonância com o preconizado no PMBOK.”

Não criar filhos artificiais só para representar os grupos de processo.

---

## 2.2 O bloco FORNECEDOR foi eliminado

Não existe mais, na nova EAP:
- estudo de mercado;
- decisão de fornecimento;
- definição de potenciais fornecedores;
- comparação de propostas;
- estratégia de contratação;
- seleção de fornecedor;
- licitação;
- contratação;
- matriz de avaliação de fornecedor.

Esses elementos devem ser considerados **fora da EAP final do projeto desta tarefa**, conforme a decisão do orientador.

Não reintroduzir esses conteúdos com nomes diferentes.

---

## 2.3 V&V/TESTES foi absorvido pelo RECEBIMENTO

Não criar um pacote separado para:
- V&V;
- testes;
- aceitação;
- plano de testes;
- ensaios.

Tudo isso foi absorvido pelo pacote:

**RECEBIMENTO DO ROV**

A ideia do orientador é evitar duplicidade entre “Recebimento” e “V&V”.

A estrutura já orientada é:

### Recebimento do ROV
- **TAF:** execução dos testes realizados na instalação da empresa;
- **TAM:** acompanhamento da realização dos testes em água doce e salgada do sistema ROV;
- **aprovação das planilhas de testes:** TAF e TAM;
- **recebimento de sobressalentes e consumíveis**.

Se a versão final da árvore utilizar subcódigos, eles devem seguir essa lógica.

---

## 2.4 Encerramento foi absorvido pelo Gerenciamento

Não existe mais:
**Encerramento do Projeto** como pai independente.

O encerramento pertence ao pacote:
**1. Gerenciamento do Projeto**.

Não criar novamente o bloco “Encerramento”.

---

## 2.5 Capacitação incorpora gestão do conhecimento

O pacote de capacitação deve contemplar:
- capacitação de operadores;
- capacitação de mantenedores;
- documentação técnica;
- aprovação dos manuais de operação;
- aprovação dos manuais de manutenção;
- aprovação do manual técnico do sistema fornecido;
- gestão do conhecimento relacionada à transferência e sustentação do conhecimento do sistema.

Não criar vários pacotes pequenos para cada manual ou tipo de treinamento sem necessidade.

---

# 3. O PONTO MAIS IMPORTANTE: NÃO DEVE HAVER “PACOTE POR ATIVIDADE”

A EAP deve representar **entregas/subprodutos**, não uma lista de todas as ações necessárias para produzir essas entregas.

Não usar como critério:
“Há uma atividade diferente, então precisa de um pacote diferente.”

Usar:
“Isso precisa ser um pacote separado para permitir planejamento e controle, ou pode ser parte do pacote existente e ser descrito no Dicionário?”

Se puder ser absorvido sem perder controle, **absorver**.

---

# 4. OS 10 MANDAMENTOS DA EAP — CRITÉRIOS DE AUDITORIA

## I — Cobiarás a EAP do próximo
Consultar estruturas semelhantes e aprender com projetos anteriores.

Aplicação:
usar boas referências, sem copiar conteúdo incompatível com o ROV-MB.

## II — Explicit­arás todos os subprodutos
Tudo que pertence ao escopo deve estar coberto pela EAP.

Aplicação:
não eliminar uma entrega real só porque a EAP foi compactada; em vez disso, absorvê-la corretamente em um pai.

## III — Não usarás os nomes em vão
Usar nomes claros, substantivos e orientados à entrega.

Evitar:
- elaborar;
- executar;
- realizar;
- fazer.

Preferir:
- documentação técnica;
- TAF;
- TAM;
- capacitação;
- recebimento do ROV.

## IV — Guardarás a descrição das entregas no Dicionário
A árvore não precisa conter explicações longas.

Detalhes ficam no Dicionário:
- escopo;
- conteúdo;
- limites;
- critérios;
- o que está incluído.

## V — Decomporás até o nível de detalhe que permita planejamento e controle
Só decompor quando a decomposição trouxer benefício real para planejar/controlar.

## VI — Não decomporás em demasia
Este é um mandamento CENTRAL para esta revisão.

O professor/orientador explicitamente quer menos pacotes.

Não criar granularidade só para “parecer completo”.

## VII — Honrarás o pai
Todo filho deve pertencer logicamente ao seu pai.

Exemplos:
- testes pertencem ao Recebimento;
- encerramento pertence ao Gerenciamento;
- documentação técnica pertence à Capacitação, quando essa for a estrutura escolhida;
- nenhum elemento do antigo Fornecedor deve reaparecer.

## VIII — Mandamento dos 100%
A soma dos filhos deve representar 100% da entrega do pai.

Ao decompor “Recebimento do ROV”, verificar se os elementos cobrem todo o escopo de recebimento que realmente permanece na Tarefa 2.

## IX — Não decomporás em somente um subproduto
Se um pai terá apenas um filho, provavelmente não existe ganho em decompor.

Isso é especialmente relevante para:
- Gerenciamento do Projeto;
- qualquer pacote que possa ser totalmente descrito no Dicionário.

## X — Não repetirás o mesmo elemento como componente de mais de uma entrega
Uma entrega deve possuir um único local na árvore.

Exemplos:
- não duplicar testes em Recebimento e V&V;
- não duplicar documentação em Capacitação e Encerramento;
- não duplicar encerramento em Gerenciamento e outro pacote.

---

# 5. ESTRUTURA DE REFERÊNCIA JÁ CONSOLIDADA

A estrutura final ainda deve ser refinada, mas o ponto de partida aprovado pela discussão foi aproximadamente:

**PROJETO ROV-MB**

**1. GERENCIAMENTO DO PROJETO**

**2. NECESSIDADES E REQUISITOS**

**3. RECEBIMENTO DO ROV**
- 3.1 TAF
- 3.2 TAM
- 3.3 Aprovação das planilhas de testes
- 3.4 Recebimento de sobressalentes e consumíveis

**4. CAPACITAÇÃO**
- 4.1 Cursos
- 4.2 Documentação técnica

IMPORTANTE:
Essa é uma estrutura de trabalho consolidada, não uma autorização para criar subdivisões adicionais.

A IA deve analisar se algum desses filhos também pode ser absorvido em um pacote ainda mais adequado, desde que isso respeite as decisões do orientador e os 10 Mandamentos.

Não criar simetria artificial.

---

# 6. COMO RECONCILIAR A EAP COM O TAP

Depois de reconstruir a EAP, fazer uma auditoria:

### Cobertura
Tudo que o TAP considera parte do escopo precisa estar representado na EAP ou explicitamente absorvido em algum pacote.

### Exclusões
Tudo que foi explicitamente retirado na reunião deve permanecer fora da EAP.

### Consistência
A EAP não pode contradizer:
- objetivo do TAP;
- requisitos do TAP;
- stakeholders;
- restrições;
- entregas-chave.

### Granularidade
A EAP não precisa reproduzir todas as entregas-chave do TAP como pacotes independentes.

Ela deve organizá-las de forma coerente e compacta.

---

# 7. O DICIONÁRIO DA EAP É O LOCAL DO DETALHAMENTO

Para cada pacote final, o Dicionário deve informar no mínimo:
- código;
- pacote de trabalho;
- especificação da entrega;
- critério de aceitação, quando aplicável.

A especificação deve explicar o que está efetivamente incluído no pacote, sem voltar a criar subpacotes escondidos.

Exemplo de lógica para o pacote 1:

**1. Gerenciamento do Projeto**

Especificação:
abrange todas as práticas necessárias ao gerenciamento do projeto nos grupos de processo de iniciação, planejamento, execução, monitoramento e controle e encerramento, incluindo governança, acompanhamento, comunicação, controle de mudanças, riscos, integração e formalização do encerramento.

Não criar 1.1, 1.2 etc. para listar esses conteúdos.

---

# 8. CUIDADO COM “ATIVIDADES DISFARÇADAS”

Evitar descrições como:

“Realizar o teste...”
“Executar o recebimento...”
“Elaborar o manual...”

A EAP deve nomear a entrega.

No Dicionário, pode-se explicar que o pacote contempla determinadas ações, mas a entrega precisa estar claramente identificada.

---

# 9. AUDITORIA FINAL DA TAREFA 2

Antes de passar para a Tarefa 3, verificar:

### Estrutura
- há poucos pacotes?
- cada pacote tem propósito claro?
- houve absorção em vez de duplicação?
- Gerenciamento é único?
- Fornecedor desapareceu?
- V&V separado desapareceu?
- Encerramento separado desapareceu?
- Recebimento concentra TAF/TAM e demais itens definidos?
- Capacitação inclui gestão do conhecimento/documentação?

### Dez Mandamentos
- cobertura de 100%?
- pai-filho lógico?
- nenhum pai com apenas um filho desnecessário?
- nenhuma duplicidade?
- nomes orientados à entrega?
- decomposição realmente necessária?
- detalhes no Dicionário?

### Compatibilidade com a Tarefa 1
- a EAP continua representando o TAP?
- nenhum requisito importante foi perdido?
- nenhuma restrição foi alterada?
- nenhuma nova atividade institucional foi inserida?

Somente após essa auditoria considerar a Tarefa 2 consolidada.

---

# 10. TRANSIÇÃO PARA A TAREFA 3

Depois que a EAP e o Dicionário forem finalizados, **congelar essa versão como referência**.

A partir dela inicia-se a:

**Tarefa 3 — Gerenciamento da Qualidade**
- Matriz de Rastreabilidade de Requisitos;
- Matriz de Qualidade.

Não construir a Tarefa 3 enquanto a EAP estiver mudando.

A Tarefa 3 deve usar:
**Tarefa 1 (TAP) + Tarefa 2 (EAP/Dicionário final)**.


# SKILL 3 — TAREFA 3: GERENCIAMENTO DA QUALIDADE — PROJETO ROV-MB
## Executar somente depois de congelar a Tarefa 2

### Objetivo

Depois que a Tarefa 1 (TAP) estiver consolidada e a Tarefa 2 (EAP + Dicionário) tiver sido redesenhada, compactada e auditada, executar a **Tarefa 3 — Gerenciamento da Qualidade**.

A Tarefa 3 deve ser construída sobre:
- o TAP da Tarefa 1;
- a EAP final da Tarefa 2;
- o Dicionário final da Tarefa 2;
- o enunciado oficial da Tarefa 3;
- o modelo de Gerenciamento da Qualidade fornecido pela disciplina.

A Tarefa 3 não pode alterar a EAP para facilitar as matrizes.

---

# 1. ENTREGAS DA TAREFA 3

São duas:

## 1.1 Matriz de Rastreabilidade de Requisitos

Modelo-base:
- Código EAP;
- Descrição;
- Stakeholder;
- Prioridade;
- Tipo do requisito;
- Status.

## 1.2 Matriz de Qualidade

Modelo-base:
- Requisito;
- Indicador;
- Meta;
- Técnica de medição;
- Frequência;
- Quem mede;
- Ação;
- Quando;
- Responsável.

Usar o modelo fornecido pela disciplina como referência estrutural, não copiar o conteúdo do exemplo de calçados.

---

# 2. REGRA DE OURO

A cadeia documental precisa ser:

**TAP**
→ define necessidade, objetivos, requisitos, stakeholders e limites;

**EAP + Dicionário**
→ organiza o escopo em pacotes e define as entregas;

**Matriz de Rastreabilidade**
→ conecta requisitos aos pacotes da EAP;

**Matriz de Qualidade**
→ define como requisitos serão medidos e como não conformidades serão tratadas.

---

# 3. USAR A EAP FINAL, NÃO A EAP ORIGINAL

Depois da Tarefa 2, a IA deve esquecer os códigos eliminados para fins de rastreabilidade.

Não utilizar:
- antigo pacote Fornecedor;
- antigo V&V separado;
- antigo Encerramento separado;
- subpacotes de Gerenciamento que foram eliminados.

Exemplo:
se o pacote final for **3. Recebimento do ROV**, os requisitos de desempenho e aceitação associados ao recebimento devem apontar para esse pacote e/ou para seus filhos efetivamente existentes.

---

# 4. MATRIZ DE RASTREABILIDADE

## 4.1 Origem dos requisitos

Priorizar os requisitos já estabelecidos no TAP.

Exemplos de categorias:
- modularidade;
- operação por uma pessoa;
- água doce e salgada;
- profundidade;
- autonomia;
- umbilical;
- imagem/vídeo;
- proteção/segurança;
- operação;
- documentação;
- treinamento;
- sobressalentes;
- testes e aceitação.

Não criar requisito arbitrário só para preencher linhas.

## 4.2 Stakeholder

Usar stakeholders do TAP.

Não copiar stakeholders do exemplo dos calçados.

## 4.3 Prioridade

Se adotada a mesma convenção do modelo:
- 1 = imprescindível;
- 2 = desejável;
- 3 = opcional.

Manter a lógica consistente.

## 4.4 Tipo

Principalmente:
- funcional;
- não funcional.

Classificar de maneira consistente com a natureza do requisito.

## 4.5 Status

Se o projeto ainda estiver em planejamento:
- NI = Não Iniciada.

Não afirmar execução concluída sem base.

---

# 5. UMA EAP COMPACTA PODE TER MUITOS REQUISITOS NO MESMO PACOTE

Isso é esperado.

Exemplo:
- profundidade;
- autonomia;
- umbilical;
- operação em água doce;
- operação em água salgada;
- desempenho nos testes;

podem ser rastreados ao mesmo pacote **Recebimento do ROV**, desde que isso reflita a EAP final e o Dicionário.

Não criar um pacote novo para cada requisito.

---

# 6. MATRIZ DE QUALIDADE

A matriz deve transformar requisitos verificáveis em controle objetivo.

Para cada requisito relevante:

### Requisito
O que precisa ser atendido.

### Indicador
O que será medido/observado.

### Meta
Qual valor/condição representa conformidade.

### Técnica de medição
Como verificar.

### Frequência
Quando ou em que situação medir.

### Quem mede
Qual função/equipe realiza a medição.

### Ação
O que fazer em caso de não conformidade.

### Quando
Qual condição dispara a ação.

### Responsável
Quem coordena/trata a resposta.

---

# 7. TAF E TAM DEVEM APARECER, MAS DENTRO DA LÓGICA DO RECEBIMENTO

Como a Tarefa 2 absorveu V&V/testes pelo Recebimento:

- TAF é parte do Recebimento;
- TAM é parte do Recebimento;
- aprovação das planilhas de testes é parte do Recebimento.

Na Matriz de Qualidade, isso deve ser refletido.

Não criar uma seção/pacote chamado V&V para “corrigir” a matriz.

---

# 8. EXEMPLO DE ESTRUTURA DE RACIOCÍNIO

Para requisito de autonomia:

Requisito:
“autonomia mínima de 2h30”.

Indicador:
“tempo de autonomia operacional”.

Meta:
“≥ 2h30”.

Técnica:
“ensaio de autonomia nas condições aprovadas”.

Frequência:
“durante os testes de aceitação correspondentes”.

Quem mede:
função responsável pelos testes, definida na governança do projeto.

Ação:
registro de não conformidade + análise/tratamento conforme procedimento de aceitação.

Responsável:
função designada para tratamento da não conformidade.

Não inventar parâmetros adicionais não presentes no TAP sem identificar que são uma proposta de controle.

---

# 9. REQUISITO NÃO É INDICADOR, E INDICADOR NÃO É META

Evitar erros conceituais:

Requisito:
“o sistema deverá possuir autonomia mínima de 2h30.”

Indicador:
“tempo de autonomia”.

Meta:
“≥ 2h30.”

Técnica:
“ensaio de autonomia.”

Esses elementos devem permanecer distintos.

---

# 10. NÃO COPIAR O EXEMPLO DOS CALÇADOS

O modelo de aula possui exemplos de:
- fornecedores de matéria-prima;
- gerente de produção;
- designer;
- distribuição;
- marketing;
- testes específicos do calçado.

Nada disso deve ser transplantado automaticamente para o ROV-MB.

O modelo serve para:
- estrutura;
- campos;
- lógica de medição;
- lógica de resposta.

O conteúdo deve vir do ROV-MB.

---

# 11. RESPONDER A NÃO CONFORMIDADES DE FORMA COMPATÍVEL COM O ROV

Não utilizar automaticamente ações como:
- trocar fornecedor;
- revisar material;
- alterar linha de produção.

Isso pertence ao exemplo do calçado.

Para o ROV, respostas podem envolver, conforme o requisito:
- registro de não conformidade;
- análise de causa;
- correção;
- repetição do teste;
- adequação/configuração;
- avaliação técnica;
- nova submissão à aceitação.

Escolher a resposta adequada ao requisito e aos limites do projeto.

---

# 12. COERÊNCIA ENTRE AS DUAS MATRIZES

Cada requisito da Matriz de Qualidade deve poder ser localizado na Matriz de Rastreabilidade.

A relação deve ser:

**Requisito → código EAP → indicador → meta → medição → resposta**

Não criar requisitos “soltos” em uma matriz.

Não alterar silenciosamente a redação de um requisito entre as matrizes.

---

# 13. AUDITORIA FINAL DA TAREFA 3

Antes da entrega:

### Tarefa 1
- requisito possui fundamento no TAP?
- stakeholder é coerente?
- restrição/objetivo não foi contradito?

### Tarefa 2
- código EAP existe na versão final?
- nenhum código excluído foi utilizado?
- a matriz respeita a compactação da EAP?
- TAF/TAM estão sob Recebimento?
- não existe V&V separado?
- não existe Encerramento separado?

### Matriz de Rastreabilidade
- requisitos mensuráveis ou verificáveis?
- prioridades consistentes?
- tipos consistentes?
- status correto?

### Matriz de Qualidade
- indicador adequado?
- meta objetiva?
- técnica de medição praticável?
- frequência coerente?
- função responsável plausível?
- ação específica para não conformidade?
- condição da ação clara?

### Coerência geral
- TAP → EAP → Dicionário → Rastreabilidade → Qualidade formam uma cadeia única?
- nenhuma matriz está alterando o escopo?
- nenhum conteúdo eliminado na Tarefa 2 reapareceu?

---

# 14. ORDEM CORRETA DE EXECUÇÃO DO TRABALHO COMPLETO

A outra IA deve seguir esta sequência:

**ETAPA 1 — Ler e compreender a Tarefa 1 (TAP).**

↓

**ETAPA 2 — Ler a EAP/Dicionário originais da Tarefa 2.**

↓

**ETAPA 3 — Aplicar as críticas do Cmdt Huback.**

↓

**ETAPA 4 — Compactar a EAP.**

↓

**ETAPA 5 — Refazer o Dicionário da EAP de acordo com a nova estrutura.**

↓

**ETAPA 6 — Auditar a Tarefa 2 contra os 10 Mandamentos da EAP e contra o TAP.**

↓

**ETAPA 7 — Congelar a EAP/Dicionário final.**

↓

**ETAPA 8 — Executar a Tarefa 3.**

↓

**ETAPA 9 — Produzir Matriz de Rastreabilidade + Matriz de Qualidade.**

↓

**ETAPA 10 — Auditar a coerência entre Tarefas 1, 2 e 3.**

---

# 15. REGRA FINAL

Nunca resolver um problema da Tarefa 3 alterando silenciosamente a Tarefa 2.

Nunca resolver um problema da Tarefa 2 alterando silenciosamente o TAP.

Quando existir uma inconsistência:
1. identificar;
2. explicar onde está;
3. propor a correção no documento correto;
4. só depois continuar.

A prioridade é manter uma cadeia documental coerente:

**TAREFA 1 — TAP**
→ **TAREFA 2 — EAP + DICIONÁRIO**
→ **TAREFA 3 — QUALIDADE**


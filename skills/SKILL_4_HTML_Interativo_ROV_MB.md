# SKILL 4 — APRESENTAÇÃO HTML INTERATIVA DO PROJETO ROV-MB
## Transformar as Tarefas 1–3 em um registro acadêmico web, estruturado e histórico

### MISSÃO

Esta skill deve ser executada **somente depois** de concluídas e revisadas:

- **Tarefa 1 — TAP**
- **Tarefa 2 — EAP + Dicionário da EAP**
- **Tarefa 3 — Gerenciamento da Qualidade**

O objetivo é transformar todo o conteúdo consolidado das três tarefas em uma **página HTML única, acadêmica, limpa, moderna e interativa**, adequada para publicação em um repositório GitHub e posterior uso via GitHub Pages.

O HTML não substitui os documentos acadêmicos. Ele é uma **camada de apresentação, documentação e histórico**, preservando fielmente o conteúdo produzido nas tarefas.

A página deve funcionar como um “arquivo vivo” do desenvolvimento do projeto.

---

# 1. PRINCÍPIO CENTRAL

A página deve:

**preservar o conteúdo → organizar visualmente → facilitar navegação → mostrar relações entre documentos → registrar evolução.**

Ela NÃO deve:
- inventar conteúdo;
- corrigir silenciosamente o projeto;
- alterar requisitos;
- modificar códigos da EAP;
- criar escopo;
- reescrever tecnicamente o TAP;
- transformar a documentação em uma apresentação genérica;
- copiar elementos sem relação com o ROV-MB.

Quando houver conflito entre aparência e conteúdo, **o conteúdo vence**.

---

# 2. FONTES QUE DEVEM SER USADAS

A IA deve trabalhar obrigatoriamente sobre os documentos finais:

### Tarefa 1
**TAP — Termo de Abertura do Projeto**

É a fonte para:
- identificação;
- objetivo;
- descrição do projeto;
- escopo;
- requisitos de alto nível;
- stakeholders;
- restrições;
- riscos;
- entregas;
- cronograma/marcos;
- critérios de término;
- demais informações efetivamente presentes no TAP.

### Tarefa 2
**EAP + Dicionário da EAP**

É a fonte para:
- estrutura final da EAP;
- códigos;
- nomes dos pacotes;
- especificações;
- critérios de aceitação;
- organização final após as críticas do Cmdt Huback.

### Tarefa 3
**Matriz de Rastreabilidade + Matriz da Qualidade**

É a fonte para:
- requisitos rastreados;
- stakeholders;
- prioridades;
- tipos;
- status;
- indicadores;
- metas;
- técnicas de medição;
- frequência;
- responsáveis;
- plano de resposta.

### Referência de design

Usar como inspiração o projeto **OpenDesign**, especialmente sua filosofia de artefato web, documentação visual, navegação clara e outputs HTML. O repositório possui templates para documentação e outras experiências web, mas o conteúdo do ROV-MB deve permanecer próprio e acadêmico.

Referência:
https://github.com/nexu-io/open-design

---

# 3. FORMATO TÉCNICO DO ARTEFATO

Preferência obrigatória:

## Um único arquivo

```text
index.html
```

O arquivo deve conter:
- HTML;
- CSS;
- JavaScript;

preferencialmente embutidos no próprio documento.

Evitar dependências externas sempre que possível.

O objetivo é que:

> “baixar o index.html e abrir no navegador” 

seja suficiente para visualizar a documentação.

O projeto deve funcionar também em hospedagem estática como GitHub Pages.

---

# 4. ESTRUTURA GERAL DA PÁGINA

A estrutura recomendada é:

```text
ROV-MB
│
├── Header / Capa
│
├── Navegação
│
├── 01 — Tarefa 1 · TAP
│
├── 02 — Tarefa 2 · EAP + Dicionário
│
├── 03 — Tarefa 3 · Gerenciamento da Qualidade
│
├── Histórico / Evolução
│
└── Referências / Metadados
```

A navegação deve permitir saltar rapidamente para cada seção.

Preferencialmente usar:
- navegação fixa;
- scroll suave;
- indicador da seção atual;
- botão “voltar ao topo”.

---

# 5. HEADER / CAPA

O topo deve comunicar imediatamente:

**PROJETO ROV-MB**

**Aquisição, Integração e Validação de um ROV Modular**

Depois, um pequeno conjunto de metadados:

- Tarefa 1 — TAP
- Tarefa 2 — EAP + Dicionário
- Tarefa 3 — Gerenciamento da Qualidade
- Gestão de Projetos / GDP
- Marinha do Brasil
- registro/documentação acadêmica

Evitar uma capa exagerada.

O estilo deve lembrar:
- documentação técnica;
- relatório de engenharia;
- sistema de documentação;
- arquivo acadêmico digital.

---

# 6. DIREÇÃO VISUAL

A estética deve ser:

**acadêmica + técnica + naval + minimalista.**

Características:

- fundo claro;
- branco/off-white;
- azul-marinho ou azul muito escuro como cor de identidade;
- cinzas neutros;
- uma cor de destaque discreta;
- bordas finas;
- sombras suaves;
- tipografia moderna;
- grande espaçamento;
- hierarquia tipográfica forte;
- poucos elementos decorativos.

Evitar:
- gradientes excessivos;
- neon;
- estética gamer;
- excesso de cards;
- efeitos chamativos;
- aparência de landing page comercial;
- excesso de ícones.

O sistema visual deve parecer um **documento técnico premium**, não um site de marketing.

---

# 7. SEÇÃO 01 — TAREFA 1 / TAP

A apresentação do TAP deve ser uma síntese organizada, e não necessariamente a reprodução página por página do documento.

Estruturar em blocos navegáveis.

### Bloco: Identificação

Mostrar:
- nome do projeto;
- objetivo geral;
- finalidade.

### Bloco: Objetivos

Apresentar os objetivos do TAP em uma lista ou timeline.

### Bloco: Requisitos de alto nível

Apresentar em tabela ou cards compactos.

Exemplos apenas quando presentes no TAP:
- modularidade;
- operação por uma pessoa;
- água doce/salgada;
- profundidade;
- autonomia;
- umbilical;
- imagem/vídeo;
- segurança;
- treinamento;
- documentação;
- sobressalentes;
- testes.

### Bloco: Entregas-chave

Mostrar as entregas do TAP em uma sequência visual.

### Bloco: Stakeholders

Mostrar em tabela ou grupos.

### Bloco: Restrições e riscos

Usar apresentação compacta.

### Bloco: Marcos

Se o TAP final possuir cronograma/marcos, apresentar como timeline.

### Regra

Não inventar indicadores, datas, cargos ou informações que não estejam na Tarefa 1.

---

# 8. SEÇÃO 02 — TAREFA 2 / EAP + DICIONÁRIO

Esta deve ser provavelmente a seção visualmente mais forte da página.

## 8.1 EAP interativa

Apresentar a EAP em forma de árvore/diagrama.

A árvore deve permitir:
- expandir;
- recolher;
- clicar em pacote;
- mostrar código;
- mostrar nome;
- visualizar relação pai-filho.

Exemplo conceitual:

```text
PROJETO ROV-MB
│
├── 1. GERENCIAMENTO DO PROJETO
│
├── 2. NECESSIDADES E REQUISITOS
│
├── 3. RECEBIMENTO DO ROV
│   ├── 3.1 TAF
│   ├── 3.2 TAM
│   ├── 3.3 Aprovação das planilhas
│   └── 3.4 Sobressalentes e consumíveis
│
└── 4. CAPACITAÇÃO
    ├── 4.1 Cursos
    └── 4.2 Documentação técnica
```

IMPORTANTE:
usar **a EAP final efetivamente aprovada**, e não esta representação conceitual se ela divergir da versão final.

## 8.2 Dicionário interativo

Ao clicar em um pacote da EAP, abrir um painel ou modal contendo:

- código;
- pacote de trabalho;
- especificação;
- critério de aceitação.

Isso permite que a EAP permaneça compacta sem perder detalhe.

## 8.3 Destacar as decisões do orientador

Criar uma pequena área:

**“Revisões da EAP após orientação”**

Mostrar visualmente:

```text
EAP ORIGINAL
     ↓
Críticas do Cmdt Huback
     ↓
EAP COMPACTADA
```

Evidenciar, com texto curto e fiel às decisões já tomadas:

- **Fornecedor → eliminado**
- **V&V/Testes separado → absorvido pelo Recebimento**
- **Encerramento → absorvido pelo Gerenciamento**
- **Gerenciamento → consolidado em um único pacote**
- **Capacitação → inclui gestão do conhecimento/documentação**

Essa seção é importante porque registra o raciocínio histórico da evolução da EAP.

Não inventar justificativas além das registradas nas anotações/reunião.

---

# 9. SEÇÃO 03 — TAREFA 3 / QUALIDADE

Criar duas subseções claramente separadas:

## 9.1 Matriz de Rastreabilidade

Tabela interativa com:

- Código EAP
- Descrição
- Stakeholder
- Prioridade
- Tipo
- Status

Funcionalidades recomendadas:
- busca textual;
- filtro por código EAP;
- filtro por prioridade;
- filtro por tipo;
- filtro por stakeholder;
- cabeçalho fixo;
- ordenação de colunas quando fizer sentido.

## 9.2 Matriz de Qualidade

Tabela interativa com:

- Requisito
- Indicador
- Meta
- Técnica de medição
- Frequência
- Quem mede
- Ação
- Quando
- Responsável

Como esta tabela pode ser larga, usar:
- scroll horizontal;
- quebra de linha inteligente;
- coluna de requisito fixa, se viável;
- modal/detalhamento ao clicar em uma linha, caso necessário.

---

# 10. VISUALIZAÇÃO DA RASTREABILIDADE

Criar uma representação visual opcional da cadeia:

```text
REQUISITO
   ↓
PACOTE DA EAP
   ↓
INDICADOR
   ↓
META
   ↓
MÉTODO DE MEDIÇÃO
   ↓
PLANO DE RESPOSTA
```

Ela deve ser explicativa, não substituir as tabelas.

Pode ser construída com elementos simples de HTML/CSS.

---

# 11. HISTÓRICO / EVOLUÇÃO

Como o objetivo é criar um registro histórico, incluir uma seção:

**“Evolução documental do projeto”**

Timeline sugerida:

```text
Tarefa 1
TAP
↓
Tarefa 2
EAP + Dicionário
↓
Reunião com orientador
Críticas e decisões
↓
EAP compactada
↓
Tarefa 3
Gerenciamento da Qualidade
```

Deixar claro que o HTML é uma fotografia documental daquela versão do projeto.

Não inserir datas fictícias. Usar apenas datas existentes nas fontes ou omitir quando não houver.

---

# 12. SEÇÃO DE REFERÊNCIAS

Ao final:

### Documentos do projeto
- TAP
- EAP + Dicionário
- Matriz de Rastreabilidade
- Matriz da Qualidade

### Referências metodológicas
- PMBOK, quando efetivamente utilizado nas tarefas;
- material da disciplina;
- 10 Mandamentos da EAP;
- OpenDesign, somente como referência de apresentação/design.

Não fabricar referências bibliográficas.

---

# 13. INTERAÇÃO

O HTML deve ser interativo, mas a interação deve melhorar a consulta.

Priorizar:

### Navegação
- menu fixo;
- scroll suave;
- anchors;
- destaque da seção ativa.

### EAP
- expandir/recolher;
- seleção de pacote;
- painel de detalhes.

### Tabelas
- busca;
- filtros;
- ordenação;
- detalhes expansíveis.

### Extras úteis
- botão copiar código;
- botão “voltar ao topo”;
- alternância claro/escuro, se implementada de forma simples;
- indicador de progresso de leitura, opcional.

Não adicionar animações que distraiam.

---

# 14. DESIGN RESPONSIVO

A página deve funcionar em:

- desktop;
- notebook;
- tablet;
- celular.

No celular:
- menu deve virar drawer ou menu compacto;
- tabelas devem permitir scroll horizontal;
- árvore da EAP deve continuar legível;
- modais devem ocupar quase toda a tela.

---

# 15. ACESSIBILIDADE E QUALIDADE TÉCNICA

Aplicar boas práticas básicas:

- HTML semântico;
- hierarquia correta de headings;
- contraste adequado;
- foco visível;
- botões reais para ações;
- `aria-label` quando necessário;
- navegação por teclado;
- não depender apenas de cor para comunicar estado.

Não usar JavaScript desnecessariamente complexo.

---

# 16. METADADOS DA PÁGINA

Incluir no `<head>`:

- título;
- descrição;
- viewport;
- tema de cor;
- charset.

Exemplo de título:

`ROV-MB — Gestão de Projetos | TAP, EAP e Qualidade`

---

# 17. ESTILO DE REDAÇÃO

A linguagem da interface deve ser:

- português;
- acadêmica;
- objetiva;
- técnica;
- impessoal.

Evitar:
- linguagem publicitária;
- frases motivacionais;
- “super”, “incrível”, “revolucionário”;
- textos genéricos de UX.

A página apresenta um trabalho acadêmico.

---

# 18. NÃO REESCREVER O CONTEÚDO SEM NECESSIDADE

A IA pode:
- condensar uma introdução;
- transformar listas em cards;
- reorganizar visualmente;
- colocar conteúdo em abas;
- transformar dados em tabelas;
- criar títulos de navegação.

A IA NÃO deve:
- mudar a interpretação dos requisitos;
- corrigir o TAP por conta própria;
- alterar metas;
- mudar prioridades;
- criar critérios de aceitação;
- mudar nomes/códigos da EAP;
- inventar stakeholders;
- acrescentar fornecedores;
- reintroduzir V&V como pacote;
- reintroduzir encerramento como pacote;
- criar conteúdo não existente nas tarefas.

Se houver uma possível inconsistência factual, preservar o documento-fonte e sinalizar a questão em uma área de observações, em vez de corrigir silenciosamente.

---

# 19. PRINCÍPIO “DOCUMENTO + INTERFACE”

Cada informação importante deve continuar acessível mesmo que o JavaScript seja desativado.

Por isso:
- o conteúdo principal deve existir no HTML;
- JavaScript deve melhorar a navegação;
- o HTML não deve ser apenas um aplicativo vazio que monta tudo dinamicamente.

---

# 20. ESTRUTURA DE ARQUIVOS RECOMENDADA

Se o repositório for mantido como projeto simples:

```text
rov-mb-project/
│
├── index.html
├── README.md
│
└── assets/
    └── (somente se houver imagens ou arquivos realmente necessários)
```

A preferência é não depender de assets externos.

Se imagens/documentos originais forem incluídos, fazer isso apenas quando houver necessidade e quando for permitido pelo contexto acadêmico.

---

# 21. README DO REPOSITÓRIO

Criar também um `README.md` curto explicando:

- o que é o repositório;
- qual projeto ele documenta;
- quais tarefas estão registradas;
- que o `index.html` é a interface documental;
- como abrir localmente;
- como publicar via GitHub Pages.

Exemplo de estrutura:

```text
# ROV-MB — Gerenciamento de Projetos

Documentação acadêmica do projeto ROV-MB.

## Conteúdo
- Tarefa 1 — TAP
- Tarefa 2 — EAP + Dicionário
- Tarefa 3 — Gerenciamento da Qualidade

## Visualização
Abra `index.html` localmente ou publique no GitHub Pages.
```

Não inventar autores, universidade, professor ou curso caso essas informações não estejam disponíveis nos documentos.

---

# 22. CHECKLIST DE ENTREGA

Antes de finalizar o HTML:

## Conteúdo
- [ ] Tarefa 1 presente.
- [ ] Tarefa 2 presente.
- [ ] EAP final correta.
- [ ] Dicionário final correto.
- [ ] Tarefa 3 presente.
- [ ] Matriz de Rastreabilidade presente.
- [ ] Matriz de Qualidade presente.
- [ ] histórico das decisões presente.

## Coerência
- [ ] códigos EAP corretos;
- [ ] nenhum pacote eliminado reapareceu;
- [ ] requisitos correspondem ao TAP;
- [ ] matriz usa a EAP final;
- [ ] não existem dados inventados.

## UX
- [ ] navegação funcional;
- [ ] EAP interativa;
- [ ] filtros funcionando;
- [ ] tabelas legíveis;
- [ ] responsivo;
- [ ] acessível;
- [ ] sem erros de JavaScript.

## Publicação
- [ ] `index.html` abre sozinho;
- [ ] nenhum caminho local está quebrado;
- [ ] assets relativos, quando existirem;
- [ ] compatível com GitHub Pages.

---

# 23. CRITÉRIO FINAL DE QUALIDADE

O resultado deve parecer:

> **um arquivo acadêmico digital interativo de um projeto de engenharia**, e não um simples documento Word convertido para HTML.

A página deve permitir que alguém que nunca viu as tarefas anteriores compreenda:

1. o que é o projeto;
2. o que foi definido no TAP;
3. como o escopo foi estruturado na EAP;
4. como a EAP foi compactada após orientação do professor/orientador;
5. o que cada pacote entrega;
6. como os requisitos são rastreados;
7. como a qualidade será medida;
8. como as três tarefas formam uma sequência documental.

---

# 24. ORDEM DE CONSTRUÇÃO

A IA deve executar nesta ordem:

### PASSO 1
Ler integralmente:
- Tarefa 1;
- Tarefa 2;
- Tarefa 3.

### PASSO 2
Extrair a estrutura de conteúdo sem alterar os documentos.

### PASSO 3
Criar a arquitetura da página.

### PASSO 4
Construir a identidade visual.

### PASSO 5
Implementar a EAP interativa.

### PASSO 6
Implementar o Dicionário interativo.

### PASSO 7
Implementar as matrizes.

### PASSO 8
Implementar filtros e navegação.

### PASSO 9
Adicionar a seção de histórico.

### PASSO 10
Testar conteúdo e interação.

### PASSO 11
Abrir o HTML em navegador e verificar visualmente.

### PASSO 12
Auditar novamente contra as três tarefas.

---

# 25. REGRA MAIS IMPORTANTE

O HTML é uma **representação da documentação**, não uma nova versão do projeto.

Primeiro:

**Tarefa 1 → Tarefa 2 → Tarefa 3**

Depois:

**Documentação final → HTML interativo**

Nunca:

**HTML → alterar o conteúdo das tarefas.**

A interface deve tornar o trabalho mais claro, rastreável, consultável e histórico, mantendo fidelidade acadêmica ao material-fonte.

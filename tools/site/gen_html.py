# -*- coding: utf-8 -*-
"""Gera o index.html (arquivo único) a partir de data.json (extraído do documento único final).
Uso: python3 -I gen_html.py data.json old.css app.js extra.css REPO_DIR OUT.html"""
import json, re, sys, os, html
from urllib.parse import quote

DATA, CSS, JS, EXTRA, REPO, OUT = sys.argv[1:7]
D = json.load(open(DATA, encoding='utf-8'))
e = lambda s: html.escape(str(s), quote=True)

DOC = 'entregas/GDP - Grupo I - ROV-MB - Tarefas 1 a 3'


def href(path):
    return quote(path)


def link(path, text=None):
    assert os.path.exists(os.path.join(REPO, path)), path
    return f'<a href="{href(path)}">{e(text or path)}</a>'


def split_num(s):
    m = re.match(r'^([0-9]+(?:\.[0-9]+)?|M-\d+)\)\s*(.*)$', s)
    return (m.group(1), m.group(2)) if m else (None, s)


def kv(items):
    out = []
    for it in items:
        k, t = split_num(it)
        out.append(f'<li><span class="k">{e(k or "")}</span><span>{e(t)}</span></li>')
    return '<ul class="kv just">' + ''.join(out) + '</ul>'


def block(title, inner, count=None, bid=None):
    c = f' <span class="count">{count}</span>' if count is not None else ''
    i = f' id="{bid}"' if bid else ''
    return f'<div class="block"{i}><h3>{e(title)}{c}</h3>{inner}</div>'


TAP = {s['n']: s for s in D['tap']}
NOMES_AGG = {'3': 'RECEBIMENTO DO ROV', '4': 'CAPACITAÇÃO'}
DIC = {r['code']: r for r in D['dicionario']}
RTM = D['rtm']
QM = {q['id']: q for q in D['qm']}


def pkg_name(code):
    return DIC[code]['nome'] if code in DIC else NOMES_AGG[code]


# ============================== CAPA ==============================
campos = dict((a.rstrip(':').upper(), b) for a, b in D['capa']['campos'])
integrantes = [x.strip() for x in campos['INTEGRANTES'].split(';')]
n_reqs_tap = len(TAP[3]['itens'])
cover = f'''<section class="cover" id="topo"><div class="wrap">
<p class="eyebrow">Marinha do Brasil · Diretoria de Ensino da Marinha · Centro de Instrução Almirante Alexandrino</p>
<h1>PROJETO <span class="nowrap">ROV-MB</span></h1>
<p class="subtitle">Recebimento, Integração e Validação de um ROV Modular</p>
<dl class="ident">
<div><dt>Curso</dt><dd>Aperfeiçoamento Avançado para Oficiais em Sistema de Armas</dd></div>
<div><dt>Disciplina</dt><dd>{e(campos['DISCIPLINA'])}</dd></div>
<div><dt>Professor</dt><dd>{e(campos['PROF'])}</dd></div>
<div><dt>Grupo</dt><dd>{e(campos['GRUPO'])}</dd></div>
<div class="wide"><dt>Integrantes</dt><dd>{' · '.join(e(x) for x in integrantes)}</dd></div>
</dl>
<div class="dl-row"><a class="btn primary" href="{href(DOC + '.docx')}" download>Documento único (.docx)</a>
<a class="btn" href="{href(DOC + '.pdf')}">Documento único (.pdf)</a></div>
<ol class="tasks"><li><a href="#tap"><span class="t"><span class="mono">01</span>Tarefa 1 · TAP</span><span class="d">Termo de Abertura do Projeto</span></a></li>
<li><a href="#eap"><span class="t"><span class="mono">02</span>Tarefa 2 · EAP + Dicionário</span><span class="d">Estrutura analítica e dicionário da EAP</span></a></li>
<li><a href="#qualidade"><span class="t"><span class="mono">03</span>Tarefa 3 · Rastreabilidade e Qualidade</span><span class="d">Matriz de Rastreabilidade de Requisitos e Matriz de Qualidade</span></a></li></ol>
<dl class="facts"><div><dt>{n_reqs_tap}</dt><dd>requisitos de alto nível no TAP</dd></div>
<div><dt>{len(TAP[4]['itens'])}</dt><dd>entregas-chave no TAP</dd></div>
<div><dt>{len(DIC) + len(NOMES_AGG)}</dt><dd>elementos na EAP, {len(DIC)} pacotes de trabalho</dd></div>
<div><dt>{len(RTM)}</dt><dd>requisitos na Matriz de Rastreabilidade</dd></div>
<div><dt>{len(QM)}</dt><dd>requisitos com métricas na Matriz de Qualidade</dd></div></dl>
</div></section>'''

# ============================== TAP ==============================
desc = TAP[1]['itens']
obj = TAP[2]['itens']
ident = f'''<div class="grid-2"><div class="just"><h4>{e(D['tap_titulo'][1].replace('PROJETO: ', ''))}</h4>{''.join(f'<p>{e(p)}</p>' for p in desc)}</div>
<div><div class="panel navy"><h4>Objetivo do projeto</h4>{''.join(f'<p>{e(p)}</p>' for p in obj)}
<p class="small tags"><span class="tag">5 unidades</span><span class="tag">10 m nominal</span><span class="tag">30 m máxima</span><span class="tag">autonomia ≥ 2h30</span><span class="tag">operação por 1 pessoa</span><span class="tag">câmera + iluminação</span></p></div></div></div>'''

# Orçamento
orc = TAP[7]['itens']
linhas, total = [], None
for it in orc[1:]:
    k, t = split_num(it)
    if k:
        dsc, val = t.rsplit(' — ', 1)
        linhas.append((k, dsc, val.rstrip(';. e').rstrip(';')))
    elif it.startswith('Total'):
        total = it.split(':', 1)[1].strip().rstrip('.')
orc_html = (f'<p class="just">{e(orc[0])}</p><div class="tbl-wrap"><table class="tbl"><caption class="sr-only">Resumo do orçamento</caption>'
            '<thead><tr><th scope="col">Nº</th><th scope="col">Grupo de custo</th><th scope="col" class="r">Valor estimado</th></tr></thead><tbody>'
            + ''.join(f'<tr><td class="c">{e(k)}</td><td>{e(d)}</td><td class="r nowrap">{e(v)}</td></tr>' for k, d, v in linhas)
            + f'</tbody><tfoot><tr><th scope="row" colspan="2">Total estimado</th><td class="r nowrap"><strong>{e(total)}</strong></td></tr></tfoot></table></div>')

# Partes interessadas
stake = '<ul class="stake">' + ''.join(
    (lambda k, t: f'<li><span class="k">{e(k)}</span><span>{e(t)}</span></li>')(*split_num(it)) for it in TAP[8]['itens']) + '</ul>'

# Riscos
rk = TAP[9]['itens']
i_op = next(i for i, x in enumerate(rk) if x.startswith('Descrição das Oportunidades'))
riscos = (f'<div class="grid-2e"><div><h4>{e(rk[0].rstrip(":"))}</h4>{kv(rk[1:i_op])}</div>'
          f'<div><h4>{e(rk[i_op].rstrip(":"))}</h4>{kv(rk[i_op + 1:])}</div></div>')

# Marcos
mk = TAP[11]['itens']
ms_rows = []
for it in mk:
    k, t = split_num(it)
    if not k:
        continue
    txt_, prazo = t.rsplit(': ', 1)
    prazo = prazo.rstrip(';. e').rstrip(';')
    m = int(re.search(r'T0 \+ (\d+)', prazo).group(1))
    ms_rows.append(f'<div class="ms-row"><div class="id">{e(k)}</div><div class="tx">{e(txt_)}</div><div class="t0">{e(prazo)}</div>'
                   f'<div class="trk"><div class="track" aria-hidden="true"><i style="left:{m / 18 * 100:.2f}%"></i></div></div></div>')
ticks = ''.join(f'<span style="left:{v / 18 * 100:.2f}%">{v}</span>' for v in range(0, 19, 3))
marcos = (f'<div class="ms" role="table" aria-label="Cronograma de marcos"><div class="ms-scale" role="row"><div>Marco</div><div>Descrição</div>'
          f'<div>Prazo</div><div><div class="ticks">{ticks}</div><span class="sr-only">Meses após T0</span></div></div>{"".join(ms_rows)}</div>'
          f'<p class="small muted">{e(mk[-1])}</p>')

paras = lambda n: ''.join(f'<p>{e(p)}</p>' for p in TAP[n]['itens'])
sig = D['assinaturas']
assin = ('<div class="sigs">' + ''.join(f'<div class="sig"><span class="line"></span><strong>{e(a)}</strong><span>{e(b)}</span></div>'
                                       for a, b in sig['campos']) + '</div>')

tap = f'''<section class="doc" id="tap" aria-labelledby="tap-titulo"><div class="wrap">
<header class="sec-head"><span class="sec-num">01</span><h2 id="tap-titulo">Tarefa 1 · Termo de Abertura do Projeto</h2>
<p class="src">Seção II do documento único · {link(DOC + '.docx', 'documento único (.docx)')}</p></header>
{block('1 · Descrição do projeto e 2 · Objetivo', ident)}
{block('3 · Requisitos de alto nível', kv(TAP[3]['itens']), len(TAP[3]['itens']))}
{block('4 · Entregas-chave do projeto', kv(TAP[4]['itens']), len(TAP[4]['itens']))}
<div class="grid-2e">{block('5 · Justificativas do projeto', kv(TAP[5]['itens']))}{block('6 · Restrições do projeto', kv(TAP[6]['itens']))}</div>
{block('7 · Resumo do orçamento do projeto', orc_html)}
{block('8 · Partes interessadas do projeto', stake, len(TAP[8]['itens']))}
{block('9 · Riscos de alto nível', riscos)}
{block('10 · Indicadores-chave do sucesso do projeto', kv(TAP[10]['itens']))}
{block('11 · Resumo do cronograma de marcos', marcos)}
<div class="grid-2e">{block('12 · Gerente do projeto', '<div class="just">' + paras(12) + '</div>')}{block('13 · Patrocinador', '<div class="just">' + paras(13) + '</div>')}</div>
<div class="grid-2e">{block('14 · Requisitos para aprovação do projeto', '<div class="just">' + paras(14) + '</div>')}{block('15 · Critérios de término do projeto', '<div class="just">' + paras(15) + '</div>')}</div>
{block(sig['titulo'], assin)}
</div></section>'''

# ============================== EAP ==============================
def node(code, l1=False):
    n = pkg_name(code)
    tipo = 'Pacote de trabalho' if code in DIC else 'Elemento de agregação'
    cls = 'node-btn' + (' l1-btn' if l1 else '') + (' wp-l1' if l1 and code in DIC else '')
    return (f'<button type="button" class="{cls}" data-code="{code}" aria-pressed="false" '
            f'aria-label="{e(code)} {e(n)} — {tipo}. Abrir no Dicionário"><span class="code">{e(code)}</span><span class="name">{e(n)}</span></button>')


l1 = []
for top in ('1', '2', '3', '4'):
    kids = sorted(c for c in DIC if c.startswith(top + '.'))
    if kids:
        sub = ''.join(f'<li data-code="{c}"><div class="node">{node(c)}</div></li>' for c in kids)
        l1.append(f'<li class="has-children agg" data-code="{top}"><div class="node">{node(top, True)}'
                  f'<button type="button" class="toggle" data-code="{top}" aria-expanded="true" aria-controls="ch-{top}" '
                  f'aria-label="Recolher {top}">−</button></div><ul class="wbs-l2" id="ch-{top}">{sub}</ul></li>')
    else:
        l1.append(f'<li data-code="{top}"><div class="node">{node(top, True)}</div><p class="leafnote">Pacote de trabalho</p></li>')
wbs = (f'<div class="wbs-frame"><div class="wbs"><div class="wbs-root"><span class="node-btn" style="cursor:default">PROJETO ROV-MB</span></div>'
       f'<ul class="wbs-l1">{"".join(l1)}</ul></div></div>'
       '<div class="detail" id="eap-detail" aria-live="polite"><p class="detail-empty">Selecione um elemento da EAP para ver a '
       'especificação, o critério de aceitação e os requisitos rastreados ao pacote.</p></div>')
dic_rows = ''.join(
    f'<tr id="dic-{r["code"]}" data-code="{r["code"]}"><td class="c">{e(r["code"])}</td><td>{e(r["nome"])}</td>'
    f'<td class="just">{e(r["spec"])}</td><td class="just">{e(r["crit"])}</td></tr>' for r in D['dicionario'])
dic = (f'<div class="tbl-wrap"><table class="tbl dict"><caption class="sr-only">Dicionário da EAP</caption><thead><tr>'
       '<th scope="col">Código na EAP</th><th scope="col">Pacote de trabalho</th><th scope="col">Especificação</th>'
       f'<th scope="col">Critério de aceitação</th></tr></thead><tbody>{dic_rows}</tbody></table></div>')
eap = f'''<section class="doc" id="eap" aria-labelledby="eap-titulo"><div class="wrap">
<header class="sec-head"><span class="sec-num">02</span><h2 id="eap-titulo">Tarefa 2 · EAP e Dicionário da EAP</h2>
<p class="src">Seções III e IV do documento único (Processo 5.4 PMBOK)</p></header>
<p class="lead just">{e(D['enunciado']['texto'])}</p>
<div class="block" id="eap-arvore"><h3>Estrutura Analítica do Projeto</h3>
<div class="wbs-toolbar"><div class="legend"><span><span class="sw agg"></span>Elemento de primeiro nível</span><span><span class="sw wp"></span>Pacote de trabalho de segundo nível</span><span>Selecione um elemento para ver o Dicionário</span></div>
<div class="btn-group js-only"><button type="button" class="btn" id="wbs-expand">Expandir tudo</button><button type="button" class="btn" id="wbs-collapse">Recolher tudo</button></div></div>
{wbs}</div>
{block('Dicionário da EAP', dic, f'{len(DIC)} pacotes', 'dicionario')}
</div></section>'''

# ============================== MATRIZES ==============================
codes = sorted({r['code'] for r in RTM}, key=lambda c: [int(x) for x in c.split('.')])
stks = sorted({r['stk'] for r in RTM})
tipos = sorted({r['tipo'] for r in RTM})
opt = lambda vals, lab=lambda v: v: ''.join(f'<option value="{e(v)}">{e(lab(v))}</option>' for v in vals)
PRI = {'1': 'Imprescindível', '2': 'Desejável', '3': 'Opcional'}

rtm_rows = ''.join(
    f'<tr data-id="{e(r["id"])}" data-code="{e(r["code"])}" data-pri="{e(r["pri"])}" data-tipo="{e(r["tipo"])}" data-stk="{e(r["stk"])}" '
    f'tabindex="0" aria-label="{e(r["id"])}: abrir detalhes"><td class="c">{e(r["code"])}</td><td class="id">{e(r["id"])}</td>'
    f'<td class="just">{e(r["desc"])}</td><td>{e(r["stk"])}</td><td><span class="pri p{e(r["pri"])}"><b>{e(r["pri"])}</b>{e(PRI[r["pri"]])}</span></td>'
    f'<td>{e(r["tipo"].capitalize())}</td><td class="c">{e(r["status"])}</td></tr>' for r in RTM)
th = lambda key, lab: f'<th scope="col" data-sort="{key}"><button type="button">{e(lab)} <span class="ar" aria-hidden="true">↕</span></button></th>'
rtm = f'''<div class="toolbar" role="search" aria-label="Filtrar a Matriz de Rastreabilidade">
<label class="fld grow"><span>Busca</span><input type="search" id="mr-q" placeholder="Texto, ID ou stakeholder"></label>
<label class="fld"><span>Código EAP</span><select id="mr-eap"><option value="">Todos</option>{opt(codes, lambda c: c + ' ' + pkg_name(c).capitalize())}</select></label>
<label class="fld"><span>Prioridade</span><select id="mr-pri"><option value="">Todas</option>{opt(sorted({r['pri'] for r in RTM}), lambda p: p + ' — ' + PRI[p])}</select></label>
<label class="fld"><span>Tipo</span><select id="mr-tipo"><option value="">Todos</option>{opt(tipos, lambda t: t.capitalize())}</select></label>
<label class="fld"><span>Stakeholder</span><select id="mr-stk"><option value="">Todos</option>{opt(stks)}</select></label>
<button type="button" class="btn" id="mr-clear">Limpar</button></div>
<p class="counter" id="mr-count" aria-live="polite">{len(RTM)} requisitos</p>
<div class="mtx-wrap"><table class="mtx" id="mr"><caption class="sr-only">Matriz de Rastreabilidade de Requisitos — selecione uma linha para ver os detalhes</caption>
<thead><tr>{th('code', 'Código EAP')}{th('id', 'ID')}{th('desc', 'Descrição')}{th('stk', 'Stakeholder')}{th('pri', 'Prioridade')}{th('tipo', 'Tipo do requisito')}{th('status', 'Status')}</tr></thead>
<tbody>{rtm_rows}</tbody></table></div>
<ul class="plain small muted legend-doc">{''.join(f'<li>{e(x)}</li>' for x in D['rtm_legenda'])}</ul>'''


def cell(lines, cls='just'):
    return f'<td class="{cls}">' + '<br>'.join(e(x) for x in lines) + '</td>'


qm_rows = ''.join(
    f'<tr data-id="{e(q["id"])}" data-code="{e(q["id"].rsplit(".", 1)[0])}" tabindex="0" aria-label="{e(q["id"])}: abrir detalhes">'
    f'<td class="just"><span class="rid">{e(q["id"])}</span>{e(q["req"])}</td>'
    + cell(q['ind']) + cell(q['meta']) + cell(q['tec']) + cell(q['freq']) + cell(q['quem'], '')
    + cell(q['acao']) + cell(q['quando']) + cell(q['resp'], '') + '</tr>' for q in D['qm'])
qcodes = sorted({q['id'].rsplit('.', 1)[0] for q in D['qm']}, key=lambda c: [int(x) for x in c.split('.')])
qm = f'''<p class="just">{e(D['qm_intro'][0])}</p>
<div class="toolbar" role="search" aria-label="Filtrar a Matriz de Qualidade">
<label class="fld grow"><span>Busca</span><input type="search" id="mq-q" placeholder="Texto, ID, indicador ou responsável"></label>
<label class="fld"><span>Código EAP</span><select id="mq-eap"><option value="">Todos</option>{opt(qcodes, lambda c: c + ' ' + pkg_name(c).capitalize())}</select></label>
<button type="button" class="btn" id="mq-clear">Limpar</button></div>
<p class="counter" id="mq-count" aria-live="polite">{len(QM)} requisitos</p>
<div class="mtx-wrap"><table class="mtx" id="mq"><caption class="sr-only">Matriz de Qualidade — selecione uma linha para ver os detalhes</caption>
<thead><tr><th scope="col" rowspan="2">Requisito</th><th scope="col" rowspan="2">Indicador</th><th scope="col" rowspan="2">Meta</th><th scope="col" rowspan="2">Técnica de medição</th>
<th scope="col" rowspan="2">Frequência</th><th scope="col" rowspan="2">Quem mede</th><th scope="colgroup" colspan="3" class="grp">Plano de resposta</th></tr>
<tr><th scope="col" class="h2">Ação</th><th scope="col" class="h2">Quando</th><th scope="col" class="h2">Responsável</th></tr></thead>
<tbody><tr class="band"><td colspan="9">{e(D['qm_faixa'])}</td></tr>{qm_rows}</tbody></table></div>'''

qual = f'''<section class="doc" id="qualidade" aria-labelledby="qualidade-titulo"><div class="wrap">
<header class="sec-head"><span class="sec-num">03</span><h2 id="qualidade-titulo">Tarefa 3 · Rastreabilidade de Requisitos e Qualidade</h2>
<p class="src">Seções V e VI do documento único (Processos 5.2 e 8.1 PMBOK)</p></header>
<div class="legend-line"><span><strong>ID:</strong> pacote da EAP . sequência -Q</span><span><strong>Prioridade:</strong> 1 imprescindível · 2 desejável · 3 opcional</span><span><strong>Status:</strong> NI — não iniciada</span></div>
{block('Matriz de Rastreabilidade de Requisitos', rtm, None, 'rastreabilidade')}
{block('Matriz de Qualidade', qm, None, 'matriz-qualidade')}
</div></section>'''

# ============================== HISTÓRICO ==============================
RH = 'tarefas/revisao-huback/'
hist_items = [
    ('key', 'Documento-base', 'Tarefa 1 — TAP (versão original)', 'Termo de Abertura do Projeto elaborado pelo grupo.',
     link('tarefas/Tarefa 01 - TAP.docx', 'tarefas/Tarefa 01 - TAP.docx')),
    ('', 'Primeira estruturação do escopo', 'Tarefa 2 — EAP + Dicionário (versão original)',
     'EAP com 7 elementos de primeiro nível (Gerenciamento, Necessidades e Requisitos, Fornecedor, Recebimento do ROV, V&V, Capacitação e Encerramento) e 23 pacotes de trabalho.',
     link('tarefas/Tarefa 02 - EAP e Dicionário.docx', 'tarefas/Tarefa 02 - EAP e Dicionário.docx')),
    ('', 'Orientação do professor', 'Compactação da EAP',
     'Gerenciamento em pacote único; Fornecedor eliminado; V&V absorvido pelo Recebimento do ROV (TAF, TAM, aprovação das planilhas de testes, sobressalentes e consumíveis); Encerramento absorvido pelo Gerenciamento; Capacitação com documentação técnica e gestão do conhecimento.',
     ''),
    ('key', 'Entrega para revisão', 'TAP e EAP, Dicionário e Matrizes enviados ao professor',
     'EAP com 4 elementos de primeiro nível e 8 pacotes de trabalho; Matriz de Rastreabilidade com 20 requisitos e Matriz de Qualidade.',
     link(RH + 'GDP Grupo I ROV - TAP (enviado).docx', 'TAP (enviado)') + ' · '
     + link(RH + 'GDP Grupo I ROV - EAP e Matrizes (enviado).docx', 'EAP e Matrizes (enviado)')),
    ('', 'Revisão do Cmdt Huback', 'Comentários e correções',
     'Reunir todas as tarefas em um único documento; montar uma capa com os participantes do grupo; aplicar as correções a carmim no TAP; EAP e Dicionário da EAP aprovados; corrigir a identificação dos requisitos na Matriz de Rastreabilidade e na Matriz de Qualidade.',
     link(RH + 'GDP Grupo I ROV - TAP (revisão Huback).docx', 'TAP (revisão)') + ' · '
     + link(RH + 'GDP Grupo I ROV - EAP e Matrizes (revisão Huback).docx', 'EAP e Matrizes (revisão)')),
    ('key', 'Versão final', 'Documento único das Tarefas 1 a 3',
     'Capa no modelo do CIAA; TAP com as correções do professor, sem aquisição ou contratação, com Gerente do Projeto, Patrocinador, orçamento estimado para 5 unidades e campos de assinatura; EAP e Dicionário mantidos; requisitos identificados por Código EAP e ID (pacote.sequência-Q) nas duas matrizes.',
     link(DOC + '.docx', 'documento único (.docx)') + ' · ' + link(DOC + '.pdf', '.pdf')),
]
hist = '<ol class="timeline">' + ''.join(
    f'<li class="{c}"><span class="dot">{i:02d}</span><span class="kind">{e(k)}</span><h4>{e(t)}</h4><p>{e(p)}</p>'
    + (f'<p class="small muted">Registro: {r}</p>' if r else '') + '</li>' for i, (c, k, t, p, r) in enumerate(hist_items, 1)) + '</ol>'
historico = f'''<section class="doc" id="historico" aria-labelledby="historico-titulo"><div class="wrap">
<header class="sec-head"><span class="sec-num">H</span><h2 id="historico-titulo">Histórico · Evolução documental</h2>
<p class="src">Sequência das etapas do trabalho. As fontes não registram datas.</p></header>{hist}</div></section>'''

# ============================== REFERÊNCIAS ==============================
mat = sorted(f for f in os.listdir(os.path.join(REPO, 'material de apoio')) if f.lower().endswith('.pdf'))
docs_proj = [('Documento único (Word)', DOC + '.docx'), ('Documento único (PDF)', DOC + '.pdf')] + \
            [(f'Revisão do professor · {os.path.splitext(f)[0].replace("GDP Grupo I ROV - ", "")}', RH + f)
             for f in sorted(os.listdir(os.path.join(REPO, RH)))] + \
            [('Original · Tarefa 1', 'tarefas/Tarefa 01 - TAP.docx'), ('Original · Tarefa 2', 'tarefas/Tarefa 02 - EAP e Dicionário.docx')]
refs = f'''<section class="doc" id="referencias" aria-labelledby="referencias-titulo"><div class="wrap">
<header class="sec-head"><span class="sec-num">R</span><h2 id="referencias-titulo">Referências e documentos</h2>
<p class="src">Seção VII do documento único e arquivos do repositório.</p></header>
<div class="grid-2e"><div>{block('Referências do documento', '<ul class="refs">' + ''.join(f'<li>{e(r)}</li>' for r in D['referencias']) + '</ul>')}</div>
<div>{block('Documentos do projeto', '<ul class="refs">' + ''.join(f'<li><span class="k">{e(k)}</span>{link(p, os.path.basename(p))}</li>' for k, p in docs_proj) + '</ul>')}
{block('Material da disciplina', '<ul class="refs">' + ''.join(f'<li>{link("material de apoio/" + f, f)}</li>' for f in mat) + '</ul>')}</div></div>
</div></section>'''

# ============================== PÁGINA ==============================
payload = {'dic': D['dicionario'], 'agg': NOMES_AGG, 'rtm': RTM, 'qm': D['qm'], 'pri': PRI}
css = open(CSS, encoding='utf-8').read() + '\n' + open(EXTRA, encoding='utf-8').read()
js = open(JS, encoding='utf-8').read()
page = f'''<!doctype html>
<html lang="pt-BR" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ROV-MB — Gerenciamento de Projetos</title>
<meta name="description" content="Projeto ROV-MB (Recebimento, Integração e Validação de um ROV Modular) — Grupo I, Curso de Aperfeiçoamento Avançado para Oficiais em Sistema de Armas (CIAA): TAP, EAP e Dicionário, Matriz de Rastreabilidade e Matriz de Qualidade.">
<meta name="theme-color" content="#0f2a4a">
<meta property="og:type" content="website">
<meta property="og:title" content="Projeto ROV-MB — TAP, EAP e Gerenciamento da Qualidade">
<meta property="og:description" content="Grupo I · GDP — Gerenciamento de Projetos · Tarefas 1 a 3.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230f2a4a'/%3E%3Ctext x='16' y='21' font-family='Arial,sans-serif' font-size='12' font-weight='700' fill='white' text-anchor='middle'%3EROV%3C/text%3E%3C/svg%3E">
<style>{css}</style>
<script>document.documentElement.className = document.documentElement.className.replace("no-js", "js");</script>
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="topbar"><div class="topbar-inner"><a class="brand" href="#topo">ROV-MB<small>Grupo I · Tarefas 1–3</small></a>
<button type="button" class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" aria-label="Seções do documento"><ol>
<li><a href="#tap"><span class="n">01 —</span> TAP</a></li><li><a href="#eap"><span class="n">02 —</span> EAP</a></li><li><a href="#qualidade"><span class="n">03 —</span> Qualidade</a></li>
<li><a href="#historico">Histórico</a></li><li><a href="#referencias">Referências</a></li></ol></nav></div><div class="progress" aria-hidden="true"><span></span></div></header>
<main id="conteudo">
{cover}
{tap}
{eap}
{qual}
{historico}
{refs}
</main>
<footer><div class="wrap"><span>Projeto ROV-MB · Grupo I · GDP — Gerenciamento de Projetos · CIAA 2026</span>
<span>Representação do documento único final das Tarefas 1 a 3. <a href="#topo">Voltar ao topo</a></span></div></footer>
<button type="button" class="totop" aria-label="Voltar ao topo">↑ Topo</button>
<dialog id="req-dialog" aria-labelledby="req-dialog-title"><div class="dlg-head"><span class="rid"></span><h3 id="req-dialog-title"></h3>
<button type="button" class="close" aria-label="Fechar detalhes">×</button></div><div class="dlg-body"></div></dialog>
<script type="application/json" id="rov-data">{json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")}</script>
<script>{js}</script>
</body>
</html>
'''
open(OUT, 'w', encoding='utf-8').write(page)
print('ok', OUT, len(page), 'bytes')

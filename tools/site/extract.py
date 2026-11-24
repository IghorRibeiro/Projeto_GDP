# -*- coding: utf-8 -*-
"""Extrai do documento único (DOCX final) os dados exibidos no site. Uso: python3 -I extract.py DOC.docx OUT.json"""
import json, re, sys
import docx
from docx.oxml.ns import qn

d = docx.Document(sys.argv[1])
body = list(d.element.body.iterchildren())


def txt(el):
    return re.sub(r'[ \t]+', ' ', ''.join(t.text or '' for t in el.iter(qn('w:t')))).strip()


def paras(el):
    return [txt(p) for p in el.iter(qn('w:p')) if txt(p)]


def rows(tbl):
    return [[paras(tc) for tc in tr.findall(qn('w:tc'))] for tr in tbl.findall(qn('w:tr'))]


def find(prefix, start=0):
    for i in range(start, len(body)):
        if body[i].tag == qn('w:p') and txt(body[i]).startswith(prefix):
            return i
    raise KeyError(prefix)


def next_tbl(i):
    while body[i].tag != qn('w:tbl'):
        i += 1
    return i


out = {}

# Capa: parágrafos e quadro antes do enunciado
i_en = find('I – ENUNCIADO')
capa_p = [txt(e) for e in body[:i_en] if e.tag == qn('w:p') and txt(e)]
capa_t = next(rows(e) for e in body[:i_en] if e.tag == qn('w:tbl'))
out['capa'] = {'linhas': capa_p, 'campos': [[' '.join(c[0]), ' '.join(c[1])] for c in capa_t]}

# Enunciado
i_tap = find('II – TERMO DE ABERTURA')
en = [txt(e) for e in body[i_en + 1:i_tap] if e.tag == qn('w:p') and txt(e)]
out['enunciado'] = {'texto': en[0], 'intro': en[1], 'docs': en[2:]}

# TAP
i_eap = find('III – ESTRUTURA')
title = rows(body[next_tbl(i_tap)])
out['tap_titulo'] = [p for c in title[0] for p in c]
secs = []
i = next_tbl(i_tap) + 1
while i < i_eap:
    e = body[i]
    s = txt(e) if e.tag == qn('w:p') else ''
    m = re.match(r'^(\d+)\.\s*(.+)$', s)
    if m:
        j = next_tbl(i)
        secs.append({'n': int(m.group(1)), 'titulo': m.group(2).strip(), 'itens': paras(body[j])})
        i = j
    elif s.startswith('Assinatura'):
        sig = rows(body[next_tbl(i)])
        out['assinaturas'] = {'titulo': s, 'campos': [[r[0][0] if r[0] else '' for r in sig[1:3]],
                                                       [r[1][0] if r[1] else '' for r in sig[1:3]]]}
    i += 1
out['tap'] = secs

# Dicionário
i_dic = find('IV – DICIONÁRIO')
dic = rows(body[next_tbl(i_dic)])
out['dicionario'] = [{'code': r[0][0], 'nome': ' '.join(r[1]), 'spec': ' '.join(r[2]), 'crit': ' '.join(r[3])} for r in dic[1:]]

# Matriz de Rastreabilidade
i_rtm = find('V – MATRIZ DE RASTREABILIDADE')
rtm = rows(body[next_tbl(i_rtm)])
out['rtm_head'] = [' '.join(c) for c in rtm[0]]
out['rtm'] = [{'code': r[0][0], 'id': r[1][0], 'desc': ' '.join(r[2]), 'stk': ' '.join(r[3]), 'pri': r[4][0],
               'tipo': ' '.join(r[5]), 'status': r[6][0]} for r in rtm[1:-1]]
out['rtm_legenda'] = [p for c in rtm[-1] for p in c]

# Matriz de Qualidade
i_qm = find('VI – MATRIZ DE QUALIDADE')
fin = [txt(e) for e in body[i_qm + 1:next_tbl(i_qm)] if e.tag == qn('w:p') and txt(e)]
out['qm_intro'] = fin
qm = rows(body[next_tbl(i_qm)])
out['qm_faixa'] = ' '.join(qm[2][0])
q = []
for r in qm[3:]:
    req = ' '.join(r[0])
    m = re.match(r'^(\S+-Q)\s*-\s*(.*)$', req)
    q.append({'id': m.group(1), 'req': m.group(2), 'ind': r[1], 'meta': r[2], 'tec': r[3], 'freq': r[4],
              'quem': r[5], 'acao': r[6], 'quando': r[7], 'resp': r[8]})
out['qm'] = q

# Referências
i_ref = find('VII – REFERÊNCIAS')
out['referencias'] = [txt(e) for e in body[i_ref + 1:] if e.tag == qn('w:p') and txt(e)]

# Títulos de seção do documento
out['secoes'] = {k: txt(body[v]) for k, v in
                 {'en': i_en, 'tap': i_tap, 'eap': i_eap, 'dic': i_dic, 'rtm': i_rtm, 'qm': i_qm, 'ref': i_ref}.items()}

json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('TAP seções:', len(secs), '| dicionário:', len(out['dicionario']), '| RTM:', len(out['rtm']), '| QM:', len(q),
      '| refs:', len(out['referencias']))

(function () {
  "use strict";
  var DATA = JSON.parse(document.getElementById("rov-data").textContent);
  var DIC = {}, RTM = {}, QM = {};
  DATA.dic.forEach(function (d) { DIC[d.code] = d; });
  DATA.rtm.forEach(function (r) { RTM[r.id] = r; });
  DATA.qm.forEach(function (q) { QM[q.id] = q; });

  function $(s, el) { return (el || document).querySelector(s); }
  function $$(s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function norm(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function codeKey(c) { return String(c).split(/[.\-]/).map(function (x) { return ("000" + x).slice(-3); }).join("."); }
  function nameOf(code) { return DIC[code] ? DIC[code].nome : DATA.agg[code]; }
  function under(code, f) { return !f || code === f || code.indexOf(f + ".") === 0; }
  function cap(s) { return s.charAt(0) + s.slice(1).toLowerCase(); }

  /* ---------- navegação ---------- */
  var menuBtn = $(".menu-btn"), nav = $("#nav");
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var open = menuBtn.getAttribute("aria-expanded") !== "true";
      menuBtn.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("open", open);
    });
    $$("#nav a").forEach(function (a) {
      a.addEventListener("click", function () { menuBtn.setAttribute("aria-expanded", "false"); nav.classList.remove("open"); });
    });
  }
  var links = $$("#nav a");
  var secs = links.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); });
  var bar = $(".progress span"), totop = $(".totop");
  function onScroll() {
    var y = window.scrollY + 120, cur = -1;
    secs.forEach(function (s, i) { if (s && s.offsetTop <= y) cur = i; });
    links.forEach(function (a, i) { if (i === cur) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current"); });
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if (bar) bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + "%";
    if (totop) totop.classList.toggle("show", window.scrollY > 800);
  }
  var ticking = false;
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(function () { onScroll(); ticking = false; }); }
  }, { passive: true });
  onScroll();
  if (totop) totop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });

  /* ---------- EAP ---------- */
  function setExpanded(li, open) {
    var t = $(".toggle", li), ul = $(".wbs-l2", li);
    if (!t || !ul) return;
    t.setAttribute("aria-expanded", String(open));
    t.setAttribute("aria-label", (open ? "Recolher " : "Expandir ") + t.getAttribute("data-code"));
    t.textContent = open ? "−" : "+";
    ul.hidden = !open;
  }
  $$(".wbs .has-children").forEach(function (li) {
    var t = $(".toggle", li);
    t.addEventListener("click", function () { setExpanded(li, t.getAttribute("aria-expanded") !== "true"); });
  });
  var ex = $("#wbs-expand"), co = $("#wbs-collapse");
  if (ex) ex.addEventListener("click", function () { $$(".wbs .has-children").forEach(function (li) { setExpanded(li, true); }); });
  if (co) co.addEventListener("click", function () { $$(".wbs .has-children").forEach(function (li) { setExpanded(li, false); }); });

  var detail = $("#eap-detail");
  function selectNode(code, scroll) {
    $$(".wbs .node-btn[data-code]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-code") === code ? "true" : "false"); });
    $$(".dict tbody tr").forEach(function (tr) { tr.classList.toggle("sel", under(tr.getAttribute("data-code"), code)); });
    var d = DIC[code];
    var kids = Object.keys(DIC).filter(function (c) { return c.indexOf(code + ".") === 0; }).sort(function (a, b) { return codeKey(a) < codeKey(b) ? -1 : 1; });
    var reqs = DATA.rtm.filter(function (r) { return under(r.code, code); });
    var main = "";
    if (d) {
      main += '<section><h4>Especificação</h4><p class="just">' + esc(d.spec) + "</p></section>";
      main += '<section><h4>Critério de aceitação</h4><p class="crit">' + esc(d.crit) + "</p></section>";
    } else {
      main += "<section><h4>Pacotes de trabalho</h4><ul class=\"linklist\">" + kids.map(function (c) {
        return '<li><button type="button" class="linkbtn" data-node="' + c + '">' + esc(c + " " + cap(nameOf(c))) + "</button></li>";
      }).join("") + "</ul></section>";
    }
    main += "<section><h4>Requisitos rastreados (" + reqs.length + ")</h4>" + (reqs.length ? '<ul class="reqlist">' + reqs.map(function (r) {
      return '<li><button type="button" class="linkbtn" data-req="' + esc(r.id) + '">' + esc(r.id) + "</button> " + esc(r.desc) + "</li>";
    }).join("") + "</ul>" : '<p class="muted">Nenhum requisito associado a este pacote nas matrizes.</p>') + "</section>";
    detail.innerHTML =
      '<div class="detail-head"><span class="dcode">' + esc(code) + "</span><h3>" + esc(cap(nameOf(code))) + "</h3>" +
      (d ? '<a class="btn" href="#dic-' + esc(code) + '">Ver no Dicionário</a>' : "") + "</div>" +
      '<div class="detail-body"><div class="detail-meta"><dl><dt>Tipo</dt><dd>' + (d ? "Pacote de trabalho" : "Elemento de agregação") +
      "</dd><dt>Nível</dt><dd>" + (code.indexOf(".") < 0 ? "1º nível" : "2º nível") + "</dd><dt>Requisitos</dt><dd>" + reqs.length +
      (reqs.length ? " (" + reqs.map(function (r) { return r.id; })[0] + (reqs.length > 1 ? " a " + reqs[reqs.length - 1].id : "") + ")" : "") +
      '</dd></dl></div><div class="detail-main">' + main + "</div></div>";
    if (scroll) detail.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }
  $$(".wbs .node-btn[data-code]").forEach(function (b) {
    b.addEventListener("click", function () { selectNode(b.getAttribute("data-code"), true); });
  });
  $$(".dict tbody tr").forEach(function (tr) {
    tr.style.cursor = "pointer";
    tr.addEventListener("click", function () {
      selectNode(tr.getAttribute("data-code"), false);
      document.getElementById("eap-arvore").scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
  document.addEventListener("click", function (ev) {
    var n = ev.target.closest("[data-node]");
    if (n) { selectNode(n.getAttribute("data-node"), true); return; }
    var r = ev.target.closest("[data-req]");
    if (r) openReq(r.getAttribute("data-req"));
  });

  /* ---------- detalhe do requisito ---------- */
  var dlg = $("#req-dialog"), lastFocus = null;
  function row(k, v) { return "<dt>" + esc(k) + "</dt><dd>" + v + "</dd>"; }
  function lines(a) {
    return a.length > 1 ? '<ul class="lines">' + a.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" : esc(a.join(" "));
  }
  function openReq(id) {
    var r = RTM[id], q = QM[id];
    if (!r) return;
    lastFocus = document.activeElement;
    $(".rid", dlg).textContent = id;
    $("h3", dlg).textContent = r.desc;
    var h = "<h4>Matriz de Rastreabilidade</h4><dl class=\"dlg-grid\">" +
      row("Código EAP", esc(r.code + " — " + cap(nameOf(r.code)))) + row("Stakeholder", esc(r.stk)) +
      row("Prioridade", esc(r.pri + " — " + DATA.pri[r.pri])) + row("Tipo do requisito", esc(cap(r.tipo))) + row("Status", esc(r.status)) + "</dl>";
    if (q) {
      h += "<h4>Matriz de Qualidade</h4><dl class=\"dlg-grid\">" + row("Indicador", lines(q.ind)) + row("Meta", lines(q.meta)) +
        row("Técnica de medição", lines(q.tec)) + row("Frequência", lines(q.freq)) + row("Quem mede", lines(q.quem)) + "</dl>" +
        "<h4>Plano de resposta</h4><dl class=\"dlg-grid\">" + row("Ação", lines(q.acao)) + row("Quando", lines(q.quando)) +
        row("Responsável", lines(q.resp)) + "</dl>";
    } else {
      h += '<p class="small muted">Requisito sem métricas na Matriz de Qualidade.</p>';
    }
    $(".dlg-body", dlg).innerHTML = h;
    if (typeof dlg.showModal === "function") dlg.showModal(); else dlg.setAttribute("open", "");
    $(".close", dlg).focus();
  }
  function closeDlg() { if (typeof dlg.close === "function") dlg.close(); else dlg.removeAttribute("open"); }
  $(".close", dlg).addEventListener("click", closeDlg);
  dlg.addEventListener("click", function (ev) { if (ev.target === dlg) closeDlg(); });
  dlg.addEventListener("close", function () { if (lastFocus && lastFocus.focus) lastFocus.focus(); });

  /* ---------- matrizes ---------- */
  function setupMatrix(cfg) {
    var table = document.getElementById(cfg.table), tbody = $("tbody", table);
    var rows = $$("tr[data-id]", tbody);
    var text = {};
    rows.forEach(function (tr) {
      text[tr.getAttribute("data-id")] = norm(tr.textContent);
      tr.addEventListener("click", function () { openReq(tr.getAttribute("data-id")); });
      tr.addEventListener("keydown", function (ev) {
        if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); openReq(tr.getAttribute("data-id")); }
      });
    });
    var search = document.getElementById(cfg.search), counter = document.getElementById(cfg.counter);
    var sels = cfg.filters.map(function (f) { return { el: document.getElementById(f.id), attr: f.attr, tree: f.tree }; });
    function apply() {
      var qv = norm(search.value.trim()), n = 0;
      rows.forEach(function (tr) {
        var ok = !qv || text[tr.getAttribute("data-id")].indexOf(qv) >= 0;
        sels.forEach(function (s) {
          var v = s.el.value, a = tr.getAttribute(s.attr);
          if (v && ok) ok = s.tree ? under(a, v) : a === v;
        });
        tr.hidden = !ok;
        if (ok) n++;
      });
      counter.textContent = n === rows.length ? rows.length + " requisitos" : n + " de " + rows.length + " requisitos";
    }
    search.addEventListener("input", apply);
    sels.forEach(function (s) { s.el.addEventListener("change", apply); });
    document.getElementById(cfg.clear).addEventListener("click", function () {
      search.value = ""; sels.forEach(function (s) { s.el.value = ""; }); apply();
    });
    $$("th[data-sort] button", table).forEach(function (btn) {
      var th = btn.parentNode, key = th.getAttribute("data-sort"), col = Array.prototype.indexOf.call(th.parentNode.children, th);
      btn.addEventListener("click", function () {
        var dir = th.getAttribute("aria-sort") === "ascending" ? -1 : 1;
        $$("th[data-sort]", table).forEach(function (o) { o.removeAttribute("aria-sort"); $(".ar", o).textContent = "↕"; });
        th.setAttribute("aria-sort", dir === 1 ? "ascending" : "descending");
        $(".ar", th).textContent = dir === 1 ? "↑" : "↓";
        rows.sort(function (a, b) {
          var x, y;
          if (key === "id" || key === "code") { x = codeKey(a.getAttribute("data-id")); y = codeKey(b.getAttribute("data-id")); if (key === "code") { x = codeKey(a.getAttribute("data-code")) + x; y = codeKey(b.getAttribute("data-code")) + y; } }
          else { x = norm(a.children[col].textContent); y = norm(b.children[col].textContent); }
          return x < y ? -dir : x > y ? dir : 0;
        });
        rows.forEach(function (tr) { tbody.appendChild(tr); });
      });
    });
  }
  setupMatrix({ table: "mr", search: "mr-q", counter: "mr-count", clear: "mr-clear",
    filters: [{ id: "mr-eap", attr: "data-code", tree: true }, { id: "mr-pri", attr: "data-pri" }, { id: "mr-tipo", attr: "data-tipo" }, { id: "mr-stk", attr: "data-stk" }] });
  setupMatrix({ table: "mq", search: "mq-q", counter: "mq-count", clear: "mq-clear",
    filters: [{ id: "mq-eap", attr: "data-code", tree: true }] });
})();

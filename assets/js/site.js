/* ============================================================
   风云激变政经智库 · 页面逻辑
   纯静态：直接读取 content/ 下的稿组，无构建步骤
   ============================================================ */
(function () {
  "use strict";

  var PAGE = document.body.getAttribute("data-page");
  var WEEK = ["日", "一", "二", "三", "四", "五", "六"];
  var ANGLE_ORDER = ["①", "②", "③", "④", "⑤"];

  var state = {
    source: null,
    articles: [],
    meta: { total: 0, dateCount: 0, dateFrom: "", dateTo: "", dates: [], angles: [], words: 0 },
    repaint: null
  };

  /* ---------------- 工具 ---------------- */
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function esc(str) {
    return String(str == null ? "" : str)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function parseDate(str) {
    var p = String(str).split("-").map(Number);
    return new Date(p[0], p[1] - 1, p[2]);
  }
  function fmtDate(str) {
    var d = parseDate(str);
    return (d.getMonth() + 1) + "月" + d.getDate() + "日";
  }
  function fmtDateFull(str) {
    var d = parseDate(str);
    return d.getFullYear() + "年" + (d.getMonth() + 1) + "月" + d.getDate() + "日";
  }
  function weekday(str) { return "周" + WEEK[parseDate(str).getDay()]; }
  function num(n) { return Number(n || 0).toLocaleString("zh-CN"); }
  function truncate(str, len) {
    str = String(str || "");
    return str.length > len ? str.slice(0, len) + "…" : str;
  }
  function href(a) { return "article.html?id=" + encodeURIComponent(a.id); }
  function angleNameOf(a) {
    if (a.angleName) return a.angleName;
    return (Zhiku.ANGLE_INFO[a.angle] || {}).name || "";
  }
  function anglePill(a) {
    if (!a.angle) return "";
    return '<span class="pill" data-a="' + a.angle + '">' + esc(a.angle + angleNameOf(a)) + "</span>";
  }
  function angleCount(code) {
    var n = 0;
    state.articles.forEach(function (a) { if (a.angle === code) n++; });
    return n;
  }

  function footLabel(a) {
    var event = a.event || "";
    if (a.kind === "thought" && event) return truncate(event, 18);
    return "";
  }

  /* ---------------- 卡片 ---------------- */
  function coverHtml(a) {
    if (!a.cover) return '<div class="cover-empty"><span>文</span></div>';
    return '<img class="cover-img" src="' + a.cover + '" alt="' + esc(a.groupTitle || a.title) +
      '" loading="lazy" decoding="async">';
  }

  function dateText(a) {
    return a.date ? fmtDate(a.date) + " · " + weekday(a.date) : "原创 · 未标日期";
  }

  function cardHtml(a, variant) {
    var mini = variant === "card--mini";
    var metaHtml = mini
      ? dateText(a)
      : dateText(a) + (a.words ? '<span class="dot">·</span>' + num(a.words) + " 字" : "");
    return (
      '<a class="card ' + (variant || "") + '" href="' + href(a) + '">' +
        '<div class="card-cover">' +
          coverHtml(a) +
          (a.angle ? '<span class="card-angle">' + esc(a.angle + " " + angleNameOf(a)) + "</span>" : "") +
          (a.own ? '<span class="card-own">原创</span>' : "") +
        "</div>" +
        '<div class="card-body">' +
          '<div class="card-meta"><span>' + metaHtml + "</span></div>" +
          "<h3>" + esc(a.title) + "</h3>" +
          (a.summary ? "<p>" + esc(a.summary) + "</p>" : '<p class="is-empty">正文载入中…</p>') +
          '<div class="card-foot"><span>' + esc(footLabel(a)) +
            '</span><span class="go">阅读 →</span></div>' +
        "</div>" +
      "</a>"
    );
  }

  /* ---------------- 通用渲染 ---------------- */
  function renderChrome() {
    var hm = $("#headerMeta");
    if (hm && state.meta.total) {
      hm.innerHTML = "共 <b>" + num(state.meta.total) + "</b> 篇 · 更新至 " + fmtDate(state.meta.dateTo);
    }
  }

  function updateStats() {
    var wrap = $("#heroStats");
    if (!wrap) return;
    var stats = [
      ["稿件", num(state.meta.total), "篇"],
      ["发布日", num(state.meta.dateCount), "天"],
      ["角度", ANGLE_ORDER.length, "个"],
      ["总字数", (state.meta.words / 10000).toFixed(1), "万"]
    ];
    wrap.innerHTML = stats.map(function (s) {
      return "<div><dt>" + s[0] + "</dt><dd>" + s[1] + "<small>" + s[2] + "</small></dd></div>";
    }).join("");

    var period = $("#heroPeriod");
    if (period && state.meta.dateFrom) {
      period.textContent = "收录区间 " + state.meta.dateFrom.replace(/-/g, ".") +
        " — " + state.meta.dateTo.replace(/-/g, ".");
    }
  }

  function showFatal(message) {
    var focus = $("#focusGrid");
    var angles = $(".angles");
    var latest = $(".latest");
    if (angles) angles.hidden = true;
    if (latest) latest.hidden = true;
    if (focus) {
      focus.innerHTML = '<div class="setup-guide"><h3>暂时读不到稿件</h3>' +
        "<p>" + esc(message) + "</p>" +
        "<p>如果是部署在 GitHub Pages，请确认仓库为公开仓库；如果是本地预览，请用任意静态服务器打开，或直接双击后选择 content 文件夹。</p></div>";
    }
  }

  /* ---------------- 本地文件选择（file:// 场景） ---------------- */
  function setupLocalPicker() {
    var focus = $("#focusGrid");
    var anglesSection = $(".angles");
    var latest = $(".latest");
    if (anglesSection) anglesSection.hidden = true;
    if (latest) latest.hidden = true;

    var focusHead = $(".focus .section-head h2");
    if (focusHead) focusHead.innerHTML = '本地预览 <span class="en">LOCAL PREVIEW</span>';
    var more = $(".focus .more");
    if (more) more.remove();

    if (focus) {
      focus.innerHTML =
        '<div class="setup-guide">' +
          "<h3>选择一次 content 文件夹</h3>" +
          "<p>直接用浏览器打开 HTML 时，出于安全限制，页面不能自行读取本地文件。" +
            "选择站点的 <code>content</code> 文件夹后，全部稿件都在本地解析，不联网、不上传。</p>" +
          "<p>部署到 GitHub Pages 后不需要这一步，页面会自动读取仓库中的 <code>content/</code>。</p>" +
          '<button class="btn-solid" id="pickFolder" type="button">选择 content 文件夹</button>' +
        "</div>";
      var btn = $("#pickFolder");
      if (btn) {
        btn.addEventListener("click", function () {
          var label = btn.textContent;
          btn.disabled = true;
          btn.textContent = "正在读取…";
          function restore() {
            if (state.source) return;
            btn.disabled = false;
            btn.textContent = label;
          }
          setTimeout(restore, 1500);
          ZhikuSource.pickFolder().then(function (src) {
            start(src);
          }).catch(restore);
        });
      }
    }
  }

  /* ---------------- 启动 ---------------- */
  async function boot() {
    try {
      var src = await ZhikuSource.init();
      start(src);
    } catch (err) {
      if (err && err.local) { setupLocalPicker(); return; }
      showFatal(err && err.message ? err.message : "未知错误");
    }
  }

  async function start(src) {
    state.source = src;
    state.articles = Zhiku.buildArticles(src.files, src);
    state.meta = Zhiku.computeMeta(state.articles);

    if (!state.articles.length) {
      showFatal("content/ 里没有找到 Markdown 稿件。");
      return;
    }

    renderChrome();
    if (PAGE === "home") initHome();
    else if (PAGE === "archive") initArchive();
    else if (PAGE === "article") await initArticle();

    Zhiku.hydrate(state.articles, src, function (done) {
      state.meta = Zhiku.computeMeta(state.articles);
      updateStats();
      if (state.repaint) state.repaint(done);
    });
  }

  /* ============================================================
     首页
     ============================================================ */
  function initHome() {
    updateStats();

    var tags = $("#heroTags");
    if (tags) {
      tags.innerHTML = ANGLE_ORDER.filter(function (k) { return angleCount(k); }).map(function (k) {
        return '<a href="archive.html?angle=' + encodeURIComponent(k) + '">' +
          esc(k + (Zhiku.ANGLE_INFO[k] || {}).name) + "</a>";
      }).join("") + '<a href="archive.html">全部稿件 →</a>';
    }

    var form = $("#heroSearch");
    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var q = $("#homeSearchInput").value.trim();
        location.href = "archive.html" + (q ? "?q=" + encodeURIComponent(q) : "");
      });
    }

    var cta = $("#ctaStats");
    if (cta) {
      cta.textContent = state.meta.dateCount + " 个发布日，" + num(state.meta.total) +
        " 篇文章，支持按角度与关键词检索。";
    }

    function renderFocus() {
      var focus = $("#focusGrid");
      if (!focus) return;
      var top = state.articles.slice(0, 3);
      focus.innerHTML = top.length
        ? cardHtml(top[0], "card--lead") + top.slice(1).map(function (a) { return cardHtml(a, "card--mini"); }).join("")
        : "";
    }

    function renderAngles() {
      var wrap = $("#angleGrid");
      if (!wrap) return;
      wrap.innerHTML = ANGLE_ORDER.map(function (k, i) {
        var info = Zhiku.ANGLE_INFO[k];
        return '<a class="angle-card" href="archive.html?angle=' + encodeURIComponent(k) + '">' +
          '<span class="angle-no">0' + (i + 1) + "</span>" +
          '<span class="angle-mark" data-a="' + k + '">' + k + "</span>" +
          "<h3>" + info.name + "</h3>" +
          "<p>" + info.desc + "</p>" +
          '<span class="angle-count"><b>' + angleCount(k) + "</b> 篇</span>" +
        "</a>";
      }).join("");
    }

    var view = { angle: "all", shown: 9 };

    function filtered() {
      return state.articles.filter(function (a) {
        if (view.angle === "own") return a.own;
        return view.angle === "all" || a.angle === view.angle;
      });
    }

    var grid = $("#latestGrid");
    var moreWrap = $("#loadMoreWrap");
    var moreBtn = $("#loadMore");

    function renderGrid() {
      var list = filtered();
      var slice = list.slice(0, view.shown);
      grid.innerHTML = slice.map(function (a) { return cardHtml(a); }).join("");
      $$(".card", grid).forEach(function (el, i) {
        el.style.animationDelay = Math.min(i * 25, 300) + "ms";
      });
      if (moreWrap) moreWrap.hidden = list.length <= view.shown;
      if (moreBtn) moreBtn.textContent = "加载更多（还有 " + Math.max(list.length - view.shown, 0) + " 篇）";
      var lc = $("#latestCount");
      if (lc) lc.textContent = "共 " + list.length + " 篇";
    }

    var angleFilter = $("#angleFilter");
    if (angleFilter) {
      angleFilter.setAttribute("data-label", "角度");
      var ownChip = state.meta.ownCount
        ? [{ value: "own", label: "原创", count: state.meta.ownCount }]
        : [];
      angleFilter.innerHTML = [{ value: "all", label: "全部角度" }].concat(
        ownChip,
        ANGLE_ORDER.filter(function (k) { return angleCount(k); }).map(function (k) {
          return { value: k, label: k + (Zhiku.ANGLE_INFO[k] || {}).name, count: angleCount(k) };
        })
      ).map(function (it) {
        return '<button type="button" class="chip' + (it.value === view.angle ? " is-active" : "") +
          '" data-angle="' + esc(it.value) + '">' + esc(it.label) +
          (it.count != null ? '<span class="num">' + it.count + "</span>" : "") + "</button>";
      }).join("");

      angleFilter.addEventListener("click", function (e) {
        var btn = e.target.closest(".chip");
        if (!btn) return;
        view.angle = btn.getAttribute("data-angle");
        view.shown = 9;
        $$(".chip", angleFilter).forEach(function (c) {
          c.classList.toggle("is-active", c.getAttribute("data-angle") === view.angle);
        });
        renderGrid();
      });
    }

    if (moreBtn) {
      moreBtn.addEventListener("click", function () {
        view.shown += 9;
        renderGrid();
      });
    }

    renderFocus();
    renderAngles();
    renderGrid();
    updateStats();

    state.repaint = function () {
      renderFocus();
      renderAngles();
      renderGrid();
      updateStats();
      if (tags) {
        tags.innerHTML = ANGLE_ORDER.filter(function (k) { return angleCount(k); }).map(function (k) {
          return '<a href="archive.html?angle=' + encodeURIComponent(k) + '">' +
            esc(k + (Zhiku.ANGLE_INFO[k] || {}).name) + "</a>";
        }).join("") + '<a href="archive.html">全部稿件 →</a>';
      }
    };
  }

  /* ============================================================
     归档
     ============================================================ */
  function initArchive() {
    var params = new URLSearchParams(location.search);
    var view = {
      angle: params.get("angle") || "all",
      q: params.get("q") || ""
    };

    var totalEl = $("#archiveTotal");
    if (totalEl) totalEl.textContent = num(state.meta.total);

    var searchInput = $("#archiveSearchInput");
    if (searchInput && view.q) searchInput.value = view.q;

    var angleFilter = $("#archiveAngleFilter");
    function renderFilters() {
      if (!angleFilter) return;
      angleFilter.setAttribute("data-label", "角度");
      var ownChip = state.meta.ownCount
        ? [{ value: "own", label: "原创", count: state.meta.ownCount }]
        : [];
      angleFilter.innerHTML = [{ value: "all", label: "全部角度" }].concat(
        ownChip,
        ANGLE_ORDER.filter(function (k) { return angleCount(k); }).map(function (k) {
          return { value: k, label: k + (Zhiku.ANGLE_INFO[k] || {}).name, count: angleCount(k) };
        })
      ).map(function (it) {
        return '<button type="button" class="chip' + (it.value === view.angle ? " is-active" : "") +
          '" data-angle="' + esc(it.value) + '">' + esc(it.label) +
          (it.count != null ? '<span class="num">' + it.count + "</span>" : "") + "</button>";
      }).join("");
    }

    function match(a) {
      if (view.angle === "own") {
        if (!a.own) return false;
      } else if (view.angle !== "all" && a.angle !== view.angle) {
        return false;
      }
      if (view.q) {
        var q = view.q.toLowerCase();
        var hay = (a.title + " " + a.event + " " + a.summary + " " + a.groupTitle + " " + a.angleName).toLowerCase();
        if (hay.indexOf(q) === -1) return false;
      }
      return true;
    }

    function highlight(text) {
      var safe = esc(text);
      if (!view.q) return safe;
      var q = view.q.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      return safe.replace(new RegExp(q, "gi"), function (m) { return "<mark>" + m + "</mark>"; });
    }

    var listEl = $("#archiveList");
    var emptyEl = $("#archiveEmpty");
    var metaEl = $("#archiveResultMeta");
    var railEl = $("#dateRail");

    function buildRail(items) {
      if (!railEl) return;
      var counts = {};
      items.forEach(function (a) { counts[a.date] = (counts[a.date] || 0) + 1; });

      var html = "";
      if (counts[""]) {
        html += '<div class="rail-item" data-date="own"><span>原创</span><em>未标日期</em><b>' +
          counts[""] + "</b></div>";
      }
      html += state.meta.dates.filter(function (d) { return counts[d.date]; }).map(function (d) {
        return '<div class="rail-item" data-date="' + d.date + '"><span>' +
          d.date.slice(5).replace("-", ".") + "</span><em>" + weekday(d.date) + "</em><b>" +
          counts[d.date] + "</b></div>";
      }).join("");
      railEl.innerHTML = html;
    }

    function render() {
      var items = state.articles.filter(match);
      buildRail(items);

      if (metaEl) {
        metaEl.textContent = view.q
          ? '匹配「' + view.q + "」· " + items.length + " 篇"
          : "共 " + items.length + " 篇";
      }

      if (!items.length) {
        if (listEl) listEl.innerHTML = "";
        if (emptyEl) {
          emptyEl.hidden = false;
          var p = emptyEl.querySelector("p");
          if (p) p.textContent = "没有找到匹配的稿件";
          var reset = $("#resetFilters");
          if (reset) reset.hidden = false;
        }
        return;
      }
      if (emptyEl) emptyEl.hidden = true;

      var groups = {};
      items.forEach(function (a) { (groups[a.date] = groups[a.date] || []).push(a); });
      var undated = groups[""] || [];
      delete groups[""];
      var order = Object.keys(groups).sort().reverse();

      function sectionHtml(date, dayItems) {
        var rows = dayItems.map(function (a, i) {
          return '<a class="item-row" href="' + href(a) + '">' +
            '<div class="idx">' + String(i + 1).padStart(3, "0") + "</div>" +
            "<div>" +
              '<h4 class="item-title">' + highlight(a.title) + "</h4>" +
              (a.summary
                ? '<p class="item-sum">' + esc(truncate(a.summary, 120)) + "</p>"
                : '<p class="item-sum is-loading">正文载入中…</p>') +
            "</div>" +
            '<div class="item-side">' +
              (a.own ? '<span class="pill pill-own">原创</span>' : "") +
              anglePill(a) +
              '<span class="src">' + (a.words ? num(a.words) + " 字" : "—") + "</span>" +
            "</div>" +
          "</a>";
        }).join("");

        var head = date
          ? '<div class="day-head"><h3>' + fmtDateFull(date) + "</h3>" +
            '<span class="wk">' + weekday(date) + "</span>" +
            '<span class="cnt">' + dayItems.length + " 篇</span></div>"
          : '<div class="day-head"><h3>原创</h3><span class="wk">未标日期</span>' +
            '<span class="cnt">' + dayItems.length + " 篇</span></div>";

        return '<section class="day-block" id="day-' + (date || "own") + '">' + head + rows + "</section>";
      }

      if (listEl) {
        var html = "";
        if (undated.length) html += sectionHtml("", undated);
        html += order.map(function (date) { return sectionHtml(date, groups[date]); }).join("");
        listEl.innerHTML = html;
      }
      observeDays();
      syncUrl();
    }

    function syncUrl() {
      var p = new URLSearchParams();
      if (view.angle !== "all") p.set("angle", view.angle);
      if (view.q) p.set("q", view.q);
      var url = location.pathname.split("/").pop() + (p.toString() ? "?" + p.toString() : "");
      try { history.replaceState(null, "", url); } catch (e) { /* file:// 下忽略 */ }
    }

    var observer;
    function observeDays() {
      if (!railEl) return;
      if (observer) observer.disconnect();
      var blocks = listEl ? listEl.querySelectorAll(".day-block") : [];
      if (!blocks.length) return;
      observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var dateKey = entry.target.id.replace("day-", "");
          $$(".rail-item", railEl).forEach(function (el) {
            el.classList.toggle("is-active", el.getAttribute("data-date") === dateKey);
          });
        });
      }, { rootMargin: "-96px 0px -72% 0px", threshold: 0 });
      Array.prototype.forEach.call(blocks, function (b) { observer.observe(b); });
    }

    if (railEl) {
      railEl.addEventListener("click", function (e) {
        var item = e.target.closest(".rail-item");
        if (!item) return;
        var target = document.getElementById("day-" + item.getAttribute("data-date"));
        if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }

    if (angleFilter) {
      angleFilter.addEventListener("click", function (e) {
        var btn = e.target.closest(".chip");
        if (!btn) return;
        view.angle = btn.getAttribute("data-angle");
        $$(".chip", angleFilter).forEach(function (c) {
          c.classList.toggle("is-active", c.getAttribute("data-angle") === view.angle);
        });
        render();
      });
    }

    var timer;
    if (searchInput) {
      searchInput.addEventListener("input", function () {
        clearTimeout(timer);
        var val = searchInput.value.trim();
        var clearBtn = $("#searchClear");
        if (clearBtn) clearBtn.hidden = !val;
        timer = setTimeout(function () { view.q = val; render(); }, 180);
      });
      searchInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter") { e.preventDefault(); view.q = searchInput.value.trim(); render(); }
      });
    }

    var clearBtn = $("#searchClear");
    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        searchInput.value = "";
        view.q = "";
        clearBtn.hidden = true;
        render();
      });
    }

    var resetBtn = $("#resetFilters");
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        view = { angle: "all", q: "" };
        if (searchInput) searchInput.value = "";
        if (clearBtn) clearBtn.hidden = true;
        renderFilters();
        render();
      });
    }

    renderFilters();
    render();
    state.repaint = render;
  }

  /* ============================================================
     文章详情
     ============================================================ */
  async function initArticle() {
    var root = $("#articleRoot");
    var params = new URLSearchParams(location.search);
    var id = params.get("id");
    var a = state.articles.filter(function (x) { return x.id === id; })[0];

    if (!a) {
      if (root) {
        root.innerHTML = '<div class="empty-state"><p>没有找到这篇稿件</p>' +
          '<a class="btn-ghost" href="archive.html">返回归档</a></div>';
      }
      return;
    }

    if (root) root.innerHTML = '<div class="article-loading">正在载入稿件…</div>';

    var parsed;
    try {
      parsed = await Zhiku.readArticle(a, state.source);
      a.hydrated = true;
      if (parsed.title) a.title = parsed.title;
      if (parsed.summary) a.summary = parsed.summary;
      if (parsed.words) a.words = parsed.words;
      if (parsed.event) a.event = parsed.event;
      if (parsed.url) a.url = parsed.url;
    } catch (e) {
      if (root) {
        root.innerHTML = '<div class="empty-state"><p>稿件读取失败：' + esc(a.mdPath) + "</p>" +
          '<a class="btn-ghost" href="archive.html">返回归档</a></div>';
      }
      return;
    }

    document.title = a.title + " · 风云激变政经智库";
    var descMeta = document.querySelector('meta[name="description"]');
    if (descMeta) descMeta.setAttribute("content", a.summary || a.title);

    var bodyHtml = window.renderMarkdown(parsed.body, { autoHeading: a.kind === "thought" });

    var used = {};
    a.images.forEach(function (img) { if (parsed.body.indexOf(img.url) !== -1) used[img.url] = true; });
    var heroImg = a.cover && !used[a.cover] ? a.images[0] : null;
    if (heroImg) used[heroImg.url] = true;
    var gallery = a.images.filter(function (img) { return !used[img.url]; });
    var siblings = state.articles.filter(function (x) { return x.groupId === a.groupId && x.id !== a.id; });

    var dateFull = a.date ? fmtDateFull(a.date) : "原创 · 未标日期";
    var dateMeta = a.date ? fmtDateFull(a.date) + " · " + weekday(a.date) : "原创 · 未标日期";

    var html =
      '<nav class="crumbs">' +
        '<a href="index.html">首页</a><span class="sep">/</span>' +
        '<a href="archive.html">归档</a><span class="sep">/</span>' +
        "<span>" + dateFull + "</span>" +
      "</nav>" +
      '<header class="article-head">' +
        '<div class="article-tags">' +
          (a.own ? '<span class="pill pill-own">原创</span>' : "") +
          anglePill(a) +
          '<span class="date">' + dateMeta +
            (a.words ? " · " + num(a.words) + " 字" : "") + "</span>" +
        "</div>" +
        '<h1 class="article-title">' + esc(a.title) + "</h1>" +
        (parsed.summary && a.kind === "thought" ? '<p class="article-lede">' + esc(parsed.summary) + "</p>" : "") +
        '<div class="article-meta">' +
          (parsed.event ? '<span><span class="k">事件</span> <span class="v">' + esc(parsed.event) + "</span></span>" : "") +
          (!a.own && a.groupTitle && a.groupTitle !== parsed.event &&
            a.title.indexOf(a.groupTitle.slice(0, 10)) === -1
            ? '<span><span class="k">素材</span> <span class="v">' + esc(a.groupTitle) + "</span></span>"
            : "") +
          (parsed.url ? '<span><span class="k">信源</span> <a href="' + esc(parsed.url) +
            '" target="_blank" rel="noopener">原文链接 ↗</a></span>' : "") +
        "</div>" +
      "</header>" +
      (heroImg
        ? '<figure class="article-hero-img"><img src="' + heroImg.url + '" alt="' + esc(heroImg.alt) + '">' +
          (heroImg.alt ? "<figcaption>" + esc(heroImg.alt) + "</figcaption>" : "") + "</figure>"
        : "") +
      '<div class="article-body">' + bodyHtml + "</div>" +
      (gallery.length
        ? '<section class="article-gallery"><h3>配图</h3><div class="gallery-grid">' +
          gallery.map(function (img) {
            return '<figure><img src="' + img.url + '" alt="' + esc(img.alt) + '" loading="lazy">' +
              "<figcaption>" + esc(img.alt) + "</figcaption></figure>";
          }).join("") + "</div></section>"
        : "") +
      (siblings.length
        ? '<section class="article-siblings"><h3 class="siblings-title">同题 · 其他角度</h3><div class="sibling-list">' +
          siblings.map(function (s) {
            return '<a class="sibling" href="' + href(s) + '">' + anglePill(s) +
              '<span class="t">' + esc(s.title) + '</span><span class="s">' +
              (s.words ? num(s.words) + " 字" : "") + "</span></a>";
          }).join("") + "</div></section>"
        : "");

    root.innerHTML = html;

    var idx = state.articles.findIndex(function (x) { return x.id === a.id; });
    var prev = state.articles[idx - 1];
    var next = state.articles[idx + 1];
    var pager = $("#articlePager");
    if (pager) {
      pager.innerHTML =
        (prev
          ? '<a class="pager-card" href="' + href(prev) + '"><span class="dir">← 更新一篇</span><span class="t">' + esc(prev.title) + "</span></a>"
          : '<span class="pager-card is-empty"><span class="dir">← 更新一篇</span><span class="t">已经是第一篇</span></span>') +
        (next
          ? '<a class="pager-card next" href="' + href(next) + '"><span class="dir">更早一篇 →</span><span class="t">' + esc(next.title) + "</span></a>"
          : '<span class="pager-card next is-empty"><span class="dir">更早一篇 →</span><span class="t">已经是最后一篇</span></span>');
    }

    buildToc();
    setupProgress();
  }

  function buildToc() {
    var toc = $("#toc");
    var nav = $("#tocNav");
    var layout = $(".article-layout");
    var heads = document.querySelectorAll(".article-body h2, .article-body h3");
    if (!toc || !nav || heads.length < 2) {
      if (layout) layout.classList.add("no-toc");
      return;
    }
    toc.hidden = false;
    nav.innerHTML = Array.prototype.map.call(heads, function (h, i) {
      if (!h.id) h.id = "sec-auto-" + i;
      return '<a class="' + (h.tagName === "H3" ? "lv3" : "lv2") + '" href="#' + h.id + '">' +
        esc(h.textContent) + "</a>";
    }).join("");

    nav.addEventListener("click", function (e) {
      var link = e.target.closest("a");
      if (!link) return;
      var target = document.getElementById(link.getAttribute("href").slice(1));
      if (!target) return;
      e.preventDefault();
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 90, behavior: "smooth" });
    });

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = entry.target.id;
        $$("a", nav).forEach(function (link) {
          link.classList.toggle("is-active", link.getAttribute("href") === "#" + id);
        });
      });
    }, { rootMargin: "-100px 0px -70% 0px" });
    Array.prototype.forEach.call(heads, function (h) { spy.observe(h); });
  }

  function setupProgress() {
    var bar = $("#progressBar");
    if (!bar) return;
    function onScroll() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? Math.min(window.scrollY / h, 1) : 0;
      bar.style.width = (p * 100).toFixed(2) + "%";
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------------- 启动 ---------------- */
  document.addEventListener("DOMContentLoaded", boot);
})();

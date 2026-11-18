/* ============================================================
   稿件数据层
   ------------------------------------------------------------
   直接从 content/ 的文件清单生成文章结构：
     1. buildArticles   由路径推断日期、稿组、角度、配图（无需读文件，秒出）
     2. hydrate         逐篇读取 Markdown，补全标题、摘要、字数（边读边渲染）
     3. readArticle     详情页读取正文并按目录改写图片地址
   ============================================================ */
(function (global) {
  "use strict";

  var IMG_RE = /\.(png|jpe?g|webp|gif|svg)$/i;
  var CACHE_KEY = "zhiku.meta.v1";
  var ANGLE_INFO = {
    "①": { name: "事实", desc: "先把发生了什么摆清楚" },
    "②": { name: "对比", desc: "横向纵向逐项比" },
    "③": { name: "影响", desc: "谁被改变，改到什么程度" },
    "④": { name: "实操", desc: "普通人怎么用、怎么避坑" },
    "⑤": { name: "争议", desc: "争议点与未被回答的问题" }
  };

  function dirOf(path) {
    var i = path.lastIndexOf("/");
    return i < 0 ? "" : path.slice(0, i);
  }

  function baseOf(path) {
    var i = path.lastIndexOf("/");
    return i < 0 ? path : path.slice(i + 1);
  }

  function imageSort(a, b) {
    var na = (a.match(/图\s*(\d+)/) || [])[1] || "99";
    var nb = (b.match(/图\s*(\d+)/) || [])[1] || "99";
    return (parseInt(na, 10) - parseInt(nb, 10)) || a.localeCompare(b);
  }

  function stripMd(text) {
    return String(text || "")
      .replace(/!\[[^\]]*\]\([^)]*\)/g, "")
      .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
      .replace(/[*_`>#|]+/g, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  function charCount(body) {
    return stripMd(body).replace(/\s/g, "").length;
  }

  function firstParagraph(body) {
    var blocks = String(body || "").split("\n\n");
    for (var i = 0; i < blocks.length; i++) {
      var block = blocks[i].trim();
      if (!block) continue;
      if (/^(#|!|\[|-|\*|>|\||```|\d+[.、])/.test(block)) continue;
      var plain = stripMd(block);
      if (plain.length < 8) continue;
      return plain.length > 110 ? plain.slice(0, 110) + "…" : plain;
    }
    return "";
  }

  function cleanBody(text) {
    return String(text || "")
      .replace(/\r\n?/g, "\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
  }

  /* ---------------- 清单 → 文章骨架 ---------------- */
  function buildArticles(files, source) {
    var imagesByDir = {};
    files.forEach(function (path) {
      if (!IMG_RE.test(path)) return;
      var d = dirOf(path);
      (imagesByDir[d] = imagesByDir[d] || []).push(path);
    });

    var articles = [];
    var usedIds = {};

    files.forEach(function (path) {
      var fileName = baseOf(path);
      if (!/\.md$/i.test(fileName)) return;
      if (/校验报告/.test(fileName)) return;
      if (/^readme\.md$/i.test(fileName)) return;

      var parts = path.split("/");
      var CONTENT_DIR = (global.ZHIKU_CONFIG && global.ZHIKU_CONFIG.contentDir) || "content";
      var relParts = parts[0] === CONTENT_DIR ? parts.slice(1) : parts;
      var own = relParts.length > 1 && relParts[0].toLowerCase() === "own";

      var date = "";
      var dateIdx = -1;
      for (var i = 0; i < parts.length; i++) {
        if (/^\d{4}-\d{2}-\d{2}$/.test(parts[i])) { dateIdx = i; date = parts[i]; break; }
      }

      var groupName = "";
      if (dateIdx >= 0) {
        if (dateIdx + 2 <= parts.length - 1) groupName = parts[dateIdx + 1];
      } else {
        var parent = parts.length >= 2 ? parts[parts.length - 2] : "";
        var lowerParent = parent.toLowerCase();
        if (parent && lowerParent !== CONTENT_DIR.toLowerCase() && lowerParent !== "own") {
          groupName = parent;
        }
        var dm = fileName.match(/(\d{4}-\d{2}-\d{2})/);
        if (dm) date = dm[1];
      }

      var groupTitle = groupName
        .replace(/^S\d{3,5}-\d{2}_/, "")
        .replace(/^\d+[_-]/, "")
        .replace(/\.md$/i, "");
      var dir = dirOf(path);

      var m = fileName.match(/^(A\d{3,5}-\d{2})_([①②③④⑤])?([^_]*)_(.+)\.md$/);
      var kind = m ? "thought" : "newmode";
      var code = m ? m[1] : ((groupName.match(/^(\d{1,4})/) || [])[1] || fileName.replace(/\.md$/i, ""));
      var angle = m ? (m[2] || "") : "";
      var angleName = m ? (m[3] || "") : "";

      var dirImages = (imagesByDir[dir] || []).slice().sort(imageSort);
      var prefix = m ? m[1] + "_" : "";
      if (prefix) {
        var matched = dirImages.filter(function (p) {
          return baseOf(p).indexOf(prefix) === 0;
        });
        if (matched.length) dirImages = matched;
      }

      var images = dirImages.map(function (p) {
        var alt = baseOf(p).replace(/\.(png|jpe?g|webp|gif|svg)$/i, "")
          .replace(/^(A\d{3,5}-\d{2}|图\s*\d+)[_-]?/, "")
          .trim();
        return { path: p, url: source.url(p), alt: alt };
      });

      var idPrefix = own ? "o-" : (kind === "thought" ? "a-" : "b-");
      var id = idPrefix + (date || "own") + "-" + code;
      if (usedIds[id]) id = id + "-" + (usedIds[id] += 1);
      else usedIds[id] = 1;

      articles.push({
        id: id,
        kind: kind,
        own: own,
        date: date,
        mdPath: path,
        dir: dir,
        group: groupName,
        groupId: date + "::" + groupName,
        groupTitle: groupTitle || fileName.replace(/\.md$/i, ""),
        code: code,
        angle: angle,
        angleName: angleName,
        title: groupTitle || fileName.replace(/\.md$/i, ""),
        summary: "",
        event: groupTitle,
        words: 0,
        url: "",
        images: images,
        cover: images.length ? images[0].url : "",
        hydrated: false
      });
    });

    // content/own/ 下的自撰文章永远排在最前
    articles.sort(function (a, b) {
      if (a.own !== b.own) return a.own ? -1 : 1;
      if (a.date !== b.date) {
        if (!a.date) return -1;
        if (!b.date) return 1;
        return a.date < b.date ? 1 : -1;
      }
      return String(a.code) < String(b.code) ? 1 : -1;
    });
    return articles;
  }

  /* ---------------- 清单统计 ---------------- */
  function computeMeta(articles) {
    var dates = {};
    var angles = {};
    var words = 0;
    var ownCount = 0;
    var undated = 0;

    articles.forEach(function (a) {
      if (a.own) ownCount++;
      if (a.date) dates[a.date] = (dates[a.date] || 0) + 1;
      else undated++;
      if (a.angle) {
        var key = a.angle + (a.angleName || "");
        angles[key] = (angles[key] || 0) + 1;
      }
      words += a.words || 0;
    });

    var dateList = Object.keys(dates).sort().reverse().map(function (d) {
      return { date: d, count: dates[d] };
    });

    return {
      total: articles.length,
      ownCount: ownCount,
      undated: undated,
      dateCount: dateList.length,
      dateFrom: dateList.length ? dateList[dateList.length - 1].date : "",
      dateTo: dateList.length ? dateList[0].date : "",
      dates: dateList,
      angles: Object.keys(angles).sort().map(function (k) { return { key: k, count: angles[k] }; }),
      words: words
    };
  }

  /* ---------------- Markdown 解析 ---------------- */
  function parseThought(text, stub) {
    var idx = text.indexOf("【正文】");
    var head = idx >= 0 ? text.slice(0, idx) : "";
    var body = idx >= 0 ? text.slice(idx + 4) : text;

    ["【配图建议】", "【发布说明】", "【数据来源】", "【校验说明】"].forEach(function (tag) {
      var p = body.indexOf(tag);
      if (p >= 0) body = body.slice(0, p);
    });

    var meta = {};
    var titles = [];
    head.split("\n").forEach(function (line) {
      var s = line.trim();
      if (!s || s.charAt(0) === "【") return;
      var t = s.match(/^\d+[.、)]\s*(.+)$/);
      if (t) { titles.push(t[1].trim()); return; }
      var kv = s.match(/^([^：:]{1,14})[：:]\s*(.*)$/);
      if (kv) meta[kv[1].trim()] = kv[2].trim();
    });

    var angleName = meta["角度"] ? meta["角度"].replace(/^[①②③④⑤]\s*/, "") : "";
    var words = parseInt(String(meta["字数"] || "").replace(/[^\d]/g, ""), 10);

    return {
      title: titles[0] || "",
      summary: meta["核心结论"] || firstParagraph(body),
      body: cleanBody(body),
      words: words || charCount(body),
      event: meta["事件"] || "",
      url: meta["主信源 URL"] || "",
      angleName: angleName
    };
  }

  function parsePlain(text) {
    var lines = text.split("\n");
    var title = "";
    var start = 0;
    for (var i = 0; i < lines.length; i++) {
      if (/^#\s+/.test(lines[i])) {
        title = lines[i].replace(/^#\s+/, "").trim();
        start = i + 1;
        break;
      }
    }
    var body = cleanBody(lines.slice(start).join("\n"));
    return {
      title: title,
      summary: firstParagraph(body),
      body: body,
      words: charCount(body),
      event: "",
      url: "",
      angleName: ""
    };
  }

  function parseArticle(text, stub) {
    var raw = String(text || "").replace(/\r\n?/g, "\n");
    var looksThought = raw.indexOf("【正文】") >= 0 || raw.indexOf("【元信息】") >= 0;
    return looksThought ? parseThought(raw, stub) : parsePlain(raw);
  }

  /* ---------------- 正文图片地址改写 ---------------- */
  function rewriteImages(body, dir, urlOf) {
    return String(body || "").replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g, function (all, alt, src) {
      if (/^(https?:|data:|blob:|\/)/i.test(src)) return all;
      var name = src.replace(/^\.\//, "").split("/").pop();
      var url = urlOf(dir + "/" + name);
      return url ? "![" + alt + "](" + url + ")" : all;
    });
  }

  /* ---------------- 元数据缓存 ---------------- */
  function readCache() {
    try { return JSON.parse(localStorage.getItem(CACHE_KEY) || "{}") || {}; } catch (e) { return {}; }
  }

  function writeCache(cache) {
    try { localStorage.setItem(CACHE_KEY, JSON.stringify(cache)); } catch (e) { /* 忽略配额与隐私模式 */ }
  }

  function applyMeta(article, meta) {
    if (meta.t) article.title = meta.t;
    if (meta.s) article.summary = meta.s;
    if (meta.w) article.words = meta.w;
    if (meta.e) article.event = meta.e;
    if (meta.u) article.url = meta.u;
    if (meta.an) article.angleName = meta.an;
    article.hydrated = true;
  }

  /* ---------------- 逐篇补全 ---------------- */
  async function hydrate(articles, source, onProgress) {
    var cache = readCache();
    var pending = [];

    var MAX_AGE = 3 * 24 * 3600 * 1000; // 缓存三天后重新读取，兼顾速度与更新
    articles.forEach(function (a) {
      var c = cache[a.mdPath];
      var fresh = c && c.t && (!c.ts || Date.now() - c.ts < MAX_AGE);
      if (fresh) applyMeta(a, c);
      else pending.push(a);
    });

    if (!pending.length) {
      if (onProgress) onProgress(true);
      return;
    }
    if (onProgress) onProgress(false);

    var cursor = 0;
    var sinceSave = 0;
    var finished = 0;

    async function worker() {
      while (cursor < pending.length) {
        var a = pending[cursor++];
        try {
          var text = await source.text(a.mdPath);
          var parsed = parseArticle(text, a);
          var meta = {
            t: parsed.title,
            s: parsed.summary,
            w: parsed.words,
            e: parsed.event,
            u: parsed.url,
            an: parsed.angleName,
            ts: Date.now()
          };
          applyMeta(a, meta);
          cache[a.mdPath] = meta;
          finished++;
          if (++sinceSave >= 20) {
            sinceSave = 0;
            writeCache(cache);
            if (onProgress) onProgress(false);
          }
        } catch (e) {
          /* 单篇失败不影响整体 */
        }
      }
    }

    var workers = [];
    var limit = Math.min(8, pending.length);
    for (var i = 0; i < limit; i++) workers.push(worker());
    await Promise.all(workers);

    writeCache(cache);
    if (onProgress) onProgress(true);
  }

  /* ---------------- 详情页正文 ---------------- */
  async function readArticle(article, source) {
    var text = await source.text(article.mdPath);
    var parsed = parseArticle(text, article);
    parsed.body = rewriteImages(parsed.body, article.dir, source.url);
    return parsed;
  }

  global.Zhiku = {
    buildArticles: buildArticles,
    computeMeta: computeMeta,
    hydrate: hydrate,
    readArticle: readArticle,
    parseArticle: parseArticle,
    ANGLE_INFO: ANGLE_INFO
  };
})(window);

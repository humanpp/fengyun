/* ============================================================
   文章来源适配层
   ------------------------------------------------------------
   三种取数方式，优先级从高到低：
     1. GitHub Pages 上：调用 GitHub Trees API 读取仓库文件清单（自动、实时）
     2. http(s) 本地预览：读取 data/index.js 中生成的清单快照
     3. file:// 双击打开：浏览器禁止读取本地文件，改为让用户选择一次
        content 文件夹（File API），之后全部在本地内存中完成
   三种方式对上提供同一套接口：
     source.files        文件路径数组（形如 content/2026-11-04/S1104-01_x/A1104-01_①事实_x.md）
     source.text(path)   读取文本
     source.url(path)    图片地址
   ============================================================ */
(function (global) {
  "use strict";

  var CFG = Object.assign(
    { owner: "", repo: "", branch: "main", contentDir: "content" },
    global.ZHIKU_CONFIG || {}
  );

  function encodePath(path) {
    return path
      .split("/")
      .map(function (part) { return encodeURIComponent(part); })
      .join("/")
      .replace(/\(/g, "%28")
      .replace(/\)/g, "%29");
  }

  /* ---------- 1. GitHub Pages 自动识别 ---------- */
  function detectRepo() {
    if (CFG.owner && CFG.repo) {
      return { owner: CFG.owner, repo: CFG.repo, branch: CFG.branch };
    }
    var host = location.hostname;
    if (/\.github\.io$/i.test(host)) {
      var owner = host.split(".")[0];
      var seg = location.pathname.split("/").filter(Boolean);
      var repo = seg.length && seg[0].indexOf(".") === -1 ? seg[0] : owner + ".github.io";
      return { owner: owner, repo: repo, branch: CFG.branch };
    }
    return null;
  }

  var TREE_KEY = "zhiku.tree.v1";
  var TREE_TTL = 10 * 60 * 1000;

  function readTreeCache(rule) {
    try {
      var cached = JSON.parse(localStorage.getItem(TREE_KEY) || "null");
      if (cached && cached.rule === rule && Date.now() - cached.ts < TREE_TTL && cached.files) {
        return cached.files;
      }
    } catch (e) { /* 忽略 */ }
    return null;
  }

  function writeTreeCache(rule, files) {
    try {
      localStorage.setItem(TREE_KEY, JSON.stringify({ rule: rule, ts: Date.now(), files: files }));
    } catch (e) { /* 忽略 */ }
  }

  async function listFromGitHub(repo) {
    var rule = repo.owner + "/" + repo.repo + "@" + repo.branch + ":" + CFG.contentDir;
    var cached = readTreeCache(rule);
    if (cached) return cached;

    var api =
      "https://api.github.com/repos/" + repo.owner + "/" + repo.repo +
      "/git/trees/" + encodeURIComponent(repo.branch) + "?recursive=1";
    var res = await fetch(api, { headers: { Accept: "application/vnd.github+json" } });
    if (!res.ok) throw new Error("GitHub API " + res.status);
    var data = await res.json();
    if (!data.tree) throw new Error("GitHub 返回为空");
    var prefix = CFG.contentDir + "/";
    var files = data.tree
      .filter(function (node) {
        return node.type === "blob" && node.path.indexOf(prefix) === 0;
      })
      .map(function (node) { return node.path; });

    if (files.length) writeTreeCache(rule, files);
    return files;
  }

  /* ---------- 2. 本地清单快照 ---------- */
  function listFromSnapshot() {
    var idx = global.ZHIKU_INDEX;
    if (!idx || !idx.files || !idx.files.length) throw new Error("没有本地清单");
    return idx.files;
  }

  function httpSource(files, mode) {
    return {
      mode: mode,
      files: files,
      text: async function (path) {
        var res = await fetch(encodePath(path));
        if (!res.ok) throw new Error("读取失败 " + path);
        return res.text();
      },
      url: function (path) { return encodePath(path); }
    };
  }

  /* ---------- 3. file:// 选择文件夹 ---------- */
  function pickFolder() {
    return new Promise(function (resolve, reject) {
      var input = document.createElement("input");
      input.type = "file";
      input.webkitdirectory = true;
      input.multiple = true;
      input.style.display = "none";
      document.body.appendChild(input);

      function clean() {
        setTimeout(function () {
          if (input.parentNode) input.parentNode.removeChild(input);
        }, 0);
      }

      input.addEventListener("change", function () {
        var picked = Array.prototype.slice.call(input.files || []);
        clean();
        if (!picked.length) { reject(new Error("没有选择文件")); return; }

        var map = Object.create(null);
        var dirName = CFG.contentDir.toLowerCase();

        picked.forEach(function (file) {
          var rel = (file.webkitRelativePath || file.name).replace(/\\/g, "/");
          var parts = rel.split("/");
          var at = -1;
          for (var i = 0; i < parts.length; i++) {
            if (parts[i].toLowerCase() === dirName) { at = i; break; }
          }
          var path = at >= 0 ? parts.slice(at).join("/") : CFG.contentDir + "/" + rel;
          map[path] = file;
        });

        var files = Object.keys(map).filter(function (p) { return /\.(md|png|jpe?g|webp|gif)$/i.test(p); });
        if (!files.length) { reject(new Error("所选文件夹里没有找到稿件")); return; }

        var urlCache = Object.create(null);
        resolve({
          mode: "local",
          files: files,
          text: function (path) {
            var f = map[path];
            if (!f) return Promise.reject(new Error("缺少文件 " + path));
            return f.text();
          },
          url: function (path) {
            if (!urlCache[path]) {
              var f = map[path];
              if (!f) return "";
              urlCache[path] = URL.createObjectURL(f);
            }
            return urlCache[path];
          }
        });
      });

      input.click();
    });
  }

  /* ---------- 统一入口 ---------- */
  async function init() {
    if (location.protocol === "file:") {
      var err = new Error("LOCAL_FILE");
      err.local = true;
      throw err;
    }

    var repo = detectRepo();
    if (repo) {
      try {
        return httpSource(await listFromGitHub(repo), "github");
      } catch (e) {
        /* 例如仓库未公开、API 限流 —— 退回本地清单 */
      }
    }

    return httpSource(listFromSnapshot(), "snapshot");
  }

  global.ZhikuSource = {
    init: init,
    pickFolder: pickFolder,
    encodePath: encodePath,
    config: CFG
  };
})(window);

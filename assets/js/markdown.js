/* ============================================================
   Markdown 渲染封装
   - 解析交给本地 vendored 的 marked（assets/js/vendor/marked.min.js，MIT）
   - 兼容无 # 标记的稿件：短行自动提升为小标题
   - 图片段落自动转成 figure + 图注
   ============================================================ */
(function (global) {
  "use strict";

  var marked = global.marked;
  if (marked && marked.use) {
    marked.use({ gfm: true, breaks: true, pedantic: false });
  }

  function looksLikeHeading(text) {
    if (!text) return false;
    if (text.length > 24) return false;
    if (/[。！？；：，、,.;:!?"'“”‘’…—（）()《》]$/.test(text)) return false;
    if (/^[#>\-*+\d|=]/.test(text)) return false;
    if (/[*_`\[\]!]/.test(text)) return false;
    if (/^[A-Za-z0-9 .,%-]+$/.test(text)) return false;
    return true;
  }

  /* 思想高地的稿件正文没有 # 标记，靠短行区分小标题 */
  function promoteHeadings(markdown) {
    return markdown
      .split(/\n{2,}/)
      .map(function (block) {
        var lines = block.split("\n").filter(function (l) { return l.trim(); });
        if (lines.length !== 1) return block;
        var text = lines[0].trim();
        return looksLikeHeading(text) ? "### " + text : block;
      })
      .join("\n\n");
  }

  function fallback(markdown) {
    return markdown
      .split(/\n{2,}/)
      .map(function (block) {
        return "<p>" + block.replace(/</g, "&lt;").replace(/\n/g, "<br>") + "</p>";
      })
      .join("");
  }

  /* 中文紧贴 ** 时，CommonMark 的 flanking 规则会导致加粗失效，
     这里对 marked 输出做一次兜底：把残留的 **文字** 转成加粗，代码块内跳过 */
  function fixCjkEmphasis(html) {
    var parts = html.split(/(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>)/i);
    for (var i = 0; i < parts.length; i += 2) {
      parts[i] = parts[i].replace(/\*\*([^*\n]+?)\*\*/g, "<strong>$1</strong>");
    }
    return parts.join("");
  }

  function renderMarkdown(markdown, options) {
    var opts = options || {};
    var text = String(markdown || "").replace(/\r\n?/g, "\n");
    if (opts.autoHeading) text = promoteHeadings(text);

    if (!marked || typeof marked.parse !== "function") {
      return fallback(text);
    }

    var html = fixCjkEmphasis(marked.parse(text));

    // 独立图片段落 → figure（带图注）
    html = html.replace(/<p>\s*(<img\b[^>]*>)\s*<\/p>/g, function (_, img) {
      var altMatch = img.match(/alt="([^"]*)"/);
      var alt = altMatch ? altMatch[1].replace(/<[^>]*>/g, "") : "";
      return "<figure>" + img + (alt ? "<figcaption>" + alt + "</figcaption>" : "") + "</figure>";
    });

    // 外链新窗口
    html = html.replace(/<a href="(https?:)?\/\//g, '<a target="_blank" rel="noopener" href="$1//');

    return html;
  }

  global.renderMarkdown = renderMarkdown;
})(window);

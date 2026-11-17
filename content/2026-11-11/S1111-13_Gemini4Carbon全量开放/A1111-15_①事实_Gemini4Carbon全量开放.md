【元信息】
稿件编号：A1111-15
素材编号：S1111-13
事件：Google 于 2026 年 11 月 10 日将 Gemini 4 Carbon 全量开放，官方评测 19 项中 17 项第一
角度：①事实
核心结论：第一不是总分第一，是某类任务第一
主信源 URL：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
声明预勾选：AI生成 + 取材网络
字数：860

【备选标题】
1. 96.2% 的长上下文，Carbon 这一项领先最多
2. 19 项测试赢 17 项，谷歌新旗舰模型全量开放
3. 开局 59 分登顶，两周后被 Fable 5.2 反超

【正文】
96.2%。这是 Gemini 4 Carbon 在 GraphWalks 长上下文测试上的分数，上一代 Argon 是 84.2%，对手最高的是 GPT-6 Astra 的 71.8%。

2026 年 11 月 10 日，谷歌把它全量开放：付费 API 开发者可在 AI Studio 与 Android Studio 调用，企业版 Gemini 与 Antigravity 同步上线，Google AI Ultra 订阅用户在 Gemini 应用和搜索的 AI Mode 里直接可选。此前两周，它只提供给 Fairwind 计划的网络安全人员。门槛也不低：普通用户要走 Google AI Ultra 订阅，美国区两档月费分别是 99.99 美元和 199.99 美元；模型仍是闭源托管，没有权重下载，也没有自托管许可。官方另给入选的科学家六个月 Antigravity 最高档的免费使用权。

按谷歌自己的统计，19 项评测里 Carbon 拿下 17 项第一。GraphWalks 测的是在 25.6 万到 100 万 token 的图结构里做遍历，Carbon 96.2%，对手最高 71.8%，这是全表差距最大的一项，也是谷歌最愿意拿出来讲的一项。

终端智能体测试 Terminal-Bench 4.0 由 Artificial Analysis 运行，Carbon 65.2%，高于 Claude Fable 5.2 的 61.6% 与 Opus 5.5 的 59.6%。这一项不是谷歌自己跑的分，参考价值更高。

也有输的两项

FrontierSWE 2 上，Fable 5.2 报的是 69.9%（Anthropic 自报），GPT-6 Astra 65.5%，Carbon 61.2%。OSWorld-2.1 的电脑操作，Opus 87.2%，Carbon 81.5%。做桌面自动化、或者要往老仓库提改动的团队，这两项值得自己复测。

还要看清是谁在测。谷歌自己运行的至少有六项：GraphWalks、OSWorld-2.1、SWE-sweep、Agents’ Last Exam、SEC-bench Pro、ExploitGym，其中后两项还是关闭防护、断网的条件——前面被当成落后证据的 OSWorld，恰好也是它自己跑的。Terminal-Bench 4.0、CWE-bench 与 Artificial Analysis 指数来自外部机构，AutomationBench 来自 Zapier。

榜首只坐了两周

首发当天，Carbon 以 59 分坐上 Artificial Analysis 指数第一。此后发生的其实是两件事：Fable 5.2 在 11 月 9 日发布并入场，榜单同期改版重算。现在 Fable 5.2 最高档 65 分，Carbon 高档 60 分，Opus 5.5 最高档 59 分，GPT-6 Astra 57 分。59 是开局分，不是现在的分。

谷歌还称在 CursorBench 4.0 与 Perplexity 的 WANDR 上排第一、成本不到对手一半。核查公开榜：CursorBench 现在是 Fable 5.2 以 60.0% 居首，表里没有 Carbon 的行；Anthropic 公布的 WANDR 表里，Fable 5.2 按宽松口径是 82.1%，Carbon 一栏空白。这两项目前只能算厂商口径。

四周验证了 Signal

比跑分更能说明能力的是同一天的另一条消息。DeepMind 发布 AlphaProof Code，用 Carbon 驱动的智能体，把 Signal 协议的实际代码、也就是编译后的机器码，做了一遍形式化验证：四周、超过六百万行 Lean，人工只复核约 1% 的代码库。

验证对象是编译后的机器码，不是设计文档，这一步跨过了“设计对了、实现有洞”的缝隙。他们还做了反例测试：把两个早已修复的真实漏洞重新放回代码，系统两次都证明这版不安全。换句话说，它能分辨对的代码和有洞的代码，不是只会堆证明。官方称这是首次由 AI 在此深度验证广泛部署的加密协议，也是首次有方法验证到它的实现层。

判断

Carbon 的第一是有条件的：长上下文、终端操作这些单项领先，总分已经让位，仓库级软件工程与桌面操作也还落后。选它，等于选那几类任务。

别按榜单迁移。挑三个你每周都要跑的任务，在 AI Studio 里各跑十次，记通过率和返工次数，再决定换不换。96.2% 这种数字，只有在你的输入上重复一次，才算数。同一份 19 项表，换个任务组合就能得出相反的结论，这也是为什么它值得被拆开看。

【配图建议】
图1（首图）：自制图表 / 文件名 A1111-15_图1.png（源文件 图表-十九项里赢了十七项.png）/ 图注“Carbon 与各项最高对手的分数对照，含两项落后；数据来源：谷歌 19 项评测报告（Quantslant 转录）、Zapier、Artificial Analysis”
图2：自制图表 / 文件名 A1111-15_图2.png（源文件 图表-榜首只坐了两周.png）/ 图注“Artificial Analysis 指数在 10 月 28 日与 11 月 10 日两个口径下的排名；数据来源：9to5Google、VentureBeat”
图3：自制图表 / 文件名 A1111-15_图3.png（源文件 图表-四周验证Signal.png）/ 图注“AlphaProof Code 的三步流程与四个数字；数据来源：Google DeepMind 2026-11-10”

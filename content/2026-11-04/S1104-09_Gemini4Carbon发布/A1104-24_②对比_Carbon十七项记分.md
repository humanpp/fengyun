【元信息】
稿件编号：A1104-24
素材编号：S1104-09
事件：Gemini 4 Carbon 官方评测表逐项对照 GPT-6 Astra、Claude Opus 5.5、Claude Fable 5.1
角度：②对比
核心结论：领先集中在长上下文与网络安全，两项失利恰在对手强项
主信源 URL：https://deepmind.google/models/gemini/
声明预勾选：AI生成 + 取材网络
字数：858

【备选标题】
1. 17项基准15项第一，谷歌输掉的两项恰是对手强项
2. 长上下文赢24分，通用指数只赢0.2分
3. 和Opus 5.5只差0.2分，谷歌这个第一不轻松

【正文】
先给结论：Gemini 4 Carbon 在官方评测表 17 项里拿下 15 个第一，但领先得很不均匀。我把每项和第二名逐行做了一遍减法：最宽的一项差 24.4 个百分点，最窄的差 0.1；对关键竞品 Claude Opus 5.5，最窄的领先只有 0.2 个百分点。输掉的两项，一项归 GPT-6 Astra，一项归 Claude Opus 5.5。

这张表是怎么测的

表格出自 Google DeepMind 官方评测页，17 行五列，对照 Carbon、Argon、GPT-6 Astra、Claude Opus 5.5、Claude Fable 5.1。

官方评测方法页写明了每项由谁测。我把 17 项归了类：11 项出自第三方公开榜或统一评测——智能指数榜（Artificial Analysis Intelligence Index v5.0）和两项带 AA 标注的终端基准由 Artificial Analysis 测，Vals 由 Vals AI 测，CWE-bench 由 Collinear AI 统一评测，FrontierSWE、AutomationBench、Vending-Bench 2、Chartography、Blueprint-Bench 2、RiemannBench 取自各家官方公开榜。

GraphWalks 一项，是所有模型都由谷歌重测。剩下 5 项是混合口径：SWE-sweep、Agents' Last Exam、OSWorld、ExploitGym、SEC-bench Pro，谷歌自测自家模型，对手分数取自对方的系统卡或榜单。

所以这不是一场"所有人考同一张卷"的考试：11 项算同卷同考场，1 项是谷歌自己监考重考，5 项是谷歌自己考、对手交的是平时成绩单。方法页逐项写了测试设置，可以点开核对。

领先最宽的地方

长上下文 GraphWalks：Carbon 96.2%，GPT-6 Astra 71.8%，Claude Opus 5.5 66.8%。对第二名的差距 24.4 个百分点，全表最宽。

网络安全三项：SEC-bench Pro 88.2%，ExploitGym 54.8%，CWE-bench 71.0%。ExploitGym 领先第二名 12.4 个百分点。

知识工作项 Vending-Bench 2 让模型经营一家自动售货机：Carbon 的账户余额 16,484 美元，GPT-6 Astra 15,515 美元，Claude Opus 5.5 只有 9,235 美元。

图纸理解项 Blueprint-Bench 2：Carbon 58.6%，Claude Opus 5.5 51.2%，差 7.4 个百分点。

顺带说一句表里的一个空缺：Claude Fable 5.1 有四项没交卷——Vals、Agents' Last Exam、ExploitGym、SEC-bench Pro。五列对照，其实是一列残卷。

输掉的两项

FrontierSWE 2，智能体编程：GPT-6 Astra 65.5%，Carbon 61.2%，差 4.3 个百分点。

OSWorld-2.1 离线子集，计算机操作：Claude Opus 5.5 87.2%，Carbon 81.5%，差 5.7 个百分点。谷歌声明用 82 题离线子集是为了同口径对比，但 Opus 的 87.2% 取自它的系统卡，跑法是否完全一致，官方没说。

巧的是这两项的位置：一项在智能体编程，一项在计算机操作，都在 Carbon 主打的长时程叙事里。官方博客说 Carbon 能在内部任务里连跑数天去啃硬骨头，但在恰好衡量这类能力的两块公开榜上，它都不是第一。

赢得惊险的三项

SWE-sweep：9.6% 对 9.5%，领先 GPT-6 Astra 0.1 个百分点。这项五个模型全在 10% 以下，基准本身难，领先 0.1 也是领先，只是含金量得打个问号。

Vals Index：70.4% 对 Claude Opus 5.5 的 70.2%，差 0.2 个百分点。

AA 智能指数：59 分对 58 分，差 1 分。

官方方法页自己写着，小基准要多轮取平均来压低方差——这种量级的差距，正好落在方差能吞掉的区间里。Artificial Analysis 自家榜单截至 11 月 4 日显示 Carbon 60 分、Opus 5.5 59 分，差距变成 1 分。指数持续更新，这个座次随时可能再动。

什么人该等谁

处理长文档、长图谱的，GraphWalks 那 24.4 个百分点是实打实的，Carbon 开放后值得优先试。做网络安全防御的，三项领先同样成立。做计算机操作——开窗口、点鼠标、填表单——按这张表，Claude Opus 5.5 更强。做智能体编程的，FrontierSWE 2 的最高分在 GPT-6 Astra 手里。做图表和图纸理解的，两项多模态 Carbon 都领先，但幅度一个 1.5 个百分点、一个 7.4 个百分点，够不上代差。

15 个第一是真的，但第一的含金量不一样。两项险胜和两项失利说明：前沿榜首现在是逐项的微弱领先拼出来的，不是每一项都拉开了距离。

【配图建议】
图1（首图）：自制图 / 文件名 A1104-24_图1.png（源文件 图表-领先幅度谱.png）/ 版面为六条横向条形图，从 24.4 个百分点排到 0.1；图注"官方评测表逐项与第二名的差距，最宽 24.4 个百分点、最窄 0.1，数据来源为 Google DeepMind 官方评测表"
图2：自制图 / 文件名 A1104-24_图2.png（源文件 图表-两项失利.png）/ 版面为两行卡片，FrontierSWE 2 与 OSWorld-2.1 的失利明细；图注"两项失利：FrontierSWE 2 归 GPT-6 Astra，OSWorld-2.1 归 Claude Opus 5.5，数据来源为官方评测表"
图3：自制图 / 文件名 A1104-24_图3.png（源文件 图表-15比2记分板.png）/ 版面为三个大数字列；图注"17 项基准 15 项第一、2 项旁落、AA 智能指数 59 分，数据来源为 Google DeepMind 官方评测表"

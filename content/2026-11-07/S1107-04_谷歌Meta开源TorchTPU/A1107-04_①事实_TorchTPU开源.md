【元信息】
稿件编号：A1107-04
素材编号：S1107-04
事件：谷歌与Meta开源TorchTPU，TPU成为PyTorch原生后端
角度：①事实
核心结论：TorchTPU让TPU成为PyTorch原生后端，迁移只改两个词
主信源 URL：https://pytorch.org/blog/introducing-torchtpu/
声明预勾选：AI生成 + 取材网络
字数：916

【备选标题】
1. TPU成为PyTorch原生后端，迁移改两个词
2. 谷歌Meta开源TorchTPU，模型搬去TPU只改两行
3. 支持450算子5000模型，TPU成原生后端

【正文】
一个跑在英伟达卡上的 PyTorch 模型，要搬到谷歌 TPU 上，得改多少代码？

TorchTPU 给的答案是两个词。把 .to("cuda") 换成 .to("tpu")，再把分布式初始化的 backend 从 nccl 换成 tpu_dist。2026 年 10 月 20 日，谷歌和 Meta 一起把项目开源，一个原生的 PyTorch 后端，接替了 2020 年就在用的 PyTorch/XLA。

旧方案为什么非换不可，得看 PyTorch/XLA 的老毛病。它建立在 Lazy Tensor 上，开发者要在源码里手动圈出哪些代码段送去编译，编译延迟很重，PyTorch 原生的 eager 执行模式它也不支持。换句话说，你想在 TPU 上像在 GPU 上那样随手 print、随手改一个 tensor，它做不到。

TorchTPU 的思路是把这些反过来。项目 2025 年中期在谷歌内部启动，之后拉上 Meta 的 PyTorch 团队合做。设计原则第一条写得很直白：运行时里不许有 JAX 依赖。第二条是把 eager 模式做好，编译走 PyTorch 自己的 Torch Dynamo，不是 Lazy Tensor。

能跑的东西已经不少。官方数字是约 450 个 Aten 算子，前向反向都覆盖；兼容验证做在 Hugging Face 的 Transformers v5、Diffusers 和 Kernels 上，5000 个下载量最高的 HF 模型开箱即用。这里的开箱即用是字面意思，Qwen、DeepSeek、Gemma、LLama 这些语言模型，Whisper、CLIP、BERT 这些语音和视觉模型，装上轮子就能跑。

性能缺口是分几处补的。eager 模式里新加了个 DeferAndFuse，把零散算子攒成一批一起提交，官方说它比严格逐算子执行快 50% 以上，还能顺带压低 HBM 峰值占用。精度这块，TPU 的矩阵乘原生走 bfloat16，默认的 medium 模式是单趟 bf16 乘法配 FP32 累加，够绝大多数深度学习任务用；真要更高精度可以切 high 或 highest，代价是 3 倍到 6 倍的矩阵乘开销。再往下，自定义算子留了 JAX/Pallas 和 Helion 两个入口。

生产数据也有了。TorchTPU 已经在部分 Google Cloud 大客户的推理和训练负载上跑。谷歌官方博客给的一组数字是：走 TorchTitan 的训练路径，Qwen 3 8B 上跑到最高 52% 的模型 FLOPs 利用率，集群扩到 8192 个 Ironwood TPU，也就是 TPU v7x，接近线性扩展，单芯片吞吐几乎不掉。另据 InfoQ 转述谷歌公布的数字，Qwen3 235B 的 MoE 模型在同等芯片规模上是 28%。两个数不是一回事，前者是 8B 的训练效率，后者是 235B 的 MoE。

开源的不是一个仓库，是四个。TorchTPU 本体之外，vLLM-TorchTPU 和 SGLang-TorchTPU 管推理引擎适配，TorchTitan 管训练，稠密、MoE、扩散模型都在支持范围内。

这不是谷歌一家的动作。AWS 几乎同时把 TorchNeuron 放进了公开测试，Trainium 芯片的接入词换成了 .to("neuron")。TPU 走的是 PyTorch 调度器里那个叫 PrivateUse1 的自定义后端注册口，厂商把后端注册进去，用户侧就只剩一个设备名的差别。

Meta 为什么愿意陪谷歌做这件事，理由落在硬件多样性上。Meta 的 PyTorch 工程总监 Jana van Greunen 说，推进 AI 前沿需要极大的算力规模和深度的硬件多样性，不能被单一硬件架构约束。Meta 工程师 Zongwei Zhou 在 10 月 21 日的 Keynote 上讲得更具体：要把 TPU 变成 PyTorch 的一等原生目标，理由是生产环境里对性能、可靠性、可维护性的真实需求。

官方公告没回避一个短板：改那两个词只是让模型先跑通。要吃到 TPU 的峰值性能，分片、形状、算子这些还得按 TPU 的硬件结构重新调。Meta 的打算是用这套后端把更大规模的 LLM 负载迁到 TPU 上，具体规模和时间表还没公布。

对写 PyTorch 的人来说，这次真正被拆掉的，是那个只能跑在英伟达卡上的默认设定。TPU 本身快不快是另一回事，代码这一层，它已经不是异类了。

【配图建议】
图1（首图）：A1107-04_图1.png / 官方编译栈图＋右侧解读 / 图注"图片来源：PyTorch 官方博客架构图（Fig.1）"
图2：A1107-04_图2.png / 迁移代码两列对照，标出 cuda→tpu、nccl→tpu_dist / 图注"数据来源：PyTorch 官方博客代码示例"
图3：A1107-04_图3.png / 四组能力数字（450 算子、5,000 模型、4 仓库、52% MFU）/ 图注"数据来源：PyTorch 与 Google Cloud 官方博客"
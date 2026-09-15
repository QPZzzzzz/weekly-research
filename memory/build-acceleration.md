# build-acceleration — Research Memory

最后更新: 2026-09-15

# 关键记忆点

## 涉及的公司/产品/项目

- **Microsoft / Visual Studio 2026**（18.7–18.10）：Copilot Chat 支持 `make my build faster` 自动优化闭环
- **MSVC Build Tools 2026**（9月预览 / 14.50）：异常处理扫描优化、死代码搜索限制、接近 C++23 完全合规、ASan 扩展 ARM64
- **sccache**（mozilla/sccache）：多级缓存 + 自动回填分层架构，GitHub 官方背书
- **Incredibuild**：提出共享缓存 + 分布式处理层方案；中国授权合作伙伴为龙智（shdsd.com）
- **Build2**：原生支持 C++ Modules、跨平台、可跳过可忽略变更重编译
- **Buck2**：Conan 集成 PR 未合并，社区期望 vcpkg 支持
- **ccache**：本期无新版本迭代，被 sccache 平台化叙事覆盖
- **FASTBuild**：Unity 构建 + 网络分发 + 缓存一体化
- **CMake / Bazel / Meson / Pants**：构建系统选型讨论对象
- **CppCon 2026**：设 C++20 编程课程（Andreas Fertig，已取消）

## 重要趋势信号

- **↑ AI Agent 接管构建优化执行闭环**（high）：Copilot Chat 自动完成基线捕获→优化→测量→回滚，工具价值锚点从"提供能力"转向"被 Agent 调用"
- **↑ MSVC 原生优化侵蚀分布式编译收益**（high）：单机编译时间持续压缩，中小项目分布式 ROI 可能率先归零
- **↑ sccache 平台化与云存储后端标准**（high）：从"自选工具"转为"平台标准配置"，挤压 ccache 云原生叙事
- **↑ CI/CD 10 分钟基准共识**（high）：基准与现实（45–90 分钟）鸿沟构成核心市场空间
- **↑ Incredibuild 竞争焦点升级**（high）：从市场教育转向技术方案定义（共享缓存 + 分布式处理层）
- **↑ C++ Modules 构建系统原生支持**（high）：Build2 抢先差异化，成选型新分水岭
- **↓ 分布式编译与缓存融合**（low）：无新增融合证据，信号相对下降
- **→ Buck2 依赖管理集成僵局**（low）：无进展也无恶化

## 值得长期跟踪的技术方向/话题

- AI Agent 自动构建优化能否从 VS 2026 扩展至 CI/CD，形成端到端自动调优闭环
- Build2 原生 C++ Modules 是否推动构建系统在模块化场景重新洗牌，CMake/Bazel 是否跟进
- Incredibuild 共享缓存 + 分布式处理层方案是否被 CI 平台原生集成
- MSVC 4GB 调试信息流与公共流 API 是否被 sccache/ccache 跟进适配
- AI 驱动提交量增长对 CI 冗余计算缺口的放大效应，是否催生新构建加速产品形态
- C++20 Modules 对依赖分析与增量编译粒度的根本性改变

## 竞品动态

- **Microsoft**：VS 2026 正式版发布，Copilot Chat 接管构建优化决策闭环；MSVC 连续修复模块缓存适配
- **sccache**：多级缓存分层架构落地，GitHub 官方 Threads 持续推广"构建时间减半"
- **Incredibuild**：诊断所有 CI 平台未解决冗余计算问题，提出共享缓存 + 分布式处理层方案
- **Build2**：原生 C++ Modules 支持建立差异化竞争优势
- **Buck2**：Conan 集成 PR 获好评但未合并，依赖管理集成停滞
- **ccache**：本期无新版本发布，传统本地缓存优势被 sccache 云原生叙事挤压

## 已消退信号（下次调研留意）

- ccache 密集版本迭代（可能进入稳定期）
- RISC-V AI 系统软件栈与 LLVM libc++ 嵌入式移植（疑为会议周期性话题）
- 预测性/自适应 CI 构建加速（Velocity CI，疑被 AI 构建优化叙事吸收）
- 分布式编译适用边界固化（已融入 MSVC 侵蚀叙事）
- CMake/Meson 构建系统选型焦点（周期性话题）
# build-acceleration — Research Memory

最后更新: 2026-09-20

# 编译加速与分布式编译产业调研 — 关键记忆点

## 涉及的公司/产品/项目

- **Pigweed**（Google 主导嵌入式框架）：SEED 0111 提案将 Bazel 升为主构建系统，GN 转维护模式，CMake 无限期支持
- **Bazel**：获嵌入式 C++ 领域首个高显著性采用信号，Remote Cache API 可能挤压 sccache/ccache 嵌入式空间
- **sccache / ccache / Icecream**：三方对比成标准选型框架，扩展至远程 CI、自托管、跨平台全场景
- **mold**：链接器定位明确，与缓存工具互补关系成共识
- **Buck2**（Meta）：依赖管理集成僵局，Conan PR 未合并，vcpkg 支持仍为期望
- **Incredibuild**：中国区官网无新增技术增量，信号自然消退
- **MSVC Build Tools**（Microsoft）：2026 年 9 月预览更新优化编译性能，但 18.3.0 构建时间回归担忧未消
- **distcc**：经典分布式编译方案进入维护期，无新版本
- **Build2**：原生 C++ Modules 差异化卖点信号消退
- **字节跳动**：大规模 C++ 编译提速实践信号消退（libc++ 迁移、LLVM20 工具链演进）
- **FASTBuild / octobuild**：中文社区提及的分布式编译工具

## 重要趋势信号

- **方向 up｜Pigweed 采用 Bazel 作主构建系统**：嵌入式 C++ 构建生态关键转折，Bazel hermetic build + 远程缓存获嵌入式认可｜强度 **high**
- **方向 up｜sccache/ccache 对比扩展至全场景**：从工具选型进入远程 CI、自托管、Mac CI 深水区，竞争焦点转向部署运维体验｜强度 **high**
- **方向 up｜mold 与缓存工具互补共识**：构建加速三层分工清晰（缓存层/链接层/分布式层），"全能型"叙事收窄，"最佳组合"集成能力成关键｜强度 **high**
- **方向 stable｜CI/CD 10 分钟基准**：与 45 分钟行业现实形成 4.5 倍差距，构成 build cache 核心价值主张，升级为量化共识｜强度 **high**
- **方向 down｜Buck2 依赖管理僵局**：Conan PR 未合并，Meta 对开源社区需求响应优先级低，momentum 持续下降｜强度 **low**
- **方向 stable｜MSVC 原生编译优化**：9 月预览更新含调试信息流支持、减少分配，但 18.3.0 回归风险存疑｜强度 **medium**
- **方向 down｜distcc 进入维护期**：经典方案活力下降，pump 模式技术遗产或被新工具吸收｜强度 **low**
- **方向 stable｜AI 驱动 CI/CD 优化**：学术论文出现但无工业界增量验证｜强度 **low**
- **方向 down｜Incredibuild 中国区推广**：无新增技术细节或案例，自然消退｜强度 **low**

## 值得长期跟踪的技术方向/话题

- **Pigweed Bazel 提案落地进展**：是否引发更多嵌入式 C++ 项目跟进，形成 Bazel 嵌入式采用浪潮（下期最值得跟踪）
- **远程 Mac CI 缓存优化实践**：是否从个案扩展为跨平台标准方案，催生新缓存策略范式（NFS 挂载优化、CCACHE_TEMPDIR 设置）
- **MSVC 18.3.0 构建时间回归反馈**：是否扩散，影响原生优化叙事可信度
- **distcc 维护期后经典分布式编译方案替代进程**：是否被 sccache/Icecream 完全替代
- **AI 驱动 CI/CD 流水线优化**：能否从学术研究获工业界增量验证
- **构建加速工具链分层标准化**：缓存层 + 链接层 + 分布式层的集成格局演变
- **Bazel Remote Cache API 对 sccache/ccache 嵌入式场景的挤压效应**

## 竞品动态

- **Pigweed（Google）**：SEED 0111 提案将 Bazel 升为主构建系统，GN 转维护模式 — 技术选型风向标事件
- **Bazel**：获嵌入式 C++ 首个高显著性采用信号，从"互联网后端构建系统"向"全场景 C++ 构建系统"扩展
- **Buck2（Meta）**：Conan 集成 PR 受好评但未合并，vcpkg 支持仍为社区期望，momentum 从 medium 降至 low；Meta 内部依赖由内部工具链解决，开源社区需求响应优先级低
- **Microsoft MSVC**：9 月预览更新含调试信息流支持、减少类型记录处理分配等编译性能优化；18.3.0 更新后社区报告构建时间异常变长
- **Incredibuild**：持续宣传分布式编译与缓存加速平台，中国区无新增技术细节或案例；博客强调共享缓存与分布式处理层消除冗余计算
- **distcc**：GitHub 仓库仍为经典文档，无新版本发布，进入维护期
- **Build2**：原生 C++ Modules 支持和无外部依赖差异化卖点本期无新增讨论或采用信号

## 整体热度判断

**整体热度持平，结构分化加剧。**
- 升温：自托管缓存与分布式编译方案、Bazel 嵌入式采用信号、mold 互补关系共识
- 降温：字节跳动工具链演进信号消退、Buck2 持续降温、distcc 进入维护期
- 稳定：MSVC 原生编译优化（存回归风险）、CI/CD 10 分钟基准、Incredibuild 中国区推广（自然消退中）
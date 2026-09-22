# build-acceleration — Research Memory

最后更新: 2026-09-22

# 编译加速与分布式编译 — 关键记忆点

## 涉及公司/产品/项目
- **Microsoft / Visual Studio 2026**：v18.0 GA，C++23 一致性接近完整，构建工具与 IDE 解耦
- **MSVC Build Tools**：9 月预览更新，支持 4GB 调试信息流，18.3.0 构建时间回归担忧未消
- **Pigweed SEED 0111**：Bazel 升为主构建系统，GN 转维护，2026 年后可能移除 GN
- **ccache**：4.13.6（2026-05），4-5 月连续发布 4.13.4/5/6
- **sccache**：社区推广中，被定位"构建时间减半"，AI 技能包列为标准工具
- **Buck2（Meta）**：Rust/Starlark，Conan 集成 PR 未合并，vcpkg 支持仍为期望
- **Bazel**：嵌入式 C++ 领域上升，Remote Cache API 可能挤压 sccache/ccache 空间
- **Incredibuild**：中文官网持续运营，无新增技术增量
- **distcc / FASTBuild**：经典方案，进入维护期/被吸收进分层叙事
- **mold**：上期互补共识消退，本期无新增讨论
- **atskills.one**：build-acceleration AI 代理技能包（156 stars）
- **Gaudi（EPJ 论文）**：80 核分发实现近 10 倍加速

## 重要趋势信号
- **up / high**：VS 2026 GA，C++ 构建工具与 IDE 解耦，MSVC 进入独立升级新范式
- **up / high**：Pigweed SEED 0111 路线图明确化，嵌入式 C++ 生态向 Bazel 倾斜（有时间表）
- **stable / high**：CI/CD 10 分钟基准 vs 45 分钟现实，4.5 倍差距构成 build cache 核心价值主张
- **new / medium**：AI 代理技能包标准化 C/C++ 构建加速工具链配置（知识载体迁移）
- **new / medium**：VS 2026 安装器构建工具版本选择受限，解耦范式早期摩擦信号
- **down / low**：Buck2 依赖管理集成僵局持续，momentum 从 medium 降至 low
- **stable / low**：AI 驱动 CI/CD 优化（预测性缓存、自愈流水线）仍无工业界验证
- **stable / medium**：MSVC Build Tools 9 月预览优化，但 18.3.0 构建时间回归担忧未消
- **弱化**：sccache 信号 high → medium，讨论焦点被 VS 2026 与 Pigweed 占据
- **消退**：sccache/ccache 全场景对比、mold 互补共识从讨论期进入实践沉淀期

## 值得长期跟踪的技术方向/话题
- VS 2026 构建工具解耦后版本选择受限反馈是否扩散（影响独立升级范式可信度）
- Pigweed Bazel 落地进展，是否引发嵌入式 C++ 项目跟进浪潮
- AI 代理技能包是否从 156 stars 扩展为跨平台标准配置
- 构建加速工具链分层标准化（缓存层+链接层+分布式层）是否形成行业集成共识
- 远程 Mac CI 缓存优化实践是否从个案扩展为跨平台标准方案
- ccache 4.13.x 连续迭代与 sccache 社区推广并行，是否重燃缓存工具选型竞争
- Bazel Remote Cache API 对 sccache/ccache 在嵌入式场景空间的挤压

## 竞品动态
- **Microsoft**：VS 2026 GA + MSVC Build Tools 独立升级范式，Copilot C++ 进入私有预览
- **Pigweed/Google**：SEED 0111 明确 Bazel 主构建系统时间表，GN 2026 年后可能移除
- **Meta Buck2**：技术架构先进但生态集成受阻，Conan PR 未合并，vcpkg 仍为期望，内部依赖由内部工具链解决
- **ccache**：维护活跃，4-5 月连续三版本发布，无重大功能增量
- **sccache**：社区推广持续，但深度对比讨论退潮，从 high 降至 medium
- **Bazel**：嵌入式领域获首个高显著性采用信号，hermetic build + 远程缓存获认可
- **Incredibuild**：中国区推广信号完全退出，仅作为分布式层工具被提及
- **AI 技能包（atskills.one）**：新传播载体，与 Incredibuild 分层叙事高度一致
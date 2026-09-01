# build-acceleration — Research Memory

最后更新: 2026-09-01

## 关键记忆点

### 公司/产品/项目
- **sccache**（Mozilla）— 编译缓存事实标准，支持 S3/GCS/Redis 远程存储，Google Android 构建官方采用
- **RECC** — 融合 ccache 缓存 + distcc 分布式编译能力
- **FASTBuild** — 原生支持分布式编译+缓存，游戏行业（UE4）广泛使用
- **TencentBlueKing/bk-turbo** — 腾讯蓝鲸跨平台分布式编译加速平台
- **Buck2**（Meta）— Rust 核心 + Starlark 规则，单一增量依赖图，Bazel 替代方案
- **IncrediBuild** — Build Runners 早鸟计划（CI 提速 4-8 倍），Islo AI 沙盒
- **distcc** — 经典分布式编译，理论最大加速 3 倍

### 趋势信号
- **分布式编译+缓存融合成为默认架构范式**（high）— "缓存优先、分布式兜底"加速闭环
- **sccache 确立编译缓存标准地位**（high）— 从本地工具向云原生基础设施组件转移
- **CI/CD 加速成为企业刚需**（high）— 商业化产品加速落地，与平台工程方向一致
- **Buck2 讨论显著升温**（high）— 反映行业对 Bazel 复杂性的反思，但 CMake 生态集成不成熟
- **共享缓存成为 CI/CD 标准组件**（high）— 信号强度从中→高强化
- **C++20 模块影响构建模型**（medium，新信号）— 可能改变缓存粒度、分布式策略和构建图设计
- **AI 构建优化产品化热度回落**（medium）— 从概念炒作期进入产品落地期

### 长期跟踪方向
- C++20 模块对构建系统的适配进度（CMake、sccache、ccache 等）
- Buck2 与 Conan 集成 PR 进展（若合并将加速替代 Bazel 讨论）
- CMake 生态主导地位 vs Bazel/Buck2 竞争格局
- 分布式编译+缓存融合架构在企业级落地案例

### 竞品动态
- **IncrediBuild**：Build Runners 早鸟计划，45 分钟→8 分钟实际案例
- **Meta**：开源 Buck2，Tweag 深度技术分析发布
- **Google**：Android 构建官方采用 sccache
- **腾讯**：bk-turbo 支持 C++/UE4 跨平台加速
- **微软**：VS 中 Linux 项目构建 + Copilot Chat 集成（上期负面反馈已消退）
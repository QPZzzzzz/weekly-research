# build-acceleration — Research Memory

最后更新: 2026-06-30

- **公司/产品/项目**: Incredibuild (AI Sandbox/ISLO), Microsoft (VS 2026 Copilot), sccache, mold, ccache, Bazel, Buck2, CMake, yadcc (腾讯), Distcc, FASTBuild, Red Hat, JetBrains
- **重要趋势信号**:
  - **AI 与编译加速深度融合** (方向: up, 强度: high) – Incredibuild AI Sandbox 和微软 Copilot 将 AI 从加速工具转为智能分析大脑
  - **CI/CD “10分钟规则”成硬标准** (方向: up, 强度: high) – 2026年指南要求管道5-10分钟，倒逼分布式编译和缓存普及
  - **sccache 与 mold 兼容性问题引发用户迁移** (方向: new, 强度: high) – Issue #1755 导致性能下降，用户可能转向 ccache 或商业方案
  - **开源分布式编译生态多元化** (方向: up, 强度: medium) – 腾讯 yadcc 和 Meta Buck2 降低企业采用门槛
  - **现代构建系统迁移壁垒巨大** (方向: stable, 强度: medium) – Bazel/Buck2 学习曲线陡峭，CMake 仍占统治地位
  - **ccache 持续活跃更新** (方向: up, 强度: medium) – v4.13.6 更新，可能受益于 sccache 用户迁移
- **值得长期跟踪的技术方向**: AI 辅助构建分析 (Copilot, AI Sandbox), 分布式编译 (yadcc, Buck2), 编译缓存工具格局 (sccache vs ccache), 现代构建系统 (Bazel/Buck2 vs CMake)
- **竞品动态**:
  - **Incredibuild**: 推出 AI Sandbox (ISLO)，定位转向“AI 开发基础设施”
  - **Microsoft**: VS 2026 集成 Copilot 构建分析功能，强调智能分析
  - **Red Hat**: 仍推荐经典 distcc + Docker 方案
  - **腾讯**: 开源 yadcc，支持数百核并行编译
  - **Meta**: 开源 Buck2，核心用 Rust 编写，支持增量依赖图
  - **ccache**: 持续更新 v4.13.6，可能抢占 sccache 市场份额
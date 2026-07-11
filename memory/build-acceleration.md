# build-acceleration — Research Memory

最后更新: 2026-07-11

- **公司/产品/项目**: Visual Studio 2026, Incredibuild, GitHub Copilot, sccache, ccache, yadcc (腾讯云), distcc, FASTBuild, Bazel, Buck2, Pigweed, mold 链接器
- **重要趋势信号**:
    - **AI驱动编译优化成为竞争焦点** (high): VS 2026 集成 Copilot, Incredibuild 推 AI Sandbox, 多篇指南强调 AI 可观测性。
    - **CI/CD管道优化需求刚性增长** (high): 多篇2026指南强调“10分钟规则”、构建缓存、并行化，云成本压力驱动。
    - **开源分布式编译工具涌现** (medium): 腾讯云开源 yadcc, FASTBuild 被 Unreal Engine 社区采用。
    - **Bazel/Buck2作为下一代构建系统受关注** (medium): Pigweed 计划迁移至 Bazel，讨论从“能否替代”转向“如何迁移”。
    - **sccache生态承压，ccache稳定更新** (medium): sccache v0.16.0 未修复 mold 兼容性问题，ccache 4.13.6 稳定发布。
- **值得长期跟踪的技术方向/话题**:
    - Bazel/Buck2 迁移案例（如 Pigweed）的实际进展与社区反馈。
    - AI 可观测性在 CI/CD 中的具体落地效果与工具成熟度。
    - FASTBuild 在 Unreal Engine 社区的采用率变化。
- **竞品动态**:
    - **微软**: VS 2026 集成 Copilot、C++23 支持、MSVC 性能提升，直接与 Incredibuild 竞争。
    - **Incredibuild**: 推出 AI Sandbox 和 Build Cache 应对微软竞争。
    - **腾讯云**: 开源 yadcc，加入分布式编译工具生态。
    - **Mozilla/Meta/Google**: 维护 sccache (Mozilla)、Buck2 (Meta)、Bazel (Google)，影响行业技术路线。
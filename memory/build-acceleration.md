# build-acceleration — Research Memory

最后更新: 2026-07-12

### 关键记忆点

- **公司/产品/项目**：微软VS 2026、Incredibuild、腾讯云yadcc、FASTBuild、Bazel、Buck2、sccache、ccache、Pigweed
- **重要趋势信号**：
  - **AI驱动编译优化成为竞争焦点** (high)：VS 2026集成Copilot，Incredibuild推出AI Sandbox，多篇指南强调AI可观测性。
  - **CI/CD管道优化需求刚性增长** (high)：多篇2026指南强调“10分钟规则”、构建缓存、并行化，云成本压力驱动。
  - **Bazel/Buck2作为下一代构建系统受关注** (high)：讨论从“能否替代”转向“如何迁移”，Pigweed计划迁移至Bazel。
  - **开源分布式编译工具涌现** (high)：腾讯云开源yadcc，FASTBuild被Unreal Engine社区采用。
  - **微软VS 2026与Incredibuild竞争加剧** (high)：竞争从工具升级为“平台+AI”生态。
  - **sccache生态承压，ccache稳定更新** (medium)：sccache v0.16.0未修复mold兼容性问题，但仍广泛用于Rust。
- **值得长期跟踪的技术方向**：AI驱动编译优化、Bazel/Buck2迁移实践、开源分布式编译工具（yadcc、FASTBuild）、CI/CD“10分钟规则”落地。
- **竞品动态**：
  - **微软VS 2026**：集成Copilot和构建优化，直接切入Incredibuild核心市场。
  - **Incredibuild**：推出AI Sandbox和Build Cache应对微软竞争。
  - **腾讯云yadcc**：开源，支持数百核并发编译。
  - **FASTBuild**：在Unreal Engine社区采用率上升。
  - **Buck2**：核心用Rust编写，备受关注。
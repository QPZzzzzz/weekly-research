# build-acceleration — Research Memory

最后更新: 2026-07-18

- **公司/产品/项目**: 微软 (Pure Virtual C++ 2026, Copilot CLI), Incredibuild, ccache (v4.13.6), sccache (v0.16.0), yadcc (腾讯), Bazel, Buck2, mold 链接器, Intel oneAPI 2026.1
- **重要趋势信号**:
  - **AI 驱动编译优化成为竞争焦点** (方向: up, 强度: high): 微软和 Incredibuild 均强调 AI 在构建加速中的应用，从代码生成扩展到构建流程。
  - **构建缓存成为 CI/CD 标配** (方向: up, 强度: high): ccache/sccache 持续更新，商业产品集成，行业指南将其列为关键手段。
  - **分布式编译性能实现量级突破** (方向: up, 强度: high): yadcc 在 1000 核集群上实现 LLVM 编译 15 倍提升 (47分51秒→3分11秒)。
  - **Bazel/Buck2 迁移讨论升温** (方向: up, 强度: high): 社区焦点从“能否替代”转向“如何迁移”，实践讨论增多。
  - **sccache 生态承压** (方向: stable, 强度: medium): 与 mold 链接器兼容性问题 (Issue #1755) 未解决，影响用户体验。
- **值得长期跟踪的技术方向/话题**: AI 原生 C++ 工作流 (微软)、分布式构建缓存、下一代构建系统 (Bazel/Buck2)、sccache 与 mold 兼容性修复进展。
- **竞品动态**:
  - **微软**: Pure Virtual C++ 2026 聚焦 AI 原生 C++ 工作流，展示 AI 驱动构建加速和 Copilot CLI。
  - **Incredibuild**: 持续推广 Build Cache 和分布式处理，发布 C++ 构建系统选择指南。
  - **腾讯 (yadcc)**: 项目活跃，1000 核集群 15 倍性能提升成为分布式编译标杆。
  - **Mozilla (sccache)**: 发布 v0.16.0 版本，但 mold 兼容性问题未解。
  - **Intel**: 发布 oneAPI 2026.1 编译器，优化向量数学库性能，与编译加速关联低。
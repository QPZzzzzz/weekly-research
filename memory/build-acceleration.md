# build-acceleration — Research Memory

最后更新: 2026-07-07

- **公司/产品/项目**: Visual Studio 2026, Incredibuild (AI Sandbox, Build Cache), sccache, ccache, mold, Bazel, Buck2, CMake, FASTBuild, Copilot
- **重要趋势信号**:
    - **AI驱动编译优化成竞争焦点** (方向: up, 强度: high): 微软VS 2026集成Copilot优化构建，直接对标Incredibuild的AI方案。
    - **CI/CD“10分钟规则”成硬共识** (方向: up, 强度: high): 管道超10分钟破坏生产力，推动分布式编译和缓存需求刚性增长。
    - **sccache生态承压加剧** (方向: down, 强度: high): v0.16.0发布但mold兼容性问题未修复，用户可能回流ccache。
    - **Bazel/Buck2讨论热但迁移壁垒大** (方向: stable, 强度: medium): 优势明显但迁移成本高，CMake主导地位稳固。
    - **FASTBuild作为开源分布式编译工具被提及** (方向: new, 强度: low): 支持缓存和网络分发，值得跟踪社区活跃度。
- **值得长期跟踪的技术方向/话题**: AI驱动编译优化、分布式构建缓存、sccache vs ccache生态演变、Bazel/Buck2迁移壁垒、FASTBuild发展。
- **竞品动态**:
    - **微软**: VS 2026集成Copilot实现上下文感知重构和构建优化，直接对标Incredibuild。
    - **Incredibuild**: 推广AI Sandbox和Build Cache，应对微软竞争。
    - **sccache**: 发布v0.16.0，但mold兼容性问题未修复，生态稳定性受质疑。
    - **ccache**: 持续更新，2026年5月发布4.13.6，维护稳定，可能吸引sccache用户回流。
    - **FASTBuild**: 作为开源分布式编译工具被提及，但社区活跃度未知。
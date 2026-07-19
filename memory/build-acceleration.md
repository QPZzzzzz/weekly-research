# build-acceleration — Research Memory

最后更新: 2026-07-19

- **公司/产品/项目**: 腾讯 yadcc, 微软 Visual Studio 2026, Mozilla sccache, Incredibuild, FASTBuild, distcc, ccache, Bazel, Buck2, mold 链接器
- **重要趋势信号**:
    - **AI 驱动编译优化产品化** (high): 微软 VS2026 集成 AI 构建优化、Sample PGO、Copilot Chat，AI 从辅助编码进入编译流程。
    - **分布式编译性能量级突破** (high): 腾讯 yadcc 在 1000 核集群上实现 15 倍编译加速（LLVM 从 47 分 51 秒降至 3 分 11 秒）。
    - **构建缓存成为 CI/CD 标配** (high): 多篇 2026 年 CI/CD 指南强调缓存依赖和“10 分钟构建规则”。
    - **Bazel/Buck2 迁移讨论升温** (high): 社区焦点从“能否替代”转向“如何迁移”，Bazel 被列为重要选项。
    - **sccache 生态承压** (medium): v0.16.0 发布但 mold 兼容性问题未解；但 sccache+mold 可加速 Rust 编译 73%，提供正面用例。
- **值得长期跟踪的技术方向/话题**:
    - AI 原生 C++ 工作流（VS2026 实际效果与用户反馈）
    - 分布式编译（yadcc 在更多场景的部署与性能数据）
    - 下一代构建系统（Bazel/Buck2 迁移实践）
    - sccache 与 mold 兼容性修复进展
- **竞品动态**:
    - **新产品/功能**: 微软 VS2026 集成 AI 驱动构建优化；sccache v0.16.0 发布。
    - **融资/合作**: 无。
    - **技术突破**: 腾讯 yadcc 实现 15 倍编译性能提升；sccache+mold 组合提升 Rust 编译速度 73%。
    - **推广**: Incredibuild 持续推广 Build Cache 和分布式处理方案。
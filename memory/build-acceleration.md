# build-acceleration — Research Memory

最后更新: 2026-07-02

- **公司/产品/项目**: Incredibuild (AI Sandbox, Build Cache), Visual Studio 2026 (Copilot 构建分析), sccache, mold, Bazel, Buck2, CMake, ccache, distcc, yadcc, homcc, FASTBuild.
- **重要趋势信号**:
    - **AI 深度集成至开发工具链** (方向: up, 强度: high): AI 从辅助升级为智能核心，主动诊断构建瓶颈、预测缓存，Incredibuild 和 VS 2026 已落地。
    - **“分布式编译+缓存”成大型 C++ 项目标配** (方向: up, 强度: high): 美团(45→8分钟)、腾讯 yadcc、Celonis homcc 等案例验证其必要性。
    - **CI/CD “10分钟规则”成硬共识** (方向: up, 强度: high): 2026年多份指南强调管道时长应控制在5-10分钟，倒逼底层加速技术普及。
    - **sccache 与 mold 兼容性问题** (方向: down, 强度: medium): Issue #1755 导致缓存失效，可能引发用户迁移至 ccache 或商业方案。
    - **现代构建系统(Bazel/Buck2)挑战 CMake** (方向: stable, 强度: medium): 讨论热度高，但迁移壁垒(学习曲线、生态兼容)巨大，CMake 主导地位短期难撼。
- **值得长期跟踪的技术方向/话题**:
    - AI 驱动编译优化 (Incredibuild vs VS 2026 竞争态势)
    - sccache 与 mold 兼容性修复进展及用户迁移路径
    - ccache 生态是否因 sccache 问题回升
    - 分布式编译开源项目 (yadcc, homcc) 社区活跃度变化
- **竞品动态**:
    - **Incredibuild**: 推出 AI Sandbox 和 Build Cache，从工具商升级为平台级基础设施。
    - **微软**: Visual Studio 2026 正式发布，集成 AI 驱动的构建优化和 Copilot 构建分析，与 Incredibuild 直接竞争。
    - **sccache**: 与 mold 链接器存在兼容性问题 (Issue #1755)，导致缓存失效，影响 clean build 性能。
    - **Bazel/Buck2**: 讨论热度持续，但缺乏大规模迁移案例，CMake 主导地位稳固。
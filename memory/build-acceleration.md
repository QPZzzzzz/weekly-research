# build-acceleration — Research Memory

最后更新: 2026-05-13

- **公司/产品/项目**: Microsoft Visual Studio 2026, MSVC 14.51, ccache, sccache, CMake, Bazel, Buck2, Incredibuild, GitNexa, Kellton, JetBrains TeamCity, CISA/FBI
- **重要趋势信号**:
    - **AI 驱动编译优化** (方向: 新趋势, 描述: AI 从辅助编码进入智能编译，用于预测性缓存、测试选择和自愈管道, 强度: high)
    - **sccache 生态崛起** (方向: 上升, 描述: sccache 凭借多语言支持和云原生特性，在 CI/CD 中成为缓存标配，C/C++ 和 Rust 命中率高, 强度: high)
    - **构建系统格局变化** (方向: 持续, 描述: CMake 主流，Bazel/Buck2 在大型项目中挑战传统方案，但易用性仍是门槛, 强度: medium)
    - **美国政策压力** (方向: 下降, 描述: CISA/FBI 要求关键软件避免 C/C++，推动向 Rust 迁移，间接促进跨语言构建优化需求, 强度: medium)
    - **云成本优化驱动** (方向: 持续, 描述: 缓存+分布式编译组合是降本增效核心方案，构建时间可从 45 分钟降至 8 分钟, 强度: high)
- **值得长期跟踪的技术方向**: AI 智能编译 (预测性缓存、自愈管道), 跨语言分布式构建 (sccache, Buck2), 内存安全语言迁移 (Rust), 构建系统易用性改进
- **竞品动态**:
    - **Microsoft**: VS 2026 Profiler Agent 支持 C++ 单元测试自动优化；MSVC 14.51 支持新架构
    - **Meta**: Buck2 用 Rust 重写，强调语言无关性和增量构建，挑战 Bazel
    - **sccache**: 在 C/C++ 和 Rust 构建中缓存命中率高，支持 Swift 等多语言
    - **Incredibuild**: 持续输出构建加速指南，强调虚拟化分布式处理
    - **JetBrains TeamCity**: 以“自优化管道”和“智能测试分割”为特色
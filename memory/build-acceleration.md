# build-acceleration — Research Memory

最后更新: 2026-05-15

- **公司/产品/项目**: Visual Studio 2026, sccache, Bazel, Buck2, CMake, Incredibuild, distcc, ccache, GitNexa, P99Soft, Xmake, C++ Modules
- **重要趋势信号**:
    - **AI驱动编译优化** (方向: up, 强度: high): AI从辅助编码演进为编译加速引擎，VS 2026集成AI，CI/CD管道采用AI驱动测试选择和预测性缓存。
    - **sccache生态崛起** (方向: up, 强度: high): 多语言支持（C++、Rust、Swift）和云原生特性使其成为CI/CD缓存标配，编译时间从58秒降至30秒。
    - **分布式编译+缓存组合** (方向: up, 强度: high): 成为大型C++项目降本增效核心方案，构建时间可缩短80%以上（如45分钟→8分钟）。
    - **CI/CD管道智能化** (方向: up, 强度: high): 2026年趋势聚焦AI驱动、自动化、自愈管道。
    - **C++ Modules逐步可用** (方向: new, 强度: medium): 兼容性方案复杂，构建系统需同时处理Modules和传统头文件。
    - **Bazel/Buck2挑战CMake** (方向: stable, 强度: medium): 技术优势明显，但易用性门槛高，CMake仍主流。
- **长期跟踪技术方向**: C++ Modules兼容性进展及构建系统支持；AI驱动测试选择和自愈管道落地效果；sccache对更多语言的支持扩展。
- **竞品动态**:
    - **新产品**: Visual Studio 2026深度集成AI；Buck2用Rust重写，强调语言无关性和增量构建。
    - **融资/合作**: 无明确提及。
    - **技术突破**: sccache在Swift社区应用；分布式编译与缓存组合在美团实践（45分钟→8分钟）；AI驱动编译优化成为明确趋势。
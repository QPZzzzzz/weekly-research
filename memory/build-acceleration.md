# build-acceleration — Research Memory

最后更新: 2026-05-17

- **公司/产品/项目**: 美团, 腾讯 yadcc, sccache, ccache, Incredibuild, Bazel, Buck2, Visual Studio 2022/2026, MSVC.
- **重要趋势信号**:
    - **分布式编译+缓存组合成为大型C++项目标配** (high): 美团(45min→8min), 腾讯yadcc(512并发), sccache(58s→30s).
    - **AI驱动CI/CD管道** (high): VS Copilot集成, AI实现40%构建时间减少.
    - **缓存工具生态活跃** (high): ccache 4.13.x更新并支持MSVC; sccache强调快速miss和云存储.
    - **CI/CD管道优化成2026年焦点** (high): 层缓存、AI自优化、临时环境(EaaS).
    - **现代构建系统(Bazel/Buck2)挑战传统** (medium): 功能强但学习曲线高.
    - **C++ Modules进入“可用”阶段** (medium): MSVC持续修复.
- **值得长期跟踪的技术方向**: 分布式编译与缓存组合策略; AI在CI/CD中的智能测试选择与预测性缓存; 缓存工具(ccache/sccache)对Windows生态的扩展; 现代构建系统(Bazel/Buck2)的易用性突破.
- **竞品动态**:
    - **新产品/开源**: 腾讯开源yadcc(512并发, 工业生产优化).
    - **融资/合作**: 无.
    - **技术突破**: ccache支持MSVC缓存; sccache云存储原生支持; AI驱动管道实现40%构建时间减少.
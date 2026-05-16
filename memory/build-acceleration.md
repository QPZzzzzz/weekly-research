# build-acceleration — Research Memory

最后更新: 2026-05-16

### 关键记忆点

- **公司/产品/项目：** Visual Studio 2026, MSVC Build Tools, ccache 4.13, zccache, Bazel, Buck2, sccache, Intel oneAPI 2026.0, Xmake, CMake, distcc, Clearwater Forest (Intel处理器)
- **重要趋势信号：**
    - **AI深度集成至开发工具链** (方向: up, 强度: high) — Visual Studio 2026整合AI平台提升编译性能；行业预测90%+开发者使用AI辅助编码，AI驱动CI/CD中的测试选择、预测性缓存和自愈管道。
    - **分布式编译与缓存组合成为大型C++项目核心策略** (方向: up, 强度: high) — 美团案例显示构建时间从45分钟降至8分钟（缩短80%+）；sccache在远程Mac CI中缓存后编译时间从58秒降至30秒。
    - **缓存工具生态持续演进** (方向: up, 强度: medium) — ccache 4.13支持MSVC缓存，扩展至Windows生态；新秀zccache出现，声称冷缓存后快速重建。
    - **现代构建系统（Bazel、Buck2）挑战传统方案** (方向: stable, 强度: medium) — 优势在分布式缓存和远程构建，但学习曲线和配置复杂性是普及门槛。
    - **C++ Modules进入“可用”阶段** (方向: stable, 强度: medium) — MSVC持续修复，Xmake支持，但兼容性方案复杂。
    - **Intel oneAPI编译器优化新处理器** (方向: up, 强度: medium) — 针对Clearwater Forest等处理器优化，提供“零成本”加速方案。
- **值得长期跟踪的技术方向/话题：**
    - AI驱动CI/CD管道（测试选择、预测性缓存、自愈管道）
    - 分布式编译与缓存组合策略（ccache/sccache/zccache）
    - 现代构建系统（Bazel/Buck2）的易用性改进
    - C++ Modules的兼容性方案与大规模普及进展
    - 硬件厂商（如Intel）对编译速度的优化
- **竞品动态：**
    - **新产品/版本：** ccache 4.13（支持MSVC），zccache（多语言缓存替代品），Intel oneAPI 2026.0（新处理器优化）
    - **融资/合作：** 无明确融资或合作信息
    - **技术突破：** Visual Studio 2026深度集成AI平台；Buck2用Rust重写解决Java性能问题；MSVC Build Tools持续修复C++ Modules
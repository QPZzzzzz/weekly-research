# build-acceleration — Research Memory

最后更新: 2026-05-21

- **公司/产品/项目**: Visual Studio 2026, GitHub Copilot, Build Insights, Incredibuild, ccache, sccache, Buck2, Bazel, CMake, FASTBuild, mold, MSVC, Unreal Engine, 美团, 腾讯, Meta, Mozilla, JetBrains, Docker, GitHub Actions.
- **重要趋势信号**:
    - **AI深度嵌入构建优化成为主流** (high): VS 2026 集成 Copilot 自动修复构建瓶颈，可减少 40% 构建时间。
    - **分布式编译+缓存组合成标配** (high): 美团/腾讯案例显示构建时间从 45 分钟降至 8 分钟。
    - **缓存工具生态空前活跃** (high): ccache 密集迭代扩展 MSVC 支持，sccache 支持云存储和多语言。
    - **现代构建系统挑战传统** (medium): Buck2 开源但 C/C++ 依赖导入仍面临兼容性挑战。
    - **大型工业级项目加速落地存兼容性问题** (medium): 历史包袱导致新技术在大型 C++ 项目中水土不服。
    - **MSVC运行时性能持续改进** (medium): VS 2026 中 Unreal Engine 示例性能提升 6%。
- **值得长期跟踪的技术方向**:
    - AI 自主构建优化 (Copilot + Build Insights)
    - 分布式编译 + 智能缓存组合策略
    - 现代构建系统 (Buck2, Bazel) 在 C++ 生态的落地
    - MSVC 运行时性能改进对游戏/高性能计算的影响
    - 缓存工具 (ccache vs sccache) 技术路线竞争
- **竞品动态**:
    - **新产品/版本**: Visual Studio 2026 发布，深度集成 AI 构建优化；ccache 4.13.2-4.13.6 密集发布；Buck2 开源。
    - **融资/合作**: 无明确融资信息；Incredibuild 引擎被集成到 VS 2026。
    - **技术突破**: sccache 提出“快速 miss 优于慢速 hit”设计哲学；Copilot 利用 Build Insights 自动修复构建性能问题。
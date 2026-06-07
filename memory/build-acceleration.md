# build-acceleration — Research Memory

最后更新: 2026-06-07

### 关键记忆点

#### 公司/产品/项目
- **微软**: Visual Studio 2026, GitHub Copilot Build Insights, MSVC
- **Google**: sccache (Android 工具链), CUDA 支持
- **Meta**: Buck2 (开源, Rust 核心)
- **mold**: 链接器 (与 sccache 兼容性问题)
- **Incredibuild**: 商业构建加速方案
- **Blender**: 开发者论坛 (C++20 模块讨论)

#### 重要趋势信号
- **AI 集成 CI/CD 构建优化** (high): 微软在 VS 2026 中集成 Copilot 进行构建性能分析，标志 AI 从代码生成延伸到构建优化。
- **分布式编译+缓存成工业级标配** (high): Google 将 sccache 纳入 Android 工具链，支持 C/C++/Rust/CUDA 及 icecream 式分布式编译。
- **现代构建系统挑战 CMake** (high): Meta 开源 Buck2 (Rust 核心, Starlark 规则)，代表构建系统向高效、安全、可扩展发展。
- **CI/CD “10分钟规则” 成共识** (high): 2026 年指南强调核心 CI 检查应控制在 10 分钟内，驱动编译加速刚性需求。
- **mold 与 sccache 兼容性问题** (medium): 使用 mold 导致 sccache 缓存失效，反映工具链集成中的实际痛点。
- **C++20 模块在大型项目中仍不可及** (low): Blender 论坛认为短期内无法用于大型项目，unity builds 仍是当前最有效手段。

#### 值得长期跟踪的技术方向
- **AI 辅助构建优化**: 微软举措可能引发行业跟风，未来或出现更多 AI 构建分析工具。
- **Buck2 社区采用与贡献**: 判断其能否挑战 Bazel 和 CMake 的关键指标。
- **sccache 与 mold 兼容性解决进展**: 衡量工具链生态成熟度的试金石。
- **C++20 模块在大型项目中的实际突破**: 一旦有成功案例，将彻底改变 C++ 编译加速格局。

#### 竞品动态
- **微软**: VS 2026 集成 AI 构建性能分析，MSVC 在 Unreal Engine 场景下运行时性能提升。
- **Google**: sccache 集成到 Android 工具链，扩展支持 CUDA 和分布式编译。
- **Meta**: 开源 Buck2，核心用 Rust 编写，规则用 Starlark，支持增量依赖图。
- **Incredibuild**: 持续输出构建系统比较内容，强调 Build Cache 和分布式处理，市场教育动作频繁。
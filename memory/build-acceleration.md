# build-acceleration — Research Memory

最后更新: 2026-06-11

### 关键记忆点

- **公司/产品/项目**: sccache (Google Android), Visual Studio 2026 (微软), Buck2 (Meta), Bazel (Pigweed项目), Intel oneAPI 2026, mold, Incredibuild, distcc, CMake, C++20 Modules, Unity Builds, GitHub Copilot
- **重要趋势信号**:
    - **CI/CD “10分钟规则” 成为行业刚性约束** (强度: high): 管道总时长控制在5-10分钟成为最佳实践，驱动编译加速需求爆发。
    - **sccache 确立主流编译缓存工具地位** (强度: high): Google Android采用，支持云存储，但存在与mold的兼容性问题。
    - **AI 集成构建分析从概念走向产品** (强度: high): Visual Studio 2026集成GitHub Copilot构建性能分析，是重要产品化里程碑。
    - **现代构建系统 (Bazel, Buck2) 加速挑战传统CMake地位** (强度: medium): Pigweed转向Bazel，Buck2社区活跃，生态分化加剧。
    - **C++20模块在大型项目中应用前景依然黯淡** (强度: medium): Blender论坛认为Unity Builds仍是现实选择，C++20模块不实用。
- **值得长期跟踪的技术方向/话题**:
    - **sccache与mold兼容性问题**的解决方案进展。
    - **Bazel在嵌入式项目（如Pigweed）中的采用**是否扩大，可能挑战CMake地位。
    - **Intel oneAPI 2026编译器**在实际项目中的构建加速效果。
    - **分布式编译技术**从distcc到sccache的演进，云存储成为关键。
- **竞品动态**:
    - **新产品**: Visual Studio 2026 (集成AI分析), Intel oneAPI 2026 (优化构建速度)
    - **融资/合作**: 无明确信息。
    - **技术突破**: sccache成为主流，Buck2开源，Bazel被Pigweed采用。
    - **技术痛点**: sccache与mold兼容性问题 (Issue #1755) 是当前最突出的技术痛点。
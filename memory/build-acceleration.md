# build-acceleration — Research Memory

最后更新: 2026-06-06

### 关键记忆点

- **公司/产品/项目**: 百度Comate, 腾讯yadcc, sccache, Incredibuild, Bazel, Buck2, Intel oneAPI, Blender, xmake, Icecream, Kubernetes, FASTBuild, ccache, distcc, homcc, mold, GitLab CI, Red Hat Developer.
- **重要趋势信号**:
    - **分布式编译+缓存成标配**: 百度、腾讯开源/发布指南，sccache实测效果显著 (首次58s→缓存后30s)。**强度: high**
    - **现代构建系统(Bazel/Buck2)挑战CMake**: 讨论热度上升，但迁移门槛高。**强度: medium**
    - **CI/CD“10分钟规则”成共识**: 核心检查控制在10分钟内，强调层缓存。**强度: medium**
    - **C++20模块有望加速编译**: 减少解析开销，但缺乏大规模验证。**强度: medium**
    - **Intel oneAPI 2026优化构建速度**: 硬件厂商开始关注编译性能。**强度: low**
- **值得长期跟踪的技术方向/话题**:
    - 腾讯yadcc开源后的社区采用与贡献情况。
    - C++20模块在大型项目中的实际编译加速效果。
    - Bazel/Buck2等现代构建系统的易用性改进与迁移工具发展。
    - AI集成CI/CD实现预测性缓存与自愈（本期热度消退，但值得关注后续进展）。
- **竞品动态**:
    - **新产品/开源**: 腾讯开源yadcc (支持512并发编译)。
    - **技术突破**: Intel oneAPI 2026编译器无需改代码即可提升构建速度。
    - **合作/内容**: 百度Comate发布系统性分布式编译指南；Incredibuild持续输出构建系统比较内容。
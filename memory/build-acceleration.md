# build-acceleration — Research Memory

最后更新: 2026-05-26

### 关键记忆点

- **公司/产品/项目：** 腾讯 yadcc、Microsoft VS 2026 / GitHub Copilot Build Performance、Incredibuild、sccache、mold、Buck2、Bazel、ccache、distcc
- **重要趋势信号：**
    - **AI 驱动构建优化 (high)**：AI 从“增加构建压力”转向“深度参与优化”，VS 2026 集成 Copilot 分析构建性能并自动建议优化。
    - **分布式编译开源新选择 (high)**：腾讯开源 yadcc，支持 512 并发编译，面向工业级场景，可能改变市场格局。
    - **C++26 反射催生新需求 (high)**：反射特性将大幅增加编译复杂度，为编译加速工具（缓存、分布式）创造巨大市场机会。
    - **构建缓存核心地位强化 (medium)**：CI/CD 最佳实践强调缓存优先，分布式编译在单文件修改场景效果有限，行业认知更成熟。
    - **工具链兼容性风险 (medium)**：sccache 与 mold 链接器存在兼容性问题，提醒集成测试的重要性。
- **长期跟踪方向：** C++26 反射特性实现进度、AI 辅助构建优化工具效果、yadcc 社区发展、Buck2/Bazel 在 C++ 生态的渗透、sccache 与 mold 兼容性修复。
- **竞品动态：**
    - **新产品/开源：** 腾讯开源 yadcc（分布式编译）。
    - **产品集成：** VS 2026 集成 AI 构建优化工具。
    - **技术突破/合作：** Incredibuild 定位为 AI 编码代理的执行层基础设施。
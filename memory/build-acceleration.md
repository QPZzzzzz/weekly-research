# build-acceleration — Research Memory

最后更新: 2026-05-28

- **公司/产品/项目**: Incredibuild, Microsoft VS 2026, Meta Buck2, ccache 4.13.6, sccache, mold, Blender, GitLab CI, FASTBuild, Distcc, Bazel, Meson, JetBrains TeamCity, Earthly
- **重要趋势信号**:
    - **缓存优先策略全面落地** (方向: 强化, 强度: high) - 行业共识从“如何分布式编译”转向“如何最大化缓存命中率”，GitLab CI、ccache、Incredibuild均强调此点。
    - **Meta开源Buck2** (方向: 新出现, 强度: high) - 用Rust编写，原生支持增量依赖图和分布式缓存，与Bazel竞争，推动新一代构建系统渗透。
    - **VS 2026引入SPGO优化** (方向: 新出现, 强度: medium) - 利用硬件采样提升5-15%运行时性能，无需合成训练场景，标志编译优化向运行时加速延伸。
    - **sccache与mold兼容性问题** (方向: 减弱, 强度: medium) - Issue #1755报告缓存无法复用，暴露工具链集成测试盲区。
    - **分布式编译在单文件修改场景局限** (方向: 稳定, 强度: low) - 仅并行编译大量文件时有效，强化“缓存优先，分布式为辅”认知。
- **长期跟踪技术方向**: Buck2社区采用及对C++生态影响、VS 2026 SPGO实际效果反馈、ccache新功能兼容性改进、C++20模块对编译加速影响、AI辅助构建优化（如VS Copilot）。
- **竞品动态**:
    - **新产品/开源**: Meta开源Buck2构建系统（Rust编写）。
    - **技术突破**: VS 2026引入SPGO优化（5-15%性能提升）。
    - **融资/合作**: 无明确提及。
    - **其他**: ccache发布4.13.6版本（持续维护）；sccache与mold存在兼容性问题（Issue #1755）；Incredibuild定位为AI编码代理执行层基础设施。
# build-acceleration — Research Memory

最后更新: 2026-07-09

- **公司/产品/项目**：Microsoft Visual Studio 2026、Incredibuild AI Sandbox & Build Cache、sccache、ccache、腾讯云 yadcc、distcc、FASTBuild、Bazel、Buck2、CMake、MSVC
- **重要趋势信号**：
    - AI驱动编译优化成为竞争焦点（方向：up，强度：high）——微软VS 2026集成Copilot，Incredibuild推AI Sandbox应对
    - CI/CD管道优化需求刚性增长（方向：up，强度：high）——多篇2026指南强调并行与缓存，“10分钟规则”成硬共识
    - sccache生态承压，ccache稳定更新（方向：down，强度：medium）——sccache v0.16.0 mold问题未修复，ccache 4.13.6稳定发布
    - 开源分布式编译工具涌现（方向：new，强度：medium）——腾讯云开源yadcc，distcc持续维护，FASTBuild被提及
    - Visual Studio 2026成为C++开发重要更新（方向：up，强度：high）——GA发布，集成Copilot、C++23、MSVC性能提升
- **值得长期跟踪的技术方向/话题**：
    - AI在编译优化中的深度集成（如Copilot与第三方工具竞争）
    - 开源分布式编译工具（yadcc、distcc、FASTBuild）的社区活跃度与实际采用
    - Bazel/Buck2的迁移壁垒与CMake主导地位变化
    - sccache vs ccache的用户回流趋势
- **竞品动态**：
    - Microsoft：VS 2026 GA，集成Copilot、C++23、MSVC性能提升，直接与Incredibuild竞争
    - Incredibuild：推广AI Sandbox和Build Cache，应对微软竞争
    - sccache：v0.16.0发布，但mold兼容性问题未修复，生态承压
    - ccache：4.13.6稳定发布，可能吸引用户回流
    - 腾讯云：开源yadcc，加入分布式编译工具生态
    - distcc：持续维护，与ccache组合使用
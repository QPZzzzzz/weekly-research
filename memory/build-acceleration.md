# build-acceleration — Research Memory

最后更新: 2026-07-05

- **公司/产品/项目**：Microsoft Visual Studio 2026、Incredibuild、sccache、mold、ccache、Bazel、Buck2、CMake、yadcc、homcc、美团、GitHub Copilot
- **重要趋势信号**：
  - **AI驱动编译优化竞争升级**：微软VS 2026集成Copilot自动优化构建，直接对标Incredibuild的AI Sandbox和Build Cache。强度：high
  - **CI/CD“10分钟规则”成硬共识**：管道超10分钟影响生产力，大型C++项目需分布式编译+缓存压缩时间（如美团案例45分钟→8分钟）。强度：high
  - **sccache生态承压**：与mold链接器兼容性问题（Issue #1755）未修复，用户可能回流ccache。强度：medium
  - **Bazel/Buck2讨论热但迁移壁垒大**：优势明显，但CMake主导地位稳固，迁移成本高。强度：medium
- **值得长期跟踪的技术方向/话题**：
  - sccache与mold兼容性修复进展及用户迁移路径
  - ccache生态是否因sccache问题回升
  - 分布式编译开源项目（yadcc, homcc）社区活跃度变化
- **竞品动态**：
  - **微软**：VS 2026集成AI构建优化工具，对标Incredibuild
  - **Incredibuild**：持续推广AI Sandbox和Build Cache，面临VS 2026竞争
  - **sccache**：与mold兼容性问题未修复，生态稳定性受质疑
  - **ccache**：可能因sccache问题重新获得关注
  - **Bazel/Buck2**：讨论热度高，但迁移壁垒大，适合大型新项目
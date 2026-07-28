# build-acceleration — Research Memory

最后更新: 2026-07-28

### 关键记忆点

- **公司/产品/项目：** 腾讯 yadcc、Microsoft Visual Studio 2026、Mozilla sccache、ccache、Incredibuild、Bazel、Buck2、Pigweed、mold 链接器
- **重要趋势信号：**
    - **分布式编译开源化与性能竞赛 (high):** 腾讯 yadcc 开源，1000核集群上编译 LLVM 仅需 3 分 11 秒，性能远超传统方案，标志开源工具进入性能竞赛阶段。
    - **AI 驱动构建优化进入 IDE (high):** Visual Studio 2026 集成 Copilot，可智能分析构建瓶颈并推荐优化选项，AI 从辅助编码转向优化工程效率。
    - **构建缓存成为 CI/CD 标配 (high):** 多个案例显示引入缓存可将构建时间降低 95%（如 10 分钟降至 30 秒），已成为 DevOps 实践的核心手段。
    - **下一代构建系统迁移加速 (high):** Bazel/Buck2 讨论焦点从“是否采用”转向“如何迁移”，Pigweed 等知名项目已计划迁移。
    - **C++26 标准利好编译加速 (medium):** 引入 `std::flat_map`/`flat_set` 和 `std::simd`，设计上考虑减少模板实例化开销，间接利好编译加速。
    - **mold 与 sccache 兼容性问题 (medium):** 技术摩擦点，可能导致用户无法同时享受两者优势，需关注后续解决方案。
- **值得长期跟踪的技术方向/话题：**
    - 分布式编译工具（yadcc, FASTBuild, distcc）的性能竞赛与开源生态。
    - AI 在构建优化中的深度应用（如 IDE 集成、智能瓶颈分析）。
    - Bazel/Buck2 等下一代构建系统的迁移实践与工具链集成。
    - C++26 新特性对编译效率的实际影响。
    - 高性能构建工具链（如 mold + sccache）的兼容性与整合。
- **竞品动态：**
    - **腾讯 yadcc:** 开源分布式编译系统，性能数据亮眼（15倍加速）。
    - **Microsoft Visual Studio 2026:** 集成 AI 驱动构建优化（Copilot），全面支持 C++23。
    - **Mozilla sccache:** v0.16.0 发布，生态成熟，但出现与 mold 的兼容性问题。
    - **ccache:** 持续维护至 4.13.6，但无重大创新。
    - **Incredibuild:** 推广商业化缓存和分布式方案，宣称“8倍更快的 CI 运行器”，并开始覆盖 Bazel 优化。
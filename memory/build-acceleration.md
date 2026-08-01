# build-acceleration — Research Memory

最后更新: 2026-08-01

## 关键记忆点

- **公司/项目**：腾讯yadcc、Mozilla sccache、Wasmer sccache fork、Incredibuild、Pigweed、Buck2（Meta）、Microsoft（VS 2026/MSVC）、ccache、mold、distcc

- **信号：开源分布式编译进入性能竞赛**（up，high）— 腾讯yadcc千核集群编译LLVM仅3分11秒，15倍加速比，性能对标商业方案

- **信号：构建缓存成为CI/CD标配**（up，high）— sccache/ccache缓存可降构建时间最高95%（45分钟→8分钟），缓存命中率成核心KPI

- **信号：下一代构建系统迁移加速**（up，high）— Pigweed正式提案迁移至Bazel（SEED 0111），讨论焦点从"是否采用"转向"如何迁移"

- **信号：商业方案跟进开源趋势**（up，medium）— Incredibuild开始覆盖Bazel优化，宣称加速CI运行器8倍，商业与开源从对立走向融合

- **信号：sccache与mold兼容性问题**（stable，medium）— v0.16.0出现兼容性问题，工具链组合兼容性成选型隐性变量

- **信号：ccache进入稳定维护期**（stable，low）— 4.13.6无重大更新，关注度自然下降

- **竞品动态**：Incredibuild内容策略转向覆盖Bazel/CMake生态；Microsoft发布VS 2026（接近完整C++23）；Wasmer fork增强sccache云存储能力

- **长期跟踪方向**：① 分布式编译集群调度效率与网络传输优化；② Bazel/Buck2生态迁移成本与CMake地位挑战；③ 商业方案与开源工具深度整合模式（"开源核心+商业增强"）；④ 工具链组合兼容性摩擦（编译器+缓存+链接器+分布式层）
# build-acceleration — Research Memory

最后更新: 2026-09-26

# 编译加速与分布式编译调研 · 关键记忆点

## 一、涉及公司/产品/项目

- **腾讯 yadcc**：C++ 分布式编译系统，腾讯内部大规模验证后开源
- **sccache**：Mozilla 开源编译器缓存（Rust 实现）
- **mold**：高速链接器
- **Visual Studio 2026**：微软 IDE，正式发布
- **Copilot @BuildPerfCpp**：VS 2026 内 AI 构建调优能力
- **MSVC Build Tools**：2026 年 9 月预览更新
- **Pigweed**：Google 主导嵌入式项目，SEED 0111 文档
- **Incredibuild**：商业化分布式编译（经龙智 DragonSoft 代理）
- **FASTBuild / Icecream / distcc**：开源分布式编译工具
- **Bazel / Buck2 / GN / CMake / Meson**：构建系统
- **ccache**：经典编译器缓存

## 二、重要趋势信号

- **方向 new｜腾讯开源 yadcc**：分布式编译层新增中国大厂级玩家，明确"提吞吐不降单文件耗时"能力边界，与 build cache 互补｜强度 **high**
- **方向 new｜sccache 与 mold 兼容性摩擦**：mold 链接器导致 sccache 缓存失效，首次暴露"缓存层+链接层"实际兼容性问题｜强度 **high**
- **方向 up｜VS 2026 正式发布**：MSVC 运行时性能提升、ARM64 ASan 支持，从预告转为落地｜强度 **medium**
- **方向 up｜Copilot @BuildPerfCpp 迭代构建优化**：AI 构建调优从第三方迁入 IDE 原生，形成"分析→迭代验证"闭环｜强度 **high**
- **方向 up｜Pigweed SEED 0111**：Bazel 升为主构建系统，嵌入式 Bazel 化进入文档化落地期｜强度 **high**
- **方向 up｜VS 2026 安装器限制构建工具版本**：最低锁定 MSVC 19.44，IDE 与构建工具解耦范式遭遇早期摩擦｜强度 **high**
- **方向 up｜MSVC Build Tools 9 月预览更新**：编译器前端/优化器/链接器持续迭代｜强度 **medium**
- **方向 stable｜CI/CD "10 分钟→30 秒"叙事**：build cache 价值主张持续破圈 DevOps｜强度 **medium**
- **方向 stable｜Incredibuild 企业级定位**：强调低维护/低占用/工作负载无关，AI 转型叙事降温（high→medium）｜强度 **medium**
- **方向 stable｜C++ 构建系统选型共识**：CMake 必学、Meson 最有前景、Bazel 可能很棒｜强度 **medium**

## 三、值得长期跟踪的技术方向/话题

- 腾讯 yadcc 与 sccache/ccache 缓存层的集成方式及自托管选型讨论
- sccache-mold 类"缓存层×链接层"兼容性问题是否扩散至更多工具组合
- 构建加速三层分工格局（缓存层+分布式层+链接层）的层间接口稳定性
- VS 2026 ARM64 ASan 对 Windows on ARM 构建与 CI 实践的影响
- 嵌入式社区是否跟进 Pigweed 的 Bazel 化决策
- Copilot @BuildPerfCpp 是否引发其他 IDE/构建工具跟进 AI 调优
- IDE 与构建工具版本解耦范式的可信度与用户接受度
- Bazel/Buck2 作为下一代构建系统的替代能力（C/C++ 依赖导入标准化缺失）

## 四、竞品动态

- **腾讯 yadcc**：开源分布式编译系统，为国内企业提供新自托管选项，可能推动分布式编译与缓存层集成范式讨论
- **Incredibuild**：经龙智 DragonSoft 强化企业级定位（低维护/低占用/工作负载无关）；Islo AI 沙箱与构建卫士无新增动态，进入落地观察期
- **微软 VS 2026**：正式发布，AI 构建调优迁入 IDE 原生，对 Incredibuild 等第三方构成直接竞争压力
- **Pigweed**：Bazel 升为主构建系统，Google 主导项目示范效应强
- **sccache**：GitHub Projects 推广为"可将构建时间减半的开源编译器缓存"，但暴露与 mold 兼容性缺陷
- **Meta Buck2 / Bazel**：Lobsters 讨论其替代现有开源构建系统能力，Tweag 指出 C/C++ 依赖导入缺乏标准方式
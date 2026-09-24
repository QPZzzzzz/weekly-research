# build-acceleration — Research Memory

最后更新: 2026-09-24

# 调研记忆点（2026年9月）

## 涉及公司/产品/项目
- Microsoft / Visual Studio 2026 / MSVC / Copilot `@BuildPerfCpp`
- Incredibuild / Islo AI 沙箱 / 构建卫士（Beta）
- sccache / ccache / Icecream / distcc / FASTBuild / mold
- CMake / Bazel / Meson / Buck2 / Pigweed SEED 0111
- Mozilla / Meta / Google / Apple / Amazon / Azure（数据来源方）

## 重要趋势信号
- **new｜产品｜high**：VS 2026 原生集成 Copilot `@BuildPerfCpp`，AI 构建调优从第三方工具迁入 IDE，冲击 Incredibuild 可观测性产品线
- **new｜竞品｜high**：Incredibuild 推出 Islo AI 沙箱，从分布式编译向 AI 编码基础设施平台转型，将面对 Codespaces/Gitpod 竞争
- **up｜技术｜high**：MSVC 构建性能提升 15-20%（9:19→7:30 等），多机器一致改善，整体上移 C++ 构建基线速度，可能延缓 build cache 引入动力
- **up｜产品｜high**：VS 2026 安装器限制构建工具版本（最低 MSVC 19.44），解耦范式早期摩擦信号扩散
- **down｜产品｜high**：VS 2026 移除 iOS/Android 移动 C++ 工作负载及嵌入式 IoT 工具，或加速嵌入式向 Bazel 迁移
- **up｜技术｜high**：构建加速工具链三层分工格局明确化（缓存层+分布式层+链接层），选型从单点对比进入架构设计
- **up｜技术｜medium**：sccache+Redis 跨域 vs ccache+APFS/NFS 热路径，远程/跨域 CI 构建缓存成独立实践领域
- **new｜技术｜medium**：Icecream 重新进入分布式编译对比视野，自托管方案或重获关注
- **stable｜行业｜medium**：CMake vs Bazel 讨论升温，CMake 生态统治力被承认但技术设计受批评
- **stable｜行业｜high**：CI/CD "10 分钟基准→缓存命中 30 秒"成标准叙事，build cache 价值主张破圈至 DevOps
- **stable｜技术｜low**：AI 驱动 CI/CD 优化进入学术论文阶段，工业界验证仍缺失

## 长期跟踪方向
- Copilot `@BuildPerfCpp` 实际效果与采纳率，是否引发其他 IDE 跟进 AI 构建调优
- Incredibuild Islo AI 沙箱与构建卫士能否形成第二增长曲线
- 嵌入式 C++ 开发者是否加速向 Bazel + 命令行工具链 + VS Code 迁移
- VS 2026 构建工具版本选择受限反馈是否扩散，影响独立升级范式可信度
- Icecream 是否重燃自托管分布式编译方案讨论
- 三层分工格局下单一层级工具的生存策略（向上集成/向下深耕/被原生吸收）
- Bazel Remote Cache API 对 sccache/ccache 的挤压效应

## 竞品动态
- **Microsoft**：VS 2026 推 AI 构建优化 + MSVC 性能提升 15-20%；同时收缩嵌入式/移动端 C++ 工具支持（"聚焦核心、收缩边缘"）
- **Incredibuild**：产品矩阵扩展至 Islo AI 沙箱、构建缓存、可观测性、构建卫士（Beta），战略向 AI 编码基础设施迁移
- **开源工具链**：sccache/ccache 在远程 Mac CI 形成明确分工；Icecream 重回对比视野；mold 稳固链接层地位
- **构建系统**：Bazel 获社区更高技术评价，Pigweed SEED 0111 将 Bazel 升为主构建系统，嵌入式"Bazel 化"浪潮待观察

## 已消退信号（本期无新增）
- ccache 4.13.6 迭代、sccache 社区推广、Pigweed SEED 0111 路线图（进入落地观察期）、Buck2 依赖管理僵局、AI 代理技能包标准化
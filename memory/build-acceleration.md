# build-acceleration — Research Memory

最后更新: 2026-07-01

### 🏢 公司/产品/项目
- **Incredibuild**: 推出 AI Sandbox (ISLO)、CI/CD Acceleration、Build Cache，从工具商升级为平台级基础设施，被微软 VS 2026 集成。
- **Microsoft**: VS 2026 集成 GitHub Copilot 构建性能分析，支持 C++ 构建优化。
- **腾讯**: 开源 yadcc（分布式编译器），支持 512 并发编译，面向工业生产环境。
- **Celonis**: 开源 homcc，主打低带宽场景下的分布式编译。
- **Meta**: 开源 Buck2（构建系统），核心用 Rust，规则用 Starlark。
- **ccache**: 持续更新至 v4.13.6，在 sccache 兼容性问题下可能受益。
- **sccache**: 被 Google 用于 Android 工具链，但存在与 mold 链接器的兼容性问题（Issue #1755）。
- **百度**: 发布 Comate C++ 分布式编译全攻略，强调 xmake 和 Kubernetes 方案。
- **美团**: 分享 C++ 编译耗时优化实践（45 分钟降至 8 分钟）。
- **Intel**: oneAPI 2026 编译器优化构建速度，无需代码修改。
- **RECC**: 开源远程执行缓存编译器，用于 C++ 构建。

### 📈 重要趋势信号
- **AI 深度集成至开发工具链** (high): AI 从“辅助”升级为“智能核心”，主动诊断构建瓶颈、预测性缓存、自愈管道。代表：VS 2026 Copilot 构建分析、Incredibuild AI Sandbox。
- **“分布式编译 + 缓存”成为大型 C++ 项目工业级标配** (high): 美团案例（45→8 分钟）、腾讯 yadcc 开源、Celonis homcc 出现，组合方案从验证进入普及。
- **CI/CD “10 分钟规则”成为行业硬共识** (high): 多篇 2026 年指南强调管道时长应控制在 5-10 分钟，否则影响开发者效率，倒逼底层加速技术普及。
- **缓存工具生态竞争加剧，兼容性问题凸显** (medium): sccache 与 mold 链接器兼容性问题（Issue #1755）导致缓存失效，推动用户评估迁移至 ccache 或商业方案。
- **现代构建系统（Bazel/Buck2）挑战 CMake，但迁移壁垒巨大** (medium): 讨论热度高，但学习曲线陡峭、与 CMake 生态兼容性差，短期内难以撼动 CMake 主导地位。
- **C++20 模块对编译加速有限** (low): 效果类似预编译头文件，代码生成冗余问题未解决，短期内不适用于大型项目。

### 🔭 值得长期跟踪的技术方向或话题
- **AI 预测性缓存与自愈管道**: 从概念走向产品落地，关注 Incredibuild、微软等厂商的具体功能发布。
- **开源分布式编译生态多元化**: yadcc、homcc、Buck2 等高质量开源项目降低企业采用门槛，关注社区活跃度和采用率。
- **编译缓存工具与链接器兼容性**: sccache 与 mold 的问题可能重塑工具格局，关注用户迁移路径和 ccache 生态变化。
- **云存储成为编译缓存关键**: sccache 支持 S3、GCS 等后端，跨团队和 CI 共享编译结果成为趋势。
- **C++26 新特性对编译复杂度的影响**: 新增“史诗级”特性可能催生新的编译优化需求。

### ⚔️ 竞品动态
- **Incredibuild**: 从独立工具商升级为平台级基础设施，推出 AI Sandbox (ISLO)、CI/CD Acceleration，被微软 VS 2026 官方集成。
- **Microsoft**: VS 2026 集成 Copilot 构建性能分析，直接与 Incredibuild 形成竞争。
- **腾讯**: 开源 yadcc，支持 512 并发编译，降低行业门槛，但热度月末有所消退。
- **Celonis**: 开源 homcc，主打低带宽场景，可能吸引对网络带宽敏感的用户。
- **ccache**: 在 sccache 兼容性问题下，凭借持续更新（v4.13.6）和稳定性，生态地位可能回升。
- **Meta (Buck2)**: 开源并采用 Rust 核心，持续吸引技术社区关注，但易用性仍是大规模普及障碍。
- **百度**: 发布 Comate C++ 分布式编译全攻略，系统梳理 Icecream、xmake、Kubernetes 等方案。
# build-acceleration — Research Memory

最后更新: 2026-08-13

## 关键记忆点

### 公司/产品/项目
- **微软 Visual Studio 2026**：C++23 接近完整、集成 GitHub Copilot、改进 MSVC 性能、扩展 ARM64 ASan
- **IncrediBuild**：推出 AI 沙箱 Islo，发布《7 Signs Your CI/CD Pipeline Needs Build Acceleration》
- **sccache**：被 Google Android 采用，支持 S3/GCS/Redis 远程存储，Rust 原生支持
- **ccache**：进入维护期（最新 4.13.6），独立存在感下降
- **NativeLink + CMake**：RE 服务组合应用，早期信号
- **Pigweed**：Bazel 转为主要构建系统，CMake 继续支持，GN 进入维护模式
- **华为云 CodeArts Build**：提供分布式编译 + 增量编译加速（Gcc/Clang）
- **Intel oneAPI DPC++/C++ 2026.0**：提升构建和迭代速度
- **distcc + ccache**：中小型项目仍为主流组合

### 重要趋势信号
- **AI 驱动构建优化产品化**：方向 up，强度 **high**（VS 2026 Copilot、IncrediBuild Islo、Pure Virtual C++ 2026 三大玩家同期布局）
- **CI/CD 构建加速上升为管理 KPI**：方向 up，强度 **high**（构建速度与开发者留存直接关联，采购决策者扩展至工程效能 VP/CTO）
- **RE 服务（Remote Execution）与 CMake 组合**：方向 stable，强度 **medium**（若 NativeLink 降低接入门槛，可能颠覆现有分布式编译格局）
- **ccache 消退，sccache 成主流**：方向 down，强度 **low**（跨语言 + 云原生存储对单语言 + 本地存储的降维打击）
- **Bazel 热度下降，CMake 保持主流**：方向 stable，强度 **low**

### 值得长期跟踪的技术方向
- **AI 驱动的智能构建调度与缓存策略优化**（IDE 原生集成 vs 独立工具链扩展两条路径）
- **RE 服务（Remote Execution）降低接入门槛**——中小团队无需迁移 Bazel 即可享受远程执行
- **sccache 与 mold 兼容性修复**（Issue #1755 本期未提及，若已解决将完善"编译缓存 + 高速链接"链路）
- **VS 2026 对第三方构建加速工具的替代压力**——未来 12 个月与 IncrediBuild 在 CI/CD 场景直接竞争加剧

### 竞品动态
- **IncrediBuild**：向"构建效能全栈平台"转型，面向管理层内容营销获客
- **微软**：VS 2026 内置性能改进 + AI 集成，侵蚀第三方工具差异化价值
- **华为云**：云厂商加速入场分布式编译赛道
- **美团技术团队**：分享 C++ 编译优化实践，指出分布式编译适合大规模项目
- **真实性能数据**：distcc 实践——16 核单机 30 分钟 → 10 台机器 112 核 8 分半
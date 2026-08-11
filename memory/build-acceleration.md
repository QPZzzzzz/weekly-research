# build-acceleration — Research Memory

最后更新: 2026-08-11

## 关键记忆点（编译加速与分布式编译调研）

### 涉及公司/产品/项目
- **sccache**（Mozilla维护，Google Android项目采用）
- **ccache**（4.13.6，稳定维护期）
- **IncrediBuild**（含AI沙箱Islo）
- **Visual Studio 2026**（微软，C++23/Copilot）
- **华为云 CodeArts Build**
- **mold**（高性能链接器，与sccache存在兼容性问题）
- **NativeLink**（RE服务）
- **Bazel / Buck2 / CMake / Meson**（构建系统）
- **yadcc**（腾讯，热度已消退）

### 重要趋势信号
- **sccache 确立跨语言编译缓存主流地位**，支持分布式编译（C/C++/Rust/CUDA）— **high**
- **IncrediBuild 转型构建效能全栈平台**，AI成为新增长点 — **high**
- **CI/CD优化上升为管理议题**，构建加速成为工程效能核心KPI — **high**
- **"分布式编译+本地缓存"组合成为标准实践**，云厂商加速入场 — **high**
- **AI在构建加速和CI/CD优化中开始应用**（产品化落地）— **medium**
- **RE服务（Remote Execution）作为新路径出现**（NativeLink+CMake）— **medium**
- **VS 2026 集成构建加速与AI**，对第三方工具链形成替代压力 — **medium**
- **ccache 信号消退**，被sccache拉开代差 — **low**
- **Bazel 热度下降**，CMake保持主流 — **low**

### 值得长期跟踪的技术方向
- **RE服务（Remote Execution）与CMake组合应用** — 早期信号，可能成为新趋势
- **AI驱动的构建优化**（智能缓存策略、构建任务调度）
- **sccache与mold兼容性修复**（Issue #1755，若解决将完善编译缓存链路）
- **构建系统格局演变**（CMake vs Bazel vs Meson vs Buck2）

### 竞品动态
- **IncrediBuild**：发布AI沙箱Islo、Unity Shader编译优化、8倍CI加速内容；发布C++构建系统指南进行内容营销
- **微软**：VS 2026正式发布，强化C++23、MSVC性能、ARM64 ASan，集成Copilot
- **华为云**：CodeArts Build提供分布式编译+增量编译加速服务（Gcc/Clang，C/C++工程）
- **sccache**：被Google Android项目采用，支持多级缓存和远程存储（S3/GCS），社区活跃度高
- **mold**：广泛使用但存在与sccache的兼容性问题
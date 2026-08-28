# build-acceleration — Research Memory

最后更新: 2026-08-28

## 关键记忆点

### 公司/产品/项目
- **微软**：Visual Studio 2026 集成 GitHub Copilot Build Performance（自动追踪/定位/优化构建瓶颈）
- **IncrediBuild**：AI 沙盒 Islo + CI 加速产品（宣称 8x 更快 CI runners）
- **Google**：Android 官方采用 sccache（支持 C/C++/Rust/CUDA + 分布式编译）
- **Meta**：Buck2 开源构建系统（Rust 核心 + Starlark 规则）
- **美团**：C++ 编译优化实践（分布式编译 + PCH + CCache 组合）
- **腾讯 yadcc**：本期零提及，竞争力下降

### 重要趋势信号
- **AI 构建优化产品化**（high）：微软 Copilot Build Performance + IncrediBuild Islo 双线推进，从"专家经验驱动"转向"AI 数据驱动"
- **sccache 确立编译缓存事实标准**（high）：Google 官方背书，云存储支持（S3/GCS/Azure）构筑壁垒
- **分布式编译 + 缓存结合成主流**（high）：FASTBuild、sccache 原生支持，美团实践验证，从"可选策略"变"主流实践"
- **CI/CD 管道加速成焦点**（high）：AI 辅助编程致提交量激增，共享缓存 + 分布式处理层成核心抓手
- **CMake 主导地位强化，Bazel 热度下滑**（medium）：工程实用主义取代技术理想主义，CMake + 远程执行（RE）成低迁移成本路径
- **Buck2 作为 Bazel 替代方案讨论增多**（medium）：需观察其 CMake 集成能力

### 值得长期跟踪的技术方向
- **AI 沙盒（如 IncrediBuild Islo）在构建优化中的应用**——可能扩展至更多开发场景
- **CI/CD 管道加速与共享缓存集成**——可能成为 2027 年标准实践
- **C++20 模块在编译加速中的应用**——长期跟踪，本期未提及，工具链进展缓慢
- **远程执行（RE）服务与 CMake 组合**——低迁移成本的分布式构建路径

### 竞品动态
- **微软**：VS 2026 集成 Copilot Build Performance，C++23 符合性提升，MSVC 构建工具预览版更新
- **IncrediBuild**：AI 沙盒 Islo + CI 加速产品，ROI 量化叙事（45min→8min），发布构建系统选择指南
- **Google**：Android 官方采用 sccache，最强背书
- **Meta**：Buck2 开源，讨论增多但采用门槛仍高
- **ccache**：持续更新（4.13.6），但功能覆盖被 sccache 超越
- **FASTBuild**：游戏行业标配（Unity/Blob 构建），分布式 + 缓存组合
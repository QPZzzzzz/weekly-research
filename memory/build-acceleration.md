# build-acceleration — Research Memory

最后更新: 2026-07-16

### 公司/产品/项目
- **微软**：Visual Studio 2026（集成 Copilot、AI 构建优化、C++23 支持）
- **Incredibuild**：AI Sandbox、Build Cache
- **腾讯云**：yadcc（开源分布式编译工具）
- **Meta**：Buck2（Rust 编写）
- **Google**：Pigweed（计划迁移至 Bazel）
- **FASTBuild**：被 Unreal Engine 社区采用
- **ccache**：稳定更新（v4.13.6）
- **sccache**：生态承压，未修复 mold 兼容性

### 重要趋势信号
- **AI 驱动编译优化成为竞争焦点**（方向：up，强度：high）：VS 2026 与 Incredibuild 正面交锋，AI 从代码生成渗透到构建流程。
- **CI/CD 管道优化需求刚性增长**（方向：up，强度：high）：“10分钟规则”成共识，云成本压力驱动缓存、并行化。
- **Bazel/Buck2 作为下一代构建系统**（方向：up，强度：high）：讨论焦点从“能否替代”转向“如何迁移”。
- **分布式编译性能显著提升**（方向：up，强度：high）：yadcc 在 1000 核集群上实现 15 倍性能提升（LLVM 编译 3 分 11 秒 vs 47 分 51 秒）。
- **构建缓存成为 CI/CD 标配**（方向：up，强度：high）：ccache、sccache、FASTBuild 从可选优化升级为标准配置。
- **开源分布式编译工具涌现**（方向：up，强度：high）：yadcc、FASTBuild、distcc 形成多层次生态。
- **微软 VS 2026 与 Incredibuild 竞争加剧**（方向：up，强度：high）：产品对位竞争明确。
- **sccache 生态承压，ccache 稳定更新**（方向：stable，强度：medium）：sccache 兼容性问题未解，但 Rust 生态依赖仍存。

### 值得长期跟踪的技术方向/话题
- AI 驱动编译优化（构建流程智能化）
- 分布式编译大规模部署（如 yadcc 的量化基准）
- 构建缓存管理与分发工具创新
- Bazel/Buck2 迁移实践与 Rust 实现
- CUDA C++ 编译时间优化（GPU 计算领域）

### 竞品动态
- **新产品/功能**：微软 VS 2026 集成 Copilot 和 AI 构建优化；Incredibuild 推出 AI Sandbox 和 Build Cache。
- **融资**：无明确融资信息。
- **合作**：无明确合作信息。
- **技术突破**：腾讯云 yadcc 在 1000 核集群上实现 15 倍性能提升；Buck2 核心用 Rust 编写；FASTBuild 被 Unreal Engine 社区采用。
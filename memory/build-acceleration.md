# build-acceleration — Research Memory

最后更新: 2026-09-05

## 关键记忆点提取

### 涉及的公司/产品/项目
- **Microsoft**: Visual Studio 2026 GA（Copilot build performance、C++23 一致性、AddressSanitizer ARM64）
- **Google**: Pigweed（SEED 0111 转向 Bazel）、Bazel
- **Meta**: Buck2（Rust 核心 + Starlark 规则，Conan 集成 PR 未合并）
- **IncrediBuild**: CI/CD 工具评测、C++ 构建系统指南
- **FASTBuild**: Unity/Blob 构建 + 分布式编译持续更新
- **sccache / ccache / mold / distcc**: 经典与新一代缓存/链接/分布式编译工具
- **Databend**: sccache CI 实践验证

### 重要趋势信号
- **共享缓存成为 CI/CD 标准组件**（方向 up，强度 high）：缓存层是构建时间优化第一杠杆，可带来 10-20 倍提升，主流 CI 工具缓存机制仍粗糙
- **AI 生成代码驱动 CI 加速需求**（方向 up，强度 high）：VS 2026 首次产品化 Copilot build performance，AI 提交量激增使冗余计算成为成本危机
- **CI 中增量编译失效，共享缓存价值凸显**（方向 up，强度 high）：CI 每次从干净状态构建，sccache 在 CI 中 ROI 远高于本地优化
- **Pigweed 转向 Bazel**（方向 up，强度 high）：嵌入式领域标志性事件，CMake 降级、GN 维护模式，可能带动嵌入式项目重估构建系统
- **经典分布式编译工具仍广泛应用**（方向 stable，强度 medium）：distcc+ccache 在中小团队（10-50人）仍解决 80% 问题，工具分层共存而非简单替代
- **Buck2 Conan 集成僵局**（方向 stable，强度 medium）：外部依赖管理是替代 Bazel 的核心瓶颈
- **sccache 与 mold 兼容性缺陷**（方向 stable，强度 medium）：需配置 sloppiness，两个编译缓存不能组合使用
- **VS 2026 无分布式编译布局**（方向 stable，强度 low）：聚焦 Copilot 和 Build Insights，与专用工具差异化竞争

### 值得长期跟踪的技术方向
- **AI 辅助构建优化**：VS 2026 Copilot build performance 为首个产品化案例，关注实际效果与采纳度
- **Bazel 嵌入式迁移潮**：Pigweed 之后是否有其他嵌入式项目跟进（工具链规则成熟度是关键变量）
- **C++20 模块对构建模型的影响**：对编译缓存和分布式编译的语义影响尚待探索
- **共享缓存后端架构**：Redis/S3/GCS 等后端的 CI 投入 ROI 高于本地优化
- **工具选型分层化**：团队规模与基础设施投入的匹配度是核心选型驱动因素

### 竞品动态
- **Microsoft**: VS 2026 GA 发布，无分布式编译集成，选择 AI 嵌入构建分析路径
- **Google**: Pigweed SEED 0111 正式批准 Bazel 为主要构建系统
- **Meta**: Buck2 核心与语言规则分离架构，Conan 集成仍无实质进展
- **IncrediBuild**: 发布 2026 十大 CI/CD 工具评测，指出主流工具缓存粗糙
- **FASTBuild**: 持续更新，Unity/Blob 构建 + 分布式编译仍具竞争力
# build-acceleration — Research Memory

最后更新: 2026-06-28

### 🧠 关键记忆点提取

#### 🏢 公司/产品/项目
- **Incredibuild**: 推出 AI Sandbox、ISLO 执行层，定位转向“AI 开发基础设施”。
- **Microsoft Visual Studio 2026**: 集成 Copilot 构建分析功能。
- **腾讯 yadcc**: 开源分布式编译系统，支持数百核并行。
- **Meta Buck2**: 开源，核心用 Rust 编写，支持增量依赖图。
- **sccache (Mozilla)**: 与 `mold` 链接器存在兼容性问题（Issue #1755）。
- **ccache**: 持续活跃更新（v4.13.6），可能受益于 sccache 用户迁移。
- **mold**: 高速链接器，与 sccache 不兼容。
- **Bazel**: 现代构建系统，迁移壁垒高。
- **CMake**: 主流构建系统，短期内难以被替代。
- **distcc**: Red Hat 仍推荐的经典分布式编译方案。

#### 📈 重要趋势信号
- **AI 与编译加速深度融合** (high): Incredibuild 和微软将 AI 作为核心差异化手段，从“加速”转向“智能分析与优化”。
- **CI/CD “10分钟规则”成为行业标准** (high): 2026年指南明确建议管道总时长控制在5-10分钟，倒逼加速技术普及。
- **开源分布式编译生态多元化** (medium): 腾讯 yadcc、Meta Buck2 等高质量项目降低企业采用门槛和成本。
- **编译缓存工具格局生变** (high): sccache 与 mold 兼容性问题可能导致用户大规模迁移至 ccache 或商业方案。
- **现代构建系统迁移壁垒巨大** (stable): Bazel/Buck2 学习曲线陡峭，与 CMake 生态兼容性差，短期内难以撼动 CMake 主流地位。

#### 🔭 值得长期跟踪的技术方向/话题
- **AI 辅助构建分析工具的实际影响**: Copilot、AI Sandbox 等能否真正提升效率。
- **Buck2 社区采用率及与 Bazel 的竞争态势**: 决定现代构建系统走向“双雄并立”还是“一家独大”。
- **sccache 用户迁移规模**: 判断编译缓存工具格局是否重塑的关键指标。
- **CMake 生态的演进**: 面对 Bazel/Buck2 挑战，CMake 如何保持主流地位。

#### ⚔️ 竞品动态
- **新产品/功能**: Incredibuild AI Sandbox、微软 VS 2026 Copilot 构建分析。
- **开源项目**: 腾讯 yadcc、Meta Buck2。
- **技术突破**: Buck2 核心用 Rust 编写，支持增量依赖图；yadcc 支持数百核并行编译。
- **兼容性问题**: sccache 与 mold 链接器不兼容，可能引发用户迁移。
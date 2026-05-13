# build-acceleration — Research Memory

最后更新: 2026-05-13

### 关键记忆点（供下次调研参考）

#### 公司/产品/项目
- **Microsoft**: Visual Studio 2026 (AI 集成, C++23 支持), MSVC 工具集
- **Mozilla**: sccache (云存储编译缓存)
- **Incredibuild**: 虚拟化分布式编译 (客户: Adobe)
- **Google**: Bazel (分布式缓存/远程构建), Buck2 (Rust 重写)
- **美团**: 分布式编译 + 预编译头文件 + CCache 实战经验
- **其他**: ccache (v4.13.5), Build2, Meson

#### 重要趋势信号
- **AI 深度融合**: VS 2026 集成 Copilot；Gartner 预测 2026 年 75% DevOps 团队用 AI 预测构建失败。
- **缓存标准化**: ccache/sccache 成为 CI/CD 标配，sccache 向云端演进 (支持 GitHub Actions, 多语言)。
- **分布式编译普及**: Incredibuild (大型项目) 与 Bazel (新一代构建系统) 并行发展。
- **构建系统多样化**: Bazel/Buck2 追求语言无关性 (Rust 重写)；CMake 仍为主流但新系统受关注。
- **云成本驱动优化**: 缓存 + 分布式编译可将构建时间从 45 分钟降至 8 分钟，直接降低云资源成本。

#### 值得长期跟踪的话题
1.  **AI 在 CI/CD 中的落地**: 预测构建失败、智能缓存策略、自动优化编译参数。
2.  **sccache 生态演进**: 云存储支持 (S3/GCS)、多语言扩展 (Rust/C++)、与 GitHub Actions 集成深度。
3.  **Bazel vs Incredibuild**: 新一代构建系统 vs 传统分布式编译方案，在大型 C++ 项目中的性能与易用性对比。
4.  **C++ 模块化对构建系统的影响**: C++23/26 模块支持如何改变缓存和分布式编译策略。
5.  **云成本优化实践**: 具体案例 (如美团) 的缓存命中率、分布式节点调度策略。

#### 竞品动态
- **Incredibuild**: 持续输出高质量指南 (构建加速、系统选择)，强调虚拟化分布式处理。
- **Bazel**: 下一代版本 (Buck2) 用 Rust 重写，强调语言无关性，挑战传统构建系统。
- **Microsoft**: 通过 VS 2026 深度集成 AI 和 C++ 标准，强化 MSVC 工具链性能与安全。
- **Mozilla**: 维护 sccache 开源项目，推动云存储缓存标准，影响力显著 (Hacker News 讨论)。
# build-acceleration — Research Memory

最后更新: 2026-08-25

## 关键记忆点

- **sccache**：编译缓存事实标准，Google Android 官方采用，多语言+云存储（S3/GCS/Azure）构筑壁垒，crates.io/GitHub 双平台活跃
- **GitHub Copilot Build Performance**：微软 VS 2026 内嵌 AI 构建优化代理，自动追踪/定位瓶颈/优化建议，标志 AI 构建优化产品化爆发
- **CMake + 远程执行（RE）服务**：低迁移成本分布式构建路径，正替代 Bazel；Bazel 因迁移成本高、集成复杂热度持续下降
- **IncrediBuild**：ROI 量化叙事（45min→8min），构建加速升级为管理 KPI；中国代理龙智（DragonSoft）主攻游戏/金融行业
- **FASTBuild**：Unity/Blob 构建 + 分布式编译 + 缓存组合，游戏行业标配实践，可能向金融/自动驾驶溢出
- **BuildXL**：微软大规模分布式构建方案，基于运行时文件访问观察的缓存算法
- **ccache**：持续更新（4.13.6），但功能覆盖被 sccache 全面超越
- **C++20 模块**：长期跟踪信号，可根本改变编译模型但工具链尚不可及
- **腾讯 yadcc**：开源热度消退，本期零提及，竞争力下降
- **Buck2**：分布式优先构建系统，社区讨论中与 CMake 通用性对比，Bazel 早期集成困难佐证
- **Databend 案例**：Rust 社区对增量编译在 CI 中效果存疑，sccache 在 CI 中优势明显
# build-acceleration — Research Memory

最后更新: 2026-09-08

- **IncrediBuild XGE**：共享缓存+分布式处理，专利缓存能力，可观测性套件，中国代理龙智定位DevSecOps加速
- **Pigweed SEED 0111**：正式批准Bazel为主要构建系统，GN/CMake降级维护，嵌入式领域标志性事件
- **Bazel vs Buck2**：Bazel语言支持更广、生态成熟；Buck2 Conan集成PR未合并，C++依赖管理是短板
- **共享缓存成为CI/CD标准组件**：多份2026指南强调智能缓存与命中率，独立缓存层市场成形，强度high
- **AI生成代码驱动CI加速需求**：提交量激增推高构建成本，AI既是问题制造者也是方案载体，强度high
- **C++模块系统对编译缓存语义挑战**：sccache/ccache未适配模块缓存，存在工具空白，强度medium
- **经典工具分层共存**：ccache/distcc、sccache、FASTBuild/IncrediBuild按规模分层，强度medium
- **分布式编译适用边界**：单机编译需数小时才值得采用，中小项目（10-50人）暂不需要，强度low
- **sccache**：Rust实现，支持S3/GCS/Redis云存储后端，跨语言（Rust/C/C++），CSDN称CMake集成可加速90%
- **Build2**：已支持C++ Modules，是模块缓存适配的先行者
- **AskanTech案例**：缓存+并行优化将构建时间从45分钟降至8分钟（降幅82%）
- **Microsoft C++**：VS 2026强调Copilot Chat AI集成和Linux支持，未见分布式编译布局
- **Buck2 Conan集成僵局**：已并入Bazel vs Buck2竞争信号，独立跟踪价值下降
- **早期跟踪信号**：模块缓存语义空白、Buck2依赖管理突破、分布式编译市场分层标准
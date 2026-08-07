# build-acceleration — Research Memory

最后更新: 2026-08-07

## 关键记忆点

- **sccache**：从 Rust 生态工具跃迁为 C++ 编译缓存主流选择，云存储 + 多语言（C/C++/Rust/CUDA）支持，Mozilla/Databend 验证编译时间降 95%，OpenDAL 存储抽象层集成增强后端灵活性 | 趋势：up | 强度：high
- **IncrediBuild**：从分布式编译工具升级为“构建效能全栈平台”，产品线扩展至 CI 运行器加速、缓存、可观测性，VS 2026 引擎级集成，可能引发与 APM 厂商（Grafana/Dynatrace）交叉竞争 | 趋势：up | 强度：medium
- **缓存命中率成为 CI/CD 工程效能核心 KPI**：从“技术指标”上升为“管理指标”，预计 2027 年进入工程效能 dashboard 标准指标集 | 趋势：up | 强度：high
- **distcc**：仍为分布式编译“入门首选”，免费易用，10 台机器 112 核 30 分钟→8 分半（3.5 倍加速），但需与 ccache/sccache 配合，“分布式编译 + 本地缓存”为社区标准实践 | 趋势：stable | 强度：medium
- **远程执行服务（RE）成为“第三条道路”**：NativeLink 等提供不迁移构建系统的加速路径，降低 Bazel 迁移紧迫性，可能形成“CMake + RE 服务”新主流组合，2026-2027 年增长最快细分赛道 | 趋势：up | 强度：medium
- **Bazel 迁移讨论降温**：6 个月实测推荐 CMake 首选，Bazel“强大但复杂”，迁移热度减弱 | 趋势：down | 强度：low
- **FASTBuild**：分布式编译工具，预告缓存功能，关注度稳定但非主流 | 趋势：stable | 强度：low
- **ccache 信号消退**：进入稳定维护期，关注度被 sccache 崛起转移，MSVC 缓存支持提升未产生新讨论 | 趋势：down | 强度：low
- **yadcc 调度效率/网络传输优化关注度下降**：腾讯 1700 核心集群标杆已确立，竞争焦点转向缓存集成与工具链整合 | 趋势：down | 强度：low
- **值得长期跟踪**：sccache × OpenDAL 集成深度（可能成为跨语言缓存标准范式）、IncrediBuild 可观测性扩展（构建效能监控新竞争）、NativeLink 等 RE 服务采用情况
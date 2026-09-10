# build-acceleration — Research Memory

最后更新: 2026-09-10

# 编译加速与分布式编译产业调研 · 关键记忆点（2026年9月）

## 涉及的公司/产品/项目

- **ccache**：编译器缓存工具，GPLv3 开源，2026-05-04 发布 4.13.6
- **sccache**：Mozilla 主导，跨语言（Rust/C/C++），2026-07-29 发布 0.17.0，累计 48 版本
- **distcc**：中小规模分布式编译，配合 Docker 容器化集群
- **FASTBuild**：中大规模，Unity/Blob 构建 + 网络分发缓存
- **IncrediBuild**：企业级，龙智中国区代理，覆盖 20 万+ 开发者
- **CMake / Bazel / Meson / Buck2 / GN**：构建系统竞争格局
- **Pigweed**：SEED 0111 批准 Bazel 为主要构建系统
- **Blender**：C++20 模块与 PCH 缓存语义讨论来源
- **Red Hat / Microsoft / Mozilla / GitHub Projects / Tweag / Kea Sigma Delta / Gentoo**

## 重要趋势信号

- **up｜CI/CD 智能缓存成为标准配置**：缓存命中可将构建从 10 分钟降至 30 秒（20 倍），AskanTech 案例 45→8 分钟（降幅 82%）｜强度 **high**
- **up｜sccache 云存储后端默认化**：0.17.0 默认支持所有存储后端（S3/GCS/Redis），缓存从本地磁盘转向云端共享｜强度 **medium**
- **up｜distcc + Docker 降低分布式编译部署门槛**：从"数天运维"降至"拉取镜像"，3 倍加速，跨 Linux/MacOS/Windows｜强度 **medium**
- **up｜Microsoft 构建性能提升 15–20%**：走"工具链优化"而非"分布式编译"路线，9:19→7:30｜强度 **medium**
- **stable｜ccache 与 sccache 双轨并行**：ccache 守成（经典稳定），sccache 进取（云原生快速迭代）｜强度 **medium**
- **stable｜分布式编译规模分层格局稳固**：中小（distcc）/中大型（FASTBuild）/企业级（IncrediBuild）｜强度 **medium**
- **stable｜CMake 保持"最大公约数"地位**：Pigweed 中 GN 转维护模式，CMake 无限期支持｜强度 **medium**
- **down｜C++20 模块缓存语义空白持续**：sccache/ccache 均未适配，PCH 在 Unity 构建下有效性降低｜强度 **medium**

## 值得长期跟踪的技术方向

- **C++20 模块缓存语义适配**：当前最大技术债务，Build2 为已知先行者，主流工具未跟进；谁先解决谁掌握下一代制高点
- **云原生缓存工具迭代节奏**：sccache 48 版本快速迭代，最可能率先适配模块缓存
- **分布式编译部署门槛下降后的中小团队采用案例**：观察是否出现更多中小项目重新评估
- **Microsoft 构建加速策略走向**：工具链优化 vs 分布式编译的路线差异
- **构建系统依赖管理短板**：Buck2 的 Conan 集成 PR 未合并，C++ 依赖管理仍是僵局
- **缓存命中率作为工程效能核心 KPI** 的行业落地

## 竞品动态

- **sccache**：0.17.0 发布，新 Rust 2024，默认全存储后端，被 GitHub Projects 推荐"可将构建时间减半"
- **ccache**：4.13.6 发布（4 月连续 4.13.4/4.13.5），稳定维护
- **FASTBuild**：Unity/Blob 构建兼容网络分发与缓存，10 倍以上提升，自动单独编译可写文件
- **distcc + Docker**：Red Hat 展示容器化集群，3 倍加速，跨平台
- **IncrediBuild**：龙智中国区代理，DevSecOps 加速定位
- **Pigweed**：Bazel 升为主要构建系统，GN 转维护模式（最早 2026 可能移除）
- **Buck2**：Conan 集成 PR 获好评但未合并，依赖管理僵局
- **Microsoft**：Pure Virtual C++ 2026 展示 15–20% 提升，未见分布式编译新布局

## 已消退信号（并入母趋势）

- AI 生成代码驱动 CI 加速需求（high → 并入智能缓存标准配置）
- Pigweed 转向 Bazel（medium → 并入构建系统竞争格局）
- Bazel 与 Buck2 竞争加剧（medium → 并入构建系统竞争趋势）

## 整体判断

- 整体热度**持平**，热点从"事件驱动"转向"结构驱动"
- 双主线持续升温：CI/CD 智能缓存 + 编译器缓存工具双轨并行
- 本期无减弱信号
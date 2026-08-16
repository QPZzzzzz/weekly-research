# build-acceleration — Research Memory

最后更新: 2026-08-16

### 关键记忆点

- **公司/产品/项目**：微软 VS 2026、GitHub Copilot AI 构建优化、IncrediBuild（Islo AI 沙箱）、NativeLink、sccache、ccache、腾讯 yadcc、FASTBuild、distcc、Buck2、Pigweed、mold、美团 C++ 编译优化实践

- **趋势信号**：
  - AI 驱动构建优化产品化加速（up, high）：微软 VS 2026 集成 Copilot AI 构建优化，IncrediBuild 推出 Islo AI 沙箱，两条路线成型（IDE 内置 vs 独立工具链）
  - CI/CD 构建加速成为管理 KPI（up, high）：IncrediBuild 面向管理层输出"构建速度=业务竞争力"叙事，采购决策链扩展至高管
  - RE 服务 + CMake 降低接入门槛（up, high）：NativeLink + CMake 组合挑战"分布式编译必须绑定 Bazel"认知，sccache 与 CMake 集成教程爆发
  - sccache 成为主流编译缓存（stable, medium）：Google Android 官方采用，地位确立但增长动力减弱，ccache 进入维护期
  - Bazel 热度下降，CMake 保持主流（stable, medium）：Pigweed 将 Bazel 设为主要构建系统但 CMake 继续支持，讨论从"下一代"转向质疑
  - 分布式编译工具多样化（new, medium）：腾讯 yadcc 开源，国内大厂工具外输信号增强，市场竞争加剧

- **长期跟踪方向**：
  - AI 构建优化两条路线竞争结果（12 个月内明朗）
  - RE 服务 + CMake 组合的生态发展和企业采用案例
  - sccache 与 mold 兼容性修复进展（完善"编译缓存 + 高速链接"链路）
  - 腾讯 yadcc 开源后的社区运营、GitHub Star 增长和集成度
  - 国内大厂（腾讯云、华为云）对"构建速度=业务竞争力"叙事的应对策略

- **竞品动态**：
  - 微软：VS 2026 GA，集成 Copilot AI 构建优化，接近完整支持 C++23，扩展 ARM64 ASan 支持
  - IncrediBuild：推出 Islo AI 沙箱和免费 8 倍加速 CI runners，产品定位从"编译加速工具"转向"构建效能全栈平台"，密集内容营销（3+ 报告、多篇博客）
  - 腾讯：开源 yadcc，明确"分布式编译主要提高吞吐而非降低单文件编译耗时"的技术定位
  - Google：Android 官方采用 sccache；Pigweed 将 Bazel 设为主要构建系统，GN 进入维护模式
  - 美团：分享 C++ 编译优化实践（分布式编译、PCH、ccache），结论"分布式编译适合大规模项目，小项目收益有限"
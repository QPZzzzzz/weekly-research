# build-acceleration — Research Memory

最后更新: 2026-08-08

### 关键记忆点（供下次调研参考）

- **公司/产品/项目**: sccache、IncrediBuild、Visual Studio 2026、Tencent/yadcc、ccache、FASTBuild、Bazel、CMake、NativeLink（RE服务）、mold、distcc、OpenDAL
- **趋势信号**: sccache 成为跨语言编译缓存主流（up, high）｜IncrediBuild 转型构建效能全栈平台（up, medium）｜VS 2026 集成构建加速+ Copilot（up, medium）｜CI/CD 优化成管理议题（up, high）｜yadcc 热度下降（down, low）｜Bazel 降温、CMake 主流（down, low）｜ccache 稳定维护期（down, low）｜分布式编译+本地缓存组合成标准实践（up, high）｜RE 服务为新路径（new, medium）
- **长期跟踪**: sccache × OpenDAL 集成深度；RE 服务（NativeLink）与 CMake 组合；VS 2026 对第三方工具链的替代效应；IncrediBuild 与 APM 厂商竞争；缓存命中率作为工程效能 KPI
- **竞品动态**: IncrediBuild 发布 C++ 构建系统指南（内容营销）；微软强化 CMake 集成（CMake 4.1.1）；腾讯 yadcc 开源（LLVM 15 倍加速）；sccache 与 mold 兼容性问题（Issue #1755）
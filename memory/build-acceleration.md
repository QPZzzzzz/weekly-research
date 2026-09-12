# build-acceleration — Research Memory

最后更新: 2026-09-12

# 编译加速 · 分布式编译 · C++ Build Cache 调研记忆点

## 涉及公司/产品/项目
- Microsoft：Visual Studio 2026、MSVC Build Tools v14.50、GitHub Copilot C++ 私密预览
- sccache（Rust 编译器缓存，云存储后端 S3/Redis/Memcached）
- ccache（经典本地缓存，守成方）
- Incredibuild（分布式编译，龙智为中国授权合作伙伴）
- 字节跳动（libstdc++ → libc++ 迁移，基于 LLVM20）
- Pigweed（SEED 0111：Bazel 升为主构建系统，GN 转维护）
- Buck2（Conan 集成 PR 未合并）
- Bazel / CMake / Meson / FASTBuild / distcc
- GitHub Projects（官方推荐 sccache）

## 重要趋势信号
- **up / high**：MSVC 率先修复 C++20 模块跨模块边界问题（ADL、默认函数实例化、头文件单元宏空白保留、全局模块片段类型、ARM64 代码生成）——模块缓存适配第一块多米诺骨牌
- **up / high**：VS2026 正式发布，配合 Ninja 构建时间降至 28 秒；工具链优化路线完成产品化落地
- **up / high**：sccache 获 GitHub Projects 官方推荐，CMake 集成宣称零配置加速 90%；编译器缓存从"自选工具"升级为"平台推荐标准配置"
- **up / high**：CI/CD 智能缓存成标准配置，缓存命中率晋升工程效能核心 KPI；全管道 10 分钟基准
- **new / medium**：字节跳动完成 libstdc++ → libc++ 大规模迁移，中国大型互联网公司首次公开标准库级迁移实践
- **stable**：Buck2 Conan 集成僵局持续，期望支持 vcpkg
- **stable**：Pigweed 批准 Bazel 为主构建系统，GN 转维护
- **stable**：CMake 仍为构建系统最大公约数

## 长期跟踪方向
- C++20 模块缓存语义：sccache/ccache 是否跟进适配（编译器+缓存工具+构建系统三方协同）
- 工具链原生优化 vs 分布式编译的决策边界（28 秒构建侵蚀分布式编译边际收益）
- 字节跳动 libstdc++ → libc++ 迁移方法论是否外溢为行业范式
- sccache 云存储后端采用率与"零配置加速 90%"实际落地验证
- Buck2 依赖管理器集成僵局是否被 vcpkg 等需求打破
- VS2026 + Copilot C++ 集成是否推动工具链优化路线替代分布式编译

## 竞品动态
- **Microsoft**：VS2026 正式发布 + MSVC Build Tools v14.50（含 C++/CLI 修复）+ Copilot C++ 私密预览；走工具链深度协同路线，非多机分发
- **sccache**：GitHub 官方背书，云存储后端默认化，迭代速度快，云原生场景拉开与 ccache 差距
- **ccache**：经典稳定守成，本地缓存模式，本期无新版本发布
- **Incredibuild**：持续定位企业级 DevSecOps 加速，覆盖 20 万+ 开发者，中国由龙智代理
- **Pigweed**：Bazel 升主构建系统，GN 最早 2026 可能移除
- **Buck2**：Conan 集成 PR 获好评但未合并，依赖管理僵局持续

## 已消退信号
- distcc + Docker 容器化集群方案（medium → 回落，并入分层母趋势）
- 分布式编译适用边界讨论（已稳定共识）
- ccache 4.13.6 版本发布（并入双轨并行母趋势）
- C++20 模块在分布式/缓存场景不可及（medium → low，被 MSVC 修复动作部分抵消）
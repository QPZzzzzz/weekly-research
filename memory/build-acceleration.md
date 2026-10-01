# build-acceleration — Research Memory

最后更新: 2026-10-01

# 编译加速与分布式编译调研 — 关键记忆点

## 涉及公司/产品/项目
- **sccache**（Mozilla，Rust 编译缓存，云对象存储支持）
- **mold**（链接器，与 sccache 组合出现兼容性问题）
- **ccache**（C/C++ 编译器缓存，4.14.1 于 2026-09-27 发布）
- **Incredibuild**（定位升级为 CI/CD 平台无关叠加层）
- **Visual Studio 2026 / MSVC**（正式 GA，C++23 接近完整一致性）
- **Pigweed**（SEED 0111：Bazel 升为主构建系统）
- **Buck2**（Meta 开源构建系统，C/C++ 依赖导入标准化缺失）
- **Bazel**（嵌入式领域构建系统集中趋势）
- **CMake / Meson / GN**（选型共识：CMake 推荐学习，Meson 最有前景）
- **腾讯 yadcc**（分布式编译系统，只提吞吐不降单文件耗时）
- **rules_foreign_cc**（Bazel C/C++ 依赖导入改善工具）

## 重要趋势信号
- **技术 | sccache+mold 兼容性裂缝** | 缓存层与链接层层间接口问题首次具象化，挑战"可干净组合"结论 | **high**
- **竞品 | Incredibuild 定位升级** | 从分布式编译工具升级为 CI/CD 平台无关的共享缓存+分布式处理叠加层 | **high**
- **产品 | VS 2026 GA** | MSVC 性能提升、C++23 一致性推进、Copilot C++ Private Preview | **high**
- **行业 | CI/CD 缓存叙事转向** | 从"是否使用"转向"如何正确失效"，缓存失效配置成核心工程实践 | **high**
- **产品 | VS 2026 安装器版本限制** | 最低仅允许 msvc 19.44，企业多版本工具链需求受阻 | **medium**
- **产品 | ccache/sccache 双缓存并行** | ccache 深耕 C/C++，sccache 覆盖 Rust+云存储，格局稳固 | **medium**
- **技术 | Bazel/Buck2 C/C++ 依赖导入标准化缺失** | rules_foreign_cc 改善但未根本解决 | **medium**
- **技术 | Pigweed Bazel 升主构建系统** | GN 转维护模式（不早于 2026 可能移除），CMake 无限期支持 | **medium**

## 值得长期跟踪的技术方向/话题
- 构建加速三层架构（缓存层+分布式层+链接层）**层间接口标准化**需求，是否催生类似 `.editorconfig` 的规范
- sccache+mold 兼容性问题是否扩散为工具链标准化讨论
- CI/CD 缓存失效配置从工程实践向**标准化规范**演进
- VS 2026 安装器 C++ 构建工具最低版本限制是否放宽
- ccache 与 sccache 是否出现功能收敛或差异化定位调整
- Bazel/Buck2 替代 autotools+Make/CMake 的迁移成本争议（可复现构建+分布式能力附加价值）
- 中文社区分布式编译从概念科普向实际试用推进节奏

## 竞品动态
- **Incredibuild**：战略转向"CI/CD 平台无关叠加层"，无需重写管道，可能引发其他厂商跟进
- **Visual Studio 2026**：正式 GA，MSVC 运行时性能改进、AddressSanitizer ARM64、Copilot C++ Private Preview
- **ccache**：4.14.1（2026-09-27）/4.14（2026-08-23）/4.13.6（2026-05-04）连续发布，迭代稳定
- **sccache**：Rust 社区持续采用，webrender 构建降至 17.3 秒案例被广泛引用
- **腾讯 yadcc**：开源分布式编译系统，定位"只提吞吐不降单文件耗时"，与缓存层互补
- **Pigweed**：Bazel 升为主构建系统，GN 转维护模式

## 已消退信号（上期对比）
- sccache+mold 组合从个人实践进入项目模板化配置（本期无新增扩散证据，兼容性问题或抑制推广）
- 分布式编译在百万行级 C++ 项目中作为门禁构建排队问题解法被实际试用（本期无新增证据）
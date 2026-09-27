# build-acceleration — Research Memory

最后更新: 2026-09-27

# 关键记忆点

## 涉及公司/产品/项目
- 腾讯 yadcc（分布式编译，已开源）
- 美团 DQU（编译优化实践）
- Incredibuild（企业级构建加速）
- 微软 MSVC Build Tools 2026 预览
- Mozilla sccache
- Google Pigweed（SEED 0111）
- Meta Buck2
- FASTBuild
- 龙智 DragonSoft
- d-o-hub/do-harness（GitHub Issue #141）
- mold（链接器）
- ccache

## 重要趋势信号

- **方向 stable | 强度 high** — sccache 与 mold 被明确界定为互补关系：缓存层管编译、链接层管链接，可干净组合
- **方向 new | 强度 medium** — sccache+mold 从个人实践进入项目模板化配置，贡献者 onboarding 构建成本被显式记录
- **方向 stable | 强度 high** — 分布式编译与缓存层分工叙事在中文社区持续强化：分布式提吞吐、缓存降单文件耗时
- **方向 stable | 强度 high** — 分布式编译在中文社区从概念科普进入百万行级项目实际试用阶段
- **方向 stable | 强度 medium** — Incredibuild 强化企业级低维护/低占用/工作负载无关定位，扩展 AOSP 与云实例场景
- **方向 stable | 强度 medium** — CI/CD 缓存叙事持续破圈："10分钟→30秒"与"45分钟→8分钟"成为标准价值主张
- **方向 stable | 强度 high** — C++ 构建系统选型共识固化：CMake 必学、Meson 最有前景、Bazel 可能很棒
- **方向 stable | 强度 medium** — Bazel/Buck2 仍面临 C/C++ 依赖导入标准化缺失的质疑
- **方向 stable | 强度 medium** — MSVC Build Tools 2026 年 9 月预览持续迭代 C++ Modules 与 ARM64 代码生成

## 值得长期跟踪的技术方向/话题
- 构建加速"三层分工"架构（缓存层 + 分布式层 + 链接层）的层间接口标准化
- sccache + mold 组合模板化配置是否扩散，是否引发工具链标准化讨论（类似 .editorconfig 地位）
- 分布式编译在中文社区从百万行项目向更多企业级场景扩散的节奏
- build cache 正确失效问题（从"是否使用"转向"如何正确失效"）
- C/C++ 依赖导入标准化缺失对 Bazel/Buck2 通用替代能力的制约
- 贡献者体验（Contributor Experience）中构建效率的标准化地位

## 竞品动态
- **腾讯 yadcc**：开源分布式编译系统，明确"只提吞吐不降单文件耗时"，与缓存互补
- **美团 DQU**：分布式编译 + PCH + CCache 并列优化，指出 Shared Library 无法共享 PCH
- **Incredibuild**：企业级低维护定位，AOSP 构建分发到工作站 + CI + 云实例
- **微软**：MSVC Build Tools 2026 年 9 月预览，C++ Modules 修复 + ARM64 代码生成改进
- **Pigweed**：SEED 0111 将 Bazel 升为主构建系统，GN 转维护模式，CMake 无限期支持
- **Meta Buck2**：核心 Rust 编写，语言规则 Starlark，核心与规则分离
- **d-o-hub/do-harness**：Issue #141 记录 sccache + mold 联合配置模板化

## 已消退信号（下期需关注是否回归）
- VS 2026 安装器限制 C++ 构建工具最低版本（上期 high）
- VS 2026 正式发布（上期 medium）
- Copilot @BuildPerfCpp 支持迭代构建优化（上期 high）
- Pigweed SEED 0111 Bazel 升主构建系统（上期 high）
- MSVC Build Tools 2026 年 9 月预览更新（上期 medium）
- 自托管分布式编译方案持续被讨论（上期 medium）
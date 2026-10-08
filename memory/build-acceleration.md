# build-acceleration — Research Memory

最后更新: 2026-10-08

# 编译加速与分布式编译产业调研 — 关键记忆点

## 涉及公司/产品/项目

- **Microsoft / VS 2026**：v18.10 将 C++ 编译速度列为三大核心改进之一，持续修复模块回归、AVX-512 代码生成
- **Incredibuild**：CI/CD 工具榜单 + Islo AI 沙箱 + 免费 8× CI runner；中国区合作伙伴为龙智 DragonSoft
- **字节跳动**：秦泽天（LLVM 贡献者）分享数千万核 libc++ 迁移（基于 LLVM20）
- **ccache**：4.14.1（2026-09-27），事实标准，零配置单机默认选择
- **sccache**：S3 兼容远程后端 + Rust 支持，与 ccache 形成互补
- **Bazel / Buck2**：Pigweed SEED 0111 批准 Bazel 为主构建系统；Buck2 与 Bazel C/C++ 依赖集成缺乏标准方式
- **腾讯 Yadcc**：2021年6月开源，无新进展
- **distcc / mold / Icecream / FASTBuild**：distcc 仅维护，mold 与 sccache/ccache 可组合

## 重要趋势信号

- **方向 up | high**：编译器厂商将构建速度上移至原生层，系统性压缩第三方缓存工具生存空间
- **方向 up | high**：Incredibuild 从加速工具向 CI/CD 全流程平台跃迁（叠加层 + AI 沙箱 + runner 资源层）
- **方向 up | high**：字节跳动数千万核 libc++ 迁移，中国大厂编译基础设施从"使用者"升级为"定义者"
- **方向 up | medium**：sccache vs ccache 讨论从单点性能升级为架构选型，远程缓存后端成竞争焦点
- **方向 new | medium**：AI 辅助 CI/CD 优化从厂商叙事扩展到学术研究，可能催生新工具品类
- **方向 down | medium**：构建系统向 Bazel 集中遇阻（无新增采用案例，C/C++ 依赖导入缺标准方式）
- **方向 down | low**：腾讯 Yadcc 信号显著减弱
- **方向 stable | low**：CI/CD 缓存叙事进入稳定期（10GB/repo、7天TTL、命中 10min→30s 成事实标准）

## 值得长期跟踪的技术方向

- 编译器原生增量编译与模块化能力成熟度（MSVC 模块回归修复节奏）
- 跨机器、跨平台、跨语言的统一缓存基础设施（第三方缓存工具新护城河）
- 大规模 C++ 运行时库整体迁移路径（libstdc++ → libc++）
- 远程缓存后端标准化（S3 兼容、Redis、自托管方案）
- AI 辅助构建加速从营销概念向工程实践过渡的拐点
- Bazel 导入 C/C++ 依赖的标准化方案
- 跨语言统一缓存层是否出现新竞争者

## 竞品动态

- **Incredibuild**：发布 2026 CI/CD 工具榜单；推广 Islo AI 沙箱；免费 8× CI runner 早期访问；叙事入口为"AI 提交量激增导致 CI 冗余计算"
- **Microsoft**：VS 2026 18.7–18.10 持续更新；AddressSanitizer 扩展至 ARM64
- **字节跳动**：libc++ 迁移演讲（2026 全球系统软件技术大会），近年最大规模 C++ 运行时库迁移案例
- **Pigweed**：SEED 0111 批准 Bazel 为主构建系统，GN 转维护模式
- **ccache**：4.14.1 后本期无新版本，事实标准地位稳固
- **sccache**：远程后端 + Rust 支持持续被讨论，与 ccache 互补
- **腾讯 Yadcc**：无新版本或新落地案例

## 早期信号（下次调研验证）

1. AI 辅助 CI/CD 是否引发更多工业界落地案例
2. Incredibuild Islo AI 沙箱和免费 runner 能否转化为实际采用
3. 字节跳动 libc++ 演讲后是否引发中文社区大规模落地分享
4. 跨语言统一缓存层是否出现新竞争者
5. Bazel C/C++ 依赖导入是否催生标准化方案
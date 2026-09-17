# build-acceleration — Research Memory

最后更新: 2026-09-17

# 编译加速与分布式编译调研 · 关键记忆点

## 涉及公司/产品/项目
- **ccache**：本地编译缓存工具，2026-04-19/04-26/05-04 连发 4.13.4/4.13.5/4.13.6
- **sccache**：Rust 系云原生编译缓存，与 mold 链接器存在兼容性问题（Issue #1755）
- **mold**：极速链接器，与 sccache 集成摩擦
- **yadcc**：国产开源分布式编译系统，日编译产出 300 万+ 目标文件
- **Incredibuild**：中国区由龙智（DragonSoft）授权代理，覆盖编译/测试/发布全流程
- **MSVC / Visual Studio 2026**：9 月预览更新优化编译时间；Copilot Chat 支持 `make my build faster`
- **Build2**：原生 C++ Modules 支持、跨平台、无外部依赖
- **Buck2**：Conan 集成 PR 未合并，社区期望 vcpkg 支持
- **Bazel**：快速可扩展但项目组织僵化
- **FASTBuild / distcc / icecc / octobuild**：分布式编译工具生态
- **CMake / Meson / xmake**：构建系统选型对比对象

## 重要趋势信号
- **方向 up｜CI/CD 10 分钟基准共识强化**｜45 分钟现实 vs 10 分钟基准，4.5 倍差距构成核心市场空间｜强度 **high**
- **方向 up｜AI 驱动构建优化双轮驱动**｜VS 2026 产品落地 + 学术论文预测分析，可能融合为端到端智能优化｜强度 **high**
- **方向 new｜ccache 密集迭代打破稳定期判断**｜三周三个版本，传统本地缓存工具活跃度回升｜强度 **medium**
- **方向 new｜sccache 与 mold 兼容性摩擦**｜云原生缓存工具面临新工具链适配挑战｜强度 **medium**
- **方向 new｜AI 优化 CI/CD 进入学术视野**｜预测分析 + 智能自动化减少构建失败｜强度 **medium**
- **方向 new｜yadcc 国产分布式编译亮相**｜参考主流方案设计，生产环境已有量级使用｜强度 **low**
- **方向 stable｜Buck2 依赖管理僵局**｜Conan PR 未合并，vcpkg 支持仍为期望｜强度 **low**
- **方向 stable｜Incredibuild 中国区渠道推广**｜龙智提供全流程加速服务｜强度 **low**

## 值得长期跟踪的技术方向
- sccache 与 mold 等新工具链兼容性问题是否扩散，影响平台化 adoption
- ccache 密集迭代是否意味着传统本地缓存工具在云原生叙事下重新定位
- AI 优化 CI/CD 的学术研究是否转化为可落地产品功能
- yadcc 等国产分布式编译方案是否形成规模化生态
- MSVC 原生优化与 Incredibuild 技术方案下期是否回归增量证据
- Build2 原生 C++ Modules 支持作为选型差异化优势的演进
- 分布式编译与缓存融合趋势（上期 low，本期进一步消退）

## 竞品动态
- **ccache**：三周连发三版，打破"稳定期"判断，巩固本地开发基本盘
- **sccache**：云原生叙事降温（high→medium），出现与 mold 集成摩擦
- **Incredibuild**：中国区龙智渠道稳定推广，无技术方案层面新进展
- **Buck2**：Conan 集成 PR 获好评但未合并，依赖管理集成僵局持续
- **yadcc**：国产新方案开源，参考 ccache/sccache/distcc/icecc 设计
- **MSVC/VS 2026**：Copilot Chat 实现基线捕获→优化→测量→回滚闭环
- **Build2**：C++ Modules 原生支持持续作为差异化卖点

## 已消退信号（下期需验证是否回归）
- MSVC 原生优化侵蚀分布式编译收益（was high，本期静默）
- Incredibuild 竞争焦点升级至共享缓存+分布式处理层（was high，本期无技术增量）
- 分布式编译与缓存融合趋势（was low，进一步消退）

## 整体热度
**持平**。CI/CD 10 分钟基准与 AI 构建优化双主线升温；MSVC 原生优化与 Incredibuild 技术叙事静默；sccache 云原生叙事小幅降温。
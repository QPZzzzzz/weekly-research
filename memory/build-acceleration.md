# build-acceleration — Research Memory

最后更新: 2026-10-10

# 编译加速与分布式编译产业调研 — 关键记忆点

## 涉及公司/产品/项目

- **字节跳动** — 数千万核 libc++ 迁移（基于 LLVM 20），秦泽天主讲
- **Microsoft** — VS 2026 GA、MSVC Build Tools、Copilot C++ Private Preview
- **Incredibuild** — 产品矩阵扩展至 CI/CD 全流程平台，含 Islo AI 沙箱
- **Mozilla** — sccache（Issue #1755 兼容性问题）
- **Pigweed** — SEED 0111 批准 Bazel 为主构建系统
- **Meta** — Buck2 构建系统
- **腾讯** — Yadcc（信号消退，无新进展）
- **CppDepend** — 2026 五款主流 C++ 编译器对比
- **Hermetiq** — Bazel vs Buck2 对比
- **Tweag** — Buck2 介绍
- **ccache** — 4.14.1（2026-09-27 发布）
- **mold** — 与 sccache 组合兼容性问题
- **Build2** — 轻量构建系统替代方案

## 重要趋势信号

- **up / high** — 字节跳动数千万核 libc++ 迁移细节落地，中国大厂从编译基础设施"使用者"升级为"定义者"
- **up / high** — Incredibuild 从编译加速工具向 CI/CD 全流程平台跃迁，产品矩阵大幅扩展
- **up / high** — VS 2026 正式 GA，C++ 构建工具与 IDE 解耦，编译器厂商"上移"策略进入执行阶段
- **new / medium** — AI 辅助 CI/CD 优化从厂商叙事扩展至学术研究，新工具品类萌芽
- **new / medium** — sccache 与 mold 组合兼容性问题暴露，工具链组合复杂性成为 build cache 新痛点
- **stable / medium** — Pigweed SEED 0111 批准 Bazel 为主构建系统，但 CMake 无限期支持
- **down / low** — 构建系统向 Bazel 集中趋势 momentum 从 rising 降为 stable
- **stable / medium** — ccache 4.14.1 持续更新，事实标准地位稳固
- **stable / medium** — CI/CD 缓存叙事进入稳定期（10 分钟→30 秒命中成为事实标准）
- **new / low** — Build2 作为轻量构建系统替代方案进入视野

## 值得长期跟踪的技术方向/话题

- sccache 与 mold 兼容性问题是否推动缓存策略改进或催生工具链组合标准
- VS 2026 构建工具与 IDE 解耦后，第三方缓存工具（ccache/sccache）生存空间是否被压缩
- Build2 在 C++ Modules 场景中是否获得实际采用案例
- 字节跳动 libc++ 迁移演讲后是否引发中文社区大规模落地分享
- Incredibuild 多产品线扩展能否转化为实际客户采用，Islo AI 沙箱落地进展
- AI 预测构建产物复用、优化缓存策略的工业界落地案例
- Bazel 导入 C/C++ 依赖标准化进展

## 竞品动态

- **Incredibuild** — 产品线扩展至构建缓存、可观测性、构建卫士、编码代理沙箱（Islo）、免费 8× CI runner；发布 2026 十大 CI/CD 工具榜单
- **Microsoft** — VS 2026 GA，C++ 构建工具可独立升级；Copilot C++ 进入 Private Preview；18.7–18.10 修复模块回归、AVX-512 代码生成，ASan 扩展 ARM64
- **字节跳动** — 数千万核 libc++ 迁移（LLVM 20），近年已知最大规模 C++ 运行时库迁移案例
- **Pigweed** — Bazel 升为主构建系统，GN 转维护模式
- **ccache** — 4.14.1 发布，事实标准地位稳固
- **Meta** — Buck2 持续推广，但 Bazel 导入 C/C++ 依赖仍缺标准方式
- **腾讯 Yadcc** — 信号消退，2021 年开源后无新版本或落地案例
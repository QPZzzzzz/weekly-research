# build-acceleration — Research Memory

最后更新: 2026-10-15

# 编译加速与分布式编译 — 关键记忆点

## 涉及公司/产品/项目

- **Microsoft**：Visual Studio 2026（18.7–18.10）、Copilot 构建优化、MSVC（接近完整 C++23 一致性）
- **字节跳动**：数据中心 libc++ 迁移（数千万核 C++ 服务，libstdc++ → LLVM 20 libc++）；秦泽天（2026 全球系统软件技术大会演讲）
- **腾讯**：Yadcc 分布式编译系统（开源，持续被引用）
- **Incredibuild**：2026 十大 CI/CD 工具榜单、Islo AI 沙箱、免费 8× CI runner、共享缓存与分布式处理层
- **Google / Pigweed**：SEED 0111 批准 Bazel 为主构建系统，GN 转维护模式，CMake 无限期支持
- **Meta**：Buck2 构建系统（Tweag 分析）
- **Tweag**：Buck2 分析，指出 Bazel 导入 C/C++ 依赖无标准方式
- **Hermetiq**：Bazel vs Buck2 vs Pants 对比
- **CppDepend**：2026 最佳 5 款 C++ 编译器对比（Clang/LLVM 领先）
- **工具**：sccache（Issue #1755）、mold、ccache（4.14.1）、CMake、Meson、Build2、MSBuild、clang-repl
- **CNCF**：项目毕业加速

## 重要趋势信号

- **AI 辅助构建优化进入 IDE 工具链** | 方向：up | VS 2026 Copilot 实现构建优化自动化闭环（捕获基线→建议→测量→回滚），学术论文同步验证 | 强度：**high**
- **Bazel 在嵌入式/系统软件领域持续扩张** | 方向：up | Pigweed 决策 + Hermetiq 对比，从单一项目升级为领域性趋势；但 C/C++ 依赖导入标准化缺位 | 强度：**high**
- **中国大厂编译基础设施实践进入国际视野** | 方向：up | 字节跳动 libc++ 迁移演讲 + 腾讯 Yadcc 持续引用 | 强度：**high**
- **sccache 与 mold 兼容性问题** | 方向：new | GitHub Issue #1755：mold 导致 sccache 无法缓存；"缓存+链接"黄金组合认知被打破 | 强度：**medium**
- **C++26 标准特性冻结** | 方向：new | 预计 2026 年内发布，AI 加速优势可能带动编译器与构建工具链适配 | 强度：**medium**
- **CI/CD 缓存叙事固化** | 方向：stable | "10 分钟→30 秒"事实标准，默认 10GB/仓库、7 天 TTL，减少 60–80% 构建时间；差异化空间收窄 | 强度：**medium**
- **Incredibuild 平台化叙事** | 方向：up | 工具榜单 + AI 沙箱 + 免费 CI runner，强度未进一步升级 | 强度：**high**
- **自托管构建缓存指南热度回落** | 方向：down | 本期无新实践内容，被更具体技术问题取代 | 强度：**low**

## 值得长期跟踪的技术方向/话题

- **AI 驱动的智能缓存策略**：下一阶段竞争焦点（智能缓存、跨平台缓存一致性、缓存与分布式编译深度集成）
- **sccache + mold 兼容性修复或替代方案**：未来 1–2 个季度关键观察点
- **Bazel C/C++ 依赖导入标准化进展**：结构性瓶颈，影响 Bazel 采纳成本
- **VS 2026 Copilot 构建优化是否引发其他 IDE 厂商跟进**
- **C++26 发布后编译器与构建工具链适配**
- **libc++ 替代 libstdc++ 对亚太 C++ 生态标准化方向的影响**
- **clang-repl 在 Jupyter 中的交互式 C/C++ 工作流与增量编译**（FOSDEM 2026）
- **构建加速工具链集成复杂度**：工具间兼容性验证应与单工具性能评估同等重要

## 竞品动态

- **Microsoft**：VS 2026 18.7–18.10 新增 Copilot 辅助构建优化（自动测量并回滚无效优化）；MSVC 接近完整 C++23 一致性；用户反馈希望提供更多构建工具版本
- **Incredibuild**：发布 2026 十大 CI/CD 工具榜单与 C++ 编译加速指南；推广 Islo AI 沙箱、免费 8× CI runner、共享缓存和分布式处理层
- **Google / Pigweed**：SEED 0111 批准 Bazel 为主构建系统，GN 转维护模式，CMake 获无限期支持
- **Meta / Buck2**：Tweag 分析指出 Buck2 覆盖 C/C++、Rust、Python 但语言支持较 Bazel 窄
- **ccache**：发布 4.14.1 版本，持续维护
- **sccache**：Issue #1755 报告 mold 兼容性问题（mozilla/sccache）
- **字节跳动**：数千万核 libc++ 迁移，全球罕见工程实践，工具链选型偏好可能影响亚太生态
- **腾讯**：Yadcc 分布式编译系统持续被行业文章引用
- **CppDepend**：Clang/LLVM 因诊断与工具生态领先
- **Kea Sigma Delta**：6 个月测试推荐 CMake，认为 Meson 最有前途
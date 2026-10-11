# build-acceleration — Research Memory

最后更新: 2026-10-11

# 编译加速与分布式编译调研记忆点

## 公司/产品/项目
- **字节跳动**：数千万核 C++ 服务从 libstdc++ 迁移至 libc++（基于 LLVM 20），工程师秦泽天将在 2026 全球系统软件技术大会分享
- **Incredibuild**：产品矩阵扩展至 Islo AI 沙箱、免费 8× CI runner、构建缓存、可观测性、构建卫士、CI runner
- **Microsoft / VS 2026**：正式 GA，C++ 构建工具与 IDE 解耦，Copilot C++ 进入 Private Preview，MSVC Build Tools 18.7–18.10
- **Pigweed**：SEED 0111 批准 Bazel 为主构建系统，GN 转维护模式，CMake 无限期支持
- **sccache / ccache / Icecream / mold / FASTBuild**：构建缓存与链接器工具链
- **Bazel / Buck2 / CMake / Meson / Build2**：构建系统选型
- **腾讯广告**：自研 C++ 分布式编译系统

## 重要趋势信号
- **up｜自托管构建缓存进入实践爆发期**：sccache/ccache/Icecream 对比指南密集涌现，从大厂专属向中小团队过渡，延伸至远程 Mac CI 场景｜**high**
- **up｜字节跳动 libc++ 迁移**：中国大厂从编译基础设施"使用者"升级为"定义者"，带动周边工具链适配需求｜**high**
- **up｜Incredibuild 向 CI/CD 全流程平台跃迁**：从单一编译加速扩展至多品类，免费 CI runner 可能引发价格竞争｜**high**
- **stable｜VS 2026 解耦冲击未兑现**：第三方缓存工具生态未受明显压缩，微软重心仍在 Copilot C++ 与 C++23 一致性｜**medium**
- **stable｜Bazel 采用持续但 C/C++ 依赖导入标准化缺位**：结构性瓶颈，对比 Rust Cargo / JS npm｜**medium**
- **stable｜CI/CD 缓存叙事进入稳定期**：10 分钟→30 秒命中成为事实标准｜**medium**
- **stable｜sccache 与 mold 组合兼容性**：从具体 bug 讨论转为一般性工具链组合复杂性｜**low**
- **stable｜FASTBuild 中文社区仍有提及但无 2026 新动态**：社区活跃度可能下降｜**low**

## 长期跟踪方向
- 自托管构建缓存在中小团队及远程 Mac CI 场景的普及进度
- VS 2026 构建工具与 IDE 解耦后，MSVC 原生缓存能力是否压缩第三方工具空间
- Bazel C/C++ 依赖导入标准化进展（对比 Cargo/npm 范式）
- sccache + mold 工具链组合是否催生组合标准或缓存策略改进
- FASTBuild 是否出现 2026 年新动态或采用案例
- 字节跳动 libc++ 迁移经验对亚太 C++ 工具链选型偏好的影响

## 竞品动态
- **Incredibuild**：推出 Islo AI 沙箱；免费 8× CI runner 针对 GitHub Actions 付费 runner 市场；发布 2026 十大 CI/CD 工具榜单；仍捆绑在 VS 中形成生态锁定
- **Microsoft**：VS 2026 GA，C++ 构建工具独立升级，Copilot C++ Private Preview，ASan 扩展 ARM64，AVX-512 代码生成
- **Pigweed（Google）**：Bazel 转为主构建系统，标志嵌入式/系统软件领域采用
- **Meta Buck2**：Tweag 发布介绍文章，与 Bazel 对比中语言支持较窄

## 已消退信号（本期未延续）
- AI 辅助 CI/CD 优化从厂商叙事扩展至学术研究（medium，可能仍停留概念阶段）
- ccache 4.14.1 版本更新与 distcc 组合（medium，进入稳定间歇期）
- Build2 轻量替代方案（low，早期信号未获跟进）
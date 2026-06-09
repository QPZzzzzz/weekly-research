# build-acceleration — Research Memory

最后更新: 2026-06-09

### 关键记忆点提取

**公司/产品/项目**
- **sccache** (Mozilla/Google) - 编译缓存工具，支持Rust/C/C++及云存储后端
- **mold** - 高速链接器，与sccache存在兼容性问题
- **Buck2** (Meta) - 开源构建系统，Rust核心+Starlark规则
- **Incredibuild** - 分布式编译与缓存解决方案提供商
- **Visual Studio 2026** (Microsoft) - 集成AI构建分析（Copilot Chat）
- **Blender** - 大型C++项目，社区讨论编译加速策略
- **Icecream, xmake** - 分布式编译工具（中文社区提及）

**重要趋势信号**
- **CI/CD 10分钟规则成为行业共识** (强度: high) - 核心CI检查控制在10分钟内，驱动编译加速刚性需求
- **sccache成为主流编译缓存工具** (强度: high) - 从大厂工具演变为行业标配，支持多语言和云存储
- **Buck2开源社区持续活跃** (强度: high) - 代表构建系统发展方向，挑战Bazel/CMake地位
- **sccache与mold兼容性问题持续存在** (强度: medium) - 工具链集成核心痛点，影响全面采用
- **C++20模块在大型项目中仍不实用** (强度: medium) - unity builds仍是当前最有效加速手段
- **Visual Studio 2026集成AI构建分析** (强度: medium) - Copilot Chat辅助迭代，但构建性能分析功能未明确

**值得长期跟踪的技术方向**
- **分布式编译+缓存** - sccache、Icecream等工具组合，实现3-10倍加速
- **现代构建系统演进** - Buck2、Bazel、Meson的竞争与社区采用情况
- **C++20模块在大型项目中的实际突破** - 一旦成功应用将改变编译加速格局
- **AI集成CI/CD** - 智能构建分析、自动优化编译参数

**竞品动态**
- **sccache** - 成为行业标配，云存储集成能力突出，但mold兼容性问题待解决
- **Buck2** - Meta持续推广，Hacker News热议，社区贡献者数量是关键指标
- **Incredibuild** - 持续市场教育，发布构建系统选择指南，强调分布式处理价值
- **Visual Studio 2026** - 发布后社区反应积极，关注MSVC性能和C++23支持
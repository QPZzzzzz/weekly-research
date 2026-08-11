# incredibuild — Research Memory

最后更新: 2026-08-11

## 关键记忆点

### 公司/产品/项目
- **Incredibuild**：从分布式编译工具转向 AI 平台，核心产品为 **Islo AI 沙盒**（2026年5月发布），推出免费 CI 加速计划（宣称 8 倍提速）
- **EngFlow**：以 SOC 2/SLSA 安全合规为差异化，C++ 构建提速 21 倍，渗透金融科技和健康科技行业
- **FASTBuild**：开源替代，在 Unity 社区从"评估"进入"迁移"阶段，针对游戏资源管线优化
- **yadcc**：腾讯云开源，针对工业场景优化，提供中心调度+容灾设计
- **tipi.build**：与 EngFlow 合作推出 **CMake RBE 方案**，提供不依赖 Visual Studio 的替代路径

### 重要趋势信号
- **Incredibuild 全面转向 AI 平台**（强度：high，方向：up）— Islo AI 沙盒成为核心战略，免费 CI 加速计划作为获客漏斗
- **EngFlow 安全合规飞轮**（强度：high，方向：up）— 安全合规从差异化升级为受监管行业准入门槛
- **CMake+Ninja+云编译替代路径**（强度：high，方向：up）— 直接绕过 Incredibuild 与 Visual Studio 深度绑定的护城河
- **FASTBuild 开源替代迁移趋势**（强度：medium，方向：up）— Unity 社区从评估进入迁移阶段
- **Incredibuild 定价暴涨 400%**（强度：medium，方向：down）— $600→$3000，可能加速中低端用户流失
- **C++ Modules 与分布式编译冲突**（强度：medium，方向：new）— 可能从"分发编译任务"转向"分发模块缓存"，2-3 年内影响有限

### 长期跟踪技术方向
- **C++ Modules 在 MSVC/GCC/Clang 的成熟度进展** — 可能颠覆分布式编译技术路线
- **Islo AI 沙盒采用率及 AI 编码代理对执行层的需求** — 决定 Incredibuild 转型成败
- **Incredibuild 定价上涨后用户流失的实际数据** — 验证定价策略影响
- **CMake RBE 方案在性能和稳定性上是否追平 Incredibuild** — 竞争格局根本性变化的关键

### 竞品动态
- **EngFlow**：C++ 构建 21 倍提速；SOC 2/SLSA 合规认证；与 tipi.build 合作推出 CMake RBE 方案
- **FASTBuild**：Unity 社区迁移趋势增强；低带宽下性能不佳（100Mbps 时 43.5 分钟 vs Incredibuild 13.6 分钟），但缓存全命中时仅 6.5 分钟
- **yadcc**：工业场景深耕，中心调度+容灾设计
- **Incredibuild**：10.36.2 版本（2026-07-30）修复仪表盘问题；通过龙智合作推广中国市场；定价 $600→$3000（+400%）
- **替代品生态**：Azure DevOps、Jenkins、Gradle 等被列为替代选项；Ansible 市场份额 50.80%、Bitbucket Pipelines 8.22%
# incredibuild — Research Memory

最后更新: 2026-09-20

# Incredibuild 竞品对比与行业格局 · 关键记忆点

## 涉及公司/产品/项目

- **Incredibuild**（主体，正从分布式编译工具转型 AI 开发加速平台）
- **Islo AI 沙盒**（Incredibuild 新叙事核心产品）
- **Visual Studio 2026 / VS 18.0**（Microsoft，深度集成方）
- **EngFlow**（技术竞品，C++/Bazel 生态）
- **FASTBuild**（开源竞品，在华影响力低位）
- **Buildkite**（被官方定位为"只编排不缓存/分发"对照靶）
- **TeamCity / Jenkins / GitLab**（通用 CI 竞品认知三角）
- **CircleCI / Azure Pipelines / Ansible / Bitbucket Pipelines / Oracle APEX**（通用 CI/CD 压制方）
- **Depot / Daytona / Blacksmith / E2B**（云原生构建加速 + 开发环境沙盒新势力）
- **腾讯 yadcc**（自研分布式编译系统，已开源）
- **美团 DQU**（暂不需要分布式编译）
- **龙智 DragonSoft / dhorde.com**（中国区授权合作伙伴与销售渠道）
- **Xoreax Software**（Incredibuild 前身）

## 重要趋势信号

- **up / high** — Incredibuild 全站叙事系统性迁移至 Islo AI 沙盒与 CI 加速，传统分布式编译叙事被主动稀释
- **up / high** — Rust 分发与缓存连续迭代（10.37.1 距 10.37.0 仅数周），sccache 工具链不成熟存在商业空白
- **up / high** — Visual Studio 2026 集成加深（含 VS 18.0 扩展），Windows/MSVC 生态绑定构成核心护城河（上期 medium 升级）
- **up / medium** — PeerSpot Build Automation 品类 mindshare 回升至 1.3%，EngFlow 0.7%
- **stable / high** — 专业构建加速品类被通用 CI/CD 平台双重压制（评分与份额均劣势）
- **stable / medium** — EngFlow 媒体热度（21 倍提速）与市场口碑（零评价）持续脱节
- **stable / medium** — 竞品对比格局高度稳定（TeamCity 24%、Jenkins 23%、EngFlow 21%、GitLab 7%）
- **stable / medium** — 中国大厂分布式编译场景分化（腾讯 yadcc 自研开源 vs 美团 DQU 暂不需要）
- **new / medium** — Incredibuild 官方博客首次系统性构建竞品话术，将 Buildkite 定位为对照靶
- **stable / low** — FASTBuild 中文社区内容停留在 2018 年，在华影响力低位
- **↓ 降级 high→low** — 云原生构建加速新势力（Depot、Daytona、Blacksmith、E2B）本期无新增证据

## 值得长期跟踪的技术方向/话题

- Incredibuild 向 AI 开发加速平台转型（Islo AI 沙盒）能否突破通用 CI/CD 压制
- Rust 构建缓存与分发商业空白窗口是否被有效占据
- Windows/MSVC 生态绑定强度是否继续上升（VS 2026 集成）
- 官方竞品话术攻势（Buildkite 对照靶）是否形成系列化
- 云原生构建加速（Depot/Blacksmith）与开发环境沙盒（Daytona/E2B）赛道边界
- 中国区渠道壁垒（龙智等授权合作伙伴）有效性
- 腾讯 yadcc 开源对国内分布式编译格局的影响

## 竞品动态

- **EngFlow**：媒体持续报道 C++ 构建提速 21 倍，定义品类性能基准线；但 PeerSpot 评分 0.0、零评价、mindshare 0.7%，商业化路径未验证
- **Buildkite**：被 Incredibuild 官方博客定位为"只编排不缓存/分发"对照靶（新增信号）
- **FASTBuild**：宣称 10 倍以上加速，支持 Win/Linux/macOS；中文社区内容陈旧（2018 年），在华低位
- **腾讯 yadcc**：分布式编译系统开源，含中心调度、心跳、本地守护进程、并发控制等工业级优化
- **Depot / Daytona / Blacksmith / E2B**：PitchBook 曾列为竞品，本期无新增证据，热度降级，需确认采集覆盖变化
- **通用 CI/CD 平台**：CircleCI 9.3、Azure Pipelines 8.5 评分压制 Incredibuild 8.0；Ansible 49.55% 品类份额领先
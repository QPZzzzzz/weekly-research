# incredibuild — Research Memory

最后更新: 2026-09-13

# 调研记忆点 — Incredibuild 竞品对比与行业格局（2026-09）

## 涉及公司/产品/项目
- **Incredibuild**（分布式编译工具，正转型 AI 原生开发加速平台）
- **Kypso**（AI 初创公司，被 Incredibuild 收购）
- **Islo**（Incredibuild AI 沙盒，2026年5月发布）
- **腾讯 yadcc**（自研分布式编译系统，已开源）
- **EngFlow**（竞品，有热度无口碑）
- **FASTBuild**（开源竞品，Win/Linux/OS X）
- **BuildXL**（微软分布式构建系统）
- **Bazel / Nx / TeamCity / Jenkins / GitLab / Ansible / Bitbucket Pipelines / Buildkite / BuildBuddy / Buildbarn / Aspect / Hermetiq**
- **龙智 DragonSoft**（Incredibuild 中国授权合作伙伴）
- **美团 DQU**（上期负面信号来源）
- **Epic MegaGrants**（游戏生态合作方）
- **百度 Comate**（中文渠道提及 C++ 编译加速）

## 重要趋势信号
- **AI 原生转型** | Incredibuild 收购 Kypso，从营销叙事升级为资本/战略层面，定位重构为 AI 原生开发加速平台 | **high**
- **多语言栈扩展** | 10.37.1 持续改进 Rust 分发与缓存，从单点动作变为连续迭代主线 | **high**
- **中国大厂自研投产** | 腾讯 yadcc 开源并披露 1700 编译核心、512 并发、每天 300 万+ 目标文件、3~5TB 生产规模 | **medium**
- **品类认知困境** | 专业构建加速品类被通用 CI/CD 与 DevOps 品类稀释，Ansible 以 49.55% 主导 6sense 分类 | **medium**
- **口碑数据稀缺** | Incredibuild 仅 1 条评价、EngFlow 零评价，制约企业采购入围 | **medium**
- **传统分布式编译叙事弱化** | 官网/博客/资源页顶部推广全面转向 Islo、Unity Shader、8 倍免费 CI 加速 | **medium**
- **中国大厂刚需减弱叙事被抵消** | 美团 DQU 负面信号被腾讯 yadcc 自研投产覆盖，态度两极分化 | **low→medium**

## 值得长期跟踪的技术方向/话题
- Kypso 收购后产品线整合方向：AI 能力是否注入 Build Cache / Islo 形成闭环
- Incredibuild Build Cache **Linux 版本发布时间**（决定 CI/CD 主战场渗透与 Rust 支持实际价值）
- 腾讯 yadcc 开源后是否形成中国大厂分布式编译事实标准
- Incredibuild 核心 C++ 分发业务**定位空心化风险**（存量客户续费/增购动能）
- 专业构建加速品类能否在采购心智中建立独立品类认知
- 口碑数据积累速度作为品类格局隐性变量
- Rust 生态在 Linux 主战场的编译缓存/分发需求渗透

## 竞品动态
- **腾讯 yadcc**：开源，披露生产规模（1700 编译核心/512 并发/300万+目标文件/3~5TB），投产腾讯广告后台，含中心调度、容灾、缓存优化、链接阶段并发限制
- **EngFlow**：评分 0.0、零评价、mindshare 0.7%（同比 0.6% 微升），有 The New Stack "C++ 构建提速 21x" 媒体热度但客户基数疑集中少数标杆
- **FASTBuild**：开源，支持 Win/Linux/OS X，编译+缓存+网络分发，10x+ 加速；中文社区内容陈旧（2018 教程仍为主要入口）
- **Incredibuild**：评分 8.0、仅 1 条评价、mindshare 1.3%（环比 1.4% 回落，同比 2025 年 0.7% 仍增长）
- **PeerSpot 对比三角**：TeamCity(24%)、Jenkins(23%)、EngFlow(21%)、GitLab(7%) 维持不变
- **6sense 分类**：Ansible(49.55%)、Bitbucket Pipelines(10.00%)、Oracle APEX(6.44%)
- **龙智**：2026-09-15 举办 AI 驱动 DevSecOps 线下沙龙，宣称服务超 20 万开发者
- **Epic MegaGrants**：向获得者提供开发加速技术，深化游戏生态
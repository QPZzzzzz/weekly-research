# incredibuild — Research Memory

最后更新: 2026-09-19

# Incredibuild 竞品对比与行业格局 · 关键记忆点

## 涉及公司/产品/项目

- **Incredibuild**（锚点公司）：分布式编译工具，正转型 AI 开发加速平台
- **Islo AI 沙盒**：Incredibuild 新叙事核心产品
- **EngFlow**：竞品，C++ 构建提速 21 倍，技术口碑强但市场验证弱
- **Bazel**：竞品，PeerSpot 对比对象
- **Depot / Blacksmith**：云原生构建缓存与远程执行新势力
- **Daytona / E2B**：开发环境沙盒新势力，与 Islo 叙事正面重叠
- **CircleCI / Azure Pipelines / GitHub / CloudBees**：通用 CI/CD 平台，评分与替代位压制 Incredibuild
- **Ansible / Bitbucket Pipelines / Oracle APEX**：6sense 品类份额前三
- **TeamCity / Jenkins / GitLab**：PeerSpot 对比三角
- **FASTBuild**：开源跨平台竞品，宣称 10 倍以上加速
- **Garden**：远程构建/测试/运行服务竞品
- **Buildkite**：被 Incredibuild 博客定位为「只编排不缓存/分发」对照靶
- **腾讯 yadcc**：中国大厂自研分布式编译系统，已开源
- **美团 DQU**：实践表明暂不需要分布式编译
- **龙智 DragonSoft**：Incredibuild 中国授权合作伙伴
- **Kypso**：被 Incredibuild 收购，AI 能力注入待跟踪
- **投资方**：Hiro Capital、Insight Partners、Fortissimo Capital

## 重要趋势信号

- **方向 up｜Incredibuild 全站叙事系统性迁移**：首页/博客/资源页/新闻归档统一置顶 Islo AI 沙盒、Unity Shader、8 倍免费 CI 加速，传统分布式编译叙事被主动稀释｜强度 **high**
- **方向 up｜Rust 分发与缓存连续迭代**：10.37.1（2026-09-07）距 10.37.0 仅数周，连续第二版以 Rust 为重点，迭代节奏加快｜强度 **high**
- **方向 up｜Visual Studio 2026 集成加深**：Microsoft Learn 明确含 IncrediBuild 支持更新与 VS 18.0 扩展｜强度 **medium**
- **方向 up｜PeerSpot mindshare 回升**：Build Automation 品类从 0.8% 升至 1.3%，方向性回升待观察｜强度 **medium**
- **方向 stable｜专业构建加速品类被通用 CI/CD 双重压制**：TrustRadius 评分 CircleCI 9.3、Azure Pipelines 8.5 > Incredibuild 8.0；6sense 份额未进前三｜强度 **high**
- **方向 stable｜EngFlow 媒体热度与市场口碑脱节**：The New Stack 再报 21 倍提速，但 PeerSpot 评分 0.0、零评价、mindshare 0.7%｜强度 **high**
- **方向 stable｜竞品对比格局高度稳定**：PeerSpot 对比三角 TeamCity 24%、Jenkins 23%、EngFlow 21%、GitLab 7% 无变动｜强度 **medium**
- **方向 new｜PitchBook 新增云原生竞品名单**：Depot、Daytona、Blacksmith、E2B 被列为竞品，赛道边界从构建加速向云原生开发环境扩展｜强度 **high**
- **方向 stable｜中国大厂分布式编译场景分化**：美团 DQU 暂不需要，腾讯 yadcc 自研投产并开源｜强度 **medium**

## 值得长期跟踪的技术方向/话题

- **Rust 构建缓存与分发**：sccache 等工具链不成熟，存在商业空白；关注 Build Cache Linux 版本发布时间（CI/CD 主战场渗透关键变量）
- **云原生构建加速**：Depot/Blacksmith 的云原生构建缓存与远程执行是否形成实际竞争压力
- **开发环境沙盒**：Daytona/E2B 与 Islo AI 沙盒的正面重叠竞争
- **AI 能力注入构建工具链**：Kypso 收购后 AI 能力注入 Build Cache / Islo 的闭环进展
- **Windows/MSVC 生态绑定**：VS 2026 集成与 VS 18.0 扩展作为核心护城河
- **可量化加速倍数**：专业品类破局点，EngFlow 21 倍正在定义性能基准线
- **中国区商业化路径**：腾讯 yadcc 自研 vs 美团暂不需要的场景分化

## 竞品动态

- **EngFlow**：The New Stack 2026-09-10 报道 C++ 构建提速 21 倍，媒体热度持续；但 PeerSpot 评分 0.0、零评价、mindshare 仅 0.7%，客户疑集中于少数标杆
- **Depot / Blacksmith**：主打云原生构建缓存与远程执行，被 PitchBook 列为 Incredibuild 竞品
- **Daytona / E2B**：聚焦开发环境沙盒，与 Incredibuild Islo AI 沙盒叙事正面重叠
- **CircleCI**：TrustRadius 评分 9.3 高于 Incredibuild 8.0，被 G2 列为最佳替代
- **Azure Pipelines**：TrustRadius 评分 8.5 高于 Incredibuild 8.0
- **Ansible**：6sense Build & Deployment Automation 品类份额 49.55% 居首
- **FASTBuild**：开源跨平台，宣称 10 倍以上加速，中文社区内容陈旧、在华影响力低位
- **腾讯 yadcc**：开源，含中心调度、心跳、本地守护进程、并发控制等工业级优化
- **融资动态**：Hiro Capital、Insight Partners、Fortissimo Capital 为相关投资方
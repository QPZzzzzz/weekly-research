# incredibuild — Research Memory

最后更新: 2026-09-15

# Incredibuild 竞品调研 · 关键记忆点

## 涉及公司/产品/项目
- **Incredibuild**（核心对象）：10.37.1 版本，Islo AI 沙盒、Build Cache、Unity Shader 编译、8 倍免费 CI 加速
- **EngFlow**：C++ 构建提速 21 倍，媒体热度高但口碑数据为零
- **腾讯 yadcc**：自研分布式编译，1700 编译核心、512 并发、日 300 万+ 目标文件、3~5TB 规模，投产广告后台
- **美团 DQU**：明确暂不需要分布式加速（场景分化对照）
- **龙智 DragonSoft**：Incredibuild 中国授权合作伙伴，宣称服务超 20 万开发者
- **竞品**：FASTBuild（开源）、Bazel、Buildkite、CircleCI、Azure Pipelines、TeamCity、Jenkins、GitLab、sccache、distcc、ccache
- **Kypso**：被 Incredibuild 收购（上期事件，影响持续）

## 重要趋势信号
- **high**｜Incredibuild 官网全站推广重心迁移至 Islo AI 沙盒与 CI 加速，传统分布式编译叙事系统性弱化（首页/博客/新闻归档/CI-CD 页/EOL 页顶部统一）
- **high**｜Rust 分发与缓存成为连续迭代主线，10.37.1 距 10.37.0 仅数周，多语言栈扩展升级为战略节奏
- **high**｜专业构建加速品类被通用 CI/CD 稀释：TrustRadius 评分 Azure Pipelines 8.5、CircleCI 9.3 > Incredibuild 8.0；6sense 中 Ansible 主导 49.55%
- **medium**｜Incredibuild 博客首次明确「加速补充层」定位，评述 Buildkite 只编排不缓存/分发
- **medium**｜口碑数据稀缺成采购隐性壁垒：Incredibuild 仅 1 条评价、EngFlow 零评价
- **low**｜中国大厂态度两极分化：腾讯 yadcc 自研投产 vs 美团 DQU 暂不需要
- **low**｜龙智渠道活跃度维持但无新增数据，信号回落

## 值得长期跟踪的技术方向/话题
- **Build Cache Linux 版本发布时间**：决定 CI/CD 主战场渗透与 Rust 支持实际价值的关键变量
- **Kypso 收购后 AI 能力是否注入 Build Cache / Islo 形成闭环**，产品线整合方向
- **Rust 生态构建缓存/分发工具链成熟度**（sccache 等尚不成熟，高价值细分场景）
- **「加速补充层」定位能否被市场接受**，是否形成系列内容
- **腾讯 yadcc 开源后是否出现新版本或更多中国大厂跟进**，形成事实标准
- **专业构建加速品类能否在通用 CI/CD 评分劣势下建立独立价值认知**

## 竞品动态
- **EngFlow**：The New Stack 持续报道 C++ 构建提速 21 倍，但 PeerSpot 零评价、0.0 评分、mindshare 0.7%，热度与口碑脱节，客户疑集中少数标杆
- **FASTBuild**：开源高性能构建系统，支持 Win/Linux/OS X，宣称 10 倍以上加速；中文社区内容陈旧（2018 教程仍为主入口）
- **通用 CI/CD 平台**：CircleCI 9.3、Azure Pipelines 8.5 评分领先，以「一站式」叙事覆盖构建加速品类
- **Buildkite**：被 Incredibuild 博客点名为「只提供编排不提供缓存与分发」，成为其补充层定位的对照靶
- **PeerSpot 对比三角**：TeamCity 24%、Jenkins 23%、EngFlow 21%、GitLab 7%（维持不变）
- **Incredibuild 自身**：Build Automation 品类 PeerSpot 排名第 27，评分 8.0（仅 1 条评价）
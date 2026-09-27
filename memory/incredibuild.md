# incredibuild — Research Memory

最后更新: 2026-09-27

# Incredibuild 调研关键记忆点

## 公司/产品/项目
- **Incredibuild**（主体）：叙事从分布式编译迁移至 AI 沙盒 + CI 加速平台
- **Islo AI 沙盒**：2026-05 发布，官网全站置顶
- **8× CI Runner**：早期访问中，与 Islo 并列第一叙事层级
- **EngFlow**：远程执行与缓存，C++ 构建快 21×
- **Buildkite**：被定位为"理想切入点"（缺缓存/分发能力）
- **腾讯 yadcc**：中国区开源分布式编译系统
- **sccache / distcc / octobuild / ccache / FASTBuild**：开源替代方案
- **龙智（shdsd.com）**：中国区授权合作伙伴
- **竞品对比对象**：Jenkins、TeamCity、Azure DevOps、CircleCI、GitLab、Harness、Bazel、Wercker、Travis CI、Bamboo、Ansible、Bitbucket Pipelines

## 重要趋势信号
- **方向 up｜叙事迁移**：官网全站置顶 Islo + 8× CI Runner，传统分布式编译退居次要｜强度 **high**
- **方向 up｜Rust 迭代**：Windows 10.37.1 首条改进 Rust distribution/caching，sccache 窗口期仍存｜强度 **high**
- **方向 up｜容器化部署**：Linux 4.30.0 支持 Manager 在 Docker 下安装｜强度 **high**
- **方向 up｜mindshare 上升**：Build Automation 品类 0.8% → 1.3%（同比 +62.5%）｜强度 **high**
- **方向 stable｜品类泛化**：官方博客主动发布 GitHub Coding Agents 排名，向 AI/LLM 工具链漂移｜强度 **high**
- **方向 stable｜品类压制**：6sense 显示 Ansible 49.55% 主导 Build And Deployment Automation，Incredibuild 边缘化｜强度 **high**
- **方向 new｜侧翼策略**：官方博客将 Buildkite 定位为理想切入点（缺缓存/分发）｜强度 **medium**
- **方向 stable｜对比格局**：PeerSpot 对比频率 TeamCity 24%、Jenkins 23%、EngFlow 21%｜强度 **medium**
- **方向 stable｜中国区替代**：腾讯 yadcc 开源，CSDN 讨论 distcc/octobuild/ccache｜强度 **medium**
- **方向 stable｜EngFlow 热度**：媒体 21× 报道持续，但 PeerSpot 评分 0.0、排名 #37、mindshare 0.7% 脱节｜强度 **medium**

## 长期跟踪方向
- **mindshare 能否突破 2% 关口**：判断新叙事是否转化为品类心智的关键阈值
- **AI 编码 Agent 排名是否系列化**：流量策略 vs 战略漂移的前兆
- **Buildkite 切入点是否形成系列营销**：若扩展至 CircleCI/Drone，侧翼策略成型
- **Docker 安装 Manager 是否带动云原生 CI 落地案例**：技术能力需转化为客户案例
- **Rust 生态默认工具心智**：sccache 不成熟窗口期的护城河机会
- **中国区头部自研分化**：腾讯 yadcc 等自研方案对 Incredibuild 的替代压力
- **上期信号缺位确认**：G2（CircleCI 4.4 星/501+ 评价）、美团 DQU、Epic MegaGrants 需确认采集遗漏或趋势消退

## 竞品动态
- **EngFlow**：The New Stack 报道 C++ 构建快 21×；PeerSpot 对比频率 21%，但评分/评价数据不匹配
- **Buildkite**：被 Incredibuild 官方博客定位为"理想切入点"，25 分钟构建无缓存/分发
- **Ansible**：6sense 显示以 49.55% 主导 Build And Deployment Automation 品类
- **Bitbucket Pipelines**：6sense 品类第二，10.00%
- **腾讯 yadcc**：开源，工业场景优化（中心调度、心跳、本地守护进程、多版本编译器共存）
- **开源替代**：sccache 分布式场景不成熟；distcc/octobuild/ccache 在中文社区活跃
- **龙智**：中国区授权合作伙伴，宣称 20 万+ 开发者、编译增速 10×，缺具体落地案例
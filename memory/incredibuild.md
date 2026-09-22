# incredibuild — Research Memory

最后更新: 2026-09-22

# 调研记忆点 · Incredibuild 竞品对比与行业格局（2026-09）

## 涉及公司/产品/项目
- **Incredibuild**（主体，含 Windows 10.37.1 / Linux 4.29.3）
- **Islo AI 沙盒**（2026-05 发布，新品牌核心）
- **8× 更快 CI runner**（早期访问）
- **EngFlow**（竞品，mindshare 0.7%）
- **FASTBuild**（开源竞品，中文社区停滞）
- **Buildkite**（被官方定位为对照靶）
- **CircleCI / Azure Pipelines / Ansible / Bitbucket Pipelines / Oracle APEX**（通用 CI/CD 压制方）
- **Depot / Daytona / Blacksmith / E2B**（云原生新势力，降温）
- **sccache**（Rust 工具链，不成熟）
- **RustRover**（JetBrains，新增插件支持）
- **Visual Studio 2026 / VS 18.0 / CMake 4.1.2**
- **龙智 DragonSoft / dhorde.com / shdsd.com**（中国区渠道）
- **腾讯 yadcc / 美团 DQU**（中国大厂自研路线）
- **Xoreax Software**（历史主体）

## 重要趋势信号
- **up｜全站叙事迁移至 Islo AI 沙盒与 CI 加速**：官网/博客/资源页/生命周期页/Tools Spotlight/中文站导航全面置顶，传统分布式编译退出主叙事。强度 **high**
- **up｜Rust 分发与缓存连续迭代**：Windows 10.37.1 与 Linux 4.29.3 密集更新，跨平台投入确认，sccache 空白留出商业窗口。强度 **high**（上期 medium）
- **up｜VS 2026 集成加深**：含 VS 18.0 扩展 + 默认集成 CMake 4.1.2，Windows/MSVC 护城河强化。强度 **high**（上期 medium）
- **up｜PeerSpot mindshare 回升至 1.3%**：EngFlow 0.7%，Incredibuild 评分 8.0、100% 愿推荐。强度 **medium**
- **stable｜专业构建加速被通用 CI/CD 双重压制**：CircleCI 9.3、Azure Pipelines 8.5 高于 Incredibuild 8.0；Ansible 49.55% 份额领先。强度 **high**
- **stable｜EngFlow 媒体热度与口碑脱节**：评分 0.0、0 评价、排名 #37。强度 **medium**
- **stable｜竞品对比格局稳定**：TeamCity 24%、Jenkins 23%、EngFlow 21%、GitLab 7%。强度 **medium**
- **stable｜中国大厂场景分化**：腾讯 yadcc 自研开源 vs 美团 DQU 暂不需要（用 PCH/CCache）。强度 **medium**
- **new｜官方首次系统性竞品话术**：Buildkite 被定位为"只编排不缓存/分发"对照靶。强度 **medium**
- **stable｜FASTBuild 中文社区停滞**：博客园内容停留 2018-03-23。强度 **low**
- **down｜云原生新势力降温**：Depot/Daytona/Blacksmith/E2B 本期无新增证据。强度 **low**

## 值得长期跟踪的技术方向/话题
- **Islo AI 沙盒产品化节奏**：中国区导航新增"编码代理沙箱""构建卫士"，是否形成系列落地动作
- **Rust 构建加速工具链**：sccache 不成熟窗口期，Incredibuild 能否借 C++ 调度/缓存基础设施切入
- **JetBrains 阵营生态绑定**：RustRover 插件是否延伸至更多 IDE
- **Windows/MSVC 默认地位**：VS 2026 + CMake 4.1.2 默认集成对护城河强度的持续影响
- **CI 全链路加速赛道**：Incredibuild 8× runner 与 Depot/Blacksmith 的正面竞争
- **官方竞品话术系列化**：Buildkite 对照靶是否扩展为内容攻势
- **中国区渠道推广力度**：龙智 DragonSoft 的落地节奏
- **中国大厂分布式编译路线分化**：自研开源 vs 替代方案（PCH/CCache）

## 竞品动态
- **EngFlow**：PeerSpot 评分 0.0、0 评价、排名 #37、mindshare 0.7%，商业化路径未验证；对比频率 21%
- **Buildkite**：被 Incredibuild 官方博客定位为"只编排不缓存/分发"对照靶，成为营销切入点
- **CircleCI / Azure Pipelines**：TrustRadius 评分 9.3 / 8.5，均高于 Incredibuild 8.0
- **Ansible / Bitbucket Pipelines / Oracle APEX**：6sense 份额 49.55% / 10.00% / 6.44% 领先
- **FASTBuild**：中文社区内容停留 2018 年，在华影响力低位
- **Depot / Daytona / Blacksmith / E2B**：本期无新动态，热度延续降级
- **腾讯 yadcc**：自研开源路线；**美团 DQU**：明确暂不需要分布式编译
- **无融资/合作/技术突破类新增动态**
# incredibuild — Research Memory

最后更新: 2026-09-12

# Incredibuild 竞品调研 — 关键记忆点

## 涉及公司/产品/项目
- **Incredibuild**（核心标的）：10.37.1 / 10.37.0、Build Cache、Islo AI 沙盒、Unity Shader 加速、8倍免费 CI 加速、SBOM 生成
- **竞品**：EngFlow、FASTBuild、BuildXL、Nx、Bazel、Buildkite
- **通用 CI/CD 平台**：TeamCity、Jenkins、GitLab、Ansible
- **中国相关**：龙智 DragonSoft（授权合作伙伴）、美团 DQU、腾讯 yadcc、百度 Comate
- **生态合作**：Epic MegaGrants、Unity、Adobe、Bandai Namco、赛轮思、ALGOTEC、ETC

## 重要趋势信号
- **up / high**：Incredibuild 分发+缓存融合架构深化 — 10.37.0 落地 Build Cache，10.37.1 扩展 Rust 分发与缓存，从 Windows 单平台向多语言栈扩展（Linux 仍缺位）
- **up / high**：营销重心转向 Islo AI 沙盒 + Unity Shader + 8倍免费 CI 加速，传统分布式编译叙事弱化，全站覆盖
- **high**：品类边界模糊 — PeerSpot 高频对比对象为 TeamCity(24%)、Jenkins(23%)、EngFlow(21%)、GitLab(7%)，战场在"CI/CD 效能工具"而非"分布式编译"
- **high**：EngFlow "有热度无口碑"持续 — 媒体曝光 21x 加速 vs PeerSpot 零评价、评分 0.0、mindshare 0.7%
- **high**：Incredibuild 用户评价仅 1 条（评分 8.0），制约企业采购入围率
- **medium→low**：Incredibuild mindshare 环比回落 1.4%→1.3%（同比 2025 年 0.7% 仍升），上升动能减弱
- **medium**：中国大厂分布式编译刚需减弱 — 美团 DQU 明确"暂不需要"，FASTBuild 中文教程 8 年未更新
- **low**：龙智持续运营中国渠道（"服务超20万开发者"表述需谨慎解读）
- **low**：中文官网跨行业案例（营销价值 > 实证价值）

## 值得长期跟踪的技术方向/话题
- Incredibuild Build Cache **Linux 版本发布时间**（决定 CI/CD 主战场渗透）
- **Islo AI 沙盒 GA 时间表**（2026年5月发布至今仍早期访问）
- Rust 分发/缓存支持是否**扩展至更多语言**（突破 C++ 单一栈依赖）
- EngFlow 用户评价是否补充（若积累口碑可能改变格局）
- Incredibuild 用户评价增长（直接影响采购入围）
- 专业构建加速工具**品类认知建立**（突破 6sense 分类困境）
- 中国大厂编译规模是否达**价值临界点**
- 游戏生态深化（Epic MegaGrants + Unity Shader）能否转化为客户增长

## 竞品动态
- **EngFlow**：The New Stack 报道 C++ 构建提速 21x 并提升安全性；但 PeerSpot 零评价、评分 0.0、mindshare 0.7%，客户基数疑集中少数标杆
- **FASTBuild**：开源，支持 Win/Linux/OSX，编译+缓存+网络分发，10x+ 加速；中文社区渗透走低
- **BuildXL**：Stack Overflow 对比显示 Incredibuild 更聚焦大型 C++ 代码库、深度集成 Visual Studio
- **Buildkite**：被 Incredibuild 博客定位为"理想切入点"（只给编排、不给缓存/分发），主动做品类教育
- **通用平台挤压**：TeamCity/Jenkins/GitLab 构成高频对比三角，Ansible 在 6sense 广义分类下以 49.55% 份额主导（本期无新增证据）
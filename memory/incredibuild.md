# incredibuild — Research Memory

最后更新: 2026-08-16

## 关键记忆点

### 公司/产品/项目
- **Incredibuild** — 从分布式编译工具转向 AI 平台，核心产品为 Islo AI 沙盒（2026年5月发布）
- **Islo AI 沙盒** — Incredibuild 新核心，定位“AI 编码代理执行层”
- **FASTBuild** — 开源高性能构建系统，Unity 社区已进入迁移阶段
- **yadcc** — 腾讯云开源分布式编译系统，强调中心调度、容灾、缓存优化
- **EngFlow** — 主要竞品，宣称 C++ 构建提速 21 倍，但用户评分仅 1/5
- **CMake RBE** — EngFlow 与 tipi.build 合作推出的云编译方案
- **龙智（DragonSoft）** — Incredibuild 中国授权合作伙伴，覆盖游戏开发和金融服务

### 重要趋势信号
- **Incredibuild 全面转向 AI 平台叙事** — 商业模式从“卖软件许可证”转向“卖 AI 开发平台服务”，免费 CI 加速计划作为漏斗顶端获客入口。强度：**high**
- **开源与云原生方案合围** — FASTBuild、yadcc、CMake RBE 多维度侵蚀 VS 绑定护城河，$3000 定价面临挑战。强度：**high**
- **EngFlow 威胁可信度下降** — 1/5 用户评分削弱其“主要竞品”地位，合规差异化未能持续转化为市场增长。强度：**low**
- **中国市场分化格局** — 高端靠代理服务溢价、中低端被开源吞噬，本土“国产替代”政策利好 yadcc。强度：**medium**
- **C++26 模块化是“慢变量”** — 理论上压缩分布式编译优化空间，但 2-3 年内影响有限。强度：**low**

### 长期跟踪方向
- **C++ Modules 在 MSVC/GCC/Clang 的落地进度** — 一旦成熟普及，可能从根本上改变分布式编译工具价值主张
- **Incredibuild 免费 CI 加速计划的转化效果** — 直接决定 AI 平台转型成败
- **FASTBuild 在 Unity 社区的迁移进度** — 开源替代从“评估”进入“迁移”阶段的关键信号
- **yadcc 在中小团队的采用情况** — 本土开源方案对 Incredibuild 中国市场的侵蚀速度

### 竞品动态
- **Incredibuild**：推出免费 CI 加速计划（8× faster CI runners），官网全面转向 AI 叙事
- **EngFlow**：与 tipi.build 合作推出 CMake RBE 方案，以 SOC 2/SLSA 合规为卖点，但用户评分低
- **腾讯云 yadcc**：开源持续活跃，明确“分布式编译提高吞吐但不降低单文件编译耗时”的技术定位
- **FASTBuild**：在 SourceForge 和博客被持续推荐，Unity 社区进入迁移阶段
- **已消退信号**：Incredibuild 定价暴涨 400%（$600→$3000）不再被讨论，可能已从热点转为既定事实
# incredibuild — Research Memory

最后更新: 2026-08-07

## 关键记忆点

### 公司/产品/项目
- **Incredibuild**：分布式编译工具，正转型AI平台，推出Islo AI沙箱（2026年5月），免费CI加速计划（8× faster），定价$600→$3000（+400%）
- **EngFlow**：最强竞品，Peerspot对比频率21%（最高），与tipi.build合作CMake RBE方案，主打SOC 2审计合规和SLSA供应链安全
- **FASTBuild**：开源替代，Unity社区从评估进入迁移阶段，存在IO瓶颈（GitHub issue #359）
- **yadcc**：腾讯云开源分布式编译系统，工业场景优化，中心调度+容灾
- **Islo AI沙箱**：Incredibuild核心战略产品，定位"AI编码代理执行层"
- **Visual Studio 2026**：确认继续集成Incredibuild，微软生态绑定稳固
- **tipi.build**：与EngFlow合作提供CMake RBE方案
- **龙智**：Incredibuild中国授权合作伙伴

### 重要趋势信号
- **开源替代"双线夹击"**：FASTBuild（Unity社区迁移）+ yadcc（工业场景）侵蚀中低端市场 — **high**
- **安全合规成准入门槛**：EngFlow在金融科技、健康科技等受监管行业渗透，SLSA框架成为入场券 — **high**
- **Incredibuild战略转型AI**：从"分布式编译工具"转向"AI编码代理执行层"，转型成功与否取决于Islo采用率 — **medium**
- **C++ Modules技术颠覆风险**：module file体积大，网络传输瓶颈挑战分布式编译核心价值主张 — **medium**
- **CMake+Ninja+云编译替代路径形成**：可能削弱Visual Studio集成护城河 — **medium**

### 长期跟踪技术方向
- **C++ Modules**（C++20）对分布式编译技术路线的影响：可能从"分发编译任务"转向"分发模块缓存"或"本地预编译"
- **AI编码代理基础设施层**：构建加速与AI编码代理的融合方向
- **供应链安全（SLSA框架）** 与分布式编译的结合
- **CMake RBE（Remote Build Execution）** 生态发展

### 竞品动态
- **EngFlow**：与tipi.build合作CMake RBE方案，主打安全合规，受监管行业渗透持续强化
- **FASTBuild**：Unity社区迁移趋势增强，IO瓶颈优化中
- **yadcc**：腾讯云开源，首个针对工业场景优化的中国开源方案，价格敏感用户新选择
- **Incredibuild**：全面转向AI平台，Islo AI沙箱为核心，免费CI加速计划止血用户流失

### 早期信号跟踪清单
- C++ Modules对分布式编译效率的实际影响
- yadcc在工业场景的采用情况
- Islo AI沙箱的采用率及AI编码代理市场渗透
- EngFlow在受监管行业的大客户获取进展
- FASTBuild在Unity社区的迁移实际案例和性能突破
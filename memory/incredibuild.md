# incredibuild — Research Memory

最后更新: 2026-06-01

### 关键记忆点提取

#### 公司/产品/项目
- **Incredibuild**: 核心调研对象，正从编译加速工具转型为AI SDLC平台。
- **EngFlow**: 最直接威胁，宣称21倍加速，获SOC 2认证，与Uber合作。
- **FASTBuild**: 开源替代，获CMake集成，缓存全命中场景性能领先。
- **Garden**: 被Incredibuild收购，增强CI/CD能力。
- **Islo**: Incredibuild发布的AI代理安全沙盒。
- **Uber**: EngFlow重量级客户。
- **tipi.build**: 与EngFlow合作推出CMake RBE方案。
- **龙智/亿道电子**: Incredibuild中国代理商，主攻游戏/汽车行业。

#### 重要趋势信号
- **Incredibuild战略转型为AI SDLC平台** (方向: 平台化, 强度: **High**)
    - 发布AI平台、收购Garden、推出Islo沙盒，从单一编译工具转向覆盖全生命周期的智能执行层。
- **EngFlow以性能+安全组合拳正面冲击** (方向: 竞争加剧, 强度: **High**)
    - 宣称21倍加速、获SOC 2认证、与Uber合作，直接对标Incredibuild核心市场。
- **CISA政策导致C/C++市场结构性下行** (方向: 市场萎缩, 强度: **High**)
    - 美国要求2026年前关键软件剔除C/C++，转向Rust/Go，威胁Incredibuild传统业务。
- **开源/CI/CD工具持续分流** (方向: 竞争泛化, 强度: **Medium**)
    - FASTBuild、Distcc、CCache、Jenkins、GitLab等被广泛列为替代品，竞争边界模糊。
- **安全合规成为选型核心门槛** (方向: 合规驱动, 强度: **Medium**)
    - Incredibuild获ISO 9001/27001、推SBOM；EngFlow获SOC 2，安全能力成关键卖点。

#### 值得长期跟踪的技术方向
- **AI编码代理安全执行层**: Incredibuild的Islo沙盒，解决AI agent在开发者机器上运行的安全问题。
- **多语言编译加速**: Incredibuild转型支持Rust、Java、Go等，应对C/C++市场萎缩。
- **CMake远程构建执行(RBE)**: EngFlow与tipi.build合作，降低迁移门槛。
- **缓存全命中场景优化**: FASTBuild在此场景性能领先，是Incredibuild的潜在弱点。
- **低带宽网络下的分布式编译**: Incredibuild在此场景性能优于FASTBuild，是差异化优势。

#### 竞品动态
- **EngFlow**:
    - 宣称C++构建速度提升21倍，获SOC 2安全认证。
    - 与Uber合办Meetup，讨论monorepo和远程缓存。
    - 与tipi.build合作推出CMake RBE方案。
- **FASTBuild**:
    - 获得CMake官方集成，增强开源生态竞争力。
    - 缓存全命中场景性能优于Incredibuild，但低带宽下性能较差。
- **开源工具**:
    - Distcc、CCache持续被企业采用（如美团技术博客推荐）。
    - Xmake内置分布式编译功能，作为新兴跨平台工具蚕食用户。
- **CI/CD平台**:
    - Jenkins、GitLab、Azure DevOps等被列为Incredibuild主要替代品，竞争边界模糊。
- **Incredibuild自身动态**:
    - 获3500万美元B轮融资，加速AI平台转型。
    - 收购Garden，增强DevOps能力。
    - 发布AI平台、Islo沙盒、自动生成SBOM功能。
    - 在中国市场通过龙智/亿道电子拓展本地化服务，汽车行业效率提升50%+。
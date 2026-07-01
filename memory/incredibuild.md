# incredibuild — Research Memory

最后更新: 2026-07-01

### 公司/产品/项目
- **Incredibuild**: 从编译加速工具转型为AI全生命周期平台，推出Islo（AI沙盒）、Build Guard（安全防护）、Build Runner（CI/CD加速）。
- **EngFlow**: 声称C++构建加速21倍，获SOC 2认证，与Uber合作，与tipi.build推CMake RBE方案。
- **腾讯 yadcc**: 开源分布式编译器，性能优于distcc/icecream，在1000核集群测试。
- **FASTBuild**: 开源替代，获CMake集成，但低带宽下性能仅为Incredibuild的1/3。
- **Bazel**: 用户评分低（1/5），逐渐边缘化。

### 重要趋势信号
- **Incredibuild AI平台转型** (方向: 持续强化, 强度: high): 从单一编译加速转向AI原生开发平台，覆盖开发、测试、安全、部署全生命周期。
- **安全合规成为选型核心门槛** (方向: 持续强化, 强度: high): Incredibuild获ISO 9001/27001认证并推SBOM，EngFlow获SOC 2认证，合规成为企业准入条件。
- **开源工具分流成本敏感用户** (方向: 先强后弱, 强度: medium): 腾讯yadcc开源引发初期热度，FASTBuild获CMake集成，但企业级支持不足。
- **C++26标准发布** (方向: 新兴, 强度: medium): 新特性（反射、模式匹配）增加编译复杂度，可能拉动分布式编译需求。
- **CISA政策致C/C++市场下行** (方向: 持续, 强度: low): 美国要求2026年前关键软件剔除C/C++，转向Rust/Go，影响长期需求。

### 值得长期跟踪的技术方向或话题
- **AI与编译加速融合**: Incredibuild的AI平台（Islo沙盒）和预测执行技术，如何提升开发效率。
- **构建缓存与共享缓存集群**: 成为核心功能，减少团队重复构建时间。
- **低带宽场景性能优化**: Incredibuild在100Mbps下性能是FASTBuild的3倍以上，成为商业产品壁垒。
- **安全合规认证竞赛**: ISO、SOC 2、SBOM生成等成为选型关键。

### 竞品动态
- **Incredibuild**: 发布AI平台，推出Islo、Build Guard、Build Runner三款产品，与Visual Studio深度集成，获ISO双认证。
- **EngFlow**: 获SOC 2认证，与Uber合作，与tipi.build推CMake RBE方案，获a16z和Tiger Global投资。
- **腾讯 yadcc**: 开源发布，性能优于distcc/icecream，在大型C++项目上表现突出。
- **FASTBuild**: 获CMake集成，降低使用门槛，但低带宽性能短板明显。
- **Bazel**: 用户评分1/5，逐渐边缘化。
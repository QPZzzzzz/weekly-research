# incredibuild — Research Memory

最后更新: 2026-06-11

- **公司/产品/项目:** Incredibuild, EngFlow, 龙智, FASTBuild, distcc, Bazel, AWS, a16z, Tiger Global, 腾讯, Adobe, Safe Software, yadcc, Islo, Build Guard, Build Runner, tipi.build, CMake RBE, BuildXL, ccache, icecream
- **重要趋势信号:**
    - **Incredibuild 平台化转型 (High):** 从编译加速工具转向AI开发全生命周期平台，推出AI沙箱(Islo)、SBOM生成(Build Guard)和CI/CD加速(Build Runner)三款新产品。
    - **安全合规成硬性门槛 (High):** 商业方案(如Incredibuild的ISO 27001/9001, EngFlow的SOC 2)与开源方案在金融、医疗等强监管行业形成显著鸿沟。
    - **构建缓存与预测执行成共识 (Medium):** 行业从“堆算力”转向“提效率”，Incredibuild和EngFlow均以此为核心技术，避免重复计算。
    - **腾讯开源yadcc (Medium):** 大厂自研趋势，宣称在1000核集群上性能优于distcc和icecream，但缺乏商业支持和合规认证。
- **值得长期跟踪的技术方向/话题:**
    - **AI驱动的开发平台:** Incredibuild的AI转型(Islo, Build Guard, Build Runner)的市场接受度和实际效果。
    - **云原生远程执行与缓存:** EngFlow的Bazel生态和CMake RBE方案能否突破Bazel生态，吸引更广泛的C/C++开发者。
    - **开源新势力:** 腾讯yadcc能否获得企业级支持和合规认证，挑战现有商业方案。
    - **分布式编译的合规化:** 安全合规(SBOM, ISO 27001)如何成为企业选型的标配。
- **竞品动态:**
    - **Incredibuild:** 推出AI新产品(Islo, Build Guard, Build Runner)，强化VS集成和构建事件追踪，强调ISO双认证。
    - **EngFlow:** 由Bazel核心团队创立，获a16z和Tiger Global投资，与tipi.build合作推出CMake RBE方案。
    - **腾讯:** 开源yadcc，宣称性能优于distcc和icecream。
    - **开源方案(FASTBuild, distcc):** 仍活跃但企业级支持不足，市场关注度减弱。
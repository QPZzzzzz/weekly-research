# build-acceleration — Research Memory

最后更新: 2026-06-21

- **公司/产品/项目**: Visual Studio 2026, Incredibuild (AI Sandbox, Build Cache, CI/CD Acceleration), GitHub Copilot, ccache, sccache, mold, Bazel, Buck2, CMake, yadcc, distcc, FASTBuild
- **趋势信号**:
    - **AI集成构建分析产品化竞争加剧** (方向: up, 强度: high): 微软和Incredibuild同步将AI作为核心功能推向市场，标志着产品化竞争阶段。
    - **CI/CD管道优化成为行业刚性需求** (方向: up, 强度: high): 多篇2026年指南强调减少运行时间，构建缓存和增量构建已成行业共识。
    - **开源编译缓存工具兼容性问题突出** (方向: stable, 强度: medium): sccache与mold的缓存失效问题长期未解决，可能推动用户迁移。
    - **现代构建系统(Bazel/Buck2)讨论热度不减，但迁移壁垒依然存在** (方向: stable, 强度: medium): CMake主导地位稳固，迁移成本和高复杂性阻碍大规模采用。
    - **分布式编译方案呈现多元化格局** (方向: stable, 强度: low): 商业、开源、经典方案并存，增加技术选型复杂性。
- **值得长期跟踪的技术方向/话题**:
    - AI集成构建分析的产品化竞争与市场反馈
    - sccache与mold兼容性问题的解决进展
    - 现代构建系统（Bazel/Buck2）的突破性迁移案例
- **竞品动态**:
    - **微软**: VS2026集成GitHub Copilot进行C++构建分析，支持C++23标准。
    - **Incredibuild**: 推出AI Sandbox、Build Cache和CI/CD Acceleration功能，与微软直接竞争。
    - **开源生态**: sccache与mold存在兼容性痛点；ccache持续更新；yadcc状态稳定。
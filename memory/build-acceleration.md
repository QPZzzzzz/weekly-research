# build-acceleration — Research Memory

最后更新: 2026-06-18

### 公司/产品/项目
- **微软**: Visual Studio 2026, GitHub Copilot (C++ 构建性能分析)
- **Incredibuild**: AI Sandbox, CI/CD Acceleration
- **RECC**: 开源远程执行缓存编译器 (对标 sccache/ccache)
- **sccache**: 与 mold 链接器存在缓存失效问题 (Issue #1755)
- **ccache**: 4.13.6 版本 (2026年5月)
- **Buck2 / Bazel**: 现代构建系统，但大规模迁移尚未发生
- **CMake**: 生态地位稳固

### 重要趋势信号
- **AI 集成构建分析产品化**: 微软和 Incredibuild 将 AI 作为核心功能推向市场，竞争加剧。**强度: high**
- **CI/CD “10分钟规则”成为行业共识**: 管道时长控制在5-10分钟，驱动编译加速刚性需求。**强度: high**
- **开源远程执行缓存编译器 RECC 出现**: 为编译缓存领域注入新变量，可能打破现有格局。**强度: medium**
- **现代构建系统挑战传统**: Buck2/Bazel 讨论热度不减，但 CMake 主导地位短期难撼。**强度: medium** (减弱)
- **编译缓存工具与链接器兼容性问题**: sccache 与 mold 问题未解，影响工具链选择。**强度: medium** (减弱)

### 值得长期跟踪的技术方向/话题
- **AI 辅助构建优化**: 从概念验证到产品化落地，成为标配能力。
- **分布式编译与缓存**: 开源方案 (RECC) 与商业方案 (Incredibuild) 竞争。
- **现代构建系统迁移**: Buck2/Bazel 在大型项目中的实际应用案例。
- **编译缓存工具兼容性**: sccache 与 mold 等链接器的解决方案进展。

### 竞品动态
- **微软**: Visual Studio 2026 正式集成 GitHub Copilot 进行 C++ 构建性能分析。
- **Incredibuild**: 推出 AI Sandbox 和 CI/CD Acceleration 新功能，向 AI 和 CI/CD 场景深度整合。
- **RECC**: 在 CppCon 上作为开源项目亮相，提供远程执行缓存新选择。
- **sccache / ccache**: 持续更新，但 sccache 与 mold 的兼容性问题 (Issue #1755) 仍未解决。
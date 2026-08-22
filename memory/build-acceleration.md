# build-acceleration — Research Memory

最后更新: 2026-08-22

## 关键记忆点

### 公司/产品/项目
- **sccache**（wasmerio/sccache）：编译缓存事实标准，Google Android 官方采用，支持 C/C++/Rust/CUDA，云存储 S3/GCS/Azure Blob + icecream 分布式编译
- **ccache**：存量优势在单语言/本地缓存场景，新建项目被 sccache 取代
- **Visual Studio 2026**：集成 GitHub Copilot Build Performance Agent，接近完整 C++23，AddressSanitizer 扩展 ARM64
- **IncrediBuild**：AI 驱动构建效能平台，跨平台/跨 IDE 独立工具链路线，内容营销密集面向 CTO/VP
- **Bazel**：热度下降，高迁移成本成主要负面因素
- **Buck2**：外部依赖管理（Conan）集成仍是痛点
- **NativeLink**：与 CMake 集成方案受关注
- **腾讯 yadcc**：分布式编译开源，稳定运行 8 个月，定位"提高吞吐"
- **FASTBuild**：关注度平稳
- **EngFlow**：宣称 C++ 构建 21 倍加速，社区质疑效果因架构而异
- **MSVC Build Tools v14.52**：C++ 前端、模块、代码生成、静态分析改进

### 重要趋势信号
- **sccache 成编译缓存事实标准**（up, high）：Google Android 官方背书是关键转折点，多语言+云存储+分布式"三位一体"全面超越 ccache
- **AI 构建优化产品化爆发**（up, high）：微软 IDE 内置 vs IncrediBuild 独立工具链，12 个月内见分晓
- **CMake + RE 服务组合兴起**（up, high）：打破"分布式编译必须绑定 Bazel"认知，低迁移成本是核心驱动力，sccache 宣称 90% 加速
- **CI/CD 构建加速升级为管理 KPI**（up, high）：采购决策延伸至 CTO/VP，ROI 量化能力成厂商核心竞争力
- **国内大厂工具外输**（up, medium）：腾讯 yadcc 开源加剧竞争
- **Bazel 热度下降**（down, medium）：社区从追捧转向理性质疑，CMake 生态位加固

### 长期跟踪方向
- **sccache 与 mold 兼容性修复进展**：编译缓存+高速链接完整链路优化
- **腾讯 yadcc 社区运营活跃度**：GitHub Star、文档、Issue 响应决定能否从"开源"走向"生态"
- **NativeLink + CMake 企业级采用案例**：验证"CMake + RE 服务"可行性
- **微软 vs IncrediBuild AI 构建优化路线竞争结果**：影响市场格局
- **构建加速工具 ROI 量化指标与高管采购叙事**：CTO/VP 决策链变长

### 竞品动态
- **微软**：VS 2026 内置 Copilot 构建性能代理，零迁移成本但锁定 VS 生态
- **IncrediBuild**：发布《CI/CD in 2026: 20 Statistics》和《Top 10 CI/CD Pipeline Tools in 2026》，强化"构建效能全栈平台"定位
- **腾讯 yadcc**：开源分布式编译系统，专为大规模 C++ 项目设计
- **VirtusLab**：发布 Bazel vs CMake 对比，承认 Bazel 远程执行优势但强调迁移成本
- **Kea Sigma Delta**：6 个月构建系统测试报告推荐 CMake，认为 Bazel"可能强大但复杂"
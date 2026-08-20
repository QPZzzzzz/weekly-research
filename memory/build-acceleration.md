# build-acceleration — Research Memory

最后更新: 2026-08-20

## 关键记忆点

### 公司/产品/项目
- **sccache**：编译缓存事实标准，Google Android 官方采用，支持 C/C++/Rust/CUDA，icecream 风格分布式编译，云存储后端（S3/GCS/Azure Blob）
- **ccache**：C/C++ 单一语言定位，面临 sccache 挑战
- **微软 Visual Studio 2026**：集成 GitHub Copilot 构建性能代理（追踪构建、发现瓶颈、应用优化）；接近完整 C++23 一致性；AddressSanitizer 扩展到 ARM64
- **IncrediBuild**：AI 驱动构建效能平台，跨平台/跨 IDE 定位，内容营销密集面向管理层
- **腾讯 yadcc**：分布式编译系统开源，定位"提高吞吐"，腾讯广告稳定运行 8 个月
- **EngFlow**：宣称 C++ 构建 21 倍加速，社区质疑效果因架构而异
- **NativeLink**：与 CMake 集成方案受关注
- **Coralogix**：入局 CI/CD 可观测性
- **FASTBuild**：分布式编译工具，关注度平稳
- **Buck2**：CMake 可输出 Buck2/Bazel 文件，但集成问题仍是痛点
- **MSVC Build Tools v14.52**：C++ 前端、模块、代码生成改进

### 重要趋势信号
- **sccache 成为编译缓存事实标准** — Google Android 官方背书，多语言+云存储+分布式组合优势 — **high**
- **AI 构建优化产品化爆发** — 微软 IDE 内置路线 vs IncrediBuild 独立工具链路线，12 个月内见分晓 — **high**
- **CMake + RE 服务组合兴起** — 打破"分布式编译必须绑定 Bazel"认知，中长尾企业受益 — **high**
- **CI/CD 构建加速升级为管理 KPI** — 采购决策延伸至 CTO/VP，需 ROI 量化指标 — **high**
- **国内大厂工具外输** — 腾讯 yadcc 开源，加剧中小型企业市场竞争 — **medium**
- **Bazel 热度下降** — 从"下一代构建系统"转向质疑，CMake 低迁移成本优势凸显 — **medium**

### 长期跟踪方向
- sccache 与 mold 兼容性修复（编译缓存 + 高速链接链路）
- 腾讯 yadcc 社区运营（GitHub Star、文档、Issue 响应）
- RE 服务 + CMake 生态（企业采用案例、NativeLink 社区活跃度）
- 微软 vs IncrediBuild AI 构建优化路线竞争结果
- 构建加速工具 ROI 量化指标与高管采购叙事

### 竞品动态
- **Google**：Android 官方仓库采用 sccache；Pigweed 项目 Bazel 为主、GN 维护模式、CMake 继续支持
- **微软**：VS 2026 正式发布，Copilot 构建性能代理，IDE 内置路线
- **IncrediBuild**：产品定位从"编译加速工具"升级为"构建效能全栈平台"；发布 C++ 构建系统选择指南
- **腾讯**：yadcc 开源，国内大厂从"工具使用者"变为"工具提供者"
- **Coralogix**：CI/CD 可观测性方案入局
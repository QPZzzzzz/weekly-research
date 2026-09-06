# build-acceleration — Research Memory

最后更新: 2026-09-06

## 关键记忆点

### 涉及的公司/产品/项目
- **IncrediBuild**（含中国代理龙智）— 共享缓存+分布式处理层核心论据
- **sccache**（Mozilla）— 云原生编译缓存，支持 S3/GCS/Redis 多后端
- **Pigweed**（Google）— SEED 0111 正式批准 Bazel 为主要构建系统
- **Visual Studio 2026** — 首次产品化 "Copilot build performance"，无分布式编译布局
- **Buck2**（Meta）— Conan 集成 PR 未合并，C++ 生态成熟度落后 Bazel
- **FASTBuild** — Unity/Blob 构建 + 分布式编译，宣称提升 10 倍以上
- **ccache / distcc** — 中小团队（10-50人）仍解决 80% 构建加速需求

### 重要趋势信号
- **共享缓存成为 CI/CD 标准组件** — 主流 CI 工具（GitHub Actions/Jenkins）缓存机制粗糙，催生独立缓存/加速层市场。类比 20 年前数据库缓存从应用逻辑分离的演进路径。强度：**high**
- **AI 生成代码驱动 CI 加速需求** — AI 提交量激增使冗余计算从"效率问题"升级为"成本危机"，构建/CI 成本成为新瓶颈约束。AI 既是问题制造者也是解决方案载体。强度：**high**
- **Pigweed 转向 Bazel** — 嵌入式领域标志性胜利，可能带动 Zephyr、Mbed OS 等重估构建系统选型。关键变量：Bazel 交叉编译工具链规则成熟度。强度：**high**
- **C++ 模块系统提升编译速度** — 本期首次出现。模块"一次编译、多次导入"减少重复解析，但对编译缓存语义粒度提出新挑战（传统头文件依赖缓存失效策略可能失效）。sccache/ccache 尚未适配，存在市场空白。强度：**medium**
- **经典工具与新一代工具分层共存** — ccache/distcc（零成本起步）→ sccache（云原生中间层）→ FASTBuild/IncrediBuild（大规模分布式），类似 IaaS/PaaS/SaaS 分层逻辑。强度：**medium**

### 值得长期跟踪的技术方向
- **C++20 模块系统对构建模型的影响**：模块依赖图 vs 头文件依赖的缓存键设计、分布式任务切分策略、MSVC/Clang/GCC 支持进度差异
- **Bazel 在嵌入式领域的后续跟进**：Pigweed 之后是否有其他嵌入式项目跟进，工具链规则成熟度
- **共享缓存作为独立抽象层**：缓存层从 CI/CD 架构中分离的演进路径
- **Buck2 外部依赖管理**：Conan 集成进展，能否突破替代 Bazel 的核心瓶颈

### 竞品动态
- **IncrediBuild**：发布 2026 年十大 CI/CD 工具评测，定位共享缓存为必备组件；推出 AI 沙盒功能
- **Visual Studio 2026**：GA 发布，核心卖点为 AI 集成 + C++ 构建工具改进；MSVC Build Tools 预览版改进模块支持、C++23 一致性、AddressSanitizer 扩展到 ARM64；选择 AI + 构建分析路径，未集成分布式编译
- **Pigweed**：GN 降级维护模式，CMake 已降级，Bazel 成为唯一主要构建系统
- **Buck2**：核心用 Rust 编写，语言规则用 Starlark 与核心分离；Conan 集成僵局未破
- **sccache**：持续迭代，多级缓存和自动回填功能完善，在 Databend 等公司 CI 实践验证显著 ROI
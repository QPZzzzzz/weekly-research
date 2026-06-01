# build-acceleration — Research Memory

最后更新: 2026-06-01

### 公司/产品/项目
- **微软**: Visual Studio 2026, MSVC 14.51, Copilot Build Performance, SPGO, IncrediBuild 引擎, CMake 4.1.1
- **Meta**: Buck2 (开源, Rust重写)
- **腾讯**: yadcc (开源, 支持512并发)
- **Incredibuild**: 被VS 2026集成, 升级为平台级基础设施
- **ccache**: 4.13.x系列 (支持MSVC缓存)
- **sccache**: 云存储支持, 多语言, 与mold存在兼容性问题
- **zccache**: 新进入者, 多语言支持
- **Bazel**: 学习曲线高, 被Buck2分流
- **Intel**: oneAPI编译器优化新处理器
- **Zig**: 构建系统重做, 编译速度提升90%

### 重要趋势信号
- **AI深度集成至开发工具链**: AI从"写代码"转向"优化构建", VS 2026 Copilot可自动检测编译瓶颈并推荐优化策略。**强度: high**
- **分布式编译+缓存组合成标配**: 大型C++项目核心策略, 美团案例显示构建时间从45分钟降至8分钟。**强度: high**
- **缓存工具生态空前活跃**: ccache密集迭代, sccache受关注, zccache出现, 竞争加剧。**强度: high**
- **AI驱动CI/CD管道**: 预测性缓存、自愈管道、测试选择成为2026年趋势。**强度: high**
- **现代构建系统挑战传统**: Buck2开源, Bazel/Buck2提供分布式缓存, 但学习曲线和C/C++集成仍是门槛。**强度: medium**
- **C++ Modules进入"可用"阶段**: MSVC持续修复, 但兼容性方案仍复杂。**强度: medium**
- **美国政策推动关键软件剔除C/C++**: 转向内存安全语言, 可能影响C++生态系统。**强度: low**
- **C++26新特性增加编译复杂度**: 反射等特性可能催生新优化需求。**强度: medium**

### 值得长期跟踪的技术方向/话题
- AI驱动的构建优化 (Copilot, 自优化管道)
- 分布式编译与缓存的组合策略 (yadcc, IncrediBuild)
- 缓存工具生态演进 (ccache vs sccache vs zccache)
- 现代构建系统 (Buck2, Bazel) 的易用性改进和C++集成
- C++ Modules的成熟度和兼容性方案
- C++26反射等新特性对编译性能的影响
- 工具链集成测试 (如sccache与mold的兼容性问题)
- 下一代Bazel兼容构建系统 (如Bonanza)

### 竞品动态
- **微软**: VS 2026发布, 集成Incredibuild引擎和Copilot构建分析工具, 降低分布式编译和AI优化门槛。SPGO优化实现5-15%运行时性能提升。
- **Meta**: Buck2开源, 核心用Rust编写, 挑战Bazel地位, 但C/C++依赖导入仍是门槛。
- **腾讯**: yadcc开源, 支持512并发编译, 针对工业生产环境优化。
- **Incredibuild**: 从独立工具商升级为平台级基础设施提供商, 被微软官方集成。
- **ccache**: 4.13.x系列密集更新, 支持MSVC缓存, 保持活跃维护。
- **sccache**: 云原生特性受青睐, 支持多语言, 但存在与mold的兼容性问题。
- **zccache**: 新进入者, 声称冷缓存后快速重建, 市场可能进一步细分。
- **Bazel**: 讨论热度被Buck2和VS 2026分流, 学习曲线问题成为普及瓶颈。
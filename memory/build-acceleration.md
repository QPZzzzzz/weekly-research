# build-acceleration — Research Memory

最后更新: 2026-06-14

### 公司/产品/项目
- **Microsoft**: Visual Studio 2026（集成GitHub Copilot构建分析）
- **Meta**: Buck2（开源构建系统）
- **Incredibuild**: Build Runner（CI加速Beta）、Coding Agent Sandbox（AI编码环境）
- **sccache**: 编译缓存工具（支持云存储，与mold链接器有兼容性问题）
- **ccache**: 编译缓存工具（持续更新至4.13.6）
- **mold**: 高性能链接器（与sccache缓存失效相关）
- **Bazel**: 现代构建系统（Rust+C++集成场景被推荐）
- **CMake**: 传统构建系统（仍占主导地位）

### 重要趋势信号
- **CI/CD“10分钟规则”成为行业刚性约束** | 多篇2026年指南强调管道时长应控制在5-10分钟，否则开发者效率下降 | **high**
- **AI集成构建分析从概念走向产品** | Visual Studio 2026集成GitHub Copilot进行构建性能分析（Public Preview） | **high**
- **现代构建系统（Bazel, Buck2）加速挑战传统CMake地位** | Buck2开源引发热议，Bazel持续获得关注，但大规模迁移未现 | **medium**
- **云存储成为编译缓存关键** | sccache支持云对象存储，ccache持续更新，两者对比讨论频繁 | **medium**
- **构建缓存工具与链接器兼容性问题显现** | 使用mold链接器时sccache缓存失效，每次构建都增加缓存大小 | **medium**（新信号）
- **C++20模块在大型项目中应用前景依然黯淡** | Blender社区认为Unity Builds更有效，C++20模块短期内不现实 | **medium**
- **Incredibuild推出CI加速和Coding Agent Sandbox等新功能** | 官网展示Build Runner（CI加速Beta）、Coding Agent Sandbox等新产品 | **medium**（新信号）

### 值得长期跟踪的技术方向/话题
- **AI辅助构建分析**：从概念进入产品化阶段，Visual Studio 2026率先集成，未来可能成为构建优化标配。
- **现代构建系统（Bazel, Buck2）与CMake的竞争**：虽未大规模迁移，但Buck2开源和Bazel持续关注表明趋势，需跟踪社区采用率。
- **编译缓存与链接器兼容性**：mold等高性能链接器与sccache的兼容性问题可能影响工具链选择，需关注解决方案。
- **分布式编译与云存储集成**：sccache支持云对象存储成为差异化优势，云原生编译缓存架构值得跟踪。
- **C++20模块在大型项目中的实际落地**：目前社区悲观，但若工具链成熟可能改变格局。

### 竞品动态
- **Microsoft**: Visual Studio 2026集成GitHub Copilot构建性能分析（Public Preview），支持迭代构建分析、检测预编译头文件优化效果。
- **Meta**: Buck2开源，强调从零重写、核心与语言规则分离、高并行性等特性。
- **Incredibuild**: 推出Build Runner（CI加速Beta）、Coding Agent Sandbox（确保AI编码连续性）等新产品，持续推广构建加速和分布式处理方案。
- **sccache**: 支持S3、GCS等云对象存储，与ccache竞争加剧；但出现与mold链接器的兼容性问题（Issue #1755）。
- **ccache**: 持续更新至4.13.6版本，保持与sccache的竞争态势。
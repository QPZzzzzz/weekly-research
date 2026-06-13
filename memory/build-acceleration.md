# build-acceleration — Research Memory

最后更新: 2026-06-13

### 关键记忆点

**公司/产品/项目**
- **sccache**：主流编译缓存工具，支持云存储（S3、GCS），用于Rust和C++项目。
- **Visual Studio 2026**：集成GitHub Copilot进行构建性能分析，AI辅助编译优化产品化。
- **Buck2**：Meta开源，Rust编写，支持分布式构建，挑战CMake地位。
- **Incredibuild**：商业分布式编译方案，持续推广。
- **FASTBuild**：开源分布式编译工具，讨论热度低。
- **Red Hat**：推广distcc+Docker容器化编译方案。
- **百度文心快码**：系统梳理分布式编译方案（Icecream、xmake、Kubernetes）。

**重要趋势信号**
- **CI/CD“10分钟规则”成为行业刚性约束**（方向：up，强度：high）：管道时长控制在5-10分钟，否则开发者效率下降。
- **sccache确立主流编译缓存工具地位**（方向：up，强度：high）：云存储支持是关键差异化优势。
- **AI集成构建分析从概念走向产品**（方向：up，强度：high）：Visual Studio 2026率先集成Copilot。
- **现代构建系统（Bazel, Buck2）加速挑战传统CMake地位**（方向：up，强度：medium）：Buck2开源引发热议，但大规模迁移未现。
- **C++20模块在大型项目中应用前景依然黯淡**（方向：stable，强度：medium）：Blender社区认为Unity Builds更现实。
- **分布式编译工具多样化，Icecream、xmake、Kubernetes方案涌现**（方向：up，强度：medium）：行业从单一工具转向组合方案。
- **云存储成为编译缓存关键**（方向：up，强度：medium）：sccache支持S3、GCS，推动全球分布式缓存。
- **Incredibuild持续推广其分布式编译方案**（方向：stable，强度：low）：商业方案与开源竞争。
- **FASTBuild作为开源分布式编译工具被提及**（方向：stable，强度：low）：讨论热度低。
- **Red Hat推广distcc+Docker方案**（方向：stable，强度：low）：容器化编译降低部署门槛。

**值得长期跟踪的技术方向或话题**
- **分布式编译工具多样化**：Icecream、xmake、Kubernetes方案是否形成主流选择。
- **云存储缓存集成深度**：sccache与云厂商的集成进展。
- **AI辅助构建分析**：Visual Studio 2026的Copilot集成效果及后续产品化。
- **现代构建系统演进**：Bazel、Buck2 vs CMake的竞争格局。
- **C++20模块采用**：大型项目中的实用性和成熟度。

**竞品动态**
- **新产品**：Buck2开源（Meta）；Visual Studio 2026集成AI构建分析（微软）。
- **融资**：无。
- **合作**：无。
- **技术突破**：sccache支持云存储；distcc+Docker容器化方案；Kubernetes编排编译任务。
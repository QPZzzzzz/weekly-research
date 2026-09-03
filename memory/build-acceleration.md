# build-acceleration — Research Memory

最后更新: 2026-09-03

## 关键记忆点提取

### 公司/产品/项目
- IncrediBuild（CI加速产品，Islo AI沙盒，Build Runners）
- sccache（mozilla开源编译器缓存）
- mold（链接器）
- Databend（Rust数据库，CI编译优化实践）
- Pigweed（Google嵌入式框架）
- Bazel / Buck2 / CMake / GN（构建系统）
- Visual Studio 2026（微软C++工具链）
- GitHub Copilot（AI编程）
- OpenDAL（Databend统一存储层）
- ccache / distcc / FASTBuild（经典编译加速工具）

### 重要趋势信号
- **共享缓存成为CI/CD标准组件** — 主流CI平台未解决冗余计算，共享缓存+分布式处理层成为必备两层架构 | **high**
- **AI生成代码驱动CI加速需求** — AI提交量激增使冗余计算从效率问题升级为成本危机 | **high**
- **CI中增量编译效果不佳** — Databed验证sccache在CI中价值远高于本地 | **high**
- **Pigweed转向Bazel** — Bazel在嵌入式领域获标志性胜利 | **medium**
- **Buck2的Conan集成僵局** — 外部依赖管理集成是替代Bazel的核心瓶颈 | **medium**
- **sccache与mold兼容性缺陷** — 工具链集成"最后一公里"问题 | **medium**
- **VS 2026无分布式编译布局** — 微软在构建加速领域仍聚焦传统路径 | **low**

### 值得长期跟踪的技术方向
- 共享缓存与分布式处理层融合架构（CI加速标准两层）
- AI辅助编程对CI负载特征的影响（提交频率/数量变化）
- Bazel在嵌入式领域的迁移潮（Pigweed是否带动）
- Buck2的Conan集成PR进展（合并与否是关键节点）
- sccache生态兼容性修复（mold问题是否引发修复）
- VS 2026后续版本是否涉足分布式编译
- C++20模块对构建模型的影响（早期阶段）

### 竞品动态
- **IncrediBuild**：发布2026 CI/CD工具评测，推出Islo AI沙盒，Build Runners早鸟计划宣称CI提速4-8倍
- **微软**：VS 2026 GA发布，接近完整C++23一致性，扩展AddressSanitizer到ARM64，预览GitHub Copilot C++能力，但无分布式编译集成
- **Google Pigweed**：SEED 0111批准Bazel成为主要构建系统，CMake降级为"继续支持"，GN进入维护模式
- **Buck2**：Conan集成PR讨论热烈但未合并，外部依赖管理集成不成熟
- **sccache**：采用广度扩大，但mold兼容性问题暴露生态成熟度不足
- **经典方案（ccache/distcc/FASTBuild）**：中小团队仍广泛应用，distcc 10台机器112核将编译时间从30分钟降至8.5分钟
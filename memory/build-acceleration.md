# build-acceleration — Research Memory

最后更新: 2026-08-04

## 关键记忆点提取

### 公司/产品/项目
- **腾讯 yadcc**：1700 核心集群，日编译 300 万+目标文件，LLVM 编译 3 分 11 秒（15 倍加速）
- **IncrediBuild**：集成至 Visual Studio 2026（引擎级），宣称加速 CI 运行器 8 倍
- **Microsoft**：VS 2026 内置 IncrediBuild 引擎，CMake 4.1.1，C++23 完整支持
- **NativeLink**：CMake 项目远程构建缓存与执行方案，开源可自托管
- **sccache**：Mozilla/Databend 生产验证降编译时间最高 95%，OpenDAL 成为组件
- **ccache**：4.13.6 发布，MSVC 缓存支持提升
- **mold**：与 sccache v0.16.0 存在兼容性问题

### 重要趋势信号
- **商业与开源深度整合**（high）："开源核心+商业增强"成主流，MSVC 引擎级集成 IncrediBuild
- **远程构建缓存/执行服务兴起**（medium）：NativeLink 提供"不迁移构建系统"的加速路径，直击 Bazel 迁移痛点
- **构建缓存成 CI/CD 标配**（high）：缓存命中率成核心 KPI，案例 45→8 分钟（降 82%）
- **sccache 深入 Rust 生态**（medium）：OpenDAL 集成增强存储后端抽象，可能带动其他语言生态
- **分布式编译性能竞赛消退**（low）：yadcc 已确立标杆，进入渐进优化期

### 长期跟踪方向
- **远程执行服务（RE）作为独立加速层**：2026-2027 年可能增长最快的细分赛道
- **工具链兼容性测试矩阵**：ccache/sccache + mold/lld + distcc/yadcc + CMake/Bazel 组合爆炸风险
- **缓存命中率进入工程效能 dashboard 标准指标集**（预计 2027 年）
- **sccache + 存储抽象（OpenDAL）范式**：可能成为"缓存工具+存储抽象"参考范式
- **Bazel/Buck2 迁移紧迫性下降**：NativeLink 模式若被验证，可能延缓迁移浪潮

### 竞品动态
- **Microsoft × IncrediBuild**：引擎级整合，从"插件捆绑"升级为"平台基础设施"
- **NativeLink**：新进入者，定位"构建系统无关"加速层，开源+自托管
- **腾讯 yadcc**：开源方案达商业级性能，竞争焦点转向调度效率与吞吐量
- **sccache**：从通用缓存工具向"语言生态基础设施"演进（OpenDAL 集成）
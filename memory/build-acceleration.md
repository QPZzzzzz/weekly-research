# build-acceleration — Research Memory

最后更新: 2026-08-29

## 关键记忆点

### 涉及公司/产品/项目
- 微软（GitHub Copilot Build Performance、Visual Studio 2026）
- IncrediBuild（Islo AI沙盒、CI加速产品）
- Google（Android采用sccache）
- Meta（Buck2开源构建系统）
- FASTBuild、EngFlow、Wasmer（sccache维护方）、Coralogix、龙智（IncrediBuild中国代理）

### 重要趋势信号
- **AI构建优化产品化落地**（up, high）：微软Copilot Build Performance与IncrediBuild Islo双线推进，从专家经验转向数据驱动
- **sccache成编译缓存事实标准**（up, high）：Google官方采用+云存储（S3/GCS/Azure）支持构筑核心壁垒
- **分布式编译+缓存结合成主流**（up, high）：FASTBuild/sccache原生支持，美团实践验证，从可选策略变默认架构
- **CI/CD管道加速成焦点**（up, high）：AI辅助编程引爆提交量，共享缓存为核心抓手，案例45min→8min（降幅82%）
- **CMake主导地位强化，Bazel热度下滑**（stable, medium）：CMake+远程执行（RE）成低迁移成本分布式路径
- **Buck2作为Bazel替代方案讨论增多**（up, medium）：Rust核心+Starlark规则，与Conan集成进展待观察
- **VS 2026构建性能负面反馈**（down, medium）：与微软AI优化正面叙事形成反差，可能成竞品营销切入点

### 长期跟踪方向
- C++20模块在编译加速中的应用（本期未提及，但可能根本性改变C++构建模型）
- Buck2与Conan集成成熟度（若成熟可能打破CMake一家独大格局）
- 共享缓存预计2027年成为CI/CD基础设施标准组件
- AI辅助编程对构建管道的持续压力与解法演进

### 竞品动态
- **微软**：VS 2026发布，MSVC性能提升，Unreal Engine基准测试提升6%；Copilot Build Performance集成至开发者工作流
- **IncrediBuild**：推广AI沙盒Islo，宣称8x更快的CI runners；ROI量化叙事（45min→8min）吸引企业客户；龙智代理宣传游戏开发10倍加速
- **Google**：Android官方采用sccache（最强背书）
- **Meta**：Buck2开源持续获关注，但采用门槛仍高
- **EngFlow**：分布式构建效果引发讨论，21x加速为最佳案例，效果因架构而异
- **Coralogix**：推出专门CI/CD加速可观测性解决方案
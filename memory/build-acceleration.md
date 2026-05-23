# build-acceleration — Research Memory

最后更新: 2026-05-23

### 关键记忆点

#### 公司/产品/项目
- **Microsoft**: Visual Studio 2026, `@BuildPerfCpp`, MSVC, Incredibuild
- **腾讯**: yadcc (开源, 512并发)
- **美团**: 分布式编译+缓存实践 (45min→8min)
- **Meta**: Buck2 (Rust, Starlark)
- **Google**: sccache, Bazel
- **其他**: ccache, sccache, Nocc, homcc, distcc, CMake, Pigweed, Celonis, GitNexa

#### 重要趋势信号
- **AI自主构建优化 (high)**: VS 2026 `@BuildPerfCpp` 自动分析瓶颈，减少40%构建时间。
- **分布式编译+缓存成标配 (high)**: 美团/腾讯案例，构建时间从45分钟降至8分钟。
- **缓存工具双雄争霸 (medium)**: ccache (本地极致) vs sccache (云原生多语言)，技术路线分化。
- **CI/CD管道优化新战场 (high)**: 层缓存、路径过滤、增量构建从可选变为必要。
- **C++26增加编译复杂度 (medium)**: 反射、内存安全等新特性可能催生新优化工具。

#### 值得长期跟踪的技术方向
- **AI编译优化**: 从辅助分析到自主优化，关注产品化进展。
- **现代构建系统兼容性**: Buck2/Bazel在C++生态的“最后一公里”问题。
- **C++26新特性影响**: 反射、内存安全对编译复杂度的实际影响。
- **CI/CD构建加速**: 层缓存、路径过滤等策略的标准化。

#### 竞品动态
- **新产品/开源**: 腾讯yadcc (512并发), Meta Buck2, Nocc (分布式编译器), homcc (流量高效).
- **融资/合作**: Incredibuild集成到VS 2026.
- **技术突破**: ccache 4.13.6 (扩展MSVC), sccache (云存储+多语言), MSVC性能提升6%.
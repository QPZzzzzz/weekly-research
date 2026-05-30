# build-acceleration — Research Memory

最后更新: 2026-05-30

- **公司/产品/项目**: 腾讯 yadcc、Meta Buck2、ccache 4.13.6、sccache、mold、Incredibuild、Bonanza、Visual Studio 2026 SPGO、Intel oneAPI、GitNexa、Kellton
- **重要趋势信号**:
  - **缓存优先策略向“预测性缓存”演进** (high): 行业共识从“被动缓存”转向AI驱动的“预测性缓存”，避免不必要的编译。
  - **分布式编译工具生态繁荣** (high): 腾讯开源yadcc（512并发），Meta开源Buck2，工具选择增多。
  - **编译优化延伸至运行时** (high): VS 2026 SPGO通过硬件采样实现5-15%运行时性能提升，无需合成训练场景。
  - **AI驱动CI/CD管道成为主流** (high): 多家机构指南指出AI在预测缓存、自愈管道中的应用，从辅助工具升级为核心驱动力。
  - **工具链集成测试存在盲区** (medium): sccache与mold兼容性问题（Issue #1755）暴露缓存与链接器组合使用的风险。
  - **构建系统向“可替换执行引擎”模块化演进** (medium): Bonanza等系统实现Bazel兼容，核心引擎可替换，降低对单一系统的依赖。
- **值得长期跟踪的技术方向**:
  - AI驱动的预测性缓存与自愈CI/CD管道
  - 分布式编译工具（yadcc、Buck2）的工业落地与社区生态
  - 运行时性能优化（如SPGO）与编译器优化策略
  - 构建系统模块化（可替换执行引擎）对现有生态的冲击
- **竞品动态**:
  - **新产品**: 腾讯开源yadcc分布式编译系统；Bonanza等下一代Bazel兼容系统出现。
  - **融资/合作**: 无明确融资信息，但Incredibuild定位为AI编码代理的执行层基础设施。
  - **技术突破**: VS 2026引入SPGO技术；Intel oneAPI增强新处理器代码生成；Buck2用Rust重写，原生支持分布式。
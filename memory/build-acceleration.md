# build-acceleration — Research Memory

最后更新: 2026-08-30

- **公司/产品**：微软（GitHub Copilot Build Performance、Visual Studio 2026）、IncrediBuild（Islo AI沙盒）、Google（sccache采用）、Meta（Buck2）、EngFlow、Coralogix、AskanTech、FASTBuild、sccache、ccache、distcc、CMake、Bazel、Buck2、Conan

- **趋势信号**：AI构建优化产品化落地加速（high，up）；sccache成编译缓存事实标准（high，up）；分布式编译+缓存融合成默认架构（high，up）；CI/CD管道加速成企业刚需（high，up）；CMake主导强化、Bazel热度下滑（medium，stable）；Buck2替代方案讨论增多（medium，up）；VS 2026构建性能负面反馈弱化（medium，down）

- **长期跟踪方向**：Buck2与Conan集成PR进展；C++20模块对构建模型的影响；共享缓存2027年成CI/CD标准组件；AI代理在构建优化中的演进；sccache云存储生态扩展

- **竞品动态**：微软Copilot Build Performance深度集成VS 2026，IncrediBuild Islo宣称8倍CI加速（45min→8min案例）；Google官方采用sccache（Android）；Meta开源Buck2（Rust核心+Starlark）；EngFlow宣称21倍加速但社区反馈因项目而异；ccache仍仅本地缓存，distcc功能迭代落后
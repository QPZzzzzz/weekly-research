# build-acceleration — Research Memory

最后更新: 2026-07-04

### 关键记忆点

- **公司/产品/项目**: Visual Studio 2026, Incredibuild, sccache, mold, ccache, Bazel, Buck2, CMake, distcc, FASTBuild, yadcc, homcc, 美团
- **重要趋势信号**:
    - **AI驱动编译优化竞争白热化**: 微软VS 2026集成AI功能，直接对标Incredibuild，竞争从工具升级为平台+AI。 (high)
    - **CI/CD“10分钟规则”成硬共识**: 管道时长需控制在5-10分钟，倒逼分布式编译和缓存成为必备基础设施。 (high)
    - **分布式编译+缓存成大型C++项目标配**: 美团案例验证效果（45分钟降至8分钟），行业共识巩固。 (high)
    - **sccache与mold兼容性问题持续**: 问题未修复，用户可能迁移至ccache或商业方案，影响缓存工具市场格局。 (medium)
    - **Bazel/Buck2讨论热但迁移壁垒大**: CMake主导地位短期难撼，学习曲线和生态兼容是主要障碍。 (medium)
- **值得长期跟踪的技术方向/话题**:
    - AI在编译优化中的深度集成（VS 2026 vs Incredibuild）
    - sccache与mold兼容性修复进展及用户迁移路径
    - ccache生态是否因sccache问题回升
    - 分布式编译开源项目（yadcc, homcc）社区活跃度变化
- **竞品动态**:
    - **微软**: Visual Studio 2026正式发布，集成AI驱动构建分析、预编译头优化、并行构建和链接设置优化，直接对标Incredibuild。
    - **Incredibuild**: 提供AI Sandbox和Build Cache，从工具商升级为平台级基础设施，但面临VS 2026的竞争威胁。
    - **sccache**: 与mold链接器存在兼容性问题（Issue #1755），生态面临挑战。
    - **Bazel/Buck2**: 讨论热度高，但缺乏大规模迁移案例，CMake主导地位稳固。
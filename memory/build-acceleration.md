# build-acceleration — Research Memory

最后更新: 2026-06-27

- **公司/产品/项目**：微软Visual Studio 2026、Incredibuild AI Sandbox、Mozilla sccache、ccache 4.13.6、腾讯yadcc、Meta Buck2、FASTBuild、distcc、CMake、Bazel、mold链接器
- **重要趋势信号**：
  - AI辅助构建分析产品化竞争白热化（方向：up，强度：high）
  - 开源编译缓存工具兼容性问题恶化（方向：up，强度：high）
  - CI/CD“10分钟规则”成为行业标准（方向：up，强度：high）
  - 分布式编译开源方案多元化（方向：new，强度：medium）
  - 现代构建系统迁移壁垒仍大（方向：stable，强度：medium）
  - ccache持续活跃更新（方向：stable，强度：low）
  - Buck2开源并采用Rust核心（方向：new，强度：high）
- **值得长期跟踪的技术方向**：AI+编译优化、分布式编译（yadcc、Buck2）、编译缓存工具格局（sccache vs ccache）、现代构建系统迁移（Buck2 vs Bazel vs CMake）
- **竞品动态**：
  - 微软：VS 2026集成Copilot构建分析，全面支持C++23
  - Incredibuild：推出AI Sandbox和ISLO执行层，定位转向AI开发基础设施
  - 腾讯：开源yadcc分布式编译系统，支持数百核并行编译
  - Meta：开源Buck2，核心用Rust编写，支持增量依赖图
  - ccache：2026年5月发布4.13.6版本，持续活跃更新
  - sccache：与mold链接器兼容性问题（Issue #1755）长期未解，用户可能迁移
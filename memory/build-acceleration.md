# build-acceleration — Research Memory

最后更新: 2026-10-03

# 编译加速与分布式编译 — 关键记忆点

## 涉及公司/产品/项目
- **字节跳动**：数千万核 C++ 服务 libc++ 迁移（秦泽天，2026 全球系统软件技术大会）
- **Incredibuild**：CI/CD 叠加层 + Islo AI 沙箱 + 8 倍速 CI runner
- **Microsoft**：Visual Studio 2026 / MSVC Build Tools v14.52
- **Meta**：Buck2 构建系统
- **Google / Pigweed**：Bazel 升为主构建系统（SEED 0111）
- **Mozilla**：sccache（Issue #1755 未解决）
- **美团**：C++ 服务编译耗时优化实践
- **Tweag**：Buck2 分析
- **ccache**：v4.14.1（2026-09-27）
- **distcc / FASTBuild**：经典分布式编译方案

## 重要趋势信号
- **new / high**：字节跳动数千万核 libc++ 迁移经验登上国际会议，中国大厂编译工程首次大规模输出
- **new / high**：VS 2026 升级 18.3.0 后构建性能回归，与 GA 性能提升叙事矛盾
- **up / high**：Incredibuild 从构建加速工具升级为 CI/CD 全流程平台（叠加层 + AI 沙箱）
- **up / high**：CI/CD 缓存叙事从「是否缓存」转向「如何正确失效」
- **up / high**：Pigweed 批准 Bazel 为主构建系统，嵌入式领域构建系统集中趋势加强
- **up / medium**：MSVC v14.52 多维度改进（前端/模块/代码生成/链接器）
- **stable / medium**：sccache + mold 兼容性问题持续（Issue #1755，2023-05 至今未解）
- **stable / medium**：Bazel/Buck2 的 C/C++ 依赖导入仍缺标准化方案
- **stable / low**：distcc/FASTBuild 中文社区讨论停留在概念科普，缺大规模落地案例

## 值得长期跟踪的技术方向
- 大规模 libc++ 迁移（ABI 兼容、性能特征、工具链适配）
- CI/CD 缓存失效策略工程化（锁文件哈希、缓存污染防护）
- Bazel/Buck2 在嵌入式与大型 C++ 项目的渗透
- 构建系统选型：CMake vs Bazel vs Meson vs Buck2
- sccache 与链接器（mold）兼容性标准化
- 分布式编译工具的平台化演进（工具层 → 平台层）
- AI 辅助开发场景在编译加速工具中的落地

## 竞品动态
- **Incredibuild**：推出 Islo AI 沙箱 + 8 倍速 CI runner 早期访问；定位「共享缓存 + 分布式处理叠加层」，无需重写管道
- **Microsoft**：VS 2026 GA 宣传性能提升，但 18.3.0 出现构建回归；MSVC v14.52 持续迭代
- **Pigweed（Google）**：Bazel 升主构建系统，GN 转维护（不早于 2026 可能移除），CMake 无限期支持
- **ccache**：4.14.1 稳定迭代，C/C++ 编译器缓存事实标准
- **sccache（Mozilla）**：与 mold 组合使用缓存失效问题长期未解
- **Meta Buck2**：C/C++ 依赖导入缺标准方式，CMake 集成不明确

## 早期信号观察清单
1. VS 2026 构建性能回归是否扩散、是否影响企业升级决策
2. 字节跳动 libc++ 迁移经验是否引发其他大厂跟进分享
3. Incredibuild Islo AI 沙箱/CI runner 是否引发厂商跟进
4. MSVC v14.52 改进与 VS 2026 回归矛盾是否推动微软修复
5. sccache+mold 兼容性问题是否升级为工具链标准化讨论

## 已消退信号
- VS 2026 安装器限制 C++ 构建工具最低版本（被更高优先级问题覆盖）
- CI/CD 缓存「10分钟→30秒」数字主张（叙事已升级为「如何正确失效」）
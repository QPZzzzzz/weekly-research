# build-acceleration — Research Memory

最后更新: 2026-10-04

# 编译加速与分布式编译 — 关键记忆点

## 涉及公司/产品/项目
- **腾讯 yadcc**：开源 C++ 分布式编译系统，定位「提升吞吐而非降低单文件耗时」
- **字节跳动**：libc++ 数千万核迁移经验（上期信号，本期被 yadcc 替代）
- **Bazel 8**：默认 Bzlmod，远程执行 effectively standard
- **Buck2**：被重写（Meta）
- **Pigweed SEED 0111**：批准 Bazel 为主构建系统，GN 转维护，CMake 无限期支持
- **MSVC Build Tools 2026**：8/9 月预览更新（模块序列化、ARM64 代码生成、编译时间）
- **Visual Studio 2026**：18.7–18.10 修复模块回归与编译器崩溃
- **Intel oneAPI DPC++/C++ 2026.0**：强调 "Faster build and iteration"，支持 Clearwater Forest / Wildcat Lake
- **Incredibuild**：CI/CD 平台化，Islo AI 沙箱 + 8 倍速 CI runner
- **ccache**：4.14.1（2026-09-27），年内多版本迭代
- **sccache**：Rust 实现，支持云对象存储
- **CMake / Meson / GN**：面临迁移压力或转维护
- **摩尔线程**：LMCache / MUSA-Aiter KV 算子（与编译缓存无关）

## 重要趋势信号
- **high** | 中国大厂分布式编译方案持续输出：字节 + 腾讯双极格局形成，从单点分享升级为系统性工具输出
- **high** | 构建系统向 Bazel/Buck2 集中：从嵌入式扩展为通用趋势，远程执行从可选变默认
- **medium** | 编译器厂商将构建速度纳入版本卖点：竞争维度从第三方工具层上移至编译器原生层
- **medium** | VS 2026 构建性能回归-修复闭环：18.3.0 异常 → 18.7–18.10 修复
- **stable** | CI/CD 缓存叙事进入稳定期：锁文件哈希成标准，创新空间收窄
- **stable** | Incredibuild 平台化定位确立：从工具层向 CI/CD 全流程加速演进
- **stable** | ccache 事实标准地位稳固
- **stable** | 中文社区分布式编译仍停留概念科普，缺大规模落地案例

## 值得长期跟踪的技术方向
- 远程执行协议与 build cache 架构的深度耦合（缓存前提从本地/共享 FS 迁移）
- 缓存粒度演进：文件级 → 目标级 → 动作级
- 跨语言统一缓存层构建
- 编译器原生增量编译/模块化对独立缓存工具的替代威胁
- 分布式编译工具从工具层向 CI/CD 平台层演进（叠加层模式）
- CMake 用户向 Bazel 迁移的渐进路径

## 竞品动态
- **Incredibuild**：推出 Islo AI 沙箱 + 8 倍速 CI runner 早期访问；主张「无需重写管道」的共享缓存 + 分布式处理叠加层；AI 辅助开发成新叙事入口
- **Intel**：oneAPI 2026.0 首次将构建速度作为核心卖点
- **Microsoft**：MSVC 持续迭代模块化与编译时间；VS 2026 修复模块回归
- **腾讯**：yadcc 开源，对 Incredibuild 中国市场定价权构成潜在压力
- **Meta**：Buck2 被重写，确认远程执行方向投入

## 早期信号观察清单
1. yadcc 开源是否引发其他大厂跟进开源分布式编译方案
2. Bazel 8 默认 Bzlmod + 远程执行是否加速 CMake 用户迁移
3. Intel 将构建速度纳入卖点是否引发其他编译器厂商跟进
4. VS 2026 构建性能回归问题是否彻底解决
5. 工具层向 CI/CD 平台层演进是否引发更多厂商推出叠加层方案

## 已消退信号（下期勿重复追踪）
- sccache + mold 兼容性问题
- Bazel/Buck2 C/C++ 依赖导入标准化缺失（rules_foreign_cc）
- 字节跳动 libc++ 迁移经验分享（已被 yadcc 替代）
- ccache 与 sccache 双缓存并行格局讨论
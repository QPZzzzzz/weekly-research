# build-acceleration — Research Memory

最后更新: 2026-10-06

# 编译加速与分布式编译 — 关键记忆点

## 涉及公司/产品/项目

- **Microsoft / Visual Studio 2026**：正式 GA，C++23 合规接近完成，MSVC 运行时性能提升，AddressSanitizer 扩展至 ARM64；18.7–18.10 持续修复编译器崩溃、模块回归、AVX-512 代码生成问题
- **字节跳动**：基于 LLVM20 完成 libstdc++ → libc++ 大规模迁移，秦泽天将在 2026 全球系统软件技术大会分享落地经验
- **Incredibuild**：强化"共享缓存 + 分布式处理叠加层"定位，可叠加于 Jenkins/GitHub Actions，无需重写管道；以 AI 提交量激增为叙事入口
- **Pigweed**：SEED 0111 批准 Bazel 为主构建系统，GN 转维护模式，CMake 无限期支持但非首选
- **ccache**：4.14.1（2026-09-27）发布，年内迭代 4.13.6 / 4.14 / 4.14.1，事实标准地位稳固
- **sccache**：编译器包装器，支持本地磁盘/云对象存储，Rust 生态集成度高
- **FASTBuild**：开源分布式编译工具，支持缓存和网络分发，中文社区持续推荐
- **distcc**：经典分布式编译工具，教程类内容为主
- **腾讯 yadcc**：上期 high 信号，本期未再追踪，需关注后续进展
- **Buck2（Meta）**：Bazel 项目导入 C/C++ 依赖缺乏标准方式，常需定制集成
- **Intel oneAPI DPC++/C++**：上期 medium 信号，本期未再出现

## 重要趋势信号

- **high｜编译器厂商将构建速度上移至原生层**：VS 2026 GA 将构建速度作为产品级卖点，对 ccache/sccache 等独立缓存工具构成长期替代压力
- **high｜构建系统向 Bazel 集中**：Pigweed 批准 Bazel 为主构建系统，远程执行与 build cache 深度耦合成为行业默认范式
- **high｜Incredibuild 平台化定位强化**：从工具层向 CI/CD 全流程加速平台演进，"叠加层"模式 + AI 叙事入口
- **high｜字节跳动在 C++ 基础设施领域持续输出**：libc++ 迁移经验分享，中国大厂"双极格局"（字节+腾讯）中字节侧信号更强
- **medium｜AI 辅助开发成为构建加速新叙事入口**：GitHub Copilot 辅助 C++ 构建工具升级（Private Preview），Incredibuild 以 AI 提交量激增切入
- **low｜CI/CD 缓存叙事进入稳定期**：锁文件哈希成事实标准，创新空间收窄，竞争焦点转向缓存粒度与跨语言统一缓存层
- **low｜开源分布式编译工具生态稳定**：无重大架构创新，均为常规迭代或教程类内容

## 值得长期跟踪的技术方向/话题

- **编译器原生增量编译与模块化**对第三方缓存工具的替代压力
- **Bazel 远程执行协议**与 build cache 架构的深度耦合范式
- **libc++ 大规模迁移**的工具链/构建系统/运行时库全面切换经验
- **缓存粒度演进**：文件级 → 目标级 → 动作级
- **跨语言统一缓存层**建设
- **AI 辅助构建加速**叙事是否引发多厂商跟进
- **sccache + mold 组合**在 Rust 增量编译中的兼容性问题是否反转
- **中文社区**是否从概念科普转向大规模落地案例分享

## 竞品动态

- **Microsoft**：VS 2026 GA，C++23 合规接近完成，AddressSanitizer 扩展 ARM64，GitHub Copilot 辅助 C++ 构建工具升级（Private Preview）
- **Incredibuild**：发布 2026 CI/CD 工具榜单，主张"共享缓存+分布式处理叠加层"无需重写管道，以 AI 提交量激增为叙事入口
- **字节跳动**：完成 libc++ 大规模迁移（基于 LLVM20），将在 2026 全球系统软件技术大会分享经验
- **Pigweed**：批准 Bazel 为主构建系统，GN 转维护
- **ccache**：4.14.1 发布，年内多次迭代，事实标准地位稳固
- **腾讯 yadcc**：上期 high 信号本期消退，需关注后续进展
- **Intel oneAPI**：上期 medium 信号本期未出现，声量暂时弱于微软

## 信号变化备忘

- **重新激活**：字节跳动 libc++ 迁移（上期被 yadcc 覆盖）
- **信号反转**：sccache + mold 兼容性问题（上期消退，本期以正向性能数据回归）
- **信号合并**：Bazel 8 默认 Bzlmod → 并入"构建系统向 Bazel 集中"宏观趋势
- **信号升级合并**：MSVC 8/9 月预览更新 → 被 VS 2026 GA 覆盖
- **增强**：Incredibuild 平台化（medium→high）、编译器厂商构建速度卖点（medium→high）、字节跳动 C++ 基础设施输出（medium→high）
- **减弱**：CI/CD 缓存叙事（medium→low）、开源分布式编译工具生态（medium→low）
# build-acceleration — Research Memory

最后更新: 2026-10-13

# 编译加速与分布式编译产业调研 — 关键记忆点

## 一、涉及公司/产品/项目

- **腾讯广告**：自研 C++ 分布式编译系统
- **字节跳动**：数据中心应用 libc++ 大规模迁移（数千万核，libstdc++ → LLVM 20 libc++），秦泽天演讲
- **阿里巴巴**：AI-Native 软件工程实践（含 AI-Native C++ 向量检索库），魏子敬分享
- **Incredibuild**：CI/CD 全流程平台（Islo AI 沙箱、免费 8× CI runner、构建缓存、可观测性、构建卫士）
- **Microsoft**：VS 2026 GA、MSVC Build Tools 18.7–18.10、Copilot C++ Private Preview、ASan ARM64
- **Pigweed（Google）**：SEED 0111 批准 Bazel 为主构建系统
- **Meta**：Buck2 构建系统
- **Tweag**：Buck2 介绍与分析
- **CppDepend**：C++ 编译器与分布式构建系统分析
- **EDG**：C/C++ Compiler Project
- **CNCF**：相关生态
- **工具链**：sccache、ccache、Icecream、mold、Bazel、Buck2、CMake、Meson、GN、FASTBuild

## 二、重要趋势信号

- **方向 up｜自托管构建缓存实践爆发**｜从通用 CI 延伸至远程 Mac CI，工具分层认知形成（ccache 单机 → sccache 远程 → Icecream 分布式）｜**high**
- **方向 up｜Incredibuild 平台化跃迁**｜从编译加速转向 CI/CD 全流程冗余计算消除，免费 8× CI runner 对标 GitHub Actions｜**high**
- **方向 up｜中国大厂升级为编译基础设施"定义者"**｜字节 libc++ 迁移 + 阿里 AI-Native C++，或影响亚太工具链选型｜**high**
- **方向 stable｜VS 2026 GA 未压缩第三方缓存生态**｜构建工具与 IDE 解耦，但 sccache/ccache 热度未减｜**low**
- **方向 new｜AI 驱动 CI/CD 优化进入学术研究**｜从厂商叙事转向学术验证，预示 12–18 个月后可能落地｜**medium**
- **方向 stable｜Bazel C/C++ 依赖导入标准化缺位**｜仍为结构性瓶颈，常需定制集成｜**medium**
- **方向 stable｜CI/CD 缓存叙事稳定**｜"10 分钟→30 秒"成事实标准，依赖缓存默认 10GB/仓库、7 天 TTL｜**medium**
- **方向 stable｜Pigweed 构建系统决策落地**｜Bazel 转正、GN 转维护、CMake 无限期支持｜**medium**

## 三、值得长期跟踪的技术方向/话题

- AI 驱动 CI/CD 优化：是否出现可落地的预测分析工具或开源实现
- 中国大厂编译基础设施组合信号：是否带动亚太 C++ 工具链选型偏好变化
- Incredibuild 共享缓存/分布式处理层切入 AI 高提交量场景：是否引发 CI/CD 平台价格竞争
- 远程 Mac CI 自托管构建缓存：是否催生跨平台缓存策略标准
- Bazel C/C++ 依赖导入标准化进展
- 嵌入式/系统软件领域构建系统选型（Bazel vs GN vs CMake）
- sccache + mold 组合实践与兼容性

## 四、竞品动态

- **Incredibuild**：发布 2026 十大 CI/CD 工具榜单与 Top C++ 编译器榜单；产品矩阵扩展至 Islo AI 沙箱、免费 8× CI runner、构建缓存、可观测性、构建卫士；仍捆绑 Visual Studio 形成生态锁定
- **Microsoft**：VS 2026 正式 GA；C++ 构建工具独立升级（MSVC Build Tools 18.7–18.10）；接近完整 C++23 一致性；MSVC 运行时性能提升；ASan 扩展至 ARM64；Copilot C++ 进入 Private Preview
- **Pigweed（Google）**：SEED 0111 批准 Bazel 为主构建系统，GN 转维护模式，CMake 无限期支持
- **Meta / Tweag**：Buck2 覆盖 C/C++、Rust、Python，但语言支持较 Bazel 窄；Bazel 导入 C/C++ 依赖无标准方式
- **FASTBuild**：信号消退，面临 sccache+mold 组合与 Incredibuild 平台化双重挤压

## 五、已消退信号（供参考）

- FASTBuild 开源分布式编译工具：缺乏新进展，社区活跃度低迷
- Incredibuild Islo AI 沙箱与免费 8× CI runner：已融入平台化叙事，不再作为独立信号
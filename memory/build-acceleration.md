# build-acceleration — Research Memory

最后更新: 2026-09-13

# 编译加速产业调研 · 关键记忆点

## 一、涉及公司/产品/项目

- **sccache**（mozilla）— Rust 实现编译器缓存，默认支持 S3/Redis/Memcached 等所有存储后端
- **ccache** — 经典本地缓存工具，2026 年 4-5 月密集发布 4.13.4/4.13.5/4.13.6
- **MSVC / Visual Studio 2026** — 连续两月修复 C++20 模块缓存适配，配合 Ninja 构建降至 28 秒
- **FASTBuild** — Unity/Blob 构建提速 10 倍以上，兼容网络分发与缓存
- **Incredibuild** — 企业级 DevSecOps 加速，中国授权合作伙伴为龙智（shdsd.com）
- **Buck2 / Bazel** — 下一代构建系统，Conan 集成 PR 未合并，新增 vcpkg 需求
- **Velocity CI**（gradle-build-accelerator）— 预测性/自适应构建加速方案
- **distcc** — Docker 化分布式编译集群（Red Hat distcc-docker-images）
- **CMake / Meson / Bazel** — 构建系统选型焦点，Meson 被认为最有前景
- **RISC-V AI 系统软件栈 / LLVM libc++ / NuttX LLVM 21 / Ruyi Buddy Compiler** — 2026 C++ 大会热点
- **字节跳动** — libstdc++ → libc++ 大规模迁移（基于 LLVM20）

## 二、重要趋势信号

- **方向 up｜编译器缓存平台化** — GitHub 官方背书 sccache 并默认化存储后端，缓存从"自选工具"升级为"平台标准配置"｜强度 **high**
- **方向 up｜MSVC 工具链原生优化侵蚀分布式编译收益** — 连续两月修复模块缓存，单机分钟级构建削弱多机分发边际收益｜强度 **high**
- **方向 up｜CI/CD 构建加速工具化落地** — 10 分钟基准强化，45-90 分钟构建被视为结构性约束，Incredibuild 发布信号清单｜强度 **high**
- **方向 stable｜分布式编译与缓存融合** — FASTBuild 将 Unity 构建+网络分发+缓存一体化，边界模糊化｜强度 **medium**
- **方向 new｜编译器生态向 RISC-V 延伸** — LLVM libc++ 嵌入式移植成新战场，中国厂商参与度高｜强度 **medium**
- **方向 new｜预测性/自适应 CI 加速萌芽** — Velocity CI 用预测算法动态分配资源，或从静态缓存向智能预判演进｜强度 **low**
- **方向 stable｜分布式编译适用边界固化** — 仅单机编译数小时以上大型项目才适合分布式｜强度 **medium**
- **方向 stable｜Buck2 依赖管理僵局** — Conan 集成未合并，vcpkg 需求持续｜强度 **low**

## 三、值得长期跟踪的技术方向/话题

- 编译器缓存双轨格局（sccache 平台化 vs ccache 追赶）未来 2-3 季度市场份额分配
- 工具链深度协同路线 vs 多机分发路线的决策边界移动
- MSVC 4GB 调试信息流与公共流 API 是否被 sccache/ccache 跟进适配
- RISC-V AI 系统软件栈的 C++ 生态空间与中国厂商参与度
- 预测性/自适应 CI 构建加速能否产品化替代静态缓存范式
- FASTBuild Unity/Blob 融合是否推动分布式编译与缓存工具边界进一步模糊
- C++20 模块在分布式/缓存场景的可用性进展

## 四、竞品动态

- **sccache**：获 GitHub Projects 官方 Threads 持续推广，默认构建支持所有存储后端，云原生场景拉开与 ccache 差距
- **ccache**：密集三版本迭代（4.13.4/4.13.5/4.13.6），反映平台化压力下的功能追赶焦虑
- **MSVC**：8-9 月连续更新，修复范围从跨模块边界扩展至序列化和调试信息处理
- **Incredibuild**：发布 CI/CD 加速 7 信号清单与构建系统选型指南，企业级市场教育完成，竞争转向落地效果验证
- **FASTBuild**：Unity/Blob 构建提速 10 倍以上，对纯分布式编译厂商构成产品定义挑战
- **Buck2**：Conan 集成 PR 获好评但未合并，社区期望支持 vcpkg
- **Velocity CI**：预测算法预判构建需求、动态分配资源，将 GitHub Actions 从线性管道转为自适应构建生态